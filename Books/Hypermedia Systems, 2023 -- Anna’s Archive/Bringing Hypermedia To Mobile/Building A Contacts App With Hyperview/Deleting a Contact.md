# Deleting A Contact

We piggybacked contact delete functionality into the same template used to edit a contact. This second form will issue an HTTP `POST` to `/contacts//delete`, and we will need to create a handler for that path as well.

Here is what the controller looks like:

    @app.route("/contacts//delete", methods=["POST"]) <3>
    def contacts_delete(contact_id=0):
        contact = Contact.find(contact_id)
        contact.delete() <2>
        flash("Deleted Contact!")
        return redirect("/contacts") <3>

The “delete contact” controller code

1.  Handle a `POST` the `/contacts//delete` path.
    
2.  Look up and then invoke the `delete()` method on the contact.
    
3.  Flash a success message and redirect to the main list of contacts.
    

The handler code is very simple since we don’t need to do any validation or conditional logic: we simply look up the contact the same way we have been doing in our other handlers and invoke the `delete()` method on it, then redirect back to the list of contacts with a success flash message.

No need for a template in this case, the contact is gone.

# Contact.app…​ Implemented!

And, well…​ believe it or not, that’s our entire contact application!

If you’ve struggled with parts of the code so far, don’t worry: we don’t expect you to be a Python or Flask expert (we aren’t!). You just need a basic understanding of how they work to benefit from the remainder of the book.

This is a small and simple application, but it does demonstrate many of the aspects of traditional, web 1.0 applications: CRUD, the Post/Redirect/Get pattern, working with domain logic in a controller, organizing our URLs in a coherent, resource-oriented manner.

And, furthermore, this is a deeply _Hypermedia-Driven_ web application. Without thinking about it very much, we have been using REST, HATEOAS and all the other hypermedia concepts we discussed earlier. We would bet that this simple little contact app of ours is more RESTful than 99% of all JSON APIs ever built!

Just by virtue of using a _hypermedia_, HTML, we naturally fall into the RESTful network architecture.

So that’s great. But what’s the matter with this little web app? Why not end here and go off to develop web 1.0 style applications?

Well, at some level, nothing is wrong with it. Particularly for an application as simple as this one, the older way of building web apps might be a perfectly acceptable approach.

However, our application does suffer from that “clunkiness” that we mentioned earlier when discussing web 1.0 applications: every request replaces the entire screen, introducing a noticeable flicker when navigating between pages. You lose your scroll state. You have to click around a bit more than you might in a more sophisticated web application.

Contact.app, at this point, just doesn’t feel like a “modern” web application.

Is it time to reach for a JavaScript framework and JSON APIs to make our contact application more interactive?

No. No it isn’t.

It turns out that we can improve the user experience of this application while retaining its fundamental hypermedia architecture.

In the next few chapters we will look at [htmx](https://htmx.org), a hypermedia-oriented library that will let us improve our contact application while retaining the hypermedia-based approach we have used so far.

# HTML Notes: Framework Soup

Components encapsulate a section of a page along with its dynamic behavior. While encapsulating behavior is a good way to organize code, it can also separate elements from their surrounding context, which can lead to wrong or inadequate relationships between elements. The result is what one might call _component soup_, where information is hidden in component state, rather than being present in the HTML, which is now incomprehensible due to missing context.

Before you reach for components for reuse, consider your options. Lower-level mechanisms often (allow you to) produce better HTML. In some cases, components can actually _improve_ the clarity of your HTML.

> The fact that the HTML document is something that you barely touch, because everything you need in there will be injected via JavaScript, puts the document and the page structure out of focus.
> 
> ℄ Manuel Matuzović, [Why I’m not the biggest fan of Single Page Applications](https://www.matuzo.at/blog/2023/single-page-applications-criticism)

In order to avoid

soup (or Markdown soup, or Component soup), you need to be aware of the markup you’re producing and be able to change it.

Some SPA frameworks, and some web components, make this more difficult by putting layers of abstraction between the code the developer writes and the generated markup.

While these abstractions can allow developers to create richer UI or work faster, their pervasiveness means that developers can lose sight of the actual HTML (and JavaScript) being sent to clients. Without diligent testing, this leads to inaccessibility, poor SEO, and bloat.

* * *

[^1]. The single-page version is too slow to load and render on most computers. There’s also a developers” edition at /dev, but the standard version has nicer styling.