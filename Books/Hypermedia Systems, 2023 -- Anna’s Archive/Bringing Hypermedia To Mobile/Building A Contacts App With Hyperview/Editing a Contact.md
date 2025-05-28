# Editing a Contact

So far, our app lets us browse a list of contacts, and view details of a specific contact. Wouldn’t it be nice to update the name, phone number, or email of a contact? Let’s add UI to edit contacts as our next enhancement.

First we have to figure out how we want to display the editing UI. We could push a new editing screen onto the stack, the same way we pushed the contact details screen. But that’s not the best design from a user-experience perspective. Pushing new screens makes sense when drilling down into data, like going from a list to a single item. But editing is not a “drill-down” interaction, it’s a mode switch between viewing and editing. So instead of pushing a new screen, let’s replace the current screen with the editing UI. That means we need to add a button and behavior that use the `reload` action. This button can be added to the header of the contact details screen.

    {% block header %}
      <text style="header-button">
        <behavior trigger="press" action="back" />
        Back
      text>
    
      <text style="header-button"> <1>
        <behavior trigger="press" action="reload"
          href="/contacts/{{contact.id}}/edit" /> <2>
        Edit
      text>
    {% endblock %}

Snippet of `hv/show.xml`

1.  The new “Edit” button.
    
2.  Behavior to reload the current screen with the edit screen when pressed.

Once again, we’re reusing an existing Flask route (`/contacts//edit`) for the edit UI, and filling in the contact ID using data passed to the Jinja template. We also need to update the `contacts_edit_get()` view to return an XML response based on an HXML template (`hv/edit.xml`). We’ll skip the code sample because the needed changes are identical to what we applied to `contacts_view()` in the previous section. Instead, let’s focus on the template for the edit screen.

    {% extends 'hv/layout.xml' %}
    
    {% block header %}
      <text style="header-button">
        <behavior trigger="press" action="back" href="#" />
        Back
      text>
    {% endblock %}
    
    {% block content %}
    <form> <1>
      <view id="form-fields"> <2>
        {% include 'hv/form_fields.xml' %} <3>
      view>
    
      <view style="button"> <4>
        <behavior
          trigger="press"
          action="replace-inner"
          target="form-fields"
          href="/contacts/{{contact.id}}/edit"
          verb="post"
        />
        <text style="button-label">Savetext>
      view>
    form>
    {% endblock %}

`hv/edit.xml`

1.  Form wrapping the input fields and buttons.
    
2.  Container with ID, containing the input fields.
    
3.  Template include to render the input fields.
    
4.  Button to submit the form data and update the input fields container.

Since the edit screen needs to send data to the backend, we wrap the entire content section in a

element. This ensures the form field data will be included in the HTTP requests to our backend. Within the element, our UI is divided into two sections: the form fields, and the Save button. The actual form fields are defined in a separate template (`form_fields.xml`) and added to the edit screen using a Jinja include tag.

    <view style="edit-group">
      <view style="edit-field">
        <text-field name="first_name" placeholder="First name"
          value="{{ contact.first }}" /> <1>
        <text style="edit-field-error">{{ contact.errors.first }}text> <2>
      view>
    
      <view style="edit-field"> <3>
        <text-field name="last_name" placeholder="Last name"
          value="{{ contact.last }}" />
        <text style="edit-field-error">{{ contact.errors.last }}text>
      view>
    
      
    view>

`hv/form_fields.xml`

1.  Text input holding the current value for the contact’s first name.
    
2.  Text element that could display errors from the contact model.
    
3.  Another text field, this time for the contact’s last name.

We omitted the code for the contact’s phone number and email address, because they follow the same pattern as the first and last name. Each contact field has its own , and a element below it to display possible errors. The has two important attributes:

*   `name` defines the name to use when serializing the text-field’s value into form data for HTTP requests. We are using the same names as the web app from previous chapters (`first_name`, `last_name`, `phone`, `email`). That way, we don’t need to make changes in our backend to parse the form data.
    
*   `value` defines the pre-filled data in the text field. Since we are editing an existing contact, it makes sense to pre-fill the text field with the current name, phone, or email.

You might be wondering, why did we choose to define the form fields in a separate template (`form_fields.xml`)? To understand that decision, we need to first discuss the “Save” button. When pressed, the Hyperview client will make an HTTP `POST` request to `contacts//edit`, with form data serialized from the inputs. The HXML response will replace the contents of form field container (ID `form-fields`). But what should that response be? That depends on the validity of the form data:

1.  If the data is invalid (e.g., duplicate email address), our UI will remain in the editing mode and show error messages on the invalid fields. This allows the user to correct the errors and try saving again.
    
2.  If the data is valid, our backend will persist the edits, and our UI will switch back to a display mode (the contact details UI).

So our backend needs to distinguish between a valid and invalid edit. To support these two scenarios, let’s make some changes to the existing `contacts_edit_post()` view in the Flask app.

    @app.route("/contacts//edit", methods=["POST"])
    def contacts_edit_post(contact_id=0):
        c = Contact.find(contact_id)
        c.update(
          request.form['first_name'],
          request.form['last_name'], 
          request.form['phone'], 
          request.form['email']) <1>
        if c.save(): <2>
            flash("Updated Contact!")
            return render_to_response("hv/form_fields.xml",
              contact=c, saved=True) <3>
        else:
            return render_to_response("hv/form_fields.xml", contact=c) <4>

`app.py`

1.  Update the contact object from the request’s form data.
    
2.  Attempt to persist the updates. This returns `False` for invalid data.
    
3.  On success, render the form fields template, and pass a `saved` flag to the template
    
4.  On failure, render the form fields template. Error messages are present on the contact object.

This view already contains conditional logic based on whether the contact model `save()` succeeds. If `save()` fails, we render the `form_fields.xml` template. `contact.errors` will contain error messages for the invalid fields, which will be rendered into the elements. If `save()` succeeds, we will also render the `form_fields.xml` template. But this time, the template will get a `saved` flag, indicating success. We will update the template to use this flag to implement our desired UI: switching the UI back to display mode.

    <view style="edit-group">
      {% if saved %} <1>
        <behavior
          trigger="load" <2>
          action="reload" <3>
          href="/contacts/{{contact.id}}" <4>
        />
      {% endif %}
    
      <view style="edit-field">
        <text-field name="first_name" placeholder="First name"
          value="{{ contact.first }}" />
        <text style="edit-field-error">{{ contact.errors.first }}text>
      view>
    
      
    view>

`hv/form_fields.xml`

1.  Only include this behavior after successfully saving a contact.
    
2.  Trigger the behavior immediately.
    
3.  The behavior will reload the entire screen.
    
4.  The screen will be reloaded with the contact details screen.

The Jinja template conditional ensures that our behavior only renders on successful saves, and not when the screen first opens (or the user submits invalid data). On success, the template includes a behavior that triggers immediately thanks to `trigger="load"`. The action reloads the current screen with the Contact Details screen (from the `/contacts/` route).

The result? When the user hits “Save”, our backend persists the new contact data, and the screen switches back to the Details screen. Since the app will make a new HTTP request to get the contact details, it’s guaranteed to show the freshly saved edits.

**Why Not Redirect?**

You may remember the web app version of this code behaved a little differently. On a successful save, the view returned `redirect("/contacts/" + str(contact_id))`. This HTTP redirect would tell the web browser to navigate to the contact details page.

This approach is not supported in Hyperview. Why? A web app’s navigation stack is simple: a linear sequence of pages, with only one active page at a time. Navigation in a mobile app is considerably more complex. Mobile apps use a nested hierarchy of navigation stacks, modals, and tabs. All screens in this hierarchy are active, and may be displayed instantly in response to user actions. In this world, how would the Hyperview client interpret an HTTP redirect? Should it reload the current screen, push a new one, or navigate to a screen in the stack with the same URL?

Instead of making a choice that would be suboptimal for many scenarios, Hyperview takes a different approach. Server-controlled redirects are not possible, but the backend can render navigation behaviors into the HXML. This is what we do to switch from the Edit UI to the Details UI in the code above. Think of these as client-side redirects, or better yet client-side navigations.

We now have a working Edit UI in our contacts app. Users can enter the Edit mode by pressing a button on the contact details screen. In the Edit mode, they can update the contact’s data and save it to the backend. If the backend rejects the edits as invalid, the app stays in Edit mode and shows the validation errors. If the backend accepts and persists the edits, the app will switch back to the details mode, showing the updated contact data.

Let’s add one more enhancement to the Edit UI. It would be nice to let the user switch away from the Edit mode without needing to save the contact. This is typically done by providing a “Cancel” action. We can add this as a new button below the “Save” button.

    <view style="button">
      <behavior trigger="press" action="replace-inner"target="form-fields"
        href="/contacts/{{contact.id}}/edit" verb="post" />
      <text style="button-label">Savetext>
    view>
    <view style="button"> <1>
      <behavior
        trigger="press"
        action="reload" <2>
        href="/contacts/{{contact.id}}" <3>
      />
      <text style="button-label">Canceltext>
    view>

Snippet of `hv/edit.xml`

1.  A new Cancel button on the edit screen.
    
2.  When pressed, reload the entire screen.
    
3.  The screen will be reloaded with the contact details screen.

This is the same technique we used to switch from the edit UI to the details UI upon successfully editing the contact. But pressing “Cancel” will update the UI faster than pressing “Save.” On save, the app will first make a `POST` request to save the data, and then a `GET` request for the details screen. Cancelling skips the `POST`, and immediately makes the `GET` request.

![](file13.png)

Contact Edit Screen

## Updating the Contacts List

At this point, we can claim to have fully implemented the Edit UI. But there’s a problem. In fact, if we stopped here, users may even consider the app to be buggy! Why? It has to do with syncing the app state across multiple screens. Let’s walk through this series of interactions:

1.  Launch the app to the Contacts List.
    
2.  Press on the contact “Joe Blow” to load his Contact Details.
    
3.  Press Edit to switch to the edit mode, and change the contact’s first name to “Joseph.”
    
4.  Press Save to switch back to viewing mode. The contact’s name is now “Joseph Blow.”
    
5.  Hit the back button to return to the Contacts List.

Did you catch the issue? Our Contacts list is still showing the same list of names as when we launched the app. The contact we just renamed to “Joseph” is still showing up in the list as “Joe.” This is a general problem in hypermedia applications. The client does not have a notion of shared data across different parts of the UI. Updates in one part of the app will not automatically update other parts of the app.

Luckily, there’s a solution to this problem in Hyperview: events. Events are built into the behavior system, and allow lightweight communication between different parts of the UI.

**Event Behaviors**

Events are a client-side feature of Hyperview. In [[/client-side-scripting/#_hyperscript|Client-Side Scripting]], we discussed events while working with HTML, \_hyperscript and the DOM. DOM Elements will dispatch events as a result of user interactions. Scripts can listen for these events, and respond to them by running arbitrary JavaScript code.

Events in Hyperview are a good deal simpler, but they don’t require any scripting and can be defined declaratively in the HXML. This is done through the behavior system. Events require adding a new behavior attribute, action type, and trigger type:

*   `event-name`: This attribute of defines the name of the event that will either be dispatched or listened for.
    
*   `action="dispatch-event"`: When triggered, this behavior will dispatch an event with the name defined by the `event-name` attribute. This event is dispatched globally across the entire Hyperview app.
    
*   `trigger="on-event"`: This behavior will trigger if another behavior in the app dispatches an event matching the `event-name` attribute.

If a element uses `action="dispatch-event"` or `trigger="on-event"`, it must also define an `event-name`. Note that multiple behaviors can dispatch an event with the same name. Likewise, multiple behaviors can trigger on the same event name.

Let’s look at this simple behavior:

.

Pressing an element containing this behavior will toggle the visibility of an element with the ID “container”. But what if the element we want to toggle is on a different screen? The “toggle” action and target ID lookup only work on the current screen, so this solution wouldn’t work. The solution is to create two behaviors, one on each screen, communicating via events:

*   Screen A:
    
*   Screen B:

Pressing an element containing the first behavior (on Screen A) will dispatch an event with the name “button-pressed”. The second behavior (on Screen B) will trigger on an event with this name, and toggle the visibility of an element with ID “container”.

Events have plenty of uses, but the most common is to inform different screens about backend state changes that require the UI to be re-fetched.

We now know enough about Hyperview’s event system to solve the bug in our app. When the user saves a change to a contact, we need to dispatch an event from the Details screen. And the Contacts screen needs to listen to that event, and reload itself to reflect the edits. Since the `form_fields.xml` template already gets the `saved` flag when the backend successfully saves a contact, it’s a good place to dispatch the event:

    {% if saved %}
      <behavior
        trigger="load" <1>
        action="dispatch-event" <2>
        event-name="contact-updated" <2>
      />
      <behavior <4>
        trigger="load"
        action="reload"
        href="/contacts/{{contact.id}}"
      />
    {% endif %}

Snippet from `hv/form_fields.xml`

1.  Trigger the behavior immediately.
    
2.  The behavior will dispatch an event.
    
3.  The event name is “contact-updated”.
    
4.  The existing behavior to show the Details UI.

Now, we just need the contacts list to listen for the `contact-updated` event, and reload itself:

    <form>
      <behavior
        trigger="on-event" <1>
        event-name="contact-updated" <2>
        action="replace-inner" <3>
        target="contacts-list"
        href="/contacts?rows_only=true"
        verb="get"
      />
      
      <list id="contacts-list">
        {% include 'hv/rows.xml' %}
      list>
    form>

Snippet from `hv/index.xml`

1.  Trigger the behavior on event dispatch.
    
2.  Trigger the behavior for dispatched events with the name “contact-updated”.
    
3.  When triggered, replace the contents of the element with rows from the backend.

Any time the user edits a contact, the Contacts List screen will update to reflect the edits. The addition of these two elements fixes the bug: the Contacts List screen will correctly show “Joseph Blow” in the list. Note that we intentionally added the new behavior inside the element. The ensures the triggered request will preserve any search query.

To show what we mean, let’s revisit the set of steps that demonstrated the buggy behavior. Assume that before pressing on “Joe Blow,” the user had searched the contacts by typing “Joe” in the search field. When the user later updates the contact to “Joseph Blow”, our template dispatches the “contact-updated” event, which triggers the `replace-inner` behavior on the contact list screen. Due to the element, the search query “Joe” will be serialized with the request: `GET /contacts?rows_only=true&q=Joe`. Since the name “Joseph” doesn’t match the query “Joe”, the contact we edited will not appear in the list (until the user clears out the query). Our app’s state remains consistent across our backend and all active screens.

Events introduce a level of abstraction to behaviors. So far, we’ve seen that editing a contact will cause the list of contacts to refresh. But the list of contacts should also refresh after other actions, such as deleting a contact or adding a new contact. As long as our HXML responses for deletion or creation include a behavior to dispatch a `contact-updated` event, then we will get the desired refresh behavior on the contacts list screen.

The screen doesn’t care what causes the `contact-updated` event to be dispatched. It just knows what it needs to do when it happens.

# Deleting a Contact

Speaking of deleting a contact, this is a good next feature to implement. We will let users delete a contact from the Edit UI. So let’s add a new button to `edit.xml`.

    <view style="button">
      <behavior trigger="press" action="replace-inner" target="form-fields"
        href="/contacts/{{contact.id}}/edit" verb="post" />
      <text style="button-label">Savetext>
    view>
    <view style="button">
      <behavior trigger="press" action="reload"
        href="/contacts/{{contact.id}}" />
      <text style="button-label">Canceltext>
    view>
    <view style="button"> <1>
      <behavior
        trigger="press"
        action="append" <2>
        target="form-fields"
        href="/contacts/{{contact.id}}/delete" <3>
        verb="post"
      />
      <text style="button-label button-label-delete">Delete Contacttext>
    view>

Snippet of `hv/edit.xml`

1.  New Delete Contact button on the edit screen.
    
2.  When pressed, append HXML to a container on the screen.
    
3.  The HXML will be fetched by making a `POST /contacts//delete` request.

The HXML for the Delete button is pretty similar to the Save button, but there are a few subtle differences. Remember, pressing the Save button results in one of two expected outcomes: failing and showing validation errors on the form, or succeeding and switching to the contact details screen. To support the first outcome (failing and showing validation errors), the save behavior replaces the contents of the container with a re-rendered version of `form_fields.xml`. Therefore, using the `replace-inner` action makes sense.

Deletion does not involve a validation step, so there’s only one expected outcome: successfully deleting the contact. When deletion succeeds, the contact no longer exists. It doesn’t make sense to show the edit UI or contact details for a non-existent contact. Instead, our app will navigate back to the previous screen (the contacts list). Our response will only include behaviors that trigger immediately, there’s no UI to change. Therefore, using the `append` action will preserve the current UI while Hyperview runs the actions.

    <view>
      <behavior trigger="load" action="dispatch-event"
        event-name="contact-updated" /> <1>
      <behavior trigger="load" action="back" /> <2>
    view>

Snippet of `hv/deleted.xml`

1.  On load, dispatch the `contact-updated` event to update the contact lists screen.
    
2.  Navigate back to the contacts list screen.

Note that in addition to behavior to navigate back, this template also includes a behavior to dispatch the `contact-updated` event. In the previous chapter section, we added a behavior to `index.xml` to refresh the list when that event is dispatched. By dispatching the event after a deletion, we will make sure the deleted contact gets removed from the list.

Once again, we’ll skip over the changes to the Flask backend. Suffice it to say, we will need to update the `contacts_delete()` view to respond with the `hv/deleted.xml` template. And we need to update the route to support `POST` in addition to `DELETE`, since the Hyperview client only understands `GET` and `POST`.

We now have a fully functioning deletion feature! But it’s not the most user-friendly: it takes one accidental tap to permanently delete a contact. For destructive actions like deleting a contact, it’s always a good idea to ask the user for confirmation.

We can add a confirmation to the delete behavior by using the `alert` system action described in the previous chapter. As you recall, the `alert` action will show a system dialog box with buttons that can trigger other behaviors. All we have to do is wrap the delete in a behavior that uses `action="alert"`.

    <view style="button">
      <behavior <1>
        xmlns:alert="https://hyperview.org/hyperview-alert"
        trigger="press"
        action="alert"
        alert:title="Confirm delete"
        alert:message="Are you sure you want to delete {{ contact.first }}?"
      >
        <alert:option alert:label="Confirm"> <2>
          <behavior <3>
            trigger="press"
            action="append"
            target="form-fields"
            href="/contacts/{{contact.id}}/delete"
            verb="post"
          />
        alert:option>
        <alert:option alert:label="Cancel" /> <4>
      behavior>
      <text style="button-label button-label-delete">Delete Contacttext>
    view>

Delete button in `hv/edit.xml`

1.  Pressing “Delete” triggers an action to show the system dialog with the given title and message.
    
2.  The first pressable option in the system dialog.
    
3.  Pressing the first option will trigger contact deletion.
    
4.  The second pressable option has no behavior, so it only closes the dialog.

Unlike before, pressing the delete button will not have an immediate effect. Instead, the user will be presented with the dialog box and asked to confirm or cancel. Our core deletion behavior didn’t change, we just chained it from another behavior.

![](file14.png)

Delete Contact confirmation

# Adding a New Contact

Adding a new contact is the last feature we want to support in our mobile app. And luckily, it’s also the easiest. We can reuse the concepts (and even some templates) from features we’ve already implemented. In particular, adding a new contact is very similar to editing an existing contact. Both features need to:

*   Show a form to collect information about the contact.
    
*   Have a way to save the entered information.
    
*   Show validation errors on the form.
    
*   Persist the contact when there are no validation errors.

Since the functionality is so similar, we’ll summarize the changes here without showing the code.

1.  Update `index.xml`.
    
    *   Override the `header` block to add a new “Add” button.
        
    *   Include a behavior in the button. When pressed, push a new screen as a modal by using `action="new"`, and request the screen content from `/contacts/new`.
        
2.  Create a template `hv/new.xml`.
    
    *   Override the header block to include a button that closes the modal, using `action="close"`.
        
    *   Include the `hv/form_fields.xml` template to render empty form fields
        
    *   Add a “Add Contact” button below the form fields.
        
    *   Include a behavior in the button. When pressed, make a `POST` request to `/contacts/new`, and use `action="replace-inner"` to update the form fields.
        
3.  Update the Flask view.
    
    *   Change `contacts_new_get()` to use `render_to_response()` with the `hv/new.xml` template.
        
    *   Change `contacts_new()` to use `render_to_response()` with the `hv/form_fields.xml` template. Pass `saved=True` when rendering the template after successfully persisting the new contact.

By reusing `form_fields.xml` for both editing and adding a contact, we get to reuse some code and ensure the two features have a consistent UI. Also, our “Add Contact” screen will benefit from the “saved” logic that’s already a part of `form_fields.xml`. After successfully adding a new contact, the screen will dispatch the `contact-updated` event, which will refresh the contacts list and show the newly added contact. The screen will reload itself to show the Contact Details.

![](file15.png)

Add Contact modal