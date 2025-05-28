# Hypermedia APIs & JSON Data APIs

So, we have a hypermedia API for Contact.app. Should we include a Data API for Contact.app as well?

Sure! The existence of a hypermedia API _in no way means_ that you can’t _also_ have a Data API. In fact, this is a common situation in traditional web applications: there is the “web application” that is entered through that entry point URL, say `https://mywebapp.example.com/`. And there is also a _separate_ JSON API that is accessible through another URL, perhaps `https://api.mywebapp.example.com/v1`.

This is a perfectly reasonable way to split up the hypermedia interface to your application and the Data API you provide to other, non-hypermedia clients.

Why would you want to include a Data API along with a hypermedia API? Well, because _non-hypermedia clients_ might also want to interact with your application as well.

For example:

*   Perhaps you have a mobile application that isn’t built using Hyperview. That application will need to interact with your server somehow, and using the existing HTML API would almost certainly be a poor fit! You want programmatic access to your system via a Data API, and JSON is a natural choice for this.
    
*   Perhaps you have an automated script that needs to interact with the system on a regular basis. For example, maybe we have a bulk-import job that runs nightly, and needs to import/sync thousands of contacts. While it would be possible to script this against the HTML API, it would also be annoying: parsing HTML in scripts is error prone and tedious. It would be better to have a simple JSON API for this use case.
    
*   Perhaps there are 3rd party clients who wish to integrate with your system’s data in some way. Maybe a partner wants to synchronize data nightly. As with the bulk-import example, this isn’t a great use case for an HTML-based API, and it would make more sense to provide something more amenable to scripting.
    

For all of these use cases, a JSON Data API makes sense: in each case the API is not being consumed by a hypermedia client, so presenting an HTML-based hypermedia API would be inefficient and complicated for the client to deal with. A simple JSON Data API fits the bill for what we want and, as always, we recommend using the right tool for the job.

**“What!?! You Want Me To Parse HTML!?!”**

A confusion we often run into in online discussions when we advocate a hypermedia approach to building web applications is that people think we mean that they should parse the HTML responses from the server, and then dump the data into their SPA framework or mobile applications.

This is, of course, silly.

What we mean, instead, is that you should consider using a hypermedia API _with a hypermedia client_, like the browser, interpreting the hypermedia response itself and presenting it to the user. A hypermedia API can’t simply be welded on top of an existing SPA approach. It requires a sophisticated hypermedia client such as the browser to be consumed effectively.

If you are writing code to tease apart your hypermedia only to then treat as data to feed into a client-side model, you are probably doing it wrong.

## Differences Between Hypermedia APIs & Data APIs

Let’s accept for a moment that we _are_ going to have a Data API for our application, in addition to our hypermedia API. At this point, some developers may be wondering: why have both? Why not have a single API, the JSON Data API, and have multiple clients use this one API to communicate with it?

Isn’t it redundant to have both types of APIs for our application?

This is a reasonable point: we do advocate having multiple APIs to your web application if necessary and, yes, this may lead to some redundancy in code. However, there are distinct advantages to both sorts of APIs and, even more so, distinct requirements for both sorts of APIs.

By supporting both of these types of APIs separately you can get the strengths of both, while keeping their varying styles of code and infrastructure needs cleanly split out.

Let’s contrast the needs of JSON APIs with Hypermedia APIs:

JSON API Needs

Hypermedia API

It must remain stable over time: you cannot change the API willy-nilly or you risk breaking clients that use the API and expect certain end points to behave in certain ways.

There is no need to remain stable over time: all URLs are discovered via HTML responses, so you can be much more aggressive in changing the shape of a hypermedia API.

It must be versioned: related to the first point, when you do make a major change, you need to version the API so that clients that are using the old API continue to work.

Versioning is not an issue, another strength of the hypermedia approach.

It should be rate limited: since data APIs are often used by other clients, not just your own internal web application, requests should be rate limited, often by user, in order to avoid a single client overloading the system.

Rate limiting probably isn’t as important beyond the prevention of Distributed Denial of Service (DDoS) attacks.

It should be a general API: since the API is for _all_ clients, not just for your web application, you should avoid specialized end points that are driven by your own application needs. Instead, the API should be general and expressive enough to satisfy as many potential client needs as possible.

The API can be _very specific_ to your application needs: since it is designed only for your particular web application, and since the API is discovered through hypermedia, you can add and remove highly tuned end points for specific features or optimization needs in your application.

Authentication for these sorts of API is typically token based, which we will discuss in more detail later.

Authentication is typically managed through a session cookie established by a login page.

These two different types of APIs have different strengths and needs, so it makes sense to use both. The hypermedia approach can be used for your web application, allowing you to specialize the API for the “shape” of your application. The Data API approach can be used for other, non-hypermedia clients like mobile, integration partners, etc.

Note that by splitting these two APIs apart, you reduce the pressure to constantly change a general Data API to address application needs. Your Data API can focus on remaining stable and reliable, rather than requiring a new version with every added feature.

This is the key advantage of splitting your Data API from your Hypermedia API.

**JSON Data APIs vs JSON “REST” APIs**

Unfortunately, today, for historical reasons, what we are calling JSON Data APIs are often referred to as “REST APIs” in the industry. This is ironic, because, by any reasonable reading of Roy Fielding’s work defining what REST means, the vast majority of JSON APIs are _not_ RESTful. Not even close.

> I am getting frustrated by the number of people calling any HTTP-based interface a REST API. Today’s example is the SocialSite REST API. That is RPC. It screams RPC. There is so much coupling on display that it should be given an X rating.
> 
> What needs to be done to make the REST architectural style clear on the notion that hypertext is a constraint? In other words, if the engine of application state (and hence the API) is not being driven by hypertext, then it cannot be RESTful and cannot be a REST API. Period. Is there some broken manual somewhere that needs to be fixed?
> 
> ℄ Roy Fielding, https://roy.gbiv.com/untangled/2008/rest-apis-must-be-hypertext-driven

The story of how “REST API” came to mean “JSON APIs” in the industry is a long and sordid one, and beyond the scope of this book. However, if you are interested, you can refer to an essay by one of the authors of this book entitled “How Did REST Come To Mean The Opposite of REST?” on the [htmx website](https://htmx.org/essays/how-did-rest-come-to-mean-the-opposite-of-rest/).

In this book we use the term “Data API” to describe these JSON APIs, while acknowledging that many people in the industry will continue to call them “REST APIs” for the foreseeable future.