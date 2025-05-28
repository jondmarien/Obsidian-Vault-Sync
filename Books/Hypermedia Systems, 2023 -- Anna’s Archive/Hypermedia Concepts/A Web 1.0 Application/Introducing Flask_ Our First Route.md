# Introducing Flask: Our First Route

Flask is a simple but flexible web framework for Python. We’ll ease into it by touching on its core elements.

A Flask application consists of a series of _routes_ tied to functions that execute when an HTTP request to a given path is made. It uses a Python feature called “decorators” to declare the route that will be handled, which is then followed by a function to handle requests to that route. We’ll use the term “handler” to refer to the functions associated with a route.

Let’s create our first route definition, a simple “Hello World” route. In the following Python code you will see the `@app` symbol. This is the flask decorator that allows us to set up our routes. Don’t worry too much about how decorators work in Python, just know that this feature allows us to map a given _path_ to a particular function (i.e., handler). The Flask application, when started, will take HTTP requests and look up the matching handler and invoke it.

    @app.route("/") <1>
    def index(): <2>
        return "Hello World!" <3>

A simple “Hello World” route

1.  Establishes we are mapping the `/` path as a route.
    
2.  The next method is the handler for that route.
    
3.  Returns the string “Hello World!” to the client.

The `route()` method on the Flask decorator takes an argument: the path you wish the route to handle. Here we pass in the root or `/` path, as a string, to handle requests to the root path.

This route declaration is then followed by a simple function definition, `index()`. In Python, decorators invoked in this manner apply to the function immediately following them. Therefore, this function becomes the “handler” for that route, and will be executed when an HTTP request to the given path is made.

Note that the name of the function doesn’t matter, we can call it whatever we’d like so long as it is unique. In this case we chose `index()` because that fits with the route we are handling: the root “index” of the web application.

So we have the `index()` function immediately following our route definition for the root, and this will become the handler for the root URL in our web application.

The handler in this case is dead simple, it just returns a string, “Hello World!”, to the client. This isn’t hypermedia yet, but a browser will render it just fine:

![](file0.png)

Hello World!

Great, there’s our first step into Flask, showing the core technique we are going to use to respond to HTTP requests: routes mapped to handlers.

For Contact.app, rather than rendering “Hello World!” at the root path, we are going to do something a little fancy: we are going to redirect to another path, the `/contacts` path. Redirects are a feature of HTTP that allow you to redirect a client to another location with an HTTP response.

We are going to display a list of contacts as our root page, and, arguably, redirecting to the `/contacts` path to display this information is a bit more consistent with the notion of resources with REST. This is a judgement call on our part, and not something we feel is too important, but it makes sense in terms of routes we will set up later in the application.

To change our “Hello World” route to a redirect, we only need to change one line of code:

    @app.route("/")
    def index():
        return redirect("/contacts") <1>

Changing “Hello World” to a redirect

1.  Update to a call to `redirect()`

Now the `index()` function returns the result of the Flask-supplied `redirect()` function with the path we’ve supplied. In this case the path is `/contacts`, passed in as a string argument. Now, if you navigate to the root path, `/`, our Flask application will forward you on to the `/contacts` path.