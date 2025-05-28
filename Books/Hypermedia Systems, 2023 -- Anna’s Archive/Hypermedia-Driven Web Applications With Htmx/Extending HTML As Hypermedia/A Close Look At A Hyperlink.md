# A Close Look At A Hyperlink

It turns out that we can boost the interactivity of our application and address both of these issues _without_ resorting to the SPA approach. We can do so by using a _hypermedia-oriented_ JavaScript library, [htmx](https://htmx.org). The authors of this book built htmx specifically to extend HTML as a hypermedia and address the issues with legacy HTML applications we mentioned above (as well as a few others.)

Before we get into how htmx allows us to improve the UX of our Web 1.0 style application, let’s revisit the hyperlink/anchor tag from Chapter

1.  Recall, a hyperlink is what is known as a _hypermedia control_,
    

a mechanism that describes some sort of interaction with a server by encoding information about that interaction directly and completely within the control itself.

Consider again this simple anchor tag which, when interpreted by a browser, creates a hyperlink to the website for this book:

    <a href="https://hypermedia.systems/">
      Hypermedia Systems
    a>

A simple hyperlink, revisited

Let’s break down exactly what happens with this link:

*   The browser will render the text “Hypermedia Systems” to the screen, likely with a decoration indicating it is clickable.
    
*   Then, when a user clicks on the text…​
    
*   The browser will issue an HTTP `GET` to `https://hypermedia.systems`…​
    
*   The browser will load the HTML body of the HTTP response into the browser window, replacing the current document.
    

So we have four aspects of a simple hypermedia link like this, with the last three aspects supplying the mechanism that distinguishes a hyperlink from “normal” text and, thus, makes this a hypermedia control.

Now, let’s take a moment and think about how we can _generalize_ these last three aspects of a hyperlink.

## Why Only Anchors & Forms?

Consider: what makes anchor tags (and forms) so special?

Why can’t other elements issue HTTP requests as well?

For example, why shouldn’t `button` elements be able to issue HTTP requests? It seems arbitrary to have to wrap a form tag around a button just to make deleting contacts work in our application, for example.

Maybe: other elements should be able to issue HTTP requests as well. Maybe other elements should be able to act as hypermedia controls on their own.

This is our first opportunity to generalize HTML as a hypermedia.

**Opportunity 1**

HTML could be extended to allow _any_ element to issue a request to the server and act as a hypermedia control.

## Why Only Click & Submit Events?

Next, let’s consider the event that triggers the request to the server on our link: a click event.

Well, what’s so special about clicking (in the case of anchors) or submitting (in the case of forms) things? Those are just two of many, many events that are fired by the DOM, after all. Events like mouse down, or key up, or blur are all events you might want to use to issue an HTTP request.

Why shouldn’t these other events be able to trigger requests as well?

This gives us our second opportunity to expand the expressiveness of HTML:

**Opportunity 2**

HTML could be extended to allow _any_ event — not just a click, as in the case of hyperlinks — to trigger HTTP requests.

## Why Only GET & POST?

Getting a bit more technical in our thinking leads us to the problem we noted earlier: plain HTML only give us access to the `GET` and `POST` actions of HTTP.

HTTP _stands_ for Hypertext Transfer Protocol, and yet the format it was explicitly designed for, HTML, only supports two of the five developer-facing request types. You _have_ to use JavaScript and issue an AJAX request to get at the other three: `DELETE`, `PUT` and `PATCH`.

Let’s recall what these different HTTP request types are designed to represent:

*   `GET` corresponds with “getting” a representation for a resource from a URL: it is a pure read, with no mutation of the resource.
    
*   `POST` submits an entity (or data) to the given resource, often creating or mutating the resource and causing a state change.
    
*   `PUT` submits an entity (or data) to the given resource for update or replacement, again likely causing a state change.
    
*   `PATCH` is similar to `PUT` but implies a partial update and state change rather than a complete replacement of the entity.
    
*   `DELETE` deletes the given resource.
    

These operations correspond closely to the CRUD operations we discussed in Chapter 2. By giving us access to only two of the five, HTML hamstrings our ability to take full advantage of HTTP.

This gives us our third opportunity to expand the expressiveness of HTML:

**Opportunity 3**

HTML could be extended so that it allows access to the missing three HTTP methods, `PUT`, `PATCH` and `DELETE`.

## Why Only Replace The Entire Screen?

As a final observation, consider the last aspect of a hyperlink: it replaces the _entire_ screen when a user clicks on it.

It turns out that this technical detail is the primary culprit for poor user experience in Web 1.0 Applications. A full page refresh can cause a flash of unstyled content, where content “jumps” on the screen as it transitions from its initial to its styled final form. It also destroys the scroll state of the user by scrolling to the top of the page, removes focus from a focused element and so forth.

But, if you think about it, there is no rule saying that hypermedia exchanges _must_ replace the entire document.

This gives us our fourth, final and perhaps most important opportunity to generalize HTML:

**Opportunity 4**

HTML could be extended to allow the responses to requests to replace elements _within_ the current document, rather than requiring that they replace the _entire_ document.

This is actually a very old concept in hypermedia. Ted Nelson, in his 1980 book “Literary Machines” coined the term _transclusion_ to capture this idea: the inclusion of content into an existing document via a hypermedia reference. If HTML supported this style of “dynamic transclusion,” then Hypermedia-Driven Applications could function much more like a Single Page Application, where only part of the DOM is updated by a given user interaction or network request.