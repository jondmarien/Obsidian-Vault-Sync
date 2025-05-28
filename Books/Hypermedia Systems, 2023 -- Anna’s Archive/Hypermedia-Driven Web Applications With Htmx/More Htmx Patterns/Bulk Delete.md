# Bulk Delete

The final feature we are going to implement in this chapter is a “Bulk Delete.” The current mechanism for deleting users is nice, but it would be annoying if a user wanted to delete five or ten contacts at a time, wouldn’t it? For the bulk delete feature, we want to add the ability to select rows via a checkbox input and delete them all in a single go by clicking a “Delete Selected Contacts” button.

To get started with this feature, we’ll need to add a checkbox input to each row in the `rows.html` template. This input will have the name `selected_contact_ids` and its value will be the `id` of the contact for the current row.

Here is what the updated code for `rows.html` looks like:

    {% for contact in contacts %}
    <tr>
      <td><input type="checkbox" name="selected_contact_ids"
        value="{{ contact.id }}">td> <1>
      <td>{{ contact.first }}td>
      ... omitted
    tr>
    {% endfor %}

Adding a checkbox to each row

1.  A new cell with the checkbox input whose value is set to the current contact’s id.

We’ll also need to add an empty column in the header for the table to accommodate the checkbox column. With that done we now get a series of check boxes, one for each row, a pattern no doubt familiar to you from the web:

![](file6.png)

Checkboxes for our contact rows

If you are not familiar with or have forgotten the way checkboxes work in HTML: a checkbox will submit its value associated with the name of the input if and only if it is checked. So if, for example, you checked the contacts with the ids 3, 7 and 9, then those three values would all be submitted to the server. Since all the checkboxes in this case have the same name, `selected_contact_ids`, all three values would be submitted with the name `selected_contact_ids`.

## The “Delete Selected Contacts” Button

The next step is to add a button below the table that will delete all the selected contacts. We want this button, like our delete links in each row, to issue an HTTP `DELETE`, but rather than issuing it to the URL for a given contact, like we do with the inline delete links and with the delete button on the edit page, here we want to issue the `DELETE` to the `/contacts` URL.

As with the other delete elements, we want to confirm that the user wishes to delete the contacts, and, for this case, we are going to target the body of page, since we are going to re-render the whole table.

Here is what the button code looks like:

    <button
      hx-delete="/contacts" <1>
      hx-confirm="Are you sure you want to delete these contacts?" <2>
      hx-target="body"> <3>
      Delete Selected Contacts
    button>

The “delete selected contacts” button

1.  Issue a `DELETE` to `/contacts`.
    
2.  Confirm that the user wants to delete the selected contacts.
    
3.  Target the body.

Pretty easy. One question though: how are we going to include the values of all the selected checkboxes in the request? As it stands right now, this is just a stand-alone button, and it doesn’t have any information indicating that it should include any other information in the `DELETE` request it makes.

Fortunately, htmx has a few different ways to include values of inputs with a request.

One way would be to use the `hx-include` attribute, which allows you to use a CSS selector to specify the elements you want to include in the request. That would work fine here, but we are going to use another approach that is a bit simpler in this case.

By default, if an element is a child of a `form` element and makes a non-`GET` request, htmx will include all the values of inputs within that form. In situations like this, where there is a bulk operation for a table, it is common to enclose the whole table in a form tag, so that it is easy to add buttons that operate on the selected items.

Let’s add that form tag around the table, and be sure to enclose the button in it as well:

    <form> <1>
      <table>
        ... omitted
      table>
      <button
        hx-delete="/contacts"
        hx-confirm="Are you sure you want to delete these contacts?"
        hx-target="body">
        Delete Selected Contacts
      button>
    form> <2>

The “delete selected contacts” button

1.  The form tag encloses the entire table.
    
2.  The form tag also encloses the button.

Now, when the button issues a `DELETE`, it will include all the contact ids that have been selected as the `selected_contact_ids` request variable.

## The Server Side for Delete Selected Contacts

The server-side implementation is going to look like our original server-side code for deleting a contact. In fact, once again, we can just copy and paste, and make a few fixes:

*   We want to change the URL to `/contacts`.
    
*   We want the handler to get _all_ the ids submitted as `selected_contact_ids` and iterate over each one, deleting the given contact.

Those are the only changes we need to make! Here is what the server-side code looks like:

    @app.route("/contacts/", methods=["DELETE"]) <1>
    def contacts_delete_all():
        contact_ids =  [
          int(id)
          for id in request.form.getlist("selected_contact_ids")
        ] <2>
        for contact_id in contact_ids: <3>
            contact = Contact.find(contact_id)
            contact.delete() <4>
        flash("Deleted Contacts!") <5>
        contacts_set = Contact.all()
        return render_template("index.html", contacts=contacts_set)

The “delete selected contacts” button

1.  We handle a `DELETE` request to the `/contacts/` path.
    
2.  Convert the `selected_contact_ids` values submitted to the server from a list of strings to a list integers.
    
3.  Iterate over all of the ids.
    
4.  Delete the given contact with each id.
    
5.  Beyond that, it’s the same code as our original delete handler: flash a message and render the `index.html` template.

So, we took the original delete logic and slightly modified it to deal with an array of ids, rather than a single id.

You might notice one other small change: we did away with the redirect that was in the original delete code. We did so because we are already on the page we want to re-render, so there is no reason to redirect and have the URL update to something new. We can just re-render the page, and the new list of contacts (sans the contacts that were deleted) will be re-rendered.

And there we go, we now have a bulk delete feature for our application. Once again, not a huge amount of code, and we are implementing these features entirely by exchanging hypermedia with a server in the traditional, RESTful manner of the web.

# HTML Notes: Accessible by Default?

Accessibility problems can arise when we try to implement controls that aren’t built into HTML.

Earlier, in Chapter One, we looked at the example of a

improvised to work like a button. Let’s look at a different example: what if you make something that looks like a set of tabs, but you use radio buttons and CSS hacks to build it? It’s a neat hack that makes the rounds in web development communities from time to time.

The problem here is that tabs have requirements beyond clicking to change content. Your improvised tabs may be missing features that will lead to user confusion and frustration, as well as some undesirable behaviors. From the [ARIA Authoring Practices Guide on tabs](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/):

*   Keyboard interaction
    
    *   Can the tabs be focused with the Tab key?
        
*   ARIA roles, states, and properties
    
    *   “\[The element that contains the tabs\] has role `tablist`.”
        
    *   “Each \[tab\] has role `tab` \[…​\]”
        
    *   “Each element that contains the content panel for a `tab` has role `tabpanel`.”
        
    *   “Each \[tab\] has the property `aria-controls` referring to its associated tabpanel element.”
        
    *   “The active `tab` element has the state `aria-selected` set to `true` and all other `tab` elements have it set to `false`.”
        
    *   “Each element with role `tabpanel` has the property `aria-labelledby` referring to its associated `tab` element.”

You would need to write a lot of code to make your improvised tabs fulfill all of these requirements. Some of the ARIA attributes can be added directly in HTML, but they are repetitive and others (like `aria-selected`) need to be set through JavaScript since they are dynamic. The keyboard interactions can be error-prone too.

It’s not impossible, not even that hard, to make your own tab set implementation. However, it’s difficult to trust that a new implementation will work for all users in all environments, since most of us have limited resources for testing.

_Stick with established libraries_ for UI interactions. If a use case requires a bespoke solution, _test exhaustively_ for keyboard interaction and accessibility. Test manually. Test automatically. Test with screen readers, test with a keyboard, test on different browsers and hardware, and run linters (while coding and/or in CI). Testing is critical to ensure machine readability, or human readability, or page weight.

Also consider: Does the information need to be presented as tabs? Sometimes the answer is yes, but if not, a sequence of details and disclosures fulfills a very similar purpose.

    <details><summary>Disclosure 1summary>
      Disclosure 1 contents
    details>
    <details><summary>Disclosure 2summary>
      Disclosure 2 contents
    details>

Compromising UX just to avoid JavaScript is bad development. But sometimes it’s possible to achieve an equal (or better!) quality of UX while allowing for a simpler and more robust implementation by changing the design.