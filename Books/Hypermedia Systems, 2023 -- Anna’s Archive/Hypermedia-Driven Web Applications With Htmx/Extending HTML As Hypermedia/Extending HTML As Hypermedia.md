# Extending HTML As Hypermedia

In the previous chapter we introduced a simple Web 1.0-style hypermedia application to manage contacts. Our application supported the normal CRUD operations for contacts, as well as a simple mechanism for searching contacts. Our application was built using nothing but forms and anchor tags, the traditional hypermedia controls used to interact with servers. The application exchanges hypermedia (HTML) with the server over HTTP, issuing `GET` and `POST` HTTP requests and receiving back full HTML documents in response.

It is a basic web application, but it is also definitely a Hypermedia-Driven Application. It is robust, it leverages the web’s native technologies, and it is simple to understand.

So what’s not to like about the application?

Unfortunately, our application has a few issues common to web 1.0 style applications:

*   From a user experience perspective: there is a noticeable refresh when you move between pages of the application, or when you create, update or delete a contact. This is because every user interaction (link click or form submission) requires a full page refresh, with a whole new HTML document to process after each action.
    
*   From a technical perspective, all the updates are done with the `POST` HTTP method. This, despite the fact that more logical actions and HTTP request types like `PUT` and `DELETE` exist and would make more sense for some of the operations we implemented. After all, if we wanted to delete a resource, wouldn’t it make more sense to use an HTTP `DELETE` request to do so? Somewhat ironically, since we have used pure HTML, we are unable to access the full expressive power of HTTP, which was designed specifically _for_ HTML.
    

The first point, in particular, is noticeable in Web 1.0 style applications like ours and is what is responsible for giving them the reputation for being “clunky” when compared with their more sophisticated JavaScript-based Single Page Application cousins.

We could address this issue by adopting a Single Page Application framework, and updating our server-side to provide JSON-based responses. Single Page Applications eliminate the clunkiness of web 1.0 applications by updating a web page without refreshing it: they can mutate parts of the Document Object Model (DOM) of the existing page without needing to replace (and re-render) the entire page.

**The DOM**

The DOM is the internal model that a browser builds up when it processes HTML, forming a tree of “nodes” for the tags and other content in the HTML. The DOM provides a programmatic JavaScript API that allows you to update the nodes in a page directly, without the use of hypermedia. Using this API, JavaScript code can insert new content, or remove or update existing content, entirely outside the normal browser request mechanism.

There are a few different styles of SPA, but, as we discussed in Chapter 1, the most common approach today is to tie the DOM to a JavaScript model and then let an SPA framework like [React](https://reactjs.org/) or [Vue](https://vuejs.org/) _reactively_ update the DOM when a JavaScript model is updated: you make a change to a JavaScript object that is stored locally in memory in the browser, and the web page “magically” updates its state to reflect the change in the model.

In this style of application, communication with the server is typically done via a JSON Data API, with the application sacrificing the advantages of hypermedia in order to provide a better, smoother user experience.

Many web developers today would not even consider the hypermedia approach due to the perceived “legacy” feel of these web 1.0 style applications.

Now, the second more technical issue we mentioned may strike you as a bit pedantic, and we are the first to admit that conversations around REST and which HTTP Action is right for a given operation can become very tedious. But still, it’s odd that, when using plain HTML, it is impossible to use all the functionality of HTTP!

Just seems wrong, doesn’t it?