# Triggering HTTP Requests

Let’s look at the first feature of htmx: the ability for any element in a web page to issue HTTP requests. This is the core functionality provided by htmx, and it consists of five attributes that can be used to issue the five different developer-facing types of HTTP requests:

*   `hx-get` - issues an HTTP `GET` request.
    
*   `hx-post` - issues an HTTP `POST` request.
    
*   `hx-put` - issues an HTTP `PUT` request.
    
*   `hx-patch` - issues an HTTP `PATCH` request.
    
*   `hx-delete` - issues an HTTP `DELETE` request.
    

Each of these attributes, when placed on an element, tells the htmx library: “When a user clicks (or whatever) this element, issue an HTTP request of the specified type.”

The values of these attributes are similar to the values of both `href` on anchors and `action` on forms: you specify the URL you wish to issue the given HTTP request type to. Typically, this is done via a server-relative path.

For example, if we wanted a button to issue a `GET` request to `/contacts` then we would write the following HTML:

    <button hx-get="/contacts"> <1>
      Get The Contacts
    button>

A simple htmx-powered button

1.  A simple button that issues an HTTP `GET` to `/contacts`.
    

The htmx library will see the `hx-get` attribute on this button, and hook up some JavaScript logic to issue an HTTP `GET` AJAX request to the `/contacts` path when the user clicks on it.

Very easy to understand and very consistent with the rest of HTML.

## It’s All Just HTML

With the request issued by the button above, we get to perhaps the most important thing to understand about htmx: it expects the response to this AJAX request _to be HTML_. Htmx is an extension of HTML. A native hypermedia control like an anchor tag will typically get an HTML response to an HTTP request it creates. Similarly, htmx expects the server to respond to the requests that _it_ makes with HTML.

This may surprise web developers who are used to responding to an AJAX request with JSON, which is far and away the most common response format for such requests. But AJAX requests are just HTTP requests and there is no rule saying they must use JSON. Recall again that AJAX stands for Asynchronous JavaScript & XML, so JSON is already a step away from the format originally envisioned for this API: XML.

Htmx simply goes another direction and expects HTML.

## Htmx vs. “Plain” HTML Responses

There is an important difference between the HTTP responses to “normal” anchor or form driven HTTP requests and to htmx-powered requests: in the case of htmx triggered requests, responses can be _partial_ bits of HTML.

In htmx-powered interactions, as you will see, we are often not replacing the entire document. Rather we are using “transclusion” to include content _within_ an existing document. Because of this, it is often not necessary or desirable to transfer an entire HTML document from the server to the browser.

This fact can be used to save bandwidth as well as resource loading time. Less overall content is transferred from the server to the client, and it isn’t necessary to reprocess a `head` tag with style sheets, script tags, and so forth.

When the “Get Contacts” button is clicked, a _partial_ HTML response might look something like this:

    <ul>
      <li><a href="mailto:joe@example.com">Joea>li>
      <li><a href="mailto:sarah@example.com">Saraha>li>
      <li><a href="mailto:fred@example.com">Freda>li>
    ul>

A partial HTML response to an htmx request

This is just an unordered list of contacts with some clickable elements in it. Note that there is no opening `html` tag, no `head` tag, and so forth: it is a _raw_ HTML list, without any decoration around it. A response in a real application might contain more sophisticated HTML than this simple list, but even if it were more complicated it wouldn’t need to be an entire page of HTML: it could just be the “inner” content of the HTML representation for this resource.

Now, this simple list response is perfect for htmx. Htmx will simply take the returned content and then swap it in to the DOM in place of some element in the page. (More on exactly where it will be placed in the DOM in a moment.) Swapping in HTML content in this manner is fast and efficient because it leverages the existing native HTML parser in the browser, rather than requiring a significant amount of client-side JavaScript to be executed.

This small HTML response shows how htmx stays within the hypermedia paradigm: just like a “normal” hypermedia control in a “normal” web application, we see hypermedia being transferred to the client in a stateless and uniform manner.

This button just gives us a slightly more sophisticated mechanism for building a web application using hypermedia.