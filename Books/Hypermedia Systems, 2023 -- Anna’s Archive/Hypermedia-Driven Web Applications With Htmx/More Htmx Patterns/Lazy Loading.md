# Lazy Loading

With Active Search behind us, let’s move on to a very different sort of enhancement: lazy loading. Lazy loading is when the loading of a particular bit of content is deferred until later, when needed. This is commonly used as a performance enhancement: you avoid the processing resources necessary to produce some data until that data is actually needed.

Let’s add a count of the total number of contacts to Contact.app, just below the bottom of our contacts table. This will give us a potentially expensive operation that we can use to demonstrate how to add lazy loading with htmx.

First let’s update our server code in the `/contacts` request handler to get a count of the total number of contacts. We will pass that count through to the template to render some new HTML.

    @app.route("/contacts")
    def contacts():
        search = request.args.get("q")
        page = int(request.args.get("page", 1))
        count = Contact.count() <1>
        if search is not None:
            contacts_set = Contact.search(search)
            if request.headers.get('HX-Trigger') == 'search':
                return render_template("rows.html",
                  contacts=contacts_set, page=page, count=count) <2>
        else:
            contacts_set = Contact.all(page)
        return render_template("index.html",
          contacts=contacts_set, page=page, count=count)

Adding a count to the UI

1.  Get the total count of contacts from the Contact model.
    
2.  Pass the count out to the `index.html` template to use when rendering.

As with the rest of the application, in the interest of staying focused on the _hypermedia_ part of Contact.app, we’ll skip over the details of how `Contact.count()` works. We just need to know that:

*   It returns the total count of contacts in the contact database.
    
*   It may be slow (for the sake of our example).

Next lets add some HTML to our `index.html` that takes advantage of this new bit of data, showing a message next to the “Add Contact” link with the total count of users. Here is what our HTML looks like:

    <p>
      <a href="/contacts/new">Add Contacta
      > <span>({{ count }} total Contacts)span> <1>
    p>

Adding a contact count element to the application

1.  A simple span with some text showing the total number of contacts.

Well that was easy, wasn’t it? Now our users will see the total number of contacts next to the link to add new contacts, to give them a sense of how large the contact database is. This sort of rapid development is one of the joys of developing web applications the old way.

Here is what the feature looks like in our application:

![](file4.png)

Total contact count display

Beautiful.

Of course, as you probably suspected, all is not perfect. Unfortunately, upon shipping this feature to production, we start getting complaints from users that the application “feels slow.” Like all good developers faced with a performance issue, rather than guessing what the issue might be, we try to get a performance profile of the application to see what exactly is causing the problem.

It turns out, surprisingly, that the problem is that innocent looking `Contacts.count()` call, which is taking up to a second and a half to complete. Unfortunately, for reasons beyond the scope of this book, it is not possible to improve that load time, nor is possible to cache the result.

This leaves us with two options:

*   Remove the feature.
    
*   Come up with some other way to mitigate the performance issue.

Let’s assume that we can’t remove the feature, and therefore look at how we can mitigate this performance issue by using htmx instead.

## Pulling Out The Expensive Code

The first step in implementing the Lazy Load pattern is to pull the expensive code — that is, the call to `Contacts.count()` — out of the request handler for the `/contacts` endpoint.

Let’s put this function call into its own HTTP request handler as a new HTTP endpoint that we will put at `/contacts/count`. For this new endpoint, we won’t need to render a template at all: its sole job is going to be to render that small bit of text that is in the span, “(22 total Contacts).”

Here is what the new code will look like:

    @app.route("/contacts")
    def contacts():
        search = request.args.get("q")
        page = int(request.args.get("page", 1)) <1>
        if search is not None:
            contacts_set = Contact.search(search)
            if request.headers.get('HX-Trigger') == 'search':
                return render_template("rows.html",
                  contacts=contacts_set, page=page)
        else:
            contacts_set = Contact.all(page)
        return render_template("index.html",
          contacts=contacts_set, page=page) <2>
    
    @app.route("/contacts/count")
    def contacts_count():
        count = Contact.count() <3>
        return "(" + str(count) + " total Contacts)" <4>

Pulling the expensive code out

1.  We no longer call `Contacts.count()` in this handler.
    
2.  `Count` is no longer passed out to the template to render in the `/contacts` handler.
    
3.  We create a new handler at the `/contacts/count` path that does the expensive calculation.
    
4.  Return the string with the total number of contacts.

So now we have moved the performance issue out of the `/contacts` handler code, which renders the main contacts table, and created a new HTTP endpoint that will produce this expensive-to-create count string for us.

Now we need to get the content from this new handler _into_ the span, somehow. As we said earlier, the default behavior of htmx is to place any content it receives for a given request into the `innerHTML` of an element, and that turns out to be exactly what we want here: we want to retrieve this text and put it into the `span`. So we can simply place an `hx-get` attribute on the span, pointing to this new path, and do exactly that.

However, recall that the default _event_ that will trigger a request for a `span` element in htmx is the `click` event. Well, that’s not what we want! Instead, we want this request to trigger immediately, when the page loads.

To do this, we can add the `hx-trigger` attribute to update the trigger of the requests for the element, and use the `load` event.

The `load` event is a special event that htmx triggers on all content when it is loaded into the DOM. By setting `hx-trigger` to `load`, we will cause htmx to issue the `GET` request when the `span` element is loaded into the page.

Here is our updated template code:

    <p>
      <a href="/contacts/new">Add Contacta
      > <span hx-get="/contacts/count" hx-trigger="load">span> <1>
    p>

Adding a contact count element to the application

1.  Issue a `GET` to `/contacts/count` when the `load` event occurs.

Note that the `span` starts empty: we have removed the content from it, and we are allowing the request to `/contacts/count` to populate it instead.

And, check it out, our `/contacts` page is fast again! When you navigate to the page it feels very snappy and profiling shows that yes, indeed, the page is loading much more quickly. Why is that? Well, we’ve deferred the expensive calculation to a secondary request, allowing the initial request to finish loading faster.

You might say “OK, great, but it’s still taking a second or two to get the total count on the page.” True, but often the user may not be particularly interested in the total count. They may just want to come to the page and search for an existing user, or perhaps they may want to edit or add a user. The total count of contacts is just a “nice to have” bit of information in these cases.

By deferring the calculation of the count in this manner we let users get on with their use of the application while we perform the expensive calculation.

Yes, the total time to get all the information on the screen takes just as long. It actually will be a bit longer, since we now need two HTTP requests to get all the information for the page. But the _perceived performance_ for the end user will be much better: they can do what they want nearly immediately, even if some information isn’t available instantaneously.

Lazy Loading is a great tool to have in your belt when optimizing web application performance.

## Adding An Indicator

A shortcoming of the current implementation is that currently there is no indication that the count request is in flight, it just appears at some point when the request finishes.

This isn’t ideal. What we want here is an indicator, just like we added in our Active Search example. And, in fact, we can simply reuse that same exact spinner image, copy-and-pasted into the new HTML we have created.

Now, in this case, we have a one-time request and, once the request is over, we are not going to need the spinner anymore. So it doesn’t make sense to use the exact same approach we did with the active search example. Recall that in that case we placed a spinner _after_ the span and using the `hx-indicator` attribute to point to it.

In this case, since the spinner is only used once, we can put it _inside_ the content of the span. When the request completes the content in the response will be placed inside the span, replacing the spinner with the computed contact count. It turns out that htmx allows you to place indicators with the `htmx-indicator` class on them inside of elements that issue htmx-powered requests. In the absence of an `hx-indicator` attribute, these internal indicators will be shown when a request is in flight.

So let’s add that spinner from the active search example as the initial content in our span:

    <span hx-get="/contacts/count" hx-trigger="load">
      <img id="spinner" class="htmx-indicator"
        src="/static/img/spinning-circles.svg"/> <1>
    span>

Adding an indicator to our lazily loaded content

1.  Yep, that’s it.

Now when the user loads the page, rather than having the total contact count magically appear, there is a nice spinner indicating that something is coming. Much better.

Note that all we had to do was copy and paste our indicator from the active search example into the `span`. Once again we see how htmx provides flexible, composable features and building blocks. Implementing a new feature is often just copy-and-paste, maybe a tweak or two, and you are done.

## But That’s Not Lazy!

You might say “OK, but that’s not really lazy. We are still loading the count immediately when the page is loaded, we are just doing it in a second request. You aren’t really waiting until the value is actually needed.”

Fine. Let’s make it _lazy_ lazy: we’ll only issue the request when the `span` scrolls into view.

To do that, lets recall how we set up the infinite scroll example: we used the `revealed` event for our trigger. That’s all we want here, right? When the element is revealed we issue the request?

Yep, that’s it. Once again, we can mix and match concepts across various UX patterns to come up with solutions to new problems in htmx.

    <span hx-get="/contacts/count" hx-trigger="revealed"> <1>
      <img id="spinner" class="htmx-indicator"
        src="/static/img/spinning-circles.svg"/>
    span>

Making it truly lazy

1.  Change the `hx-trigger` to `revealed`.

Now we have a truly lazy implementation, deferring the expensive computation until we are absolutely sure we need it. A pretty cool trick, and, again, a simple one-attribute change demonstrates the flexibility of both htmx and the hypermedia approach.