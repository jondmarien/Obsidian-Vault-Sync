# Next Steps: Validating Contact Emails

Let’s move on to another improvement in our application. A big part of any web app is validating the data that is submitted to the server: ensuring emails are correctly formatted and unique, numeric values are valid, dates are acceptable, and so forth.

Currently, our application has a small amount of validation that is done entirely server-side and that displays an error message when an error is detected.

We are not going to go into the details of how validation works in the model objects, but recall what the code for updating a contact looks like from Chapter 3:

    def contacts_edit_post(contact_id=0):
        c = Contact.find(contact_id)
        c.update(
          request.form['first_name'],
          request.form['last_name'],
          request.form['phone'],
          request.form['email']) <1>
        if c.save():
            flash("Updated Contact!")
            return redirect("/contacts/" + str(contact_id))
        else:
            return render_template("edit.html", contact=c) <2>

Server-side validation on contact update

1.  We attempt to save the contact.
    
2.  If the save does not succeed we re-render the form to display error messages.

So we attempt to save the contact, and, if the `save()` method returns true, we redirect to the contact’s detail page. If the `save()` method does not return true, that indicates that there was a validation error; instead of redirecting, we re-render the HTML for editing the contact. This gives the user a chance to correct the errors, which are displayed alongside the inputs.

Let’s take a look at the HTML for the email input:

    <p>
      <label for="email">Emaillabel>
      <input name="email" id="email" type="text"
        placeholder="Email" value="{{ contact.email }}">
      <span class="error">{{ contact.errors['email'] }}span> <1>
    p>

Validation error messages

1.  Display any errors associated with the email field

We have a label for the input, an input of type `text` and then a bit of HTML to display any error messages associated with the email. When the template is rendered on the server, if there are errors associated with the contact’s email, they will be displayed in this span, which will be highlighted red.

**Server-Side Validation Logic**

Right now there is a bit of logic in the contact class that checks if there are any other contacts with the same email address, and adds an error to the contact model if so, since we do not want to have duplicate emails in the database. This is a very common validation example: emails are usually unique and adding two contacts with the same email is almost certainly a user error.

Again, we are not going into the details of how validation works in our models, but almost all server-side frameworks provide ways to validate data and collect errors to display to the user. This sort of infrastructure is very common in Web 1.0 server-side frameworks.

The error message shown when a user attempts to save a contact with a duplicate email is “Email Must Be Unique”:

![](file2.png)

Email validation error

All of this is done using plain HTML and using Web 1.0 techniques, and it works well.

However, as the application currently stands, there are two annoyances.

*   First, there is no email format validation: you can enter whatever characters you’d like as an email and, as long as they are unique, the system will allow it.
    
*   Second, we only check the email’s uniqueness when all the data is submitted: if a user has entered a duplicate email, they will not find out until they have filled in all the fields. This could be quite annoying if the user was accidentally reentering a contact and had to put all the contact information in before being made aware of this fact.

## Updating Our Input Type

For the first issue, we have a pure HTML mechanism for improving our application: HTML 5 supports inputs of type `email`. All we need to do is switch our input from type `text` to type `email`, and the browser will enforce that the value entered properly matches the email format:

    <p>
      <label for="email">Emaillabel>
      <input name="email" id="email" type="email" <1>
        placeholder="Email" value="{{ contact.email }}">
      <span class="error">{{ contact.errors['email'] }}span>
    p>

Changing the input to type `email`

1.  A change of the `type` attribute to `email` ensures that values entered are valid emails.

With this change, when the user enters a value that isn’t a valid email, the browser will display an error message asking for a properly formed email in that field.

So a simple single-attribute change done in pure HTML improves our validation and addresses the first problem we noted.

**Server-Side vs. Client-Side Validations**

Experienced web developers might be grinding their teeth at the code above: this validation is done on _the client-side_. That is, we are relying on the browser to detect the malformed email and correct the user. Unfortunately, the client-side is not trustworthy: a browser may have a bug in it that allows the user to circumvent this validation code. Or, worse, the user may be malicious and figure out a mechanism around our validation entirely, such as using the developer console to edit the HTML.

This is a perpetual danger in web development: all validations done on the client-side cannot be trusted and, if the validation is important, _must be redone_ on the server-side. This is less of a problem in Hypermedia-Driven Applications than in Single Page Applications, because the focus of HDAs is the server-side, but it is worth bearing in mind as you build your application.

## Inline Validation

While we have improved our validation experience a bit, the user must still submit the form to get any feedback on duplicate emails. We can next use htmx to improve this user experience.

It would be better if the user were able to see a duplicate email error immediately after entering the email value. It turns out that inputs fire a `change` event and, in fact, the `change` event is the _default trigger_ for inputs in htmx. So, putting this feature to work, we can implement the following behavior: when the user enters an email, immediately issue a request to the server and validate that email, and render an error message if necessary.

Recall the current HTML for our email input:

    <p>
      <label for="email">Emaillabel>
      <input name="email" id="email" type="email"
        placeholder="Email" value="{{ contact.email }}"> <1>
      <span class="error">{{ contact.errors['email'] }}span> <2>
    p>

The initial email configuration

1.  This is the input that we want to have drive an HTTP request to validate the email.
    
2.  This is the span we want to put the error message, if any, into.

So we want to add an `hx-get` attribute to this input. This will cause the input to issue an HTTP `GET` request to a given URL to validate the email. We then want to target the error span following the input with any error message returned from the server.

Let’s make those changes to our HTML:

    <p>
      <label for="email">Emaillabel>
      <input name="email" id="email" type="email"
        hx-get="/contacts/{{ contact.id }}/email" <1>
        hx-target="next .error" <2>
        placeholder="Email" value="{{ contact.email }}">
      <span class="error">{{ contact.errors['email'] }}span>
    p>

Our updated HTML

1.  Issue an HTTP `GET` to the `email` endpoint for the contact.
    
2.  Target the next element with the class `error` on it.

Note that in the `hx-target` attribute we are using a _relative positional_ selector, `next`. This is a feature of htmx and an extension to normal CSS. Htmx supports prefixes that will find targets _relative_ to the current element.

**Relative Positional Expressions in Htmx**

`next`

Scan forward in the DOM for the next matching element, e.g., `next .error`

`previous`

Scan backwards in the DOM for the closest previous matching element, e.g., `previous .alert`

`closest`

Scan the parents of this element for matching element, e.g., `closest table`

`find`

Scan the children of this element for matching element, e.g., `find span`

`this`

the current element is the target (default)

By using relative positional expressions we can avoid adding explicit ids to elements and take advantage of the local structure of HTML.

So, in our example with added `hx-get` and `hx-target` attributes, whenever someone changes the value of the input (remember, `change` is the _default_ trigger for inputs in htmx) an HTTP `GET` request will be issued to the given URL. If there are any errors, they will be loaded into the error span.

## Validating Emails Server-Side

Next, let’s look at the server-side implementation. We are going to add another endpoint, similar to our edit endpoint in some ways: it is going to look up the contact based on the ID encoded in the URL. In this case, however, we only want to update the email of the contact, and we obviously don’t want to save it! Instead, we will call the `validate()` method on it.

That method will validate the email is unique and so forth. At that point we can return any errors associated with the email directly, or the empty string if none exist.

    @app.route("/contacts//email", methods=["GET"])
    def contacts_email_get(contact_id=0):
        c = Contact.find(contact_id) <1>
        c.email = request.args.get('email') <2>
        c.validate() <3>
        return c.errors.get('email') or "" <4>

Code for our email validation endpoint

1.  Look up the contact by id.
    
2.  Update its email (note that since this is a `GET`, we use the `args` property rather than the `form` property).
    
3.  Validate the contact.
    
4.  Return a string, either the errors associated with the email field or, if there are none, the empty string.

With this small bit of server-side code in place, we now have the following user experience: when a user enters an email and tabs to the next input field, they are immediately notified if the email is already taken.

Note that the email validation is _still_ done when the entire contact is submitted for an update, so there is no danger of allowing duplicate email contacts to slip through: we have simply made it possible for users to catch this situation earlier by use of htmx.

It is also worth noting that this particular email validation _must_ be done on the server side: you cannot determine that an email is unique across all contacts unless you have access to the data store of record. This is another simplifying aspect of Hypermedia-Driven Applications: since validations are done server-side, you have access to all the data you might need to do any sort of validation you’d like.

Here again we want to stress that this interaction is done entirely within the hypermedia model: we are using declarative attributes and exchanging hypermedia with the server in a manner very similar to how links or forms work. But we have managed to improve our user experience dramatically.

## Taking The User Experience Further

Despite the fact that we haven’t added a lot of code here, we have a fairly sophisticated user interface, at least when compared with plain HTML-based applications. However, if you have used more advanced Single Page Applications you have probably seen the pattern where an email field (or a similar sort of input) is validated _as you type_.

This seems like the sort of interactivity that is only possible with a sophisticated, complex JavaScript framework, right?

Well, no.

It turns out that you can implement this functionality in htmx, using pure HTML attributes.

In fact, all we need to do is to change our trigger. Currently, we are using the default trigger for inputs, which is the `change` event. To validate as the user types, we would want to capture the `keyup` event as well:

    <p>
      <label for="email">Emaillabel>
      <input name="email" id="email" type="email"
        hx-get="/contacts/{{ contact.id }}/email"
        hx-target="next .error"
        hx-trigger="change, keyup" <1>
        placeholder="Email" value="{{ contact.email }}">
      <span class="error">{{ contact.errors['email'] }}span>
    p>

Triggering With `keyup` events

1.  An explicit `keyup` trigger has been added along with `change`.

With this tiny change, every time a user types a character we will issue a request and validate the email. Simple.

## Debouncing Our Validation Requests

Simple, yes, but probably not what we want: issuing a new request on every key up event would be very wasteful and could potentially overwhelm your server. What we want instead is only issue the request if the user has paused for a small amount of time. This is called “debouncing” the input, where requests are delayed until things have “settled down”.

Htmx supports a `delay` modifier for triggers that allows you to debounce a request by adding a delay before the request is sent. If another event of the same kind appears within that interval, htmx will not issue the request and will reset the timer.

This turns out to be exactly what we want for our email input: if the user is busy typing in an email we won’t interrupt them, but as soon as they pause or leave the field, we’ll issue a request.

Let’s add a delay of 200 milliseconds to the `keyup` trigger, which is long enough to detect that the user has stopped typing.:

    <p>
      <label for="email">Emaillabel>
      <input name="email" id="email" type="email"
        hx-get="/contacts/{{ contact.id }}/email"
        hx-target="next .error"
        hx-trigger="change, keyup delay:200ms" <1>
        placeholder="Email" value="{{ contact.email }}">
      <span class="error">{{ contact.errors['email'] }}span>
    p>

Debouncing the `keyup` event

1.  We debounce the `keyup` event by adding a `delay` modifier.

Now we no longer issue a stream of validation requests as the user types. Instead, we wait until the user pauses for a bit and then issue the request. Much better for our server, and still a great user experience.

## Ignoring Non-Mutating Keys

There is one last issue we should address with the keyup event: as it stands we will issue a request no matter _which_ keys are pressed, even if they are keys that have no effect on the value of the input, such as arrow keys. It would be better if there were a way to only issue a request if the input value has changed.

And it turns out that htmx has support for that exact pattern, by using the `changed` modifier for events. (Not to be confused with the `change` event triggered by the DOM on input elements.)

By adding `changed` to our `keyup` trigger, the input will not issue validation requests unless the keyup event actually updates the inputs value:

    <p>
      <label for="email">Emaillabel>
      <input name="email" id="email" type="email"
        hx-get="/contacts/{{ contact.id }}/email"
        hx-target="next .error"
        hx-trigger="change, keyup delay:200ms changed" <1>
        placeholder="Email" value="{{ contact.email }}">
      <span class="error">{{ contact.errors['email'] }}span>
    p>

Only sending requests when the input value changes

1.  We do away with pointless requests by only issuing them when the input’s value has actually changed.

That’s some pretty good-looking and powerful HTML, providing an experience that most developers would think requires a complicated client-side solution.

With a total of three attributes and a simple new server-side endpoint, we have added a fairly sophisticated user experience to our web application. Even better, any email validation rules we add on the server side will _automatically_ just work using this model: because we are using hypermedia as our communication mechanism there is no need to keep a client-side and server-side model in sync with one another.

A great demonstration of the power of the hypermedia architecture!