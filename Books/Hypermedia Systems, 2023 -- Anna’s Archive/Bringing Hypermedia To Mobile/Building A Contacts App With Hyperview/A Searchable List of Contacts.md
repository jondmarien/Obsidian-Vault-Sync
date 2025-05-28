# A Searchable List of Contacts

We will start building our Hyperview app with the entry point screen, the list of contacts. For the initial version of this screen, let’s support the following features from the web app:

*   display a scrollable list of contacts
    
*   “search-as-you-type” field above the list
    
*   “infinite-scroll” to load more contacts as the user scrolls through

Additionally, we will add a “pull-to-refresh” interaction on the list, since users expect this from list UIs in mobile apps.

If you recall, all of the pages in the Contacts web app extended a common base template, `layout.html`. We need a similar base template for the screens of the mobile app. This base template will contain the style rules of our UI, and a basic structure common to all screens. Let’s call it `layout.xml`.

    <doc xmlns="https://hyperview.org/hyperview">
      <screen>
        <styles>styles>
        <body style="body" safe-area="true">
          <header style="header">
            {% block header %} <1>
              <text style="header-title">Contact.apptext>
            {% endblock %}
          header>
    
          <view style="main">
            {% block content %}{% endblock %} <2>
          view>
        body>
      screen>
    doc>

Base template `hv/layout.xml`

1.  The header section of the template, with a default title.
    
2.  The content section of the template, to be provided by other templates.

We’re using the HXML tags and attributes covered in the previous chapter. This template sets up a basic screen layout using , , ,

, and tags. Note that the HXML syntax plays well with the Jinja templating library. Here, we’re using Jinja’s blocks to define two sections (`header` and `content`) that will hold the unique content of a screen. With our base template completed, we can create a template specifically for the contacts list screen.

    {% extends 'hv/layout.xml' %} <1>
    
    {% block content %} <2>
      <form> <3>
        <text-field name="q" value="" placeholder="Search..."
          style="search-field" />
        <list id="contacts-list"> <4>
          {% include 'hv/rows.xml' %}
        list>
      form>
    {% endblock %}

Start of `hv/index.xml`

1.  Extend the base layout template
    
2.  Override the `content` block of the layout template
    
3.  Create a search form that will issue an HTTP `GET` to `/contacts`
    
4.  The list of contacts, using a Jinja `include` tag.

This template extends the base `layout.xml`, and overrides the `content` block with a

. At first, it might seem strange that the form wraps both the and the elements. But remember: in Hyperview, the form data gets included in any request originating from a child element. We will soon add interactions to the list (pull to refresh) that will require the form data. Note the use of a Jinja `include` tag to render the HXML for the rows of contacts in the list (`hv/rows.xml`). Just like in the HTML templates, we can use the `include` to break up our HXML into smaller pieces. It also allows the server to respond with just the `rows.xml` template for interactions like searching, infinite scroll, and pull-to-refresh.

    <items xmlns="https://hyperview.org/hyperview"> <1>
      {% for contact in contacts %} <2>
        <item key="{{ contact.id }}" style="contact-item"> <3>
          <text style="contact-item-label">
            {% if contact.first %}
              {{ contact.first }} {{ contact.last }}
            {% elif contact.phone %}
              {{ contact.phone }}
            {% elif contact.email %}
              {{ contact.email }}
            {% endif %}
          text>
        item>
      {% endfor %}
    items>

`hv/rows.xml`

1.  An HXML element that groups a set of elements in a common ancestor.
    
2.  Iterate over the contacts that were passed in to the template.
    
3.  Render an for each contact, showing the name, phone number, or email.

In the web app, each row in the list showed the contact’s name, phone number, and email address. But in a mobile app, we have less real-estate. It would be hard to cram all this information into one line. Instead, the row just shows the contact’s first and last name, and falls back to email or phone if the name is not set. To render the row, we again make use of Jinja template syntax to render dynamic text with data passed to the template.

We now have templates for the base layout, the contacts screen, and the contact rows. But we still have to update the Flask views to use these templates. Let’s take a look at the `contacts()` view in its current form, written for the web app:

    @app.route("/contacts")
    def contacts():
        search = request.args.get("q")
        page = int(request.args.get("page", 1))
        if search:
            contacts_set = Contact.search(search)
            if request.headers.get('HX-Trigger') == 'search':
                return render_template("rows.html",
                  contacts=contacts_set, page=page)
        else:
            contacts_set = Contact.all(page)
        return render_template("index.html",
          contacts=contacts_set, page=page)

`app.py`

This view supports fetching a set of contacts based on two query params, `q` and `page`. It also decides whether to render the full page (`index.html`) or just the contact rows (`rows.html`) based on the `HX-Trigger` header. This presents a minor problem. The `HX-Trigger` header is set by the htmx library; there’s no equivalent feature in Hyperview. Moreover, there are multiple scenarios in Hyperview that require us to respond with just the contact rows:

*   searching
    
*   pull-to-refresh
    
*   loading the next page of contacts

Since we can’t depend on a header like `HX-Trigger`, we need a different way to detect if the client needs the full screen or just the rows in the response. We can do this by introducing a new query param, `rows_only`. When this param has the value `true`, the view will respond to the request by rendering the `rows.xml` template. Otherwise, it will respond with the `index.xml` template:

    @app.route("/contacts")
    def contacts():
        search = request.args.get("q")
        page = int(request.args.get("page", 1))
        rows_only = request.args.get("rows_only") == "true" <1>
        if search:
            contacts_set = Contact.search(search)
        else:
            contacts_set = Contact.all(page)
    
        template_name = "hv/rows.xml" if rows_only else "hv/index.xml" <1>
        return render_template(template_name,
          contacts=contacts_set, page=page)

`app.py`

1.  Check for a new `rows_only` query param.
    
2.  Render the appropriate HXML template based on `rows_only`.

There’s one more change we have to make. Flask assumes that most views will respond with HTML. So Flask defaults the `Content-Type` response header to a value of `text/html`. But the Hyperview client expects to receive HXML content, indicated by a `Content-Type` response header with value `application/vnd.hyperview+xml`. The client will reject responses with a different content type. To fix this, we need to explicitly set the `Content-Type` response header in our Flask views. We will do this by introducing a new helper function, `render_to_response()`:

    def render_to_response(template_name, *args, **kwargs):
        content = render_template(template_name, *args, **kwargs) <1>
        response = make_response(content) <2>
        response.headers['Content-Type'] =
          'application/vnd.hyperview+xml' <3>
        return response

`app.py`

1.  Renders the given template with the supplied arguments and keyword arguments.
    
2.  Create an explicit response object with the rendered template.
    
3.  Sets the response `Content-Type` header to XML.

As you can see, this helper function uses `render_template()` under the hood. `render_template()` returns a string. This helper function uses that string to create an explicit `Response` object. The response object has a `headers` attribute, allowing us to set and change the response headers. Specifically, `render_to_response()` sets `Content-Type` to `application/vnd.hyperview+xml` so that the Hyperview client recognizes the content. This helper is a drop-in replacement for `render_template` in our views. So all we need to do is update the last line of the `contacts()` function.

    return render_to_response(template_name,
      contacts=contacts_set, page=page) <1>

`contacts() function`

1.  Render the HXML template to an XML response.

With these changes to the `contacts()` view, we can finally see the fruits of our labor. After restarting the backend and refreshing the screen in our mobile app, we can see the contacts screen!

![](file9.png)

Contacts Screen

## Searching Contacts

So far, we have a mobile app that displays a screen with a list of contacts. But our UI doesn’t support any interactions. Typing a query in the search field doesn’t filter the list of contacts. Let’s add a behavior to the search field to implement a search-as-you-type interaction. This requires expanding to add a element.

    <text-field name="q" value="" placeholder="Search..."
      style="search-field">
      <behavior
        trigger="change" <1>
        action="replace-inner" <2>
        target="contacts-list" <3>
        href="/contacts?rows_only=true" <4>
        verb="get" <5>
      />
    text-field>

Snippet of `hv/index.xml`

1.  This behavior will trigger when the value of the text field changes.
    
2.  When the behavior triggers, the action will replace the content inside the target element.
    
3.  The target of the action is the element with ID `contacts-list`.
    
4.  The replacement content will be fetched from this URL path.
    
5.  The replacement content will be fetched with the `GET` HTTP method.

The first thing you’ll notice is that we changed the text field from using a self-closing tag () to using opening and closing tags (`…​`). This allows us to add a child element to define an interaction.

The `trigger="change"` attribute tells Hyperview that a change to the value of the text field will trigger an action. Any time the user edits the content of the text field by adding or deleting characters, an action will trigger.

The remaining attributes on the element define the action. `action="replace-inner"` means the action will update content on the screen, by replacing the HXML content of an element with new content. For `replace-inner` to do its thing, we need to know two things: the current element on the screen that will be targeted by the action, and the content that will used for the replacement. `target="contacts-list"` tells us the ID of the current element. Note that we set `id="contacts-list"` on the element in `index.xml`. So when the user enters a search query into the text field, Hyperview will replace the content of (a bunch of elements) with new content ( elements that match the search query) received in the relative href response. The domain here is inferred from the domain used to fetch the screen. Note that `href` includes our `rows_only` query param; we want the response to only include the rows and not the entire screen.

![](file10.png)

Searching for Contacts

That’s all it takes to add search-as-you-type functionality to our mobile app! As the user types a search query, the client will make requests to the backend and replace the list with the search results. You may be wondering, how does the backend know the query to use? The `href` attribute in the behavior does not include the `q` param expected by our backend. But remember, in `index.xml`, we wrapped the and elements with a element. The element defines a group of inputs that will be serialized and included in any HTTP requests triggered by its child elements. In this case, the element surrounds the search behavior and the text field. So the value of the will be included in our HTTP request for the search results. Since we are making a `GET` request, the name and value of the text field will be serialized as a query param. Any existing query params on the `href` will be preserved. This means the actual HTTP request to our backend looks like `GET /contacts?rows_only=true&q=Car`. Our backend already supports the `q` param for searching, so the response will include rows that match the string “Car.”

## Infinite scroll

If the user has hundreds or thousands of contacts, loading them all at once may result in poor app performance. That’s why most mobile apps with long lists implement an interaction known as “infinite scroll.” The app loads a fixed number of initial items in the list, let’s say 100 items. If the user scrolls to the bottom of the list, they see a spinner indicating more content is loading. Once the content is available, the spinner is replaced with the next page of 100 items. These items are appended to the list, they don’t replace the first set of items. So the list now contains 200 items. If the user scrolls to the bottom of the list again, they will see another spinner, and the app will load the next set of content. Infinite scroll improves app performance in two ways:

*   The initial request for 100 items will be processed quickly, with predictable latency.
    
*   Subsequent requests can also be fast and predictable.
    
*   If the user doesn’t scroll to the bottom of the list, the app won’t have to make subsequent requests.

Our Flask backend already supports pagination on the `/contacts` endpoint via the `page` query param. We just need to modify our HXML templates to make use of this parameter. To do this, let’s edit `rows.xml` to add a new below the Jinja for-loop:

    <items xmlns="https://hyperview.org/hyperview">
      {% for contact in contacts %}
        <item key="{{ contact.id }}" style="contact-item">
          
        item>
      {% endfor %}
      {% if contacts|length > 0 %}
        <item key="load-more" id="load-more" style="load-more-item"> <1>
          <behavior
            trigger="visible" <2>
            action="replace" <3>
            target="load-more" <4>
            href="/contacts?rows_only=true&page={{ page + 1 }}" <5>
            verb="get"
          />
          <spinner /> <6>
        item>
      {% endif %}
    items>

Snippet of `hv/rows.xml`

1.  Include an extra in the list to show the spinner.
    
2.  The item behavior triggers when visible in the viewport.
    
3.  When triggered, the behavior will replace an element on the screen.
    
4.  The element to be replaced is the item itself (ID `load-more`).
    
5.  Replace the item with the next page of content.
    
6.  The spinner element.

If the current list of contacts passed to the template is empty, we can assume there’s no more contacts to fetch from the backend. So we use a Jinja conditional to only include this new if the list of contacts is non-empty. This new element gets an ID and a behavior. The behavior defines the infinite scroll interaction.

Up until now, we’ve seen `trigger` values of `change` and `refresh`. But to implement infinite scroll, we need a way to trigger the action when the user scrolls to the bottom of the list. The `visible` trigger can be used for this exact purpose. It will trigger the action when the element with the behavior is visible in the device viewport. In this case, the new element is the last item in the list, so the action will trigger when the user scrolls down far enough for the item to enter the viewport. As soon as the item is visible, the action will make an HTTP GET request, and replace the loading element with the response content.

Note that our href must include the `rows_only=true` query param, so that our response will only include HXML for the contact items, and not the entire screen. Also, we’re passing the `page` query param, incrementing the current page number to ensure we load the next page.

What happens when there’s more than one page of items? The initial screen will include the first 100 items, plus the “load-more” item at the bottom. When the user scrolls to the bottom of the screen, Hyperview will request the second page of items (`&page=2`), and replace the “load-more” item with the new items. But this second page of items will include a new “load-more” item. So once the user scrolls through all of the items from the second page, Hyperview will again request more items (`&page=3`). And once again, the “load-more” item will be replaced with the new items. This will continue until all of the items will be loaded on the screen. At that point, there will be no more contacts to return, the response will not include another “load-more” item, and our pagination is over.

## Pull-to-refresh

Pull-to-refresh is a common interaction in mobile apps, especially on screens featuring dynamic content. It works like this: At the top of a scrolling view, the user pulls the scrolling content downwards with a swipe-down gesture. This reveals a spinner “below” the content. Pulling the content down sufficiently far will trigger a refresh. While the content refreshes, the spinner remains visible on screen, indicating to the user that the action is still taking place. Once the content is refreshed, the content retracts back up to its default position, hiding the spinner and letting the user know that the interaction is done.

![](file11.png)

Pull-to-refresh

This pattern is so common and useful that it’s built in to Hyperview via the `refresh` action. Let’s add pull-to-refresh to our list of contacts to see it in action.

    <list id="contacts-list"
      trigger="refresh" <1>
      action="replace-inner" <2>
      target="contacts-list" <3>
      href="/contacts?rows_only=true" <4>
      verb="get" <5>
    >
      {% include 'hv/rows.xml' %}
    list>

Snippet of `hv/index.xml`

1.  This behavior will trigger when the user does a “pull-to-refresh” gesture.
    
2.  When the behavior triggers, this action will replace the content inside the target element.
    
3.  The target of the action is the element itself.
    
4.  The replacement content will be fetched from this URL path.
    
5.  The replacement content will be fetched with the `GET` HTTP method.

You’ll notice something unusual in the snippet above: rather than adding a element to the , we added the behavior attributes directly to the element. This is a shorthand notation that’s sometimes useful for specifying single behaviors on an element. It is equivalent to adding a element to the with the same attributes.

So why did we use the shorthand syntax here? It has to do with the action, `replace-inner`. Remember, this action replaces all child elements of the target with the new content. This includes elements too! Let’s say our did contain a . If the user did a search or pull-to-refresh, we would replace the content of with the content from `rows.xml`. The would no longer be defined on the , and subsequent attempts to pull-to-refresh would not work. By defining the behavior as attributes of , the behavior will persist even when replacing the items in the list. Generally, we prefer to use explicit elements in HXML. It makes it easier to define multiple behaviors, and to move the behavior around while refactoring. But the shorthand syntax is good to apply in situations like this.

## Viewing The Details Of A Contact

Now that our contacts list screen is in good shape, we can start adding other screens to our app. The natural next step is to create a details screen, which appears when the user taps an item in the contacts list. Let’s update the template that renders the contact elements, and add a behavior to show the details screen.

    <items xmlns="https://hyperview.org/hyperview">
      {% for contact in contacts %}
        <item key="{{ contact.id }}" style="contact-item">
          <behavior trigger="press" action="push"
            href="/contacts/{{ contact.id }}" /> <1>
          <text style="contact-item-label">
            
          text>
        item>
      {% endfor %}
    items>

`hv/rows.xml`

1.  Behavior to push the contact details screen onto the stack when pressed.

Our Flask backend already has a route for serving the contact details at `/contacts/`. In our template, we use a Jinja variable to dynamically generate the URL path for the current contact in the for-loop. We also used the “push” action to show the details by pushing a new screen onto the stack. If you reload the app, you can now tap any contact in the list, and Hyperview will open the new screen. However, the new screen will show an error message. That’s because our backend is still returning HTML in the response, and the Hyperview client expects HXML. Let’s update the backend to respond with HXML and the proper headers.

    @app.route("/contacts/")
    def contacts_view(contact_id=0):
        contact = Contact.find(contact_id)
        return render_to_response("hv/show.xml", contact=contact) <1>

`app.py`

1.  Generate an XML response from a new template file.

Just like the `contacts()` view, `contacts_view()` uses `render_to_response()` to set the `Content-Type` header on the response. We’re also generating the response from a new HXML template, which we can create now:

    {% extends 'hv/layout.xml' %} <1>
    
    {% block header %} <2>
      <text style="header-button">
        <behavior trigger="press" action="back" /> <3>
        Back
      text>
    {% endblock %}
    
    {% block content %} <4>
    <view style="details">
      <text style="contact-name">
        {{ contact.first }} {{ contact.last }}
      text>
    
      <view style="contact-section">
        <text style="contact-section-label">Phonetext>
        <text style="contact-section-info">{{contact.phone}}text>
      view>
    
      <view style="contact-section">
        <text style="contact-section-label">Emailtext>
        <text style="contact-section-info">{{contact.email}}text>
      view>
    view>
    {% endblock %}

`hv/show.xml`

1.  Extend the base layout template.
    
2.  Override the `header` block of the layout template to include a “Back” button.
    
3.  Behavior to navigate to the previous screen when pressed.
    
4.  Override the `content` block to show the full details of the selected contact.

The contacts detail screen extends the base `layout.xml` template, just like we did in `index.xml`. This time, we’re overriding content in both the `header` block and `content` block. Overriding the header block lets us add a “Back” button with a behavior. When pressed, the Hyperview client will unwind the navigation stack and return the user to the contacts list.

Note that triggering this behavior is not the only way to navigate back. The Hyperview client respects navigation conventions on different platforms. On iOS, users can also navigate to the previous screen by swiping right from the left edge of the device. On Android, users can also navigate to the previous screen by pressing the hardware back button. We don’t need to specify anything extra in the HXML to get these interactions.

![](file12.png)

Contact Details Screen

With just a few simple changes, we’ve gone from a single-screen app to a multi-screen app. Note that we didn’t need to change anything in the actual mobile app code to support our new screen. This is a big deal. In traditional mobile app development, adding screens can be a significant task. Developers need to create the new screen, insert it into the appropriate place of the navigation hierarchy, and write code to open the new screen from existing screens. In Hyperview, we just added a behavior with `action="push"`.