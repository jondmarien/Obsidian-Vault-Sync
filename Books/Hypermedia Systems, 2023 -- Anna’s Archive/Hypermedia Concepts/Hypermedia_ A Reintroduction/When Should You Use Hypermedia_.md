# When Should You Use Hypermedia?

Hypermedia is often, though _not always_, a great choice for a web application.

Perhaps you are building a website or application that simply doesn’t _need_ a huge amount of user-interactivity. There are many useful web applications like this, and there is no shame in it! Applications like Amazon, eBay, any number of news sites, shopping sites, message boards and so on don’t need a massive amount of interactivity to be effective: they are mainly text and images, which is exactly what the web was designed for.

Perhaps your application adds most of its value on the _server side_, by coordinating users or by applying sophisticated data analysis and then presenting it to a user. Perhaps your application adds value by simply sitting in front of a well-designed database, with simple Create-Read-Update-Delete (CRUD) operations. Again, there is no shame in this!

In any of these cases, using a hypermedia approach would likely be a great choice: the interactivity needs of these applications are not dramatic, and much of the value of these applications lives on the server side, rather than on the client side.

All of these applications are amenable to what Roy Fielding called “large-grain hypermedia data transfers”: you can simply use anchor tags and forms, with responses that return entire HTML documents from requests, and things will work just fine. This is exactly what the web was designed to do!

By adopting the hypermedia approach for these applications, you will save yourself a huge amount of client-side complexity that comes with adopting the Single Page Application approach: there is no need for client-side routing, for managing a client-side model, for hand-wiring in JavaScript logic, and so forth. The back button will “just work.” Deep linking will “just work.” You will be able to focus your efforts on your server, where your application is actually adding value.

And, by layering htmx or another hypermedia-oriented library on top of this approach, you can address many of the usability issues that come with vanilla HTML and take advantage of finer-grained hypermedia transfers. This opens up a whole slew of new user interface and experience possibilities, making the set of applications that can be built using hypermedia _much_ larger.

But more on that later.