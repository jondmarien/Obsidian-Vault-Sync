# A Second Step: Deleting Contacts With HTTP DELETE

For our next step with htmx, recall that Contact.app has a small form on the edit page of a contact that is used to delete the contact:

    <form action="/contacts/{{ contact.id }}/delete" method="post">
      <button>Delete Contactbutton>
    form>

Plain HTML form to delete a contact

This form issued an HTTP `POST` to, for example, `/contacts/42/delete`, in order to delete the contact with the ID 42.

We mentioned previously that one of the annoying things about HTML is that you can’t issue an HTTP `DELETE` (or `PUT` or `PATCH`) request directly, even though these are all part of HTTP and HTTP is _obviously designed_ for transferring HTML.

Thankfully, now, with htmx, we have a chance to rectify this situation.

The “right thing,” from a RESTful, resource-oriented perspective is, rather than issuing an HTTP `POST` to `/contacts/42/delete`, to issue an HTTP `DELETE` to `/contacts/42`. We want to delete the contact. The contact is a resource. The URL for that resource is `/contacts/42`. So the ideal is a `DELETE` request to `/contacts/42/`.

Let’s update our application to do this by adding the htmx `hx-delete` attribute to the “Delete Contact” button:

    <button hx-delete="/contacts/{{ contact.id }}">Delete Contactbutton>

An htmx-powered button for deleting a contact

Now, when a user clicks this button, htmx will issue an HTTP `DELETE` request via AJAX to the URL for the contact in question.

A couple of things to notice:

*   We no longer need a `form` tag to wrap the button, because the button itself carries the hypermedia action that it performs directly on itself.
    
*   We no longer need to use the somewhat awkward `"/contacts/{{ contact.id }}/delete"` route, but can simply use the `"/contacts/{{ contact.id }}` route, since we are issuing a `DELETE`. By using a `DELETE` we disambiguate between a request intended to update the contact and a request intended to delete it, using the native HTTP tools available for exactly this reason.
    

Note that we have done something pretty magical here: we have turned this button into a _hypermedia control_. It is no longer necessary that this button be placed within a larger `form` tag in order to trigger an HTTP request: it is a stand-alone, and fully featured hypermedia control on its own. This is at the heart of htmx, allowing any element to become a hypermedia control and fully participate in a Hypermedia-Driven Application.

We should also note that, unlike with the `hx-boost` examples above, this solution will _not_ degrade gracefully. To make this solution degrade gracefully, we would need to wrap the button in a form element and handle a `POST` on the server side as well.

In the interest of keeping our application simple, we are going to omit that more elaborate solution.

## Updating The Server-Side Code

We have updated the client-side code (if HTML can be considered code) so it now issues a `DELETE` request to the appropriate URL, but we still have some work to do. Since we updated both the route and the HTTP method we are using, we are going to need to update the server-side implementation as well to handle this new HTTP request.

    @app.route("/contacts//delete", methods=["POST"])
    def contacts_delete(contact_id=0):
        contact = Contact.find(contact_id)
        contact.delete()
        flash("Deleted Contact!")
        return redirect("/contacts")

The original server-side code for deleting a contact

We’ll need to make two changes to our handler: update the route, and update the HTTP method we are using to delete contacts.

    @app.route("/contacts/", methods=["DELETE"]) <1>
    def contacts_delete(contact_id=0):
        contact = Contact.find(contact_id)
        contact.delete()
        flash("Deleted Contact!")
        return redirect("/contacts")

Updated handler with new route and method

1.  An updated path and method for the handler.
    

Pretty simple, and much cleaner.

### A response code gotcha

Unfortunately, there is a problem with our updated handler: by default, in Flask the `redirect()` method responds with a `302 Found` HTTP Response Code.

According to the Mozilla Developer Network (MDN) web docs on the [302 Found](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/302) response, this means that the HTTP _method_ of the request _will be unchanged_ when the redirected HTTP request is issued.

We are now issuing a `DELETE` request with htmx and then being redirected to the `/contacts` path by flask. According to this logic, that would mean that the redirected HTTP request would still be a `DELETE` method. This means that, as it stands, the browser will issue a `DELETE` request to `/contacts`.

This is definitely _not_ what we want: we would like the HTTP redirect to issue a `GET` request, slightly modifying the Post/Redirect/Get behavior we discussed earlier to be a Delete/Redirect/Get.

Fortunately, there is a different response code, [303 See Other](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/303), that does what we want: when a browser receives a `303 See Other` redirect response, it will issue a `GET` to the new location.

So we want to update our code to use the `303` response code in the controller.

Thankfully, this is very easy: there is a second parameter to `redirect()` that takes the numeric response code you wish to send.

    @app.route("/contacts/", methods=["DELETE"])
    def contacts_delete(contact_id=0):
        contact = Contact.find(contact_id)
        contact.delete()
        flash("Deleted Contact!")
        return redirect("/contacts", 303) <1>

Updated handler with `303` redirect response

1.  The response code is now a 303.
    

Now, when you want to remove a given contact, you can simply issue a `DELETE` to the same URL as you used to access the contact in the first place.

This is a natural HTTP-based approach to deleting a resource.

## Targeting The Right Element

We aren’t quite finished with our updated delete button. Recall that, by default, htmx “targets” the element that triggers a request, and will place the HTML returned by the server inside that element. Right now, the “Delete Contact” button is targeting itself.

That means that, since the redirect to the `/contacts` URL is going to re-render the entire contact list, we will end up with that contact list placed _inside_ the “Delete Contact” button.

Mis-targeting like this comes up from time to time when you are working with htmx and can lead to some pretty funny situations.

The fix for this is easy: add an explicit target to the button, and target the `body` element with the response:

    <button hx-delete="/contacts/{{ contact.id }}"
        hx-target="body"> <1>
      Delete Contact
    button>

A fixed htmx-powered button for deleting a contact

1.  An explicit target added to the button.
    

Now our button behaves as expected: clicking on the button will issue an HTTP `DELETE` to the server against the URL for the current contact, delete the contact and redirect back to the contact list page, with a nice flash message.

Is everything working smoothly now?

## Updating The Location Bar URL Properly

Well, almost.

If you click on the button you will notice that, despite the redirect, the URL in the location bar is not correct. It still points to `/contacts/{{ contact.id }}`. That’s because we haven’t told htmx to update the URL: it just issues the `DELETE` request and then updates the DOM with the response.

As we mentioned, boosting via `hx-boost` will naturally update the location bar for you, mimicking normal anchors and forms, but in this case we are building a custom button hypermedia control to issue a `DELETE`. We need to let htmx know that we want the resulting URL from this request “pushed” into the location bar.

We can achieve this by adding the `hx-push-url` attribute with the value `true` to our button:

    <button hx-delete="/contacts/{{ contact.id }}"
      hx-target="body"
      hx-push-url="true"> <1>
      Delete Contact
    button>

Deleting a contact, now with proper location information

1.  We tell htmx to push the redirected URL up into the location bar.
    

_Now_ we are done.

We have a button that, all by itself, is able to issue a properly formatted HTTP `DELETE` request to the correct URL, and the UI and location bar are all updated correctly. This was accomplished with three declarative attributes placed directly on the button: `hx-delete`, `hx-target` and `hx-push-url`.

This required more work than the `hx-boost` change, but the explicit code makes it easy to see what the button is doing as a custom hypermedia control. The resulting solution feels clean; it takes advantage of the built-in features of the web as a hypermedia system without any URL hacks.

## One More Thing…​

There is one additional “bonus” feature we can add to our “Delete Contact” button: a confirmation dialog. Deleting a contact is a destructive operation and as it stands right now, if the user inadvertently clicked the “Delete Contact” button, the application would just delete that contact. Too bad, so sad for the user.

Fortunately htmx has an easy mechanism for adding a confirmation message on destructive operations like this: the `hx-confirm` attribute. You can place this attribute on an element, with a message as its value, and the JavaScript method `confirm()` will be called before a request is issued, which will show a simple confirmation dialog to the user asking them to confirm the action. Very easy and a great way to prevent accidents.

Here is how we would add confirmation of the contact delete operation:

    <button hx-delete="/contacts/{{ contact.id }}"
      hx-target="body"
      hx-push-url="true"
      hx-confirm="Are you sure you want to delete this contact?"> <1>
      Delete Contact
    button>

Confirming deletion

1.  This message will be shown to the user, asking them to confirm the delete.
    

Now, when someone clicks on the “Delete Contact” button, they will be presented with a prompt that asks “Are you sure you want to delete this contact?” and they will have an opportunity to cancel if they clicked the button in error. Very nice.

With this final change we now have a pretty solid “delete contact” mechanism: we are using the correct RESTful routes and HTTP Methods, we are confirming the deletion, and we have removed a lot of the cruft that normal HTML imposes on us, all while using declarative attributes in our HTML and staying firmly within the normal hypermedia model of the web.

## Progressive Enhancement?

As we noted earlier about this solution: it is _not_ a progressive enhancement to our web application. If someone has disabled JavaScript then this “Delete Contact” button will no longer work. We would need to do additional work to keep the older form-based mechanism working in a JavaScript-disabled environment.

Progressive Enhancement can be a hot-button topic in web development, with lots of passionate opinions and perspectives. Like nearly all JavaScript libraries, htmx makes it possible to create applications that do not function in the absence of JavaScript. Retaining support for non-JavaScript clients requires additional work and complexity in your application. It is important to determine exactly how important supporting non-JavaScript clients is before you begin using htmx, or any other JavaScript framework, for improving your web applications.