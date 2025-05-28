# One Backend, Multiple Hypermedia formats

To create a mobile app using the hypermedia architecture, we started with the web-based contacts app and made a few changes, primarily replacing HTML templates with HXML templates. But in the process of porting the backend to serve our mobile app, we lost the web application functionality. Indeed, if you tried to visit `http://0.0.0.0:5000` in a web browser, you would see a jumble of text and XML markup. That’s because web browsers don’t know how to render plain XML, and they certainly don’t know how to interpret the tags and attributes of HXML to render an app. It’s a shame, because the Flask code for the web application and mobile app are nearly identical. The database and model logic are shared, and most of the views are unchanged as well.

At this point you’re surely wondering: is it possible to use the same backend to serve both a web application and mobile app? The answer is yes! In fact, this is one of the benefits of using a hypermedia architecture across multiple platforms. We don’t need to port any client-side logic from one platform to another, we just need to respond to requests with the appropriate Hypermedia format. To do this, we will utilize content negotiation built into HTTP.

## What is Content Negotiation?

Imagine a German speaker and Japanese speaker both visit `https://google.com` in their web browser. They will see the Google home page localized in German and Japanese, respectively. How does Google know to return a different version of the homepage based on the user’s preferred language? The answer lies in the REST architecture, and how it separates the concepts of resources and representations.

In the REST architecture, the Google homepage is considered to be a single “resource,” represented by a unique URL. However, that single resource can have multiple “representations.” Representations are variations on how the content of the resource is presented to the client. The German and Japanese versions of the Google homepage are two representations of the same resource. To determine the best representation of a resource to return, HTTP clients and servers engage in a process called “content negotiation.” It works like this:

*   Clients specify the preferred representation through `Accept-*` request headers.
    
*   The server tries to match the preferred representation as best it can, and communicates back the chosen representation using `Content-*`.
    

In the Google homepage example, the German speaker uses a browser that is set to prefer content localized for German. Every HTTP request made by the web browser will include a header `Accept-Language: de-DE`. The server sees the request header, and it will return a response localized for German (if it can). The HTTP response will include a `Content-Language: de-DE` header to inform the client of the language of the response content.

Language is just one factor for resource representation. More importantly for us, resources can be represented using different content types, such as HTML or HXML. Content negotiation over content type is done using the `Accept` request header and `Content-Type` response header. Web browsers set `text/html` as the preferred content type in the `Accept` header. The Hyperview client sets `application/vnd.hyperview+xml` as the preferred content type. This gives our backend a way to distinguish requests coming from a web browser or Hyperview client, and serve the appropriate content to each.

There are two main approaches to content negotiation: fine-grained and global.

## Approach 1: Template Switching

When we ported the Contacts app from the web to mobile, we kept all of the Flask views but made some minor changes. Specifically, we introduced a new function `render_to_response()` and called it in the return statement of each view. Here’s the function again to refresh your memory:

    def render_to_response(template_name, *args, **kwargs):
        content = render_template(template_name, *args, **kwargs)
        response = make_response(content)
        response.headers['Content-Type'] = 'application/vnd.hyperview+xml'
        return response

`app.py`

`render_to_response()` renders a template with the given context, and turns it into an Flask response object with the appropriate Hyperview `Content-Type` header. Obviously, the implementation is highly-specific to serving our Hyperview mobile app. But we can modify the function to do content negotiation based on the request’s `Accept` header:

    HTML_MIME = 'text/html'
    HXML_MIME = 'application/vnd.hyperview+xml'
    
    def render_to_response(
        html_template_name, hxml_template_name, *args, **kwargs <1>
    ):
        response_type = request.accept_mimetypes.best_match(
          [HTML_MIME, HXML_MIME], default=HTML_MIME) <2>
        template_name =
          hxml_template_name
          if response_type == HXML_MIME
          else html_template_name <3>
        content = render_template(template_name, *args, **kwargs)
        response = make_response(content)
        response.headers['Content-Type'] = response_type <4>
        return response

`app.py`

1.  Function signature takes two templates, one for HTML and one for HXML.
    
2.  Determine whether the client wants HTML or HXML.
    
3.  Select the template based on the best match for the client.
    
4.  Set the `Content-Type` header based on the best match for the client.
    

Flask’s request object exposes an `accept_mimetypes` property to help with content negotiation. We pass our two content MIME types to `request.accept_mimetypes.best_match()` and get back the MIME type that works for our client. Based on the best matching MIME type, we choose to either render an HTML template or HXML template. We also make sure to set the `Content-Type` header to the appropriate MIME type. The only difference in our Flask views is that we need to provide both an HTML and HXML template:

    @app.route("/contacts/")
    def contacts_view(contact_id=0):
        contact = Contact.find(contact_id)
        return render_to_response("show.html", "hv/show.xml",
          contact=contact)

`app.py`

*   Template switching between an HTML and HXML template, based on the client.
    

After updating all of the Flask views to support both templates, our backend will support both web browsers and our mobile app! This technique works well for the Contacts app because the screens in the mobile app map directly to pages of the web application. Each app has a dedicated page (or screen) for listing contacts, showing and editing details, and creating a new contact. This meant the Flask views could be kept as-is without major changes.

But what if we wanted to re-imagine the Contacts app UI for our mobile app? Perhaps we want the mobile app to use a single screen, with rows that expanded in-line to support viewing and editing the information? In situations where the UI diverges between platforms, Template Switching becomes cumbersome or impossible. We need a different approach to have one backend serve both hypermedia formats.

## Approach 2: The Redirect Fork

If you recall, the Contacts web app has an `index` view, routed from the root path `/`:

    @app.route("/")
    def index():
        return redirect("/contacts") <1>

`app.py`

1.  Redirect requests from “/” to “/contacts”
    

When someone requests to the root path of the web application, Flask redirects them to the `/contacts` path. This redirect also works in our Hyperview mobile app. The Hyperview client’s `ENTRY_POINT_URL` points to `http://0.0.0.0:5000/`, and the server redirects it to `http://0.0.0.0:5000/contacts`. But there’s no law that says we need to redirect to the same path in our web application and mobile app. What if we used the `Accept` header to redirect to decide on the redirect path?

    HTML_MIME = 'text/html'
    HXML_MIME = 'application/vnd.hyperview+xml'
    
    @app.route("/")
    def index():
        response_type = request.accept_mimetypes.best_match(
          [HTML_MIME, HXML_MIME], default=HTML_MIME) <1>
        if response_type == HXML_MIME:
          return redirect("/mobile/contacts") <2>
        else:
          return redirect("/web/contacts") <3>

`app.py`

1.  Determine whether the client wants HTML or HXML.
    
2.  If the client wants HXML, redirect them to `/mobile/contacts`.
    
3.  If the client wants HTML, redirect them to `/web/contacts`.
    

The entry point is a fork in the road: if the client wants HTML, we redirect them to one path. If the client wants HXML, we redirect them to a different path. These redirects would be handled by different Flask views:

    @app.route("/mobile/contacts")
    def mobile_contacts():
      # Render an HXML response
    
    @app.route("/web/contacts")
    def web_contacts():
      # Render an HTML response

`app.py`

The `mobile_contacts()` view would render an HXML template with a list of contacts. Tapping a contact item would open a screen requested from `/mobile/contacts/1`, handled by a view `mobile_contacts_view`. After the initial fork, all subsequent requests from our mobile app go to paths prefixed with `/mobile/`, and get handled by mobile-specific Flask views. Likewise, all subsequent requests from the web app go to paths prefixed with `/web/`, and get handled by web-specific Flask views. (Note that in practice, we would want to separate the web and mobile views into separate parts of our codebase: `web_app.py` and `mobile_app.py`. We may also choose not to prefix the web paths with `/web/`, if we want more elegant URLs displayed in the browser’s address bar.)

You may be thinking that the Redirect Fork leads to a lot of code duplication. After all, we need to write double the number of views: one set for the web application, and one set for the mobile app. That is true, which is why the Redirect Fork is only preferred if the two platforms require a disjointed set of view logic. If the apps are similar on both platforms, Template Switching will save a lot of time and keep the apps consistent. Even if we need to use the Redirect Fork, the bulk of the logic in our models can be shared by both sets of views.

In practice, you may start out using Template Switching, but then realize you need to implement a fork for platform-specific features. In fact, we’re already doing that in the Contacts app. When porting the app from web to mobile, we didn’t bring over certain features like archiving functionality. The dynamic archive UI is a power feature that wouldn’t make sense on a mobile device. Since our HXML templates don’t expose any entry points to the Archive functionality, we can treat it as “web-only” and not worry about supporting it in Hyperview.