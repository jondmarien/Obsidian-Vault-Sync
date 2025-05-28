# Adding a JSON Data API To Contact.app

Alright, so how are we going to add a JSON Data API to our application? One approach, popularized by the Ruby on Rails web framework, is to use the same URL endpoints as your hypermedia application, but use the HTTP `Accept` header to determine if the client wants a JSON representation or an HTML representation. The HTTP `Accept` header allows a client to specify what sort of Multipurpose Internet Mail Extensions (MIME) types, that is file types, it wants back from the server: JSON, HTML, text and so on.

So, if the client wanted a JSON representation of all contacts, they might issue a `GET` request that looks like this:

    Accept: application/json
    
    GET /contacts
    

A request for a JSON representation of all contacts

If we adopted this pattern then our request handler for `/contacts/` would need to be updated to inspect this header and, depending on the value, return a JSON rather than HTML representation for the contacts. Ruby on Rails has support for this pattern baked into the framework, making it very easy to switch on the requested MIME type.

Unfortunately, our experience with this pattern has not been great, for reasons that should be clear given the differences we outlined between Data and hypermedia APIs: they have different needs and often take on very different “shapes”, and trying to pound them into the same set of URLs ends up creating a lot of tension in the application code.

Given the different needs of the two APIs and our experience managing multiple APIs like this, we think separating the two, and, therefore, breaking the JSON Data API out to its own set of URLs is the right choice. This will allow us to evolve the two APIs separately from one another, and give us room to improve each independently, in a manner consistent with their own individual strengths.

## Picking a Root URL For Our API

Given that we are going to split our JSON Data API routes out from our regular hypermedia routes, where should we place them? One important consideration here is that we want to make sure that we can version our API cleanly in some way, regardless of the pattern we choose.

Looking around, a lot of places use a subdomain for their APIs, something like `https://api.mywebapp.example.com` and, in fact, often encode versioning in the subdomain: `https://v1.api.mywebapp.example.com`.

While this makes sense for large companies, it seems like a bit of overkill for our modest little Contact.app. Rather than using subdomains, which are a pain for local development, we will use sub-paths within the existing application:

*   We will use `/api` as the root for our Data API functionality
    
*   We will use `/api/v1` as the entry point for version 1 of our Data API
    

If and when we decide to bump the API version, we can move to `/api/v2` and so on.

This approach isn’t perfect, of course, but it will work for our simple application and can be adapted to a subdomain approach or various other methods at a later point, when our Contact.app has taken over the internet and we can afford a large team of API developers. :)

## Our First JSON Endpoint: Listing All Contacts

Let’s add our first Data API endpoint. It will handle an HTTP `GET` request to `/api/v1/contacts`, and return a JSON list of all contacts in the system. In some ways it will look quite a bit like our initial code for the hypermedia route `/contacts`: we will load all the contacts from the contacts database and then render some text as a response.

We are also going to take advantage of a nice feature of Flask: if you simply return an object from a handler, it will serialize (that is, convert) that object into a JSON response. This makes it very easy to build simple JSON APIs in flask!

    @app.route("/api/v1/contacts", methods=["GET"]) <1>
    def json_contacts():
        contacts_set = Contact.all()
        contacts_dicts = [c.__dict__ for c in contacts_set] <2>
        return {"contacts": contacts_dicts} <3>

A JSON data API to return all contacts

1.  JSON API gets its own path, starting with `/api`.
    
2.  Convert the contacts array into an array of simple dictionary (map) objects.
    
3.  Return a dictionary that contains a `contacts` property of all the contacts.
    

This Python code might look a little foreign to you if you are not a Python developer, but all we are doing is converting our contacts into an array of simple name/value pairs and returning that array in an enclosing object as the `contacts` property. This object will be serialized into a JSON response automatically by Flask.

With this in place, if we make an HTTP `GET` request to `/api/v1/contacts`, we will see a response that looks something like this:

    {
      "contacts": [
        {
          "email": "carson@example.com",
          "errors": {},
          "first": "Carson",
          "id": 2,
          "last": "Gross",
          "phone": "123-456-7890"
        },
        {
          "email": "joe@example2.com",
          "errors": {},
          "first": "",
          "id": 3,
          "last": "",
          "phone": ""
        },
        ...
      ]
    }

Some sample data from our API

So, you can see, we now have a way to get a relatively simple JSON representation of our contacts via an HTTP request. Not perfect, but it’s a good start. It’s certainly good enough to write some basic automated scripts against. For example, you could use this Data API to:

*   Move your contacts to another system on a nightly basis
    
*   Back your contacts up to a local file
    
*   Automate an email blast to your contacts
    

Having this small JSON Data API opens up a lot of automation possibilities that would be messier to achieve with our existing hypermedia API.

## Adding Contacts

Let’s move on to the next piece of functionality: the ability to add a new contact. Once again, our code is going to look similar in some ways to the code that we wrote for our normal web application. However, here we are also going to see the JSON API and the hypermedia API for our web application begin to obviously diverge.

In the web application, we needed a separate path, `/contacts/new` to host the HTML form for creating a new contact. In the web application we made the decision to issue a `POST` to that same path to keep things consistent.

In the case of the JSON API, there is no such path needed: the JSON API “just is”: it doesn’t need to provide any hypermedia representation for creating a new contact. You simply know where to issue a `POST` to create a contact — likely through some documentation provided about the API — and that’s it.

Because of that fact, we can put the “create” handler on the same path as the “list” handler: `/api/v1/contacts`, but have it respond only to HTTP `POST` requests.

The code here is relatively straightforward: populate a new contact with the information from the `POST` request, attempt to save it, and — if it is not successful — show error messages. Here is the code:

    @app.route("/api/v1/contacts", methods=["POST"]) <1>
    def json_contacts_new():
        c = Contact(None,
          request.form.get('first_name'),
          request.form.get('last_name'),
          request.form.get('phone'),
          request.form.get('email')) <2>
        if c.save(): <3>
            return c.__dict__
        else:
            return {"errors": c.errors}, 400 <4>

Adding contacts with our JSON API

1.  This handler is on the same path as the first one for our JSON API, but handles `POST` requests.
    
2.  We create a new Contact based on values submitted with the request.
    
3.  We attempt to save the contact and, if successful, render it as a JSON object.
    
4.  If the save is not successful, we render an object showing the errors, with a response code of `400 (Bad Request)`.
    

In some ways this is similar to our `contacts_new()` handler from our web application; we are creating the contact and attempting to save it. In other ways it is very different:

*   There is no redirection happening here on a successful creation, because we are not dealing with a hypermedia client like the browser.
    
*   In the case of a bad request, we simply return an error response code, `400 (Bad Request)`. This is in contrast with the web application, where we re-render the form with error messages in it.
    

These sorts of differences, over time, build up and make the idea of keeping your JSON and hypermedia APIs on the same set of URLs less and less appealing.

## Viewing Contact Details

Next, let’s make it possible for a JSON API client to download the details for a single contact. We will naturally use an HTTP `GET` for this functionality and will follow the convention we established for our regular web application, and put the path at `/api/v1/contacts/`. So, for example, if you want to see the details of the contact with the id `42`, you would issue an HTTP `GET` to `/api/v1/contacts/42`.

This code is quite simple:

    @app.route("/api/v1/contacts/", methods=["GET"]) <1>
    def json_contacts_view(contact_id=0):
        contact = Contact.find(contact_id) <2>
        return contact.__dict__ <3>

Getting the details of a contact in JSON

1.  Add a new `GET` route at the path we want to use for viewing contact details
    
2.  Look the contact up via the id passed in through the path
    
3.  Convert the contact to a dictionary, so it can be rendered as JSON response
    

Nothing too complicated: we look the contact up by the ID provided in the path to the controller. We then render it as JSON. You have to appreciate the simplicity of this code!

Next, let’s add updating and deleting a contact as well.

## Updating & Deleting Contacts

As with the create contact API endpoint, because there is no HTML UI to produce for them, we can reuse the `/api/v1/contacts/` path. We will use the `PUT` HTTP method for updating a contact and the `DELETE` method for deleting one.

Our update code is going to look nearly identical to the create handler, except that, rather than creating a new contact, we will look up the contact by ID and update its fields. In this sense we are just combining the code of the create handler and the detail view handler.

    @app.route("/api/v1/contacts/", methods=["PUT"]) <1>
    def json_contacts_edit(contact_id):
        c = Contact.find(contact_id) <2>
        c.update(
            request.form['first_name'],
            request.form['last_name'],
            request.form['phone'],
            request.form['email']) <3>
        if c.save(): <4>
            return c.__dict__
        else:
            return {"errors": c.errors}, 400

Updating a contact with our JSON API

1.  We handle `PUT` requests to the URL for a given contact.
    
2.  Look the contact up via the id passed in through the path.
    
3.  We update the contact’s data from the values included in the request.
    
4.  From here on the logic is identical to the `json_contacts_create()` handler.
    

Once again, thanks to the built-in functionality in Flask, simple to implement.

Let’s look at deleting a contact now. This turns out to be even simpler: as with the update handler we are going to look up the contact by id, and then, well, delete it. At that point we can return a simple JSON object indicating success.

    @app.route("/api/v1/contacts/", methods=["DELETE"]) <1>
    def json_contacts_delete(contact_id=0):
        contact = Contact.find(contact_id)
        contact.delete() <2>
        return jsonify({"success": True}) <3>

Deleting a contact with our JSON API

1.  We handle `DELETE` requests to the URL for a given contact.
    
2.  Look the contact up and invoke the `delete()` method on it.
    
3.  Return a simple JSON object indicating that the contact was successfully deleted.
    

And, with that, we have our simple little JSON Data API to live alongside our regular web application, nicely separated out from the main web application, so it can evolve separately as needed.

## Additional Data API Considerations

Now, we would have a lot more to do if we wanted to make this a production ready JSON API. At minimum we would need to add:

*   Rate limiting, important for any public-facing Data API to avoid abusive clients.
    
*   An authentication mechanism. (We don’t have one for our web application either!)
    
*   Support for pagination of our contact data.
    
*   Several small items, such as rendering a proper `404 (Not Found)` response if someone makes a request with a contact id that doesn’t exist.
    

These topics are beyond the scope of this book, but we’d like to focus on one in particular, authentication, in order to show the difference between our hypermedia and JSON API. In order to secure our application we need to add _authentication_, some mechanism for determining who a request is coming from, and also _authorization_, determining if they have the right to perform the request.

We will set authorization aside for now and consider only authentication.

### Authentication in web applications

In the HTML web application world, authentication has traditionally been done via a login page that asks a user for their username (often their email) and a password. This password is then checked against a database of (hashed) passwords to establish that the user is who they say they are. If the password is correct, then a _session cookie_ is established, indicating who the user is. This cookie is then sent with every request that the user makes to the web application, allowing the application to know which user is making a given request.

**HTTP Cookies**

HTTP Cookies are kind of a strange feature of HTTP. In some ways they violate the goal of remaining stateless, a major component of the RESTful architecture: a server will often use a session cookie as an index into state kept on the server “on the side”, such as a cache of the last action performed by the user.

Nonetheless, cookies have proven extremely useful and so people tend not to complain about this aspect of them too much (We are not sure what our other options would be here!) An interesting example of pragmatism gone (relatively) right in web development.

In comparison with the standard web application approach to authentication, a JSON API will typically use some sort of _token based_ authentication: an authentication token will be established via a mechanism like OAuth, and that authentication token will then be passed, often as an HTTP Header, with every request that a client makes.

At a high level this is similar to what happens in normal web application authentication: a token is established somehow and then that token is part of every request. However, in practice, the mechanics tend to be wildly different:

*   Cookies are part of the HTTP specification and can be easily _set_ by an HTTP Server.
    
*   JSON Authentication tokens, in contrast, often require elaborate exchange mechanics like OAuth to be established.
    

These differing mechanics for establishing authentication are yet another good reason for splitting up our JSON and hypermedia APIs.

## The “Shape” of Our Two APIs

When we were building out our API, we noted that in many cases the JSON API didn’t require as many end points as our hypermedia API did: we didn’t need a `/contacts/new` handler, for example, to provide a hypermedia representation for creating contacts.

Another aspect of our hypermedia API to consider was the performance improvement we made: we pulled the total contact count out to a separate endpoint and implemented the “Lazy Load” pattern, to improve the perceived performance of our application.

Now, if we had both our hypermedia and JSON API sharing the same paths, would we want to publish this API as a JSON endpoint as well?

Maybe, but maybe not. This was a pretty specific need for our web application, and, absent a request from a user of our JSON API, it doesn’t make sense to include it for JSON consumers.

And what if, by some miracle, the performance issues with `Contact.count()` that we were addressing with the Lazy Load pattern goes away? Well, in our Hypermedia-Driven Application we can simply revert to the old code and include the count directly in the request to `/contacts`. We can remove the `contacts/count` endpoint and all the logic associated with it. Because of the uniform interface of hypermedia, the system will continue to work just fine.

But what if we had tied our JSON API and hypermedia API together, and published `/contacts/count` as a supported end point for our JSON API? In that case we couldn’t simply remove the endpoint: a (non-hypermedia) client might be relying on it.

Once again you can see the flexibility of the hypermedia approach and why separating your JSON API out from your hypermedia API lets you take maximum advantage of that flexibility.

## The Model View Controller (MVC) Paradigm

One thing you may have noticed about the handlers for our JSON API is that they are relatively simple and regular. Most of the hard work of updating data and so forth is done within the contact model itself: the handlers act as simple connectors that provide a go-between the HTTP requests and the model.

This is the ideal controller of the Model-View-Controller (MVC) paradigm that was so popular in the early web: a controller should be “thin”, with the model containing the majority of the logic in the system.

**The Model View Controller pattern**

The Model View Controller design pattern is a classic architectural pattern in software development, and was a major influence in early web development. It is no longer emphasized as heavily, as web development has split into frontend and backend camps, but most web developers are still familiar with the idea.

Traditionally, the MVC pattern mapped into web development like so:

*   Model - A collection of “domain” classes that implement all the logic and rules for the particular domain your application is designed for. The model typically provides “resources” that are then presented to clients as HTML “representations.”
    
*   View - Typically views would be some sort of client-side templating system, and would render the aforementioned HTML representation for a given Model instance.
    
*   Controller - The controller’s job is to take HTTP requests, convert them into sensible requests to the Model and forward those requests on to the appropriate Model objects. It then passes the HTML representation back to the client as an HTTP response.
    

Thin controllers make it easy to split your JSON and hypermedia APIs out, because all the important logic lives in the domain model that is shared by both. This allows you to evolve both separately, while still keeping logic in sync with one another.

With properly built “thin” controllers and “fat” models, keeping two separate APIs both in sync and yet still evolving separately is not as difficult or as crazy as it might sound.

# HTML Notes: Microformats

[Microformats](https://microformats.org/) is a standard for embedding machine-readable structured data in HTML. It uses classes to mark certain elements as containing information to be extracted, with conventions for extracting common properties like name, URL and photo without classes. By adding these classes into the HTML representation of an object, we allow the properties of the object to be recovered from the HTML. For example, this simple HTML:

    <a class="h-card" href="https://john.example">
      <img src="john.jpg" alt=""> John Doe
    a>

can be parsed into this JSON-like structure by a microformats parser:

    {
      "type": ["h-card"],
      "properties": {
        "name": ["John Doe"],
        "photo": ["john.jpg"],
        "url": ["https://john.example"]
      }
    }

Using a variety of properties and nested objects, we could mark up every bit of information about a contact, for example, in a machine-readable way.

As explained in the above chapter, trying to use the same mechanism for human and machine interaction is not a good idea. Your human-facing and machine-facing interfaces may end up being limited by each other. If you want to expose domain-specific data and actions to users and developers, a JSON API is a great option.

However, microformats are way easier to adopt. A protocol or standard that requires websites to implement a JSON API has a high technical barrier. In comparison, any website can be augmented with microformats simply by adding a few classes. Other HTML-embedded data formats like microdata, Open Graph are similarly easy to adopt. This makes microformats useful for cross-website (dare we say _web-scale_) systems like the [IndieWeb](https://indieweb.org), which uses it pervasively.

* * *

[^1]. Rendering here refers to HTML generation. Framework support for server-side rendering is not needed in a HDA because generating HTML on the server is the default.

[^2]. Beware that Shadow DOM is a newer web platform feature that’s still in development at the time of writing. In particular, there are some accessibility bugs that may occur when elements inside and outside the shadow root interact.