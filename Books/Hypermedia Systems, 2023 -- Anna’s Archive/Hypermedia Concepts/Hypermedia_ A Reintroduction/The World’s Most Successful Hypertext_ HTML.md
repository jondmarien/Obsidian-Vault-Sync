# The World’s Most Successful Hypertext: HTML

> In the beginning was the hyperlink, and the hyperlink was with the web, and the hyperlink was the web. And it was good.
> 
> ℄ Rescuing REST From the API Winter, https://intercoolerjs.org/2016/01/18/rescuing-rest.html

The system that Berners-Lee, Fielding and many others had created revolved around a hypermedia: HTML. HTML started as a read-only hypermedia, used to publish (at first) academic documents. These documents were linked together via anchor tags which created _hyperlinks_ between them, allowing users to quickly navigate between documents.

When HTML 2.0 was released, it introduced the notion of the `form` tag, joining the anchor tag (i.e., hyperlink) as a second hypermedia control. The introduction of the form tag made building _applications_ on the web viable by providing a mechanism for _updating_ resources, rather than just reading them.

It was at this point that the web transitioned from an interesting document-oriented system to a compelling _application architecture_.

Today HTML is the most widely used hypermedia in existence and this book naturally assumes that the reader has a reasonable familiarity with it. You do not need to be an HTML (or CSS) expert to understand the code in this book, but the better you understand the core tags and concepts of HTML, the more you will get out of it.

## The Essence of HTML as a Hypermedia

Let us consider these two defining hypermedia elements (that is the two defining _hypermedia controls_) of HTML, the anchor tag and the form tag, in a bit of detail.

### Anchor tags

Anchor tags are so familiar as to be boring but, as the original hypermedia control, it is worth reviewing the mechanics of hyperlinks to get our minds in the right place for developing a deeper understanding of hypermedia.

Consider a simple anchor tag, embedded within a larger HTML document:

    <a href="https://hypermedia.systems/">
      Hypermedia Systems
    a>

A simple hyperlink

An anchor tag consists of the tag itself, `[[null|]]`, as well as the attributes and content within the tag. Of particular interest is the `href` attribute, which specifies a _hypertext reference_ to another document or document fragment. It is this attribute that makes the anchor tag a hypermedia control.

In a typical web browser, this anchor tag would be interpreted to mean:- Show the text “Hypermedia Systems” in a manner indicating that it is clickable- When the user clicks on that text, issue an HTTP `GET` request to the URL `https://hypermedia.systems/`\- Take the HTML content in the body of the HTTP response to this request and replace the entire screen in the browser as a new document, updating the navigation bar to this new URL.

Anchors provide the main mechanism we use to navigate around the web today, by selecting links to navigate from document to document, or from resource to resource.

Here is what a user interaction with an anchor tag/hyperlink looks like in visual form:

    ┌────────────────────────┐      ┌─HTTP REQUEST────────────────┐
    │ BROWSER              X │      │                             │
    ├────────────────────────┤      │ GET /                       │
    │                        │      │ Host: hypermedia.systems    │
    │ lorem ipsum dolor      │      └─────────────────────────────┘
    │                        │
    │ Hypermedia Systems ────┼───────────┐
    │ ──────────────────     │           │
    │ sit amet               │           │
    │                        │           │
    └────────────────────────┘           │
                                  ┌──────▼──────┐
                                  │   H T T P   │
                                  │ S E R V E R │
                                  └──────┬──────┘
    ┌────────────────────────┐           │
    │ BROWSER              X │           │
    ├────────────────────────┤           │
    │                        │           │
    │ HYPERMEDIA SYSTEMS     ◀───────────┘
    │                        │
    │ The revolutionary      │      ┌─HTTP RESPONSE───────────────┐
    │                        │      │                             │
    │ ideas that empowered...│      │ 200 OK                      │
    │                        │      │ ...                         │
    └────────────────────────┘      │ Hypermedia Systems │
                                    │ ...                         │
                                    └─────────────────────────────┘
    

An HTTP GET In Action

When the link is clicked the browser (or, as we sometimes refer to it, the _hypermedia client_) initiates an HTTP `GET` request to the URL encoded in the link’s `href` attribute.

Note that the HTTP request includes additional data (i.e., _metadata_) on what, exactly, the browser wants from the server, in the form of headers. We will discuss these headers, and HTTP in more depth in Chapter 2.

The _hypermedia server_ then responds to this request with a _hypermedia response_ — the HTML — for the new page. This may seem like a small and obvious point, but it is an absolutely crucial aspect of a truly RESTful _hypermedia system_: the client and server must communicate via hypermedia!

### Form tags

Anchor tags provide _navigation_ between documents or resources, but don’t allow you to update those resources. That functionality falls to the form tag.

Here is a simple example of a form in HTML:

    <form action="/signup" method="post">
      <input type="text" name="email" placeholder="Enter Email To Sign Up">
      <button>Sign Upbutton>
    form>

A simple form

Like an anchor tag, a form tag consists of the tag itself,

, combined with the attributes and content within the tag. Note that the form tag does not have an `href` attribute, but rather has an `action` attribute that specifies where to issue an HTTP request.

Furthermore, it also has a `method` attribute, which specifies exactly which HTTP “method” to use. In this example the form is asking the browser to issue a `POST` request.

In contrast with anchor tags, the content and tags _within_ a form can have an effect on the hypermedia interaction that the form makes with a server. The _values_ of `input` tags and other tags such as `select` tags will be included with the HTTP request when the form is submitted, as URL parameters in the case of a `GET` and as part of the request body in the case of a `POST`. This allows a form to include an arbitrary amount of information collected from a user in a request, unlike the anchor tag.

In a typical browser this form tag and its contents would be interpreted by the browser roughly as follows:- Show a text input and a “Sign Up” button to the user- When the user submits the form by clicking the “Sign Up” button or by hitting the enter key while the input element is focused, issue an HTTP `POST` request to the path `/signup` on the “current” server- Take the HTML content in the body of the HTTP response body and replace the entire screen in the browser as a new document, updating the navigation bar to this new URL.

This mechanism allows the user to issue requests to _update the state_ of resources on the server. Note that despite this new type of request the communication between client and server is still done entirely with _hypermedia_.

It is the form tag that makes Hypermedia-Driven Applications possible.

If you are an experienced web developer you probably recognize that we are omitting a few details and complications here. For example, the response to a form submission often _redirects_ the client to a different URL.

This is true, and we will get down into the muck with forms in more detail in later chapters but, for now, this simple example suffices to demonstrate the core mechanism for updating system state purely within hypermedia.

Here is a diagram of the interaction:

    ┌────────────────────────┐      ┌─HTTP REQUEST────────────────┐
    │ BROWSER              X │      │                             │
    ├────────────────────────┤      │ POST /                      │
    │                        │      │ Host: hypermedia.systems    │
    │ SIGN UP                │      │ ...                         │
    │ ┌────────────────────┐ │      │ email=joe@example.com       │
    │ │ joe@example.com    │ │      └─────────────────────────────┘
    │ └────────────────────┘ │
    │ ┌─────────┐        ────┼───────────┐
    │ │ Sign up │            │           │
    │ └─────────┘            │           │
    └────────────────────────┘           │
                                  ┌──────▼──────┐
                                  │   H T T P   │
                                  │ S E R V E R │
                                  └──────┬──────┘
    ┌────────────────────────┐           │
    │ BROWSER              X │           │
    ├────────────────────────┤           │
    │                        │           │
    │ THANK YOU FOR SIGNING  ◀───────────┘
    │ UP                     │
    │                        │      ┌─HTTP RESPONSE───────────────┐
    │                        │      │                             │
    │                        │      │ 201 Created                 │
    │                        │      │ ...                         │
    └────────────────────────┘      │ Thank you for signing   │
                                    │ up                     │
                                    └─────────────────────────────┘
    

An HTTP POST In Action

### Web 1.0 applications

As someone interested in web development, the above diagrams and discussion are probably very familiar to you. You may even find this content boring. But take a step back and consider the fact that these two hypermedia controls, anchors and forms, are the _only_ native ways for a user to interact with a server in plain HTML.

Only two tags!

And yet, armed with only these two tags, the early web was able to grow exponentially and offer a staggeringly large amount of online, dynamic functionality to billions of people.

This is strong evidence of the power of hypermedia. Even today, in a web development world increasingly dominated by large JavaScript-centric front end frameworks, many people choose to use simple vanilla HTML to achieve their application goals and are often perfectly happy with the results.

These two tags give a tremendous amount of expressive power to HTML.

## So What Isn’t Hypermedia?

So links and forms are the two main hypermedia-based mechanisms for interacting with a server available in HTML.

Now let’s consider a different approach: let’s interact with a server by issuing an HTTP request via JavaScript. To do this, we will use the [fetch()](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) API, a popular API for issuing an “Asynchronous JavaScript and XML,” or AJAX request, available in all modern web browsers:

    <button onclick="fetch('/api/v1/contacts/1') <1>
                    .then(response => response.json()) <2>
                    .then(data => updateUI(data)) "> <3>
        Fetch Contact
    button>

JavaScript

1.  Issue the request.
    
2.  Convert the response to a JavaScript object.
    
3.  Invoke the `updateUI()` function with the object.
    

This button has an `onclick` attribute that specifies some JavaScript to run when the button is clicked.

The JavaScript will issue an AJAX HTTP `GET` request to `/api/v1/contacts/1` using `fetch()`. An AJAX request is like a “normal” HTTP request, but it is issued “behind the scenes” by the browser. The user does not see a request indicator from the browser as they would with normal links and forms. Additionally, unlike requests issued by those hypermedia controls, it is up to the JavaScript code to handle the response from the server.

Despite AJAX having XML as part of its acronym, today the HTTP response to this request would almost certainly be in the JavaScript Object Notation (JSON) format rather than XML.

An HTTP response to this request might look something like this:

    { <1>
      "id": 42, <2>
      "email" : "json-example@example.org" <3>
    }

JSON

1.  The start of a JSON object.
    
2.  A property, in this case with the name `id` and the value `42`.
    
3.  Another property, the email of the contact with this id.
    

The JavaScript code above converts the JSON text received from the server into a JavaScript object by calling the `json()` method on it. This new JavaScript object is then handed off to the `updateUI()` method.

The `updateUI()` method is responsible for updating the UI based on the data encoded in the JavaScript Object, perhaps by displaying the contact in a bit of HTML generated via a client-side template in the JavaScript application.

The details of exactly what the `updateUI()` function does aren’t important for our discussion.

What _is_ important, what is the _crucial_ aspect of this JSON-based server interaction is that it is _not_ using hypermedia. The JSON API being used here does not return a hypermedia response. There are no _hyperlinks_ or other hypermedia-style controls in it.

This JSON API is, rather, a _Data API_.

Because the response is in JSON and is _not_ hypermedia, the JavaScript `updateUI()` method must understand how to turn this contact data into HTML.

In particular, the code in `updateUI()` needs to know about the _internal structure_ and meaning of the data.

It needs to know:- Exactly how the fields in the JSON data object are structured and named.- How they relate to one another.- How to update the local data this new data corresponds with.- How to render this data to the browser.- What additional actions/API end points can be called with this data.

In short, the logic in `updateUI()` needs to have intimate knowledge of the API endpoint at `/api/v1/contact/1`, knowledge provided via some side-channel beyond the response itself. As a result, the `updateUI()` code and the API have a strong relationship, known as _tight coupling_: if the format of the JSON response changes, then the code for `updateUI()` will almost certainly also need to be changed as well.

### Single Page Applications

This bit of JavaScript, while very modest, is the organic beginnings of a much larger conceptual approach to building web applications. This is the beginning of a _Single Page Application (SPA)_. The web application is no longer navigating _between_ pages using hypermedia controls as was the case with links and forms.

Instead, the application is exchanging _plain data_ with the server and then updating the content _within_ a single page.

When this strategy or architecture is adopted for an entire application, everything happens on a “Single Page” and, thus the application becomes a “Single Page Application.”

The Single Page Application architecture is extremely popular today and has been the dominant approach to building web applications for the last decade. This can be observed by the high level of mind-share and discussion it has received in the industry.

Today the vast majority of Single Page Applications adopt far more sophisticated frameworks for managing their user interface than this simple example shows. Popular libraries such as React, Angular, Vue.js, etc. are now the common — indeed, the standard — way to build web applications.

With these more complex frameworks developers typically work with an elaborate client-side model — that is, with JavaScript objects stored locally in the browser’s memory that represent the “model” or “domain” of your application. These JavaScript objects are updated via JavaScript code and the framework then “reacts” to these changes, updating the user interface.

When the user interface is updated by a user these changes also flow _into_ the model objects, establishing a “two-way” binding mechanism: the model can update the UI, and the UI can update the model.

This is a much more sophisticated approach to a web client than hypermedia, and it typically does away almost entirely with the underlying hypermedia infrastructure available in the browser.

HTML is still used to build user interfaces, but the _hypermedia_ aspect of the two major hypermedia controls, anchors and forms, are unused. Neither tag interacts with a server via their native _hypermedia_ mechanism. Rather, they become user interface elements that drive local interactions with the in-memory domain model via JavaScript, which is then synchronized with the server using plain data JSON APIs.

So, as with our simple button above, the Single Page Application approach foregoes the hypermedia architecture. It leaves aside the advantages of the existing RESTful architecture of the web and the built-in functionality found in HTML’s native hypermedia controls in favor of JavaScript driven behaviors.

SPAs are much more like _thick client applications_, that is, like the client-server applications of the 1980s — an architecture popular _before_ the web came along and that the web was, in many ways, a reaction to.

This approach isn’t necessarily wrong, of course: there are times when a thick client approach is the appropriate choice for an application. But it is worth thinking about _why_ web developers so frequently make this choice without considering other alternatives, and if there are reasons _not_ to go down this path.