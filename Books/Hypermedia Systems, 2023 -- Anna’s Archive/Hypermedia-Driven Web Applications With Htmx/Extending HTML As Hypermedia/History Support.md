# History Support

We have a final piece of functionality to close out our overview of htmx: browser history support. When you use normal HTML links and forms, your browser will keep track of all the pages that you have visited. You can then use the back button to navigate back to a previous page and, once you have done this, you can use a forward button to go forward to the original page you were on.

This notion of history was one of the killer features of the early web. Unfortunately it turns out that history becomes tricky when you move to the Single Page Application paradigm. An AJAX request does not, by itself, register a web page in your browser’s history, which is a good thing: an AJAX request may have nothing to do with the state of the web page (perhaps it is just recording some activity in the browser), so it wouldn’t be appropriate to create a new history entry for the interaction.

However, there are likely to be a lot of AJAX driven interactions in a Single Page Application where it _is_ appropriate to create a history entry. There is a JavaScript API to work with browser history, but this API is deeply annoying and difficult to work with, and thus often ignored by JavaScript developers.

If you have ever used a Single Page Application and accidentally clicked the back button, only to lose your entire application state and have to start over, you have seen this problem in action.

In htmx, as with Single Page Application frameworks, you will often need to explicitly work with the history API. Fortunately, since htmx sticks so close to the native model of the web and since it is declarative, getting web history right is typically much easier to do in an htmx-based application.

Consider the button we have been looking at to load contacts:

    <button hx-get="/contacts" hx-target="#main">
      Get The Contacts
    button>

Our trusty button

As it stands, if you click this button it will retrieve the content from `/contacts` and load it into the element with the id `main`, but it will _not_ create a new history entry.

If we wanted it to create a history entry when this request happened, we would add a new attribute to the button, the `hx-push-url` attribute:

    <button hx-get="/contacts" hx-target="#main" hx-push-url="true"> <1>
      Get The Contacts
    button>

Our trusty button, now with history!

1.  `hx-push-url` will create an entry in history when the button is clicked.
    

Now, when the button is clicked, the `/contacts` path will be put into the browser’s navigation bar and a history entry will be created for it. Furthermore, if the user clicks the back button, the original content for the page will be restored, along with the original URL.

Now, the name `hx-push-url` for this attribute might sound a little obscure, but it is based on the JavaScript API, `history.pushState()`. This notion of “pushing” derives from the fact that history entries are modeled as a stack, and so you are “pushing” new entries onto the top of the stack of history entries.

With this relatively simple, declarative mechanism, htmx allows you to integrate with the back button in a way that mimics the “normal” behavior of HTML.

Now, there is one additional thing we need to handle to get history “just right”: we have “pushed” the `/contacts` path into the browsers location bar successfully, and the back button works. But what if someone refreshes their browser while on the `/contacts` page?

In this case, you will need to handle the htmx-based “partial” response as well as the non-htmx “full page” response. You can do this using HTTP headers, a topic we will go into in detail later in the book.

# Conclusion

So that’s our whirlwind introduction to htmx. We’ve only seen about ten attributes from the library, but you can see a hint of just how powerful these attributes can be. Htmx enables a much more sophisticated web application than is possible in plain HTML, with minimal additional conceptual load compared to most JavaScript-based approaches.

Htmx aims to incrementally improve HTML as a hypermedia in a manner that is conceptually coherent with the underlying markup language. Like any technical choice, this is not without trade-offs: by staying so close to HTML, htmx does not give developers a lot of infrastructure that many might feel should be there “by default”.

By staying closer to the native model of the web, htmx aims to strike a balance between simplicity and functionality, deferring to other libraries for more elaborate frontend extensions on top of the existing web platform. The good news is that htmx plays well with others, so when these needs arise it is often easy enough to bring in another library to handle them.

# HTML Notes: Budgeting For HTML

The close relationship between content and markup means that good HTML is labor-intensive. Most sites have a separation between the authors, who are rarely familiar with HTML, and the developers, who need to develop a generic system able to handle any content that’s thrown at it — this separation usually taking the form of a CMS. As a result, having markup tailored to content, which is often necessary for advanced HTML, is rarely feasible.

Furthermore, for internationalized sites, content in different languages being injected into the same elements can degrade markup quality as stylistic conventions differ between languages. It’s an expense few organizations can spare.

Thus, we don’t expect every site to contain perfectly conformant HTML. What’s most important is to avoid _wrong_ HTML — it can be better to fall back on a more generic element than to be precisely incorrect.

If you have the resources, however, putting more care in your HTML will produce a more polished site.