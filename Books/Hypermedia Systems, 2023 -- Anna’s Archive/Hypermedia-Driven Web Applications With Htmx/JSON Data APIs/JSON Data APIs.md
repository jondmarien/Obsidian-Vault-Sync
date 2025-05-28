# JSON Data APIs

So far we have been focusing on using hypermedia to build Hypermedia-Driven Applications. In doing so we are following and taking advantage of the native network architecture of the web, and building a RESTful system, in the original sense of that term.

However, today, we should acknowledge that many web applications are often _not_ built using this approach. Instead, they use a Single Page Application front end library such as React to build their application, and they interact with the server via a JSON API. This JSON API almost never uses hypermedia concepts. Rather JSON APIs tend to be _Data APIs_, that is, an API that simply returns structured domain data to the client without any hypermedia control information. The client itself must know how to interpret the JSON Data: what end points are associated with the data, how certain fields should be interpreted, and so on.

Now, believe it or not, we _have_ been creating an API for Contact.app.

This may sound confusing to you: an API? We have just been creating a web application, with handlers that just return HTML.

How is that an API?

It turns out that Contact.app is, indeed, providing an API. It just happens to be a _hypermedia_ API that a _hypermedia client_, that is, a browser, understands. We are building an API for the browser to interact with over HTTP, and, thanks to the magic of HTML and hypermedia, the browser doesn’t need to know anything about our hypermedia API beyond an entry point URL: all the actions and display information comes, self-contained, within the HTML responses.

Building RESTful web applications like this is so natural and simple that you might not think of it as an API at all, but we assure you, it is.