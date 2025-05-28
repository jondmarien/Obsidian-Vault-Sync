# Picking A “Web Stack”

In order to demonstrate how web 1.0 applications work, we need to pick a server-side language and a library for handling HTTP requests. Colloquially, this is called our “Server-Side” or “Web” stack, and there are literally hundreds of options to choose from, many with passionate followings. You probably have a web framework that you prefer and, while we wish we could write this book for every possible stack out there, in the interest of simplicity (and sanity) we can only pick one.

For this book we are going to use the following stack:

*   [Python](https://www.python.org/) as our programming language.
    
*   [Flask](https://palletsprojects.com/p/flask/) as our web framework, allowing us to connect HTTP requests to Python logic.
    
*   [Jinja2](https://palletsprojects.com/p/jinja/) for our server-side templating language, allowing us to render HTML responses using a familiar and intuitive syntax.
    

Why this particular stack?

Python is the most popular programming language in the world, as of this writing, according to the [TIOBE index](https://www.tiobe.com/tiobe-index/), a respected measure of programming language popularity. More importantly, Python is easy to read even if you aren’t familiar with it.

We chose the Flask web framework because it is simple and does not impose a lot of structure on top of the basics of HTTP request handling.

This bare-bones approach is a good match for our needs: in other cases you might consider a more full-featured Python framework, such as [Django](https://www.djangoproject.com/), which supplies much more functionality out of the box than Flask does.

By using Flask for our book, we will be able to keep our code focused on _hypermedia exchanges_.

We picked Jinja2 templates because they are the default templating language for Flask. They are simple enough and similar enough to most other server-side templating languages that most people who are familiar with any server-side (or client-side) templating library should be able to understand them quickly and easily.

Even if this combination of technologies isn’t your preferred stack, please, keep reading: you will learn quite a bit from the patterns we introduce in the coming chapters and it shouldn’t be hard to map them into your preferred language and frameworks.

With this stack we will be rendering HTML _on the server-side_ to return to clients, rather than producing JSON. This is the traditional approach to building web applications. However, with the rise of SPAs, this approach is not as widely used a technique as it once was. Today, as people are rediscovering this style of web applications, the term “Server-Side Rendering” or SSR is emerging as the way that people talk about it. This contrasts with “Client-Side Rendering”, that is, rendering templates in the browser with data retrieved in JSON form from the server, as is common in SPA libraries.

In Contact.app we will intentionally keep things as simple as possible to maximize the teaching value of our code: it won’t be perfectly factored code, but it will be easy to follow for readers, even if they have little Python experience, and it should be easy to translate both the application and the techniques demonstrated into your preferred programming environment.