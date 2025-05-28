# What is a Hypermedia System?

To understand what a hypermedia system is we’ll first take an in-depth look at _the_ canonical hypermedia system: the World Wide Web. Roy Fielding, an engineer who helped create specifications and build the implementations of many early pieces of the web, gave us the term REpresentational State Transfer, or REST. In his PhD dissertation he described REST as a _network architecture_, and he contrasted it with earlier approaches to building distributed software.

We define a _hypermedia system_ as a system that adheres to the RESTful network architecture in Fielding’s _original_ sense of this term.

Unfortunately, today, you probably associate the term “REST” with JSON APIs, since that is where the term is typically used in industry. This is a misapplied use of the term REST because JSON is not a _natural_ hypermedia due to the absence of hypermedia controls. The exchange of hypermedia is an explicit requirement for a system to be considered “RESTful.” It is a long story how we got here, using the term REST so incorrectly, and we will go into the details later in this book. But, for now, if you think REST implies JSON, please try to set that understanding aside while reading this book, and come to the concept with fresh eyes.

It is important to understand that, in his dissertation, Fielding was describing The World Wide Web as it existed in the late 1990s. The web, at that point, was simply web browsers exchanging hypermedia. That system, with its simple links and forms, was what Fielding was calling RESTful.

JSON APIs were a decade away from becoming a common tool in web development: REST was about _hypermedia_ and the 1.0 version of the web.