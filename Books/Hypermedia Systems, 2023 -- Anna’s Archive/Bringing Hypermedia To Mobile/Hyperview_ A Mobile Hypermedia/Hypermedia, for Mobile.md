# Hypermedia, for Mobile

There is a strong case for Hypermedia-Driven Applications on mobile. Mobile app platforms push developers towards a thick-client architecture. But apps that use a thick client suffer from the same problems as SPAs on the web. Using the hypermedia architecture for mobile apps can solve these problems.

Hyperview, based on a new format called HXML, offers a path here. It provides an open-source mobile thin client to render HXML. And HXML opens a toolkit of elements and patterns that correspond to mobile UIs. Developers can evolve Hyperview to suit their apps” requirements, while fully embracing the hypermedia architecture. That’s a win.

Yes, hypermedia can work for mobile apps, too. In the next two chapters we’ll show how by turning the Contact.app web application into a native mobile app using Hyperview.

# Hypermedia Notes: Maximize Your Server-Side Strengths

In the Hyperview sections of the book, since we aren’t using HTML, we are going to make broader observations on hypermedia rather than offer HTML-specific advice and thoughts.

A big advantage of the hypermedia-driven approach is that it makes the server-side environment far more important when building your web application. Rather than simply producing JSON, your back end is an integral component in the user experience of your hypermedia application.

Because of this, it makes sense to look deeply into the functionality available there. Many older web frameworks, for example, have incredibly deep functionality available around producing HTML. Features like server-side caching can make the difference between an incredibly snappy web application and a sluggish user experience.

Take time to learn all the tools available to you.

A good rule of thumb is to shoot to have server responses in your hypermedia-driven application take less than 100ms to complete, and mature server-side frameworks have tools to help make this happen.

Server-side environments often have extremely mature mechanisms for factoring (or organizing) your code properly. The Model/View/Controller pattern is well-developed in most environments, and tools like modules, packages, etc. provide an excellent way to organize your code.

Whereas today’s SPA and mobile user interfaces are typically organized via components, hypermedia-driven applications are typically organized via template inclusion, where the server-side templates are broken up according to the hypermedia-rendering needs of the application, and then included in one another as needed. This tends to lead to fewer, chunkier files than you would find in a component-based application.

Another technology to look for are Template Fragments, which allow you to render only part of a template file. This can reduce even further the number of template files required for your server-side application.

A related tip is to take advantage of direct access to the data store. When an application is built using a thick client approach, the data store typically lives behind a data API (e.g. JSON). This level of indirection often prevents front end developers from being able to take full advantage of the tools available in the data store. GraphQL, for example, can help address this issue, but comes with security-related issues that do not appear to be well understood by many developers.

When you produce your hypermedia on the server side, on the other hand, the developer creating that hypermedia can have full access to the data store and take advantage of, for example, joins and aggregation functions in SQL stores.

This puts far more expressive power directly in the hands of the developer producing the final hypermedia. Because your hypermedia API can be structured around your UI needs, you can tune each endpoint to issue as few data store requests as possible.

A good rule of thumb is that every request to your server should shoot to have three or fewer data-store accesses. If you follow this rule of thumb, your hypermedia-driven application should be extremely snappy.