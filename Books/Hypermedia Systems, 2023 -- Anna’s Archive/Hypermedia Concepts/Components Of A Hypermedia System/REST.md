# REST

Now that we have reviewed the major components of a hypermedia system, it’s time to look more deeply into the concept of REST. The term “REST” comes from Roy Fielding’s PhD dissertation on the architecture of the web. Fielding wrote his dissertation at U.C. Irvine, after having helped build much of the infrastructure of the early web, including the Apache web server. Roy was attempting to formalize and describe the novel distributed computing system that he had helped to build.

We are going to focus on what we feel is the most important section of Fielding’s writing, from a web development perspective: Section 5.1. This section contains the core concepts (Fielding calls them _constraints_) of Representational State Transfer, or REST.

Before we get into the muck, however, it is important to understand that Fielding discusses REST as a _network architecture_, that is, as an entirely different way to architect a distributed system. And, further, as a novel network architecture that should be _contrasted_ with earlier approaches to distributed systems.

It is also important to emphasize that, at the time Fielding wrote his dissertation, JSON APIs and AJAX did not exist. He was describing the early web, with HTML being transferred over HTTP by early browsers, as a hypermedia system.

Today, in a strange turn of events, the term “REST” is mainly associated with JSON Data APIs, rather than with HTML and hypermedia. This is extremely funny once you realize that the vast majority of JSON Data APIs aren’t RESTful, in the original sense, and, in fact, _can’t_ be RESTful, since they aren’t using a natural hypermedia format.

To re-emphasize: REST, as coined by Fielding, describes the _pre-API web_, and letting go of the current, common usage of the term REST to simply mean “a JSON API” is necessary to develop a proper understanding of the idea.

## The “Constraints” of REST

In his dissertation, Fielding defines various “constraints” to describe how a RESTful system must behave. This approach can feel a little round-about and difficult to follow for many people, but it is an appropriate approach for an academic document. Given a bit of time thinking about the constraints he outlines and some concrete examples of those constraints it will become easy to assess whether a given system actually satisfies the architectural requirements of REST or not.

Here are the constraints of REST Fielding outlines:- It is a client-server architecture (section 5.1.2).- It must be stateless; (section 5.1.3) that is, every request contains all information necessary to respond to that request.- It must allow for caching (section 5.1.4).- It must have a _uniform interface_ (section 5.1.5).- It is a layered system (section 5.1.6).- Optionally, it can allow for Code-On-Demand (section 5.1.7), that is, scripting.

Let’s go through each of these constraints in turn and discuss them in detail, looking at how (and to what extent) the web satisfies each of them.

## The Client-Server Constraint

See [Section 5.1.2](https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm#sec_5_1_2) for the Client-Server constraint.

The REST model Fielding was describing involved both _clients_ (browsers, in the case of the web) and _servers_ (such as the Apache Web Server he had been working on) communicating via a network connection. This was the context of his work: he was describing the network architecture of the World Wide Web, and contrasting it with earlier architectures, notably thick-client networking models such as the Common Object Request Broker Architecture (CORBA).

It should be obvious that any web application, regardless of how it is designed, will satisfy this requirement.

## The Statelessness Constraint

See [Section 5.1.3](https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm#sec_5_1_3) for the Stateless constraint.

As described by Fielding, a RESTful system is stateless: every request should encapsulate all information necessary to respond to that request, with no side state or context stored on either the client or the server.

In practice, for many web applications today, we actually violate this constraint: it is common to establish a _session cookie_ that acts as a unique identifier for a given user and that is sent along with every request. While this session cookie is, by itself, not stateful (it is sent with every request), it is typically used as a key to look up information stored on the server, in what is usually termed “the session.”

This session information is typically stored in some sort of shared storage across multiple web servers, holding things like the current user’s email or id, their roles, partially created domain objects, caches, and so forth.

This violation of the Statelessness REST architectural constraint has proven to be useful for building web applications and does not appear to have had a major impact on the overall flexibility of the web. But it is worth bearing in mind that even Web 1.0 applications often violate the purity of REST in the interest of pragmatic trade-offs.

And it must be said that sessions _do_ cause additional operational complexity headaches when deploying hypermedia servers; these may need shared access to session state information stored across an entire cluster. So Fielding was correct in pointing out that an ideal RESTful system, one that did not violate this constraint, would be simpler and therefore more robust.

## The Caching Constraint

See [Section 5.1.4](https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm#sec_5_1_4) for the Caching constraint.

This constraint states that a RESTful system should support the notion of caching, with explicit information on the cache-ability of responses for future requests of the same resource. This allows both clients as well as intermediary servers between a given client and final server to cache the results of a given request.

As we discussed earlier, HTTP has a sophisticated caching mechanism via response headers that is often overlooked or underutilized when building hypermedia applications. Given the existence of this functionality, however, it is easy to see how this constraint is satisfied by the web.

## The Uniform Interface Constraint

Now we come to the most interesting and, in our opinion, most innovative constraint in REST: that of the _uniform interface_.

This constraint is the source of much of the _flexibility_ and _simplicity_ of a hypermedia system, so we are going to spend some time on it.

See [Section 5.1.5](https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm#sec_5_1_5) for the Uniform Interface constraint.

In this section, Fielding says:

> The central feature that distinguishes the REST architectural style from other network-based styles is its emphasis on a uniform interface between components…​ In order to obtain a uniform interface, multiple architectural constraints are needed to guide the behavior of components. REST is defined by four interface constraints: identification of resources; manipulation of resources through representations; self-descriptive messages; and, hypermedia as the engine of application state
> 
> ℄ Roy Fielding, Architectural Styles and the Design of Network-based Software Architectures

So we have four sub-constraints that, taken together, form the Uniform Interface constraint.

### Identification of resources

In a RESTful system, resources should have a unique identifier. Today the concept of Universal Resource Locators (URLs) is common, but at the time of Fielding’s writing they were still relatively new and novel.

What might be more interesting today is the notion of a _resource_, thus being identified: in a RESTful system, _any_ sort of data that can be referenced, that is, the target of a hypermedia reference, is considered a resource. URLs, though common enough today, end up solving the very complex problem of uniquely identifying any and every resource on the internet.

### Manipulation of resources through representations

In a RESTful system, _representations_ of the resource are transferred between clients and servers. These representations can contain both data and metadata about the request (such as “control data” like an HTTP method or response code). A particular data format or _media type_ may be used to present a given resource to a client, and that media type can be negotiated between the client and the server.

We saw this latter aspect of the uniform interface in the `Accept` header in the requests above.

### Self-descriptive messages

The Self-Descriptive Messages constraint, combined with the next one, HATEOAS, form what we consider to be the core of the Uniform Interface, of REST and why hypermedia provides such a powerful system architecture.

The Self-Descriptive Messages constraint requires that, in a RESTful system, messages must be _self-describing_.

This means that _all information_ necessary to both display _and also operate_ on the data being represented must be present in the response. In a properly RESTful system, there can be no additional “side” information necessary for a client to transform a response from a server into a useful user interface. Everything must “be in” the message itself, in the form of hypermedia controls.

This might sound a little abstract so let’s look at a concrete example.

Consider two different potential responses from an HTTP server for the URL `https://example.com/contacts/42`.

Both responses will return information about a contact, but each response will take very different forms.

The first implementation returns an HTML representation:

    <html lang="en">
    <body>
    <h1>Joe Smithh1>
    <div>
        <div>Email: joe@example.bardiv>
        <div>Status: Activediv>
    div>
    <p>
        <a href="/contacts/42/archive">Archivea>
    p>
    body>
    html>

The second implementation returns a JSON representation:

    {
      "name": "Joe Smith",
      "email": "joe@example.org",
      "status": "Active"
    }

What can we say about the differences between these two responses?

One thing that may initially jump out at you is that the JSON representation is smaller than the HTML representation. Fielding notes exactly this trade-off when using a RESTful architecture:

> The trade-off, though, is that a uniform interface degrades efficiency, since information is transferred in a standardized form rather than one which is specific to an application’s needs.
> 
> ℄ Roy Fielding, Architectural Styles and the Design of Network-based Software Architectures

So REST _trades off_ representational efficiency for other goals.

To understand these other goals, first notice that the HTML representation has a hyperlink in it to navigate to a page to archive the contact. The JSON representation, in contrast, does not have this link.

What are the ramifications of this fact for a _client_ of the JSON API?

What this means is that the JSON API client must know _in advance_ exactly what other URLs (and request methods) are available for working with the contact information. If the JSON client is able to update this contact in some way, it must know how to do so from some source of information _external_ to the JSON message. If the contact has a different status, say “Archived”, does this change the allowable actions? If so, what are the new allowable actions?

The source of all this information might be API documentation, word of mouth or, if the developer controls both the server and the client, internal knowledge. But this information is implicit and _outside_ the response.

Contrast this with the hypermedia (HTML) response. In this case, the hypermedia client (that is, the browser) needs only to know how to render the given HTML. It doesn’t need to understand what actions are available for this contact: they are simply encoded _within_ the HTML response itself as hypermedia controls. It doesn’t need to understand what the status field means. In fact, the client doesn’t even know what a contact is!

The browser, our hypermedia client, simply renders the HTML and allows the user, who presumably understands the concept of a Contact, to make a decision on what action to pursue from the actions made available in the representation.

This difference between the two responses demonstrates the crux of REST and hypermedia, what makes them so powerful and flexible: clients (again, web browsers) don’t need to understand _anything_ about the underlying resources being represented.

Browsers only (only! As if it is easy!) need to understand how to interpret and display hypermedia, in this case HTML. This gives hypermedia-based systems unprecedented flexibility in dealing with changes to both the backing representations and to the system itself.

### Hypermedia As The Engine of Application State (HATEOAS)

The final sub-constraint on the Uniform Interface is that, in a RESTful system, hypermedia should be “the engine of application state.” This is sometimes abbreviated as “HATEOAS”, although Fielding prefers to use the terminology “the hypermedia constraint” when discussing it.

This constraint is closely related to the previous self-describing message constraint. Let us consider again the two different implementations of the endpoint `/contacts/42`, one returning HTML and one returning JSON. Let’s update the situation such that the contact identified by this URL has now been archived.

What do our responses look like?

The first implementation returns the following HTML:

    <html lang="en">
    <body>
    <h1>Joe Smithh1>
    <div>
        <div>Email: joe@example.bardiv>
        <div>Status: Archiveddiv>
    div>
    <p>
        <a href="/contacts/42/unarchive">Unarchivea>
    p>
    body>
    html>

The second implementation returns the following JSON representation:

    {
      "name": "Joe Smith",
      "email": "joe@example.org",
      "status": "Archived"
    }

The important point to notice here is that, by virtue of being a self-describing message, the HTML response now shows that the “Archive” operation is no longer available, and a new “Unarchive” operation has become available. The HTML representation of the contact _encodes_ the state of the application; it encodes exactly what can and cannot be done with this particular representation, in a way that the JSON representation does not.

A client interpreting the JSON response must, again, understand not only the general concept of a Contact, but also specifically what the “status” field with the value “Archived” means. It must know exactly what operations are available on an “Archived” contact, to appropriately display them to an end user. The state of the application is not encoded in the response, but rather conveyed through a mix of raw data and side channel information such as API documentation.

Furthermore, in the majority of front end SPA frameworks today, this contact information would live _in memory_ in a JavaScript object representing a model of the contact, while the page data is held in the browser’s [Document Object Model](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model) (DOM). The DOM would be updated based on changes to this model, that is, the DOM would “react” to changes to this backing JavaScript model.

This approach is certainly _not_ using Hypermedia As The Engine Of Application State: rather, it is using a JavaScript model as the engine of application state, and synchronizing that model with a server and with the browser.

With the HTML approach, the Hypermedia is, indeed, The Engine Of Application State: there is no additional model on the client side, and all state is expressed directly in the hypermedia, in this case HTML. As state changes on the server, it is reflected in the representation (that is, HTML) sent back to the client. The hypermedia client (a browser) doesn’t know anything about contacts, what the concept of “Archiving” is, or anything else about the particular domain model for this response: it simply knows how to render HTML.

Because a hypermedia client doesn’t need to know anything about the server model beyond how to render hypermedia to a client, it is incredibly flexible with respect to the representations it receives and displays to users.

### HATEOAS & API churn

This last point is critical to understanding the flexibility of hypermedia, so let’s look at a practical example of it in action. Consider a situation where a new feature has been added to the web application with these two end points. This feature allows you to send a message to a given Contact.

How would this change each of the two responses—​HTML and JSON—​from the server?

The HTML representation might now look like this:

    <html lang="en">
    <body>
    <h1>Joe Smithh1>
    <div>
        <div>Email: joe@example.bardiv>
        <div>Status: Activediv>
    div>
    <p>
        <a href="/contacts/42/archive">Archivea>
        <a href="/contacts/42/message">Messagea>
    p>
    body>
    html>

The JSON representation, on the other hand, might look like this:

    {
      "name": "Joe Smith",
      "email": "joe@example.org",
      "status": "Active"
    }

Note that, once again, the JSON representation is unchanged. There is no indication of this new functionality. Instead, a client must _know_ about this change, presumably via some shared documentation between the client and the server.

Contrast this with the HTML response. Because of the uniform interface of the RESTful model and, in particular, because we are using Hypermedia As The Engine of Application State, no such exchange of documentation is necessary! Instead, the client (a browser) simply renders the new HTML with this operation in it, making this operation available for the end user without any additional coding changes.

A pretty neat trick!

Now, in this case, if the JSON client is not properly updated, the error state is relatively benign: a new bit of functionality is simply not made available to users. But consider a more severe change to the API: what if the archive functionality was removed? Or what if the URLs or the HTTP methods for these operations changed in some way?

In this case, the JSON client may be broken in a much more serious manner.

The HTML response, however, would simply be updated to exclude the removed options or to update the URLs used for them. Clients would see the new HTML, display it properly, and allow users to select whatever the new set of operations happens to be. Once again, the uniform interface of REST has proven to be extremely flexible: despite a potentially radically new layout for our hypermedia API, clients continue to work.

An important fact emerges from this: due to this flexibility, hypermedia APIs _do not have the versioning headaches that JSON Data APIs do_.

Once a Hypermedia-Driven Application has been “entered into” (that is, loaded through some entry point URL), all functionality and resources are surfaced through self-describing messages. Therefore, there is no need to exchange documentation with the client: the client simply renders the hypermedia (in this case HTML) and everything works out. When a change occurs, there is no need to create a new version of the API: clients simply retrieve updated hypermedia, which encodes the new operations and resources in it, and display it to users to work with.

## Layered System

The final “required” constraint on a RESTful system that we will consider is The Layered System constraint. This constraint can be found in [Section 5.1.6](https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm#sec_5_1_6) of Fielding’s dissertation.

To be frank, after the excitement of the uniform interface constraint, the “layered system” constraint is a bit of a let down. But it is still worth understanding and it is actually utilized effectively by The web. The constraint requires that a RESTful architecture be “layered,” allowing for multiple servers to act as intermediaries between a client and the eventual “source of truth” server.

These intermediary servers can act as proxies, transform intermediate requests and responses and so forth.

A common modern example of this layering feature of REST is the use of Content Delivery Networks (CDNs) to deliver unchanging static assets to clients more quickly, by storing the response from the origin server in intermediate servers more closely located to the client making a request.

This allows content to be delivered more quickly to the end user and reduces load on the origin server.

Not as exciting for web application developers as the uniform interface, at least in our opinion, but useful nonetheless.

## An Optional Constraint: Code-On-Demand

We called The Layered System constraint the final “required” constraint because Fielding mentions one additional constraint on a RESTful system. This Code On Demand constraint is somewhat awkwardly described as “optional” (Section 5.1.7).

In this section, Fielding says:

> REST allows client functionality to be extended by downloading and executing code in the form of applets or scripts. This simplifies clients by reducing the number of features required to be pre-implemented. Allowing features to be downloaded after deployment improves system extensibility. However, it also reduces visibility, and thus is only an optional constraint within REST.
> 
> ℄ Roy Fielding, Architectural Styles and the Design of Network-based Software Architectures

So, scripting was and is a native aspect of the original RESTful model of the web, and thus should of course be allowed in a Hypermedia-Driven Application.

However, in a Hypermedia-Driven Application the presence of scripting should _not_ change the fundamental networking model: hypermedia should continue to be the engine of application state, server communication should still consist of hypermedia exchanges rather than, for example, JSON data exchanges, and so on. (JSON Data API’s certainly have their place; in Chapter 10 we’ll discuss when and how to use them).

Today, unfortunately, the scripting layer of the web, JavaScript, is quite often used to _replace_, rather than augment the hypermedia model. We will elaborate in a later chapter what scripting that does not replace the underlying hypermedia system of the web looks like.