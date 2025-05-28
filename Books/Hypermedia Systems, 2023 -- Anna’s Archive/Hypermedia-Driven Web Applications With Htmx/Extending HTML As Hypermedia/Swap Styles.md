# Swap Styles

Now, perhaps we don’t want to load the content from the server response _into_ the div, as child elements. Perhaps, for whatever reason, we wish to _replace_ the entire div with the response. To handle this, htmx provides another attribute, `hx-swap`, that allows you to specify exactly _how_ the content should be swapped into the DOM.

The `hx-swap` attribute supports the following values:

*   `innerHTML` - The default, replace the inner html of the target element.
    
*   `outerHTML` - Replace the entire target element with the response.
    
*   `beforebegin` - Insert the response before the target element.
    
*   `afterbegin` - Insert the response before the first child of the target element.
    
*   `beforeend` - Insert the response after the last child of the target element.
    
*   `afterend` - Insert the response after the target element.
    
*   `delete` - Deletes the target element regardless of the response.
    
*   `none` - No swap will be performed.
    

The first two values, `innerHTML` and `outerHTML`, are taken from the standard DOM properties that allow you to replace content within an element or in place of an entire element respectively.

The next four values are taken from the `Element.insertAdjacentHTML()` DOM API, which allow you to place an element or elements around a given element in various ways.

The last two values, `delete` and `none` are specific to htmx. The first option will remove the target element from the DOM, while the second option will do nothing (you may want to only work with response headers, an advanced technique we will look at later in the book.)

Again, you can see htmx stays as close as possible to existing web standards in order to minimize the conceptual load necessary for its use.

So let’s consider that case where, rather than replacing the `innerHTML` content of the main div above, we want to replace the _entire div_ with the HTML response.

To do so would require only a small change to our button, adding a new `hx-swap` attribute:

    <div id="main">
    
      <button hx-get="/contacts" hx-target="#main" hx-swap="outerHTML"> <1>
        Get The Contacts
      button>
    
    div>

Replacing the entire div

1.  The `hx-swap` attribute specifies how to swap in new content.
    

Now, when a response is received, the _entire_ div will be replaced with the hypermedia content:

    <ul>
      <li><a href="mailto:joe@example.com">Joea>li>
      <li><a href="mailto:sarah@example.com">Saraha>li>
      <li><a href="mailto:fred@example.com">Freda>li>
    ul>

Our HTML after the htmx request finishes

You can see that, with this change, the target div has been entirely removed from the DOM, and the list that was returned as the response has replaced it.

Later in the book we will see additional uses for `hx-swap`, for example when we implement infinite scrolling in our contact management application.

Note that with the `hx-get`, `hx-post`, `hx-put`, `hx-patch` and `hx-delete` attributes, we have addressed two of the four opportunities for improvement that we enumerated regarding plain HTML:

*   Opportunity 1: We can now issue an HTTP request with _any_ element (in this case we are using a button).
    
*   Opportunity 3: We can issue _any sort_ of HTTP request we want, `PUT`, `PATCH` and `DELETE`, in particular.
    

And, with `hx-target` and `hx-swap` we have addressed a third shortcoming: the requirement that the entire page be replaced.

*   Opportunity 4: We can now replace any element we want in our page via transclusion, and we can do so in any manner we want.
    

So, with only seven relatively simple additional attributes, we have addressed most of the shortcomings of HTML as a hypermedia that we identified earlier.

What’s next? Recall the one other opportunity we noted: the fact that only a `click` event (on an anchor) or a `submit` event (on a form) can trigger an HTTP request. Let’s look at how we can address that limitation.