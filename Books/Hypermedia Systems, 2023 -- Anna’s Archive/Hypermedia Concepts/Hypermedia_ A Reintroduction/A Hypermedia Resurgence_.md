# A Hypermedia Resurgence?

It is interesting to think about how HTML _could_ have advanced. Instead of stalling as a hypermedia, how could HTML have continued to develop? Could it have kept adding new hypermedia controls and increasing the expressiveness of existing ones? Would it have been possible to build modern web applications within this original, hypermedia-oriented and RESTful model that made the early web so powerful, so flexible, so much fun?

This might seem like idle speculation, but we have some good news on this score: in the last decade a few idiosyncratic, alternative front end libraries have arisen that attempt to get HTML moving again. Ironically, these libraries are written in JavaScript, the technology that supplanted HTML as the center of web development.

However, these libraries use JavaScript not as a _replacement_ for the fundamental hypermedia system of the web.

Instead, they use JavaScript to augment HTML itself _as a hypermedia_.

These _hypermedia-oriented_ libraries re-center hypermedia as the core technology in web applications.

## Hypermedia-Oriented JavaScript Libraries

In the web development world there is an ongoing debate between the Single Page Application (SPA) approach and what is now being called the “Multi-Page Application” (MPA) approach. MPA is a modern name for the old, Web 1.0 way of building web applications, using links and forms located on multiple web pages, submitting HTTP requests and getting HTML responses.

MPA applications, by their nature, are Hypermedia-Driven Applications: after all, they are exactly what Roy Fielding was describing in his dissertation.

These applications tend to be clunky, but they work reasonably well. Many web developers and teams choose to accept the limitations of plain HTML in the interest of simplicity and reliability.

Rich Harris, creator of Svelte.js, a popular SPA library, and a thought-leader on the SPA side of the debate, has proposed a mix of this older MPA style and the newer SPA style. Harris calls this approach to building web applications “transitional,” in that it attempts to blend the MPA approach and the newer SPA approach into a coherent whole. (This is somewhat similar to the “transitional” trend in architecture, which combines traditional and modern architectural styles.)

“Transitional” is a fitting term for mixed-style applications, and it offers a reasonable compromise between the two approaches, using either one as appropriate on a case-by-case basis.

But this compromise still feels unsatisfactory.

Must we default to having these two very different architectural models in our applications?

Recall that the crux of the trade-off between SPAs and MPAs is the _user experience_, or interactivity of the application. This typically drives the decision to choose one approach versus the other for an application or — in the case of a “transitional” application — for a particular feature.

It turns out that by adopting a hypermedia-oriented library, the interactivity gap between the MPA and the SPA approach closes dramatically. You can use the MPA approach, that is, the hypermedia approach, for much more of your application without compromising your user interface. You might even be able to use the hypermedia approach for _all_ your application needs.

Rather than having an SPA with a bit of hypermedia around the edges, or some mix of the two approaches, you can often create a web application that is _primarily_ or _entirely_ hypermedia-driven, and that still satisfies the interactivity that your users require.

This can _tremendously_ simplify your web application and produce a much more coherent and understandable piece of software. While there are still times and places for the more complex SPA approach, which we will discuss later in the book, by adopting a hypermedia-first approach and using a hypermedia-oriented library to push HTML as far as possible, your web application can be powerful, interactive _and_ simple.

One such hypermedia oriented library is [htmx](https://htmx.org). Htmx will be the focus of Part Two of this book. We show that you can, in fact, create many common “modern” UI features found in sophisticated Single Page Applications by instead using the hypermedia model.

And, it is refreshingly fun and simple to do so.

## Hypermedia-Driven Applications

When building a web application with htmx the term Multi-Page Application applies _roughly_, but it doesn’t fully characterize the core of the application architecture. As you will see, htmx doesn’t _need_ to replace entire pages, and, in fact, an htmx-based application can reside entirely within a single page. We don’t recommend this practice, but it is possible!

So it isn’t quite right to call web applications built with htmx “Multi-Page Applications.” What the older Web 1.0 MPA approach and the newer hypermedia-oriented library powered applications have in common is their use of _hypermedia_ as their core technology and architecture.

Therefore, we use the term _Hypermedia-Driven Applications (HDAs)_ to describe both.

This clarifies that the core distinction between these two approaches and the SPA approach _isn’t_ the number of pages in the application, but rather the underlying _system_ architecture.

Hypermedia-Driven Application (HDA)

A web application that uses _hypermedia_ and _hypermedia exchanges_ as its primary mechanism for communicating with a server.

So, what does an HDA look like up close?

Let’s look at an htmx-powered implementation of the simple JavaScript-powered button above:

    <button hx-get="/contacts/1" hx-target="#contact-ui"> <1>
        Fetch Contact
    button>

An htmx implementation

1.  issues a `GET` request to `/contacts/1`, replacing the `contact-ui`.
    

As with the JavaScript powered button, this button has been annotated with some attributes. However, in this case we do not have any (explicit) JavaScript scripting.

Instead, we have _declarative_ attributes much like the `href` attribute on anchor tags and the `action` attribute on form tags. The `hx-get` attribute tells htmx: “When the user clicks this button, issue a `GET` request to `/contacts/1`.” The `hx-target` attribute tells htmx: “When the response returns, take the resulting HTML and place it into the element with the id `contact-ui`.”

Here we get to the crux of htmx and how it allows you to build Hypermedia-Driven Applications:

_The HTTP response from the server is expected to be in HTML format, not JSON_.

An HTTP response to this htmx-driven request might look something like this:

    <details>
      <div>
        Contact: HTML Example
      div>
      <div>
        <a href="mailto:html-example@example.com">Emaila>
      div>
    details>

HTML

This small bit of HTML would be placed into the element in the DOM with the id `contact-ui`.

Thus, this htmx-powered button is exchanging _hypermedia_ with the server, just like an anchor tag or form might, and thus the interaction is still using the basic hypermedia model of the web. Htmx _is_ adding functionality to this button (via JavaScript), but that functionality is _augmenting_ HTML as a hypermedia. Htmx extends the hypermedia system of the web, rather than _replacing_ that hypermedia system with a totally different architecture.

Despite looking superficially similar to one another it turns out that this htmx-powered button and the JavaScript-based button are using extremely different system architectures and, thus, approaches to web development.

As we walk through building a Hypermedia-Driven Application in this book, the differences between the two approaches will become more and more apparent.