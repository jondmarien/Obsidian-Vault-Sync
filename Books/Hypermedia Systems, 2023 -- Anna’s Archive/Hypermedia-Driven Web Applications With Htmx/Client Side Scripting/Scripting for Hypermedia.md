# Scripting for Hypermedia

Borrowing from Roy Fielding’s notion of “constraints” defining REST, we offer two constraints of hypermedia-friendly scripting. You are scripting in an HDA-compatible manner if the following two constraints are adhered to:

*   The main data format exchanged between server and client must be hypermedia, the same as it would be without scripting.
    
*   Client-side state, outside the DOM itself, is kept to a minimum.
    

The goal of these constraints is to confine scripting to where it shines best and where nothing else comes close: _interaction design_. Business logic and presentation logic are the responsibility of the server, where we can pick whichever languages or tools are appropriate for our business domain.

**The Server**

Keeping business logic and presentation logic both “on the server” does not mean these two “concerns” are mixed or coupled. They can be modularized on the server. In fact, they _should_ be modularized on the server, along with all the other concerns of our application.

Note also that, especially in web development parlance, the humble “server” is usually a whole fleet of racks, virtual machines, containers and more. Even a worldwide network of datacenters is reduced to “the server” when discussing the server-side of a Hypermedia-Driven Application.

Satisfying these two constraints sometimes requires us to diverge from what is typically considered best practice for JavaScript. Keep in mind that the cultural wisdom of JavaScript was largely developed in JavaScript-centric SPA applications.

The Hypermedia-Driven Application cannot as comfortably fall back on this tradition. This chapter is our contribution to the development of a new style and best practices for what we are calling Hypermedia-Driven Applications.

Unfortunately, simply listing “best practices” is rarely convincing or edifying. To be honest, it’s boring.

Instead, we will demonstrate these best practices by implementing client-side features in Contact.app. To cover different aspects of hypermedia-friendly scripting, we will implement three different features:

*   An overflow menu to hold the _Edit_, _View_ and _Delete_ actions, to clean up visual clutter in our list of contacts.
    
*   An improved interface for bulk deletion.
    
*   A keyboard shortcut for focusing the search box.
    

The important takeaway in the implementation of each of these features is that, while they are implemented entirely on the client-side using scripting, they _don’t exchange information with the server_ via a non-hypermedia format, such as JSON, and that they don’t store a significant amount of state outside of the DOM itself.