# Components Of A Hypermedia System

A _hypermedia system_ consists of a number of components, including:

*   A hypermedia, such as HTML.
    
*   A network protocol, such as HTTP.
    
*   A server that presents a hypermedia API responding to network requests with hypermedia responses.
    
*   A client that properly interprets those responses.
    

In this chapter we will look at these components and their implementation in the context of the web.

Once we have reviewed the major components of the web as a hypermedia system, we will look at some key ideas behind this system — especially as developed by Roy Fielding in his dissertation, “Architectural Styles and the Design of Network-based Software Architectures.” We will see where the terms REpresentational State Transfer (REST), RESTful and Hypermedia As The Engine Of Application State (HATEOAS) come from, and we will analyze these terms in the context of the web.

This should give you a stronger understanding of the theoretical basis of the web as a hypermedia system, how it is supposed to fit together, and why Hypermedia-Driven Applications are RESTful, whereas JSON APIs — despite the way the term REST is currently used in the industry — are not.