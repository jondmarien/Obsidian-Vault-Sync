# Adding A New Contact

The next bit of functionality that we will add to our application is the ability to add new contacts. To do this, we are going to need to handle that `/contacts/new` URL referenced in the “Add Contact” link above. Note that when a user clicks on that link, the browser will issue a `GET` request to the `/contacts/new` URL.

All the other routes we have so far use `GET` as well, but we are actually going to use two different HTTP methods for this bit of functionality: an HTTP `GET` to render a form for adding a new contact, and then an HTTP `POST` _to the same path_ to actually create the contact, so we are going to be explicit about the HTTP method we want to handle when we declare this route.

Here is the code:

    @app.route("/contacts/new", methods=['GET']) <1>
    def contacts_new_get():
        return render_template("new.html", contact=Contact()) <2>

The “new contact” GET route

1.  Declare a route, explicitly handling `GET` requests to this path.
    
2.  Render the `new.html` template, passing in a new contact object.
    

Simple enough. We just render a `new.html` template with a new Contact. (`Contact()` is how you construct a new instance of the `Contact` class in Python, if you aren’t familiar with it.)

While the handler code for this route is very simple, the `new.html` template is more complicated.

For the remaining templates we are going to omit the layout directive and the content block declaration, but you can assume they are the same unless we say otherwise. This will let us focus on the “meat” of the template.

If you are familiar with HTML you are probably expecting a form element here, and you will not be disappointed. We are going to use the standard form hypermedia control for collecting contact information and submitting it to the server.

Here is what our HTML looks like:

    <form action="/contacts/new" method="post"> <1>
      <fieldset>
        <legend>Contact Valueslegend>
        <p>
          <label for="email">Emaillabel> <2>
          <input name="email" id="email" 
            type="email" placeholder="Email"
            value="{{ contact.email or '' }}"> <3>
          <span class="error">
            {{ contact.errors['email'] }} <4>
          span>
        p>

The “new contact” form

1.  A form that submits to the `/contacts/new` path, using an HTTP `POST`.
    
2.  A label for the first form input.
    
3.  The first form input, of type email.
    
4.  Any error messages associated with this field.
    

In the first line of code we create a form that will submit back _to the same path_ that we are handling: `/contacts/new`. Rather than issuing an HTTP `GET` to this path, however, we will issue an HTTP `POST` to it. Using a `POST` in this manner will signal to the server that we want to create a new Contact, rather than get a form for creating one.

We then have a label (always a good practice!) and an input that captures the email of the contact being created. The name of the input is `email` and, when this form is submitted, the value of this input will be submitted in the `POST` request, associated with the `email` key.

Next we have inputs for the other fields for contacts:

    <p>
      <label for="first_name">First Namelabel>
      <input name="first_name" id="first_name" type="text"
        placeholder="First Name" value="{{ contact.first or '' }}">
      <span class="error">{{ contact.errors['first'] }}span>
    p>
    <p>
      <label for="last_name">Last Namelabel>
      <input name="last_name" id="last_name" type="text"
        placeholder="Last Name" value="{{ contact.last or '' }}">
      <span class="error">{{ contact.errors['last'] }}span>
    p>
    <p>
      <label for="phone">Phonelabel>
      <input name="phone" id="phone" type="text" placeholder="Phone"
        value="{{ contact.phone or '' }}">
      <span class="error">{{ contact.errors['phone'] }}span>
    p>

Inputs and labels for the “new contact” form

Finally, we have a button that will submit the form, the end of the form tag, and a link back to the main contacts table:

    <button>Savebutton>
      fieldset>
    form>
    
    <p>
      <a href="/contacts">Backa>
    p>

The submit button for the “new contact” form

It is easy to miss in this straight-forward example: we are seeing the flexibility of hypermedia in action.

If we add a new field, remove a field, or change the logic around how fields are validated or work with one another, this new state of affairs would be reflected in the new hypermedia representation given to users. A user would see the updated new form and be able to work with these new features, with no software update required.

## Handling the post to /contacts/new

The next step in our application is to handle the `POST` that this form makes to `/contacts/new`.

To do so, we need to add another route to our application that handles the `/contacts/new` path. The new route will handle an HTTP `POST` method instead of an HTTP `GET`. We will use the submitted form values to attempt to create a new Contact.

If we are successful in creating a Contact, we will redirect the user to the list of contacts and show a success message. If we aren’t successful, then we will render the new contact form again with whatever values the user entered and render error messages about what issues need to be fixed so that the user can correct them.

Here is our new request handler:

    @app.route("/contacts/new", methods=['POST'])
    def contacts_new():
        c = Contact(
          None,
          request.form['first_name'],
          request.form['last_name'],
          request.form['phone'],
          request.form['email']) <1>
        if c.save(): <2>
            flash("Created New Contact!")
            return redirect("/contacts") <3>
        else:
            return render_template("new.html", contact=c) <4>

The “new contact” controller code

1.  We construct a new contact object with the values from the form.
    
2.  We try to save it.
    
3.  On success, “flash” a success message & redirect to the `/contacts` page.
    
4.  On failure, re-render the form, showing any errors to the user.
    

The logic in this handler is a bit more complex than other methods we have seen. The first thing we do is create a new Contact, again using the `Contact()` syntax in Python to construct the object. We pass in the values that the user submitted in the form by using the `request.form` object, a feature provided by Flask.

This `request.form` allows us to access submitted form values in an easy and convenient way, by simply passing in the same name associated with the various inputs.

We also pass in `None` as the first value to the `Contact` constructor. This is the “id” parameter, and by passing in `None` we are signaling that it is a new contact, and needs to have an ID generated for it. (Again, we are not going into the details of how this model object is implemented, our only concern is using it to generate hypermedia responses.)

Next, we call the `save()` method on the Contact object. This method returns `true` if the save is successful, and `false` if the save is unsuccessful (for example, a bad email was submitted by the user).

If we are able to save the contact (that is, there were no validation errors), we create a _flash_ message indicating success, and redirect the browser back to the list page. A “flash” is a common feature in web frameworks that allows you to store a message that will be available on the _next_ request, typically in a cookie or in a session store.

Finally, if we are unable to save the contact, we re-render the `new.html` template with the contact. This will show the same template as above, but the inputs will be filled in with the submitted values, and any errors associated with the fields will be rendered to feedback to the user as to what validation failed.

**The Post/Redirect/Get Pattern**

This handler implements a common strategy in web 1.0-style development called the [Post/Redirect/Get](https://en.wikipedia.org/wiki/Post/Redirect/Get) or PRG pattern. By issuing an HTTP redirect once a contact has been created and forwarding the browser on to another location, we ensure that the `POST` does not end up in the browsers request cache.

This means that if the user accidentally (or intentionally) refreshes the page, the browser will not submit another `POST`, potentially creating another contact. Instead, it will issue the `GET` that we redirect to, which should be side-effect free.

We will use the PRG pattern in a few different places in this book.

OK, so we have our server-side logic set up to save contacts. And, believe it or not, this is about as complicated as our handler logic will get, even when we look at adding more sophisticated htmx-driven behaviors.

# Viewing The Details Of A Contact

The next piece of functionality we will implement is the detail page for a Contact. The user will navigate to this page by clicking the “View” link in one of the rows in the list of contacts. This will take them to the path `/contact/` (e.g., `/contacts/42`).

This is a common pattern in web development: contacts are treated as resources and the URLs around these resources are organized in a coherent manner.

*   If you wish to view all contacts, you issue a `GET` to `/contacts`.
    
*   If you want a hypermedia representation allowing you to create a new contact, you issue a `GET` to `/contacts/new`.
    
*   If you wish to view a specific contact (with, say, an id of ``42), you issue a `GET`` to `/contacts/42`.
    

**The Eternal Bike Shed of URL Design**

It is easy to quibble about the particulars of the path scheme you use for your application:

“Should we `POST` to `/contacts/new` or to `/contacts`?”

We have seen many arguments online and in person advocating for one approach versus another. We feel it is more important to understand the overarching idea of _resources_ and _hypermedia representations_, rather than getting worked up about the smaller details of your URL design.

We recommend you just pick a reasonable, resource-oriented URL layout you like and then stay consistent. Remember, in a hypermedia system, you can always change your endpoints later, because you are using hypermedia as the engine of application state!

Our handler logic for the detail route is going to be _very_ simple: we just look the Contact up by id, which is embedded in the path of the URL for the route. To extract this ID we are going to need to introduce a final bit of Flask functionality: the ability to call out pieces of a path and have them automatically extracted and passed in to a handler function.

Here is what the code looks like, just a few lines of simple Python:

    @app.route("/contacts/") <1>
    def contacts_view(contact_id=0): <2>
        contact = Contact.find(contact_id) <3>
        return render_template("show.html", contact=contact) <4>

1.  Map the path, with a path variable named `contact_id`.
    
2.  The handler takes the value of this path parameter.
    
3.  Look up the corresponding contact.
    
4.  Render the `show.html` template.
    

You can see the syntax for extracting values from the path in the first line of code: you enclose the part of the path you wish to extract in `<>` and give it a name. This component of the path will be extracted and then passed into the handler function, via the parameter with the same name.

So, if you were to navigate to the path `/contacts/42`, the value `42` would be passed into the `contacts_view()` function for the value of `contact_id`.

Once we have the id of the contact we want to look up, we load it up using the `find` method on the `Contact` object. We then pass this contact into the `show.html` template and render a response.

# The Contact Detail Template

Our `show.html` template is relatively simple, just showing the same information as the table but in a slightly different format (perhaps for printing). If we add functionality like “notes” to the application later on, this will give us a good place to do so.

Again, we will omit the “chrome” of the template and focus on the meat:

    <h1>{{contact.first}} {{contact.last}}h1>
    
    <div>
      <div>Phone: {{contact.phone}}div>
      <div>Email: {{contact.email}}div>
    div>
    
    <p>
      <a href="/contacts/{{contact.id}}/edit">Edita>
      <a href="/contacts">Backa>
    p>

The “contact details” template

We simply render a First Name and Last Name header, with the additional contact information below it, and a couple of links: a link to edit the contact and a link to navigate back to the full list of contacts.

# Editing And Deleting A Contact

Next up we will tackle the functionality on the other end of that “Edit” link. Editing a contact is going to look very similar to creating a new contact. As with adding a new contact, we are going to need two routes that handle the same path, but using different HTTP methods: a `GET` to `/contacts//edit` will return a form allowing you to edit the contact and a `POST` to that path will update it.

We are also going to piggyback the ability to delete a contact along with this editing functionality. To do this we will need to handle a `POST` to `/contacts//delete`.

Let’s look at the code to handle the `GET`, which, again, will return an HTML representation of an editing interface for the given resource:

    @app.route("/contacts//edit", methods=["GET"])
    def contacts_edit_get(contact_id=0):
        contact = Contact.find(contact_id)
        return render_template("edit.html", contact=contact)

The “edit contact” controller code

As you can see this looks a lot like our “Show Contact” functionality. In fact, it is nearly identical except for the template: here we render `edit.html` rather than `show.html`.

While our handler code looked similar to the “Show Contact” functionality, the `edit.html` template is going to look very similar to the template for the “New Contact” functionality: we will have a form that submits updated contact values to the same “edit” URL and that presents all the fields of a contact as inputs for editing, along with any error messages.

Here is the first bit of the form:

    <form action="/contacts/{{ contact.id }}/edit" method="post"> <1>
      <fieldset>
        <legend>Contact Valueslegend>
        <p>
          <label for="email">Emaillabel>
          <input name="email" id="email" type="text"
            placeholder="Email" value="{{ contact.email }}"> <2>
          <span class="error">{{ contact.errors['email'] }}span>
        p>

The “edit contact” form start

1.  Issue a `POST` to the `/contacts/{{ contact.id }}/edit` path.
    
2.  As with the `new.html` page, the input is tied to the contact’s email.
    

This HTML is nearly identical to our `new.html` form, except that this form is going to submit a `POST` to a different path, based on the id of the contact that we want to update. (It’s worth mentioning here that, rather than `POST`, we would prefer to use a `PUT` or `PATCH`, but those are not available in plain HTML.)

Following this we have the remainder of our form, again very similar to the `new.html` template, and our button to submit the form.

    <p>
          <label for="first_name">First Namelabel>
          <input name="first_name" id="first_name" type="text"
            placeholder="First Name" value="{{ contact.first }}">
          <span class="error">{{ contact.errors['first'] }}span>
        p>
        <p>
          <label for="last_name">Last Namelabel>
          <input name="last_name" id="last_name" type="text"
            placeholder="Last Name" value="{{ contact.last }}">
          <span class="error">{{ contact.errors['last'] }}span>
        p>
        <p>
          <label for="phone">Phonelabel>
          <input name="phone" id="phone" type="text"
            placeholder="Phone" value="{{ contact.phone }}">
          <span class="error">{{ contact.errors['phone'] }}span>
        p>
        <button>Savebutton>
      fieldset>
    form>

The “edit contact” form body

In the final part of our template we have a small difference between the `new.html` and `edit.html`. Below the main editing form, we include a second form that allows you to delete a contact. It does this by issuing a `POST` to the `/contacts//delete` path. Just as we would prefer to use a `PUT` to update a contact, we would much rather use an HTTP `DELETE` request to delete one. Unfortunately that also isn’t possible in plain HTML.

To finish up the page, there is a simple hyperlink back to the list of contacts.

    <form action="/contacts/{{ contact.id }}/delete" method="post">
      <button>Delete Contactbutton>
    form>
    
    <p>
      <a href="/contacts/">Backa>
    p>

The “edit contact” form footer

Given all the similarities between the `new.html` and `edit.html` templates, you may be wondering why we are not _refactoring_ these two templates to share logic between them. That’s a good observation and, in a production system, we would probably do just that.

For our purposes, however, since our application is small and simple, we will leave the templates separate.

**Factoring Your Applications**

One thing that often trips people up who are coming to hypermedia applications from a JavaScript background is the notion of “components”. In JavaScript-oriented applications it is common to break your app up into small client-side components that are then composed together. These components are often developed and tested in isolation and provide a nice abstraction for developers to create testable code.

With Hypermedia-Driven Applications, in contrast, you factor your application on the server side. As we said, the above form could be refactored into a shared template between the edit and create templates, allowing you to achieve a reusable and DRY (Don’t Repeat Yourself) implementation.

Note that factoring on the server-side tends to be coarser-grained than on the client-side: you tend to split out common _sections_ rather than create lots of individual components. This has benefits (it tends to be simple) as well as drawbacks (it is not nearly as isolated as client-side components).

Overall, a properly factored server-side hypermedia application can be extremely DRY.

## Handling the post to /contacts//edit

Next we need to handle the HTTP `POST` request that the form in our `edit.html` template submits. We will declare another route that handles the same path as the `GET` above.

Here is the new handler code:

    @app.route("/contacts//edit", methods=["POST"]) <1>
    def contacts_edit_post(contact_id=0):
        c = Contact.find(contact_id) <2>
        c.update(
          request.form['first_name'],
          request.form['last_name'],
          request.form['phone'],
          request.form['email']) <3>
        if c.save(): <4>
            flash("Updated Contact!")
            return redirect("/contacts/" + str(contact_id)) <5>
        else:
            return render_template("edit.html", contact=c) <6>

1.  Handle a `POST` to `/contacts//edit`.
    
2.  Look the contact up by id.
    
3.  Update the contact with the new information from the form.
    
4.  Attempt to save it.
    
5.  On success, flash a success message & redirect to the detail page.
    
6.  On failure, re-render the edit template, showing any errors.
    

The logic in this handler is very similar to the logic in the handler for adding a new contact. The only real difference is that, rather than creating a new Contact, we look the contact up by id and then call the `update()` method on it with the values that were entered in the form.

Once again, this consistency between our CRUD operations is one of the nice and simplifying aspects of traditional CRUD web applications.