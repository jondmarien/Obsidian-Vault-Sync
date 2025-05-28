# Active Search

So far so good with Contact.app: we have a nice little web application with some significant improvements over a plain HTML-based application. We’ve added a proper “Delete Contact” button, done some dynamic validation of input and looked at different approaches to add paging to the application. As we have said, many web developers would expect that a lot of JavaScript-based scripting would be required to get these features, but we’ve done it all in relatively pure HTML, using only htmx attributes.

We _will_ eventually add some client-side scripting to our application: hypermedia is powerful, but it isn’t _all powerful_ and sometimes scripting might be the best (or only) way to achieve a given goal. For now, however, let’s see what we can accomplish with hypermedia.

The first advanced htmx feature we will create is known as the “Active Search” pattern. Active Search is when, as a user types text into a search box, the results of that search are dynamically shown. This pattern was made popular when Google adopted it for search results, and many applications now implement it.

To implement Active Search, we are going to use techniques closely related to the way we did email validation in the previous chapter. If you think about it, the two features are similar in many ways: in both cases we want to issue a request as the user types into an input and then update some other element with a response. The server-side implementations will, of course, be very different, but the frontend code will look fairly similar due to htmx’s general approach of “issue a request on an event and replace something on the screen.”

## Our Current Search UI

Let’s recall what the search field in our application currently looks like:

    <form action="/contacts" method="get" class="tool-bar">
      <label for="search">Search Termlabel>
      <input id="search" type="search" name="q"
        value="{{ request.args.get('q') or '' }}"> <1>
      <input type="submit" value="Search"/>
    form>

Our search form

1.  The `q` or “query” parameter our client-side code uses to search.
    

Recall that we have some server-side code that looks for the `q` parameter and, if it is present, searches the contacts for that term.

As it stands right now, the user must hit enter when the search input is focused, or click the “Search” button. Both of these events will trigger a `submit` event on the form, causing it to issue an HTTP `GET` and re-rendering the whole page.

Currently, thanks to `hx-boost`, the form will use an AJAX request for this `GET`, but we don’t yet get that nice search-as-you-type behavior we want.

## Adding Active Search

To add active search behavior, we will attach a few htmx attributes to the search input. We will leave the current form as it is, with an `action` and `method`, so that the normal search behavior works even if a user does not have JavaScript enabled. This will make our “Active Search” improvement a nice “progressive enhancement.”

So, in addition to the regular form behavior, we _also_ want to issue an HTTP `GET` request when a key up occurs. We want to issue this request to the same URL as the normal form submission. Finally, we only want to do this after a small pause in typing has occurred.

As we said, this functionality is very similar to what we needed for email validation. We can, in fact copy the `hx-trigger` attribute directly from our email validation example, with its small 200-millisecond delay, to allow a user to stop typing before a request is triggered.

This is another example of how common patterns come up again and again when using htmx.

    <form action="/contacts" method="get" class="tool-bar">
      <label for="search">Search Termlabel>
      <input id="search" type="search" name="q"
        value="{{ request.args.get('q') or '' }}" <1>
        hx-get="/contacts" <2>
        hx-trigger="search, keyup delay:200ms changed"/> <3>
      <input type="submit" value="Search"/>
    form>

Adding active search behavior

1.  Keep the original attributes, so search will work if JavaScript is not available.
    
2.  Issue a `GET` to the same URL as the form.
    
3.  Nearly the same `hx-trigger` specification as for the email input validation.
    

We made a small change to the `hx-trigger` attribute: we switched out the `change` event for the `search` event. The `search` event is triggered when someone clears the search or hits the enter key. It is a non-standard event, but it doesn’t hurt to include here. The main functionality of the feature is provided by the second triggering event, the `keyup`. As in the email example, this trigger is delayed with the `delay:200ms` modifier to “debounce” the input requests and avoid hammering our server with requests on every keyup.

## Targeting The Correct Element

What we have is close to what we want, but we need to set up the correct target. Recall that the default target for an element is itself. As things currently stand, an HTTP `GET` request will be issued to the `/contacts` path, which will, as of now, return an entire HTML document of search results, and then this whole document will be inserted into the _inner_ HTML of the search input.

This is, in fact, nonsense: `input` elements aren’t allowed to have any HTML inside of them. The browser will, sensibly, just ignore the htmx request to put the response HTML inside the input. So, at this point, when a user types anything into our input, a request will be issued (you can see it in your browser development console if you try it out) but, unfortunately, it will appear to the user as if nothing has happened at all.

To fix this issue, what do we want to target with the update instead? Ideally we’d like to just target the actual results: there is no reason to update the header or search input, and that could cause an annoying flash as focus jumps around.

The `hx-target` attribute allows us to do exactly that. Let’s use it to target the results body, the `tbody` element in the table of contacts:

    <form action="/contacts" method="get" class="tool-bar">
      <label for="search">Search Termlabel>
      <input id="search" type="search" name="q"
        value="{{ request.args.get('q') or '' }}"
        hx-get="/contacts"
        hx-trigger="search, keyup delay:200ms changed"
        hx-target="tbody"/> <1>
      <input type="submit" value="Search"/>
    form>
    <table>
      ...
      <tbody>
        ...
      tbody>
    table>

Adding active search behavior

1.  Target the `tbody` tag on the page.
    

Because there is only one `tbody` on the page, we can use the general CSS selector `tbody` and htmx will target the body of the table on the page.

Now if you try typing something into the search box, we’ll see some results: a request is made and the results are inserted into the document within the `tbody`. Unfortunately, the content that is coming back is still an entire HTML document.

Here we end up with a “double render” situation, where an entire document has been inserted _inside_ another element, with all the navigation, headers and footers and so forth re-rendered within that element. This is an example of one of those mis-targeting issues we mentioned earlier.

Thankfully, it is pretty easy to fix.

## Paring Down Our Content

Now, we could use the same trick we reached for in the “Click To Load” and “Infinite Scroll” features: the `hx-select` attribute. Recall that the `hx-select` attribute allows us to pick out the part of the response we are interested in using a CSS selector.

So we could add this to our input:

    <input id="search" type="search" name="q"
      value="{{ request.args.get('q') or '' }}"
      hx-get="/contacts"
      hx-trigger="change, keyup delay:200ms changed"
      hx-target="tbody"
      hx-select="tbody tr"/> <1>

Using “hx-select” for active search

1.  Adding an `hx-select` that picks out the table rows in the `tbody` of the response.
    

However, that isn’t the only fix for this problem, and, in this case, it isn’t the most efficient one. Instead, let’s change the _server-side_ of our Hypermedia-Driven Application to serve _only the HTML content needed_.

## HTTP Request Headers In Htmx

In this section, we’ll look at another, more advanced technique for dealing with a situation where we only want a _partial bit_ of HTML, rather than a full document. Currently, we are letting the server create the full HTML document as response and then, on the client side, we filter the HTML down to the bits that we want. This is easy to do, and, in fact, might be necessary if we don’t control the server side or can’t easily modify responses.

In our application, however, since we are doing “Full Stack” development (that is: we control both frontend _and_ backend code, and can easily modify either) we have another option: we can modify our server responses to return only the content necessary, and remove the need to do client-side filtering.

This turns out to be more efficient, since we aren’t returning all the content surrounding the bit we are interested in, saving bandwidth as well as CPU and memory on the server side. So let’s explore returning different HTML content based on the context information that htmx provides with the HTTP requests it makes.

Here’s a look again at the current server-side code for our search logic:

    @app.route("/contacts")
    def contacts():
        search = request.args.get("q")
        if search is not None:
            contacts_set = Contact.search(search) <1>
        else:
            contacts_set = Contact.all()
        return render_template("index.html", contacts=contacts_set) <2>

Server-side search

1.  This is where the search logic happens.
    
2.  We simply re-render the `index.html` template every time, no matter what.
    

How do we want to change this? We want to render two different bits of HTML content _conditionally_:

*   If this is a “normal” request for the entire page, we want to render the `index.html` template in the current manner. In fact, we don’t want anything to change if this is a “normal” request.
    
*   However, if this is an “Active Search” request, we only want to render the content that is within the `tbody`, that is, just the table rows of the page.
    

So we need some way to determine exactly which of these two different types of requests to the `/contact` URL is being made, in order to know exactly which content we want to render.

It turns out that htmx helps us distinguish between these two cases by including a number of HTTP _Request Headers_ when it makes requests. Request Headers are a feature of HTTP, allowing clients (e.g., web browsers) to include name/value pairs of metadata associated with requests to help the server understand what the client is requesting.

Here is an example of (some of) the headers the FireFox browser issues when requesting `https://hypermedia.systems`:

    GET / HTTP/2
    Host: hypermedia.systems
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:103.0) Gecko/20100101 Firefox/103.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
    Accept-Encoding: gzip, deflate, br
    Accept-Language: en-US,en;q=0.5
    Cache-Control: no-cache
    Connection: keep-alive
    DNT: 1
    Pragma: no-cache
    

HTTP headers

Htmx takes advantage of this feature of HTTP and adds additional headers and, therefore, additional _context_ to the HTTP requests that it makes. This allows you to inspect those headers and choose what logic to execute on the server, and what sort of HTML response you want to send to the client.

Here is a table of the HTTP headers that htmx includes in HTTP requests:

`HX-Boosted`

This will be the string “true” if the request is made via an element using hx-boost

`HX-Current-URL`

This will be the current URL of the browser

`HX-History-Restore-Request`

This will be the string “true” if the request is for history restoration after a miss in the local history cache

`HX-Prompt`

This will contain the user response to an hx-prompt

`HX-Request`

This value is always “true” for htmx-based requests

`HX-Target`

This value will be the id of the target element if it exists

`HX-Trigger-Name`

This value will be the name of the triggered element if it exists

`HX-Trigger`

This value will be the id of the triggered element if it exists

Looking through this list of headers, the last one stands out: we have an id, `search` on our search input. So the value of the `HX-Trigger` header should be set to `search` when the request is coming from the search input, which has the id `search`.

Let’s add some conditional logic to our controller to look for that header and, if the value is `search`, we render only the rows rather than the whole `index.html` template:

    @app.route("/contacts")
    def contacts():
        search = request.args.get("q")
        if search is not None:
            contacts_set = Contact.search(search)
            if request.headers.get('HX-Trigger') == 'search': <1>
              # TODO: render only the rows here <2>
        else:
            contacts_set = Contact.all()
        return render_template("index.html", contacts=contacts_set)

Updating our server-side search

1.  If the request header `HX-Trigger` is equal to “search” we want to do something different.
    
2.  We need to learn how to render just the table rows.
    

OK, so how do we render only the result rows?

## Factoring Your Templates

Now we come to a common pattern in htmx: we want to _factor_ our server-side templates. This means that we want to break our templates up a bit so that they can be called from multiple contexts. In this case, we want to break the rows of the results table out to a separate template we will call `rows.html`. We will include it from the original `index.html` template, and also use it in our controller to render it by itself when we want to respond with only the rows for Active Search requests.

Here’s what the table in our `index.html` file currently looks like:

    <table>
      <thead>
      <tr>
        <th>First <th>Last <th>Phone <th>Email <th/>
      tr>
      thead>
      <tbody>
      {% for contact in contacts %}
        <tr>
          <td>{{ contact.first }}td>
          <td>{{ contact.last }}td>
          <td>{{ contact.phone }}td>
          <td>{{ contact.email }}td>
          <td><a href="/contacts/{{ contact.id }}/edit">Edita>
            <a href="/contacts/{{ contact.id }}">Viewa>td>
        tr>
      {% endfor %}
      tbody>
    table>

The contacts table

The `for` loop in this template is what produces all the rows in the final content generated by `index.html`. What we want to do is to move the `for` loop and, therefore, the rows it creates out to a _separate template file_ so that only that small bit of HTML can be rendered independently from `index.html`.

Again, let’s call this new template `rows.html`:

    {% for contact in contacts %}
      <tr>
        <td>{{ contact.first }}td>
        <td>{{ contact.last }}td>
        <td>{{ contact.phone }}td>
        <td>{{ contact.email }}td>
        <td><a href="/contacts/{{ contact.id }}/edit">Edita>
          <a href="/contacts/{{ contact.id }}">Viewa>td>
      tr>
    {% endfor %}

Our new `rows.html` file

Using this template we can render only the `tr` elements for a given collection of contacts.

Of course, we still want to include this content in the `index.html` template: we are _sometimes_ going to be rendering the entire page, and sometimes only rendering the rows. In order to keep the `index.html` template rendering properly, we can include the `rows.html` template by using the jinja `include` directive at the position we want the content from `rows.html` inserted:

    <table>
      <thead>
      <tr>
        <th>Firstth>
        <th>Lastth>
        <th>Phoneth>
        <th>Emailth>
        <th>th>
      tr>
      thead>
      <tbody>
      {% include 'rows.html' %} <1>
      tbody>
    table>

Including the new file

1.  This directive “includes” the `rows.html` file, inserting its content into the current template.
    

So far, so good: our `/contacts` page is still rendering properly, just as it did before we split the rows out of the `index.html` template.

## Using Our New Template

The last step in factoring our templates is to modify our web controller to take advantage of the new `rows.html` template file when it responds to an active search request.

Since `rows.html` is just another template, just like `index.html`, all we need to do is call the `render_template` function with `rows.html` rather than `index.html`. This will render _only_ the row content rather than the entire page:

    @app.route("/contacts")
    def contacts():
        search = request.args.get("q")
        if search is not None:
            contacts_set = Contact.search(search)
            if request.headers.get('HX-Trigger') == 'search':
              return render_template("rows.html", contacts=contacts_set) <1>
        else:
            contacts_set = Contact.all()
        return render_template("index.html", contacts=contacts_set)

Updating our server-side search

1.  Render the new template in the case of an active search.
    

Now, when an Active Search request is made, rather than getting an entire HTML document back, we only get a partial bit of HTML, the table rows for the contacts that match the search. These rows are then inserted into the `tbody` on the index page, without any need for `hx-select` or other client-side processing.

And, as a bonus, the old form-based search _still works_. We conditionally render the rows only when the `search` input issues the HTTP request via htmx. Again, this is a progressive enhancement to our application.

**HTTP Headers & Caching**

One subtle aspect of the approach we are taking here, using headers to determine the content of what we return, is a feature baked into HTTP: caching. In our request handler, we are now returning different content depending on the value of the `HX-Trigger` header. If we were to use HTTP Caching, we might get into a situation where someone makes a _non-htmx_ request (e.g., refreshing a page) and yet the _htmx_ content is returned from the HTTP cache, resulting in a partial page of content for the user.

The solution to this problem is to use the HTTP Response `Vary` header and call out the htmx headers that you are using to determine what content you are returning. A full explanation of HTTP Caching is beyond the scope of this book, but the [MDN article on the topic](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching) is quite good, and the [htmx documentation](https://htmx.org/docs/#caching) discusses this issue as well.

## Updating the Navigation Bar With “hx-push-url”

One shortcoming of our current Active Search implementation, when compared with the normal form submission, is that when you submit the form version it updates the navigation bar of the browser to include the search term. So, for example, if you search for “joe” in the search box, you will end up with a url that looks like this in your browser’s nav bar:

    https://example.com/contacts?q=joe
    

The updated location after a form search

This is a nice feature of browsers: it allows you to bookmark this search or to copy the URL and send it to someone else. All they have to do is to click on the link, and they will repeat the exact same search. This is also tied in with the browser’s notion of history: if you click the back button it will take you to the previous URL that you came from. If you submit two searches and want to go back to the first one, you can simply hit back and the browser will “return” to that search.

As it stands right now, during our Active Search, we are not updating the browser’s navigation bar. So, users aren’t getting links that can be copied and pasted, and you aren’t getting history entries either, which means no back button support. Fortunately, we’ve already seen how to fix this: with the `hx-push-url` attribute.

The `hx-push-url` attribute lets you tell htmx “Please push the URL of this request into the browser’s navigation bar.” Push might seem like an odd verb to use here, but that’s the term that the underlying browser history API uses, which stems from the fact that it models browser history as a “stack” of locations: when you go to a new location, that location is “pushed” onto the stack of history elements, and when you click “back”, that location is “popped” off the history stack.

So, to get proper history support for our Active Search, all we need to do is to set the `hx-push-url` attribute to `true`.

    <input id="search" type="search" name="q"
      value="{{ request.args.get('q') or '' }}"
      hx-get="/contacts"
      hx-trigger="change, keyup delay:200ms changed"
      hx-target="tbody"
      hx-push-url="true"/> <1>

Updating the URL during active search

1.  By adding the `hx-push-url` attribute with the value `true`, htmx will update the URL when it makes a request.
    

Now, as Active Search requests are sent, the URL in the browser’s navigation bar is updated to have the proper query in it, just like when the form is submitted.

You might not _want_ this behavior. You might feel it would be confusing to users to see the navigation bar updated and have history entries for every Active Search made, for example. Which is fine: you can simply omit the `hx-push-url` attribute and it will go back to the behavior you want. The goal with htmx is to be flexible enough to achieve the UX that _you_ want, while staying within the declarative HTML model.

## Adding A Request Indicator

A final touch for our Active Search pattern is to add a request indicator to let the user know that a search is in progress. As it stands the user has no explicit signal that the active search functionality is handling a request. If the search takes a bit, a user may end up thinking that the feature isn’t working. By adding a request indicator we let the user know that the hypermedia application is busy and they should wait (hopefully not too long!) for the request to complete.

Htmx provides support for request indicators via the `hx-indicator` attribute. This attribute takes, you guessed it, a CSS selector that points to the indicator for a given element. The indicator can be anything, but it is typically some sort of animated image, such as a gif or svg file, that spins or otherwise communicates visually that “something is happening.”

Let’s add a spinner after our search input:

    <input id="search" type="search" name="q"
      value="{{ request.args.get('q') or '' }}"
      hx-get="/contacts"
      hx-trigger="change, keyup delay:200ms changed"
      hx-target="tbody"
      hx-push-url="true"
      hx-indicator="#spinner"/> <1>
    <img id="spinner" class="htmx-indicator"
      src="/static/img/spinning-circles.svg"
      alt="Request In Flight..."/> <2>

Adding a request indicator to search

1.  The `hx-indicator` attribute points to the indicator image after the input.
    
2.  The indicator is a spinning circle svg file, and has the `htmx-indicator` class on it.
    

We have added the spinner right after the input. This visually co-locates the request indicator with the element making the request, and makes it easy for a user to see that something is in fact happening.

It just works, but how does htmx make the spinner appear and disappear? Note that the indicator `img` tag has the `htmx-indicator` class on it. `htmx-indicator` is a CSS class that is automatically injected into the page by htmx. This class sets the default `opacity` of an element to `0`, which hides the element from view, while at the same time not disrupting the layout of the page.

When an htmx request is triggered that points to this indicator, another class, `htmx-request` is added to the indicator which transitions its opacity to 1. So you can use just about anything as an indicator, and it will be hidden by default. Then, when a request is in flight, it will be shown. This is all done via standard CSS classes, allowing you to control the transitions and even the mechanism by which the indicator is shown (e.g., you might use `display` rather than `opacity`).

**Use Request Indicators!**

Request indicators are an important UX aspect of any distributed application. It is unfortunate that browsers have de-emphasized their native request indicators over time, and it is doubly unfortunate that request indicators are not part of the JavaScript ajax APIs.

Be sure not to neglect this significant aspect of your application. Requests might seem instant when you are working on your application locally, but in the real world they can take quite a bit longer due to network latency. It’s often a good idea to take advantage of browser developer tools that allow you to throttle your local browser’s response times. This will give you a better idea of what real world users are seeing, and show you where indicators might help users understand exactly what is going on.

With this request indicator, we now have a pretty sophisticated user experience when compared with plain HTML, but we’ve built it all as a hypermedia-driven feature. No JSON or JavaScript to be seen. And our implementation has the benefit of being a progressive enhancement; the application will continue to work for clients that don’t have JavaScript enabled.