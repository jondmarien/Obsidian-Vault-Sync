# Another Application Improvement: Paging

Let’s move on from the contact editing page for a bit and improve the root page of the application, found at the `/contacts` path and rendering the `index.html` template.

Currently, Contact.app does not support paging: if there are 10,000 contacts in the database we will show all 10,000 contacts on the root page. Showing so much data can bog a browser (and a server) down, so most web applications adopt a concept of “paging” to deal with data sets this large, where only one “page” of a smaller number of items is shown, with the ability to navigate around the pages in the data set.

Let’s fix our application so that we only show ten contacts at a time with a “Next” and “Previous” link if there are more than 10 contacts in the contact database.

The first change we will make is to add a simple paging widget to our `index.html` template.

We will conditionally include two links:

*   If we are beyond the “first” page, we will include a link to the previous page
    
*   If there are ten contacts in the current result set, we will include a link to the next page

This isn’t a perfect paging widget: ideally we’d show the number of pages and offer the ability to do more specific page navigation, and there is the possibility that the next page might have 0 results in it since we aren’t checking the total results count, but it will do for now for our simple application.

Let’s look at the jinja template code for this in `index.html`.

    <div>
      <span style="float: right"> <1>
        {% if page > 1 %}
          <a href="/contacts?page={{ page - 1 }}">Previousa> <2>
        {% endif %}
        {% if contacts|length == 10 %}
          <a href="/contacts?page={{ page + 1 }}">Nexta> <1>
        {% endif %}
      span>
    div>

Adding paging widgets to our list of contacts

1.  Include a new div under the table to hold our navigation links.
    
2.  If we are beyond page 1, include an anchor tag with the page decremented by one.
    
3.  If there are 10 contacts in the current page, include an anchor tag linking to the next page by incrementing it by one.

Note that here we are using a special jinja filter syntax `contacts|length` to compute the length of the contacts list. The details of this filter syntax is beyond the scope of this book, but in this case you can think of it as invoking the `contacts.length` property and then comparing that with `10`.

Now that we have these links in place, let’s address the server-side implementation of paging.

We are using the `page` request parameter to encode the paging state of the UI. So, in our handler, we need to look for that `page` parameter and pass that through to our model, as an integer, so the model knows which page of contacts to return:

    @app.route("/contacts")
    def contacts():
        search = request.args.get("q")
        page = int(request.args.get("page", 1)) <1>
        if search is not None:
            contacts_set = Contact.search(search)
        else:
            contacts_set = Contact.all(page) <2>
        return render_template("index.html",
          contacts=contacts_set, page=page)

Adding paging to our request handler

1.  Resolve the page parameter, defaulting to page 1 if no page is passed in.
    
2.  Pass the page through to the model when loading all contacts so it knows which page of 10 contacts to return.

This is fairly straightforward: we just need to get another parameter, like the `q` parameter we passed in for searching contacts earlier, convert it to an integer and then pass it through to the `Contact` model, so it knows which page to return.

And, with that small change, we are done: we now have a very basic paging mechanism for our web application.

And, believe it or not, it is already using AJAX, thanks to our use of `hx-boost` in the application. Easy!

## Click To Load

This paging mechanism is fine for a basic web application, and it is used extensively on the internet. But it has some drawbacks associated with it: every time you click the “Next” or “Previous” buttons you get a whole new page of contacts and lose any context you had on the previous page.

Sometimes a more advanced paging UI pattern might be better. Maybe, rather than loading in a new page of elements and replacing the current elements, it would be nicer to append the next page of elements _inline_, after the current elements.

This is the common “click to load” UX pattern, found in more advanced web applications.

![](file3.png)

A Click To Load UI

Here, you have a button that you can click, and it will load the next set of contacts directly into the page, rather than “paging” to the next page. This allows you to keep the current contacts “in context” visually on the page, but still progress through them as you would in a normal, paged user interface.

Let’s see how we can implement this UX pattern in htmx.

It’s actually surprisingly simple: we can just take the existing “Next” link and repurpose it a bit using nothing but a few htmx attributes!

We want to have a button that, when clicked, appends the rows from the next page of contacts to the current, existing table, rather than re-rendering the whole table. This can be achieved by adding a new row to our table that has just such a button in it:

    <tbody>
    {% for contact in contacts %}
      <tr>
        <td>{{ contact.first }}td>
        <td>{{ contact.last }}td>
        <td>{{ contact.phone }}td>
        <td>{{ contact.email }}td>
        <td>
          <a href="/contacts/{{ contact.id }}/edit">Edita>
          <a href="/contacts/{{ contact.id }}">Viewa>td>
      tr>
    {% endfor %}
    {% if contacts|length == 10 %} <1>
      <tr>
        <td colspan="5" style="text-align: center">
          <button hx-target="closest tr" <2>
            hx-swap="outerHTML" <3>
            hx-select="tbody > tr" <4>
            hx-get="/contacts?page={{ page + 1 }}">
            Load More
          button>
        td>
      tr>
    {% endif %}
    tbody>

Changing to “click to load”

1.  Only show “Load More” if there are 10 contact results in the current page.
    
2.  Target the closest enclosing row.
    
3.  Replace the entire row with the response from the server.
    
4.  Select out the table rows from the response.

Let’s go through each attribute in detail here.

First, we are using `hx-target` to target the “closest” `tr` element, that is, the closest _parent_ table row.

Second, we want to replace this _entire_ row with whatever content comes back from the server.

Third, we want to yank out only the `tr` elements in the response. We are replacing this `tr` element with a new set of `tr` elements, which will have additional contact information in them, as well as, if necessary, a new “Load More” button that points to the _next_ next page. To do this, we use a CSS selector `tbody > tr` to ensure we only pull out the rows in the body of the table in the response. This avoids including rows in the table header, for example.

Finally, we issue an HTTP `GET` to the url that will serve the next page of contacts, which looks just like the “Next” link from above.

Somewhat surprisingly, no server-side changes are necessary for this new functionality. This is because of the flexibility that htmx gives you with respect to how it processes server responses.

So, four attributes, and we now have a sophisticated “Click To Load” UX, via htmx.

## Infinite Scroll

Another common pattern for dealing with large sets of things is known as the “Infinite Scroll” pattern. In this pattern, as the last item of a list or table of elements is scrolled into view, more elements are loaded and appended to the list or table.

Now, this behavior makes more sense in situations where a user is exploring a category or series of social media posts, rather than in the context of a contact application. However, for completeness, and to just show what you can do with htmx, we will implement this pattern as well.

It turns out that we can repurpose the “Click To Load” code to implement this new pattern quite easily: if you think about it for a moment, infinite scroll is really just the “Click To Load” logic, but rather than loading when a click event occurs, we want to load when an element is “revealed” in the view portal of the browser.

As luck would have it, htmx offers a synthetic (non-standard) DOM event, `revealed` that can be used in tandem with the `hx-trigger` attribute, to trigger a request when, well, when an element is revealed.

So let’s convert our button to a span and take advantage of this event:

    {% if contacts|length == 10 %}
      <tr>
        <td colspan="5" style="text-align: center">
          <span hx-target="closest tr"
            hx-trigger="revealed"
            hx-swap="outerHTML"
            hx-select="tbody > tr"
            hx-get="/contacts?page={{ page + 1 }}">Loading More...span>
        td>
      tr>
    {% endif %}

Changing to “infinite scroll”

1.  We have converted our element from a button to a span, since the user will not be clicking on it.
    
2.  We trigger the request when the element is revealed, that is when it comes into view in the portal.

All we needed to do to convert from “Click to Load” to “Infinite Scroll” was to update our element to be a span and then add the `revealed` event trigger.

The fact that switching to infinite scroll was so easy shows how well htmx generalizes HTML: just a few attributes allow us to dramatically expand what we can achieve in the hypermedia.

And, again, we are doing all this while taking advantage of the RESTful model of the web. Despite all this new behavior, we are still exchanging hypermedia with the server, with no JSON API response to be seen.

As the web was designed.

# HTML Notes: Caution With Modals and “display: none”

_Think twice about modals._ Modal windows have become popular, almost standard, in many web applications today.

Unfortunately, modal windows do not play well with much of the infrastructure of the web and introduce client-side state that can be difficult (though not impossible) to integrate cleanly with the hypermedia-based approach.

Modal windows can be used safely for views that don’t constitute a resource or correspond to a domain entity:

*   Alerts
    
*   Confirmation dialogs
    
*   Forms for creating/updating entities

Otherwise, consider using alternatives such as inline editing, or a separate page, rather than a modal.

_Use `display: none;` with care_. The issue is that it is not purely cosmetic — it also removes elements from the accessibility tree and keyboard focus. This is sometimes done to present the same content to visual and aural interfaces. If you want to hide an element visually without hiding it from assistive technology (e.g. the element contains information that is communicated through styling), you can use this utility class:

    .vh {
        clip: rect(0 0 0 0);
        clip-path: inset(50%);
        block-size: 1px;
        inline-size: 1px;
        overflow: hidden;
        white-space: nowrap;
    }

`vh` is short for “visually hidden.” This class uses multiple methods and workarounds to make sure no browser removes the element’s function.