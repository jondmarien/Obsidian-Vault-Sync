# Introduction

This is a book about building applications using hypermedia systems. _Hypermedia systems_ might seem like a strange phrase: how is hypermedia a _system_? Isn’t hypermedia just a way to link documents together?

Like with HTML, on the World Wide Web?

What do you mean hypermedia _systems_?

Well, yes, HTML is _a_ hypermedia. But there is more to the way the web works than just HTML: HTTP, the Hyper Text Transfer Protocol, is what transfers HTML from servers to clients, and there are many details and features associated with it: caching, various headers, response codes, and so forth.

And then, of course, there are _hypermedia servers_, which present _hypermedia APIs_ (yes, _APIs_) to clients over the network.

And, finally, there is the all-important _hypermedia client_: a software client that understands how to render a _hypermedia response_ intelligibly to a human, so that a human can interact with the remote system. The most widely known and used hypermedia clients are, of course, web browsers.

Web browsers are perhaps the most sophisticated pieces of software we use. They not only understand HTML, CSS and many other file formats, but they also provide a JavaScript runtime and programming environment that is so powerful that web developers can create entire applications in it that are nearly as sophisticated as _thick clients_, that is, native applications.

This JavaScript runtime is so powerful, in fact, that today many developers ignore the _hypermedia_ features of the browser, in favor of building their web applications entirely in JavaScript. Applications built in this manner have come to be called Single Page Applications (SPAs). Rather than navigating between pages, these web applications use JavaScript for updating the user interface directly. When they communicate with a server, these applications typically use JSON API calls via AJAX. And they often update the user interface using a “reactive” style frontend JavaScript library.

In these applications HTML becomes a (somewhat awkward) graphical interface description language that is used because, for historical reasons, that’s what happens to be there, in the browser.

Applications built in this style are not _hypermedia-driven_: they do not take advantage of the underlying hypermedia system of the web.

To explain what a hypermedia-driven application looks like, and to contrast it with the popular SPA approach of today, we need to first explore the entire _hypermedia system_ of the web, beyond just discussing HTML. We need to look at the _network architecture_ of the web, including how a web server delivers a hypermedia API, and how to effectively use the hypermedia features available in the hypermedia _client_ (e.g., the browser).

Each of these are important aspects of building an effective hypermedia-driven application, and it is the entire _hypermedia system_ that comes together to make hypermedia such a powerful architecture.