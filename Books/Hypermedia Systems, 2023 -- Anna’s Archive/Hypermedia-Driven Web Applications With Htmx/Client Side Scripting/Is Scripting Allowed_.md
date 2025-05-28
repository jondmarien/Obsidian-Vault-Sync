# Is Scripting Allowed?

A common criticism of the web is that it’s being misused. There is a narrative that WWW was created as a delivery system for “documents”, and only came to be used for “applications” by way of an accident or bizarre circumstances.

However, the concept of hypermedia challenges the split of document and application. Hypermedia systems like HyperCard, which preceded the web, featured rich capabilities for active and interactive experiences, including scripting.

HTML, as specified and implemented, does lack affordances needed to build highly interactive applications. This doesn’t mean, however, that hypermedia’s _purpose_ is “documents” over “applications.”

Rather, while the theoretical foundation is there, the implementation is underdeveloped. With JavaScript being the only extension point and hypermedia controls not being well integrated to JavaScript (why can’t one click a link without halting the program?), developers have not internalized hypermedia and have instead used the web as a dumb pipe for apps that imitate “native” ones.

A goal of this book is to show that it is possible to build sophisticated web applications using the original technology of the web, hypermedia, without the application developer needing to reach for the abstractions provided by the large, popular JavaScript frameworks.

Htmx itself is, of course, written in JavaScript, and one of its advantages is that hypermedia interactions that go through htmx expose a rich interface to JavaScript code with configuration, events, and htmx’s own extension support.

Htmx expands the expressiveness of HTML enough that it removes the need for scripting in many situations. This makes htmx attractive to people who don’t want to write JavaScript, and there are many of those sorts of developers, wary of the complexity of Single Page Application frameworks.

However, dunking on JavaScript is not the aim of the htmx project. The goal of htmx is not less JavaScript, but less code, more readable and hypermedia-friendly code.

Scripting has been a massive force multiplier for the web. Using scripting, web application developers are not only able to enhance their HTML websites, but also create full-fledged client-side applications that can often compete with native, thick client applications.

This JavaScript-centric approach to building web applications is a testament to the power of the web and to the sophistication of web browsers in particular. It has its place in web development: there are situations where the hypermedia approach simply can’t provide the level of interaction that an SPA can.

However, in addition to this more JavaScript-centric style, we want to develop a style of scripting more compatible and consistent with Hypermedia-Driven Applications.