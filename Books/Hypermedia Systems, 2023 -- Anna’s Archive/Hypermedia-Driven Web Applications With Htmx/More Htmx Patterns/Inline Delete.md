# Inline Delete

For our next hypermedia trick, we are going to implement the “Inline Delete” pattern. With this feature, a contact can be deleted directly from the table of all contacts, rather than requiring the user to navigate all the way to the edit view of particular contact, in order to access the “Delete Contact” button we added in the last chapter.

Recall that we already have “Edit” and “View” links for each row, in the `rows.html` template:

    <td>
        <a href="/contacts/{{ contact.id }}/edit">Edita>
        <a href="/contacts/{{ contact.id }}">Viewa>
    td>

The existing row actions

Now we want to add a “Delete” link as well. And, thinking on it, we want that link to act an awful lot like the “Delete Contact” button from `edit.html`, don’t we? We’d like to issue an HTTP `DELETE` to the URL for the given contact and we want a confirmation dialog to ensure the user doesn’t accidentally delete a contact.

Here is the “Delete Contact” button html:

    <button
      hx-delete="/contacts/{{ contact.id }}"
      hx-push-url="true"
      hx-confirm="Are you sure you want to delete this contact?"
      hx-target="body">
      Delete Contact
    button>

The existing row actions

As you may suspect by now, this is going to be another copy-and-paste job.

One thing to note is that, in the case of the “Delete Contact” button, we wanted to re-render the whole screen and update the URL, since we are going to be returning from the edit view for the contact to the list view of all contacts. In the case of this link, however, we are already on the list of contacts, so there is no need to update the URL, and we can omit the `hx-push-url` attribute.

Here is the code for our inline “Delete” link:

    <td>
      <a href="/contacts/{{ contact.id }}/edit">Edita>
      <a href="/contacts/{{ contact.id }}">Viewa>
      <a href="#" hx-delete="/contacts/{{ contact.id }}"
        hx-confirm="Are you sure you want to delete this contact?"
        hx-target="body">Deletea> <1>
    td>

The existing row actions

1.  Almost a straight copy of the “Delete Contact” button.

As you can see, we have added a new anchor tag and given it a blank target (the `#` value in its `href` attribute) to retain the correct mouse-over styling behavior of the link. We’ve also copied the `hx-delete`, `hx-confirm` and `hx-target` attributes from the “Delete Contact” button, but omitted the `hx-push-url` attributes since we don’t want to update the URL of the browser.

We now have inline delete working, even with a confirmation dialog. A user can click on the “Delete” link and the row will disappear from the UI as the entire page is re-rendered.

**A Style Sidebar**

One side effect of adding this delete link is that we are starting to pile up the actions in a contact row:

![](file5.png)

That’s a lot of actions

It would be nice if we didn’t show the actions all in a row, and, additionally, it would be nice if we only showed the actions when the user indicated interest in a given row. We will return to this problem after we look at the relationship between scripting and a Hypermedia-Driven Application in a later chapter.

For now, let’s just tolerate this less-than-ideal user interface, knowing that we will fix it later.

## Narrowing Our Target

We can get even fancier here, however. What if, rather than re-rendering the whole page, we just removed the row for the contact? The user is looking at the row anyway, so is there really a need to re-render the whole page?

To do this, we’ll need to do a couple of things:

*   We’ll need to update this link to target the row that it is in.
    
*   We’ll need to change the swap to `outerHTML`, since we want to replace (really, remove) the entire row.
    
*   We’ll need to update the server side to render empty content when the `DELETE` is issued from a “Delete” link rather than from the “Delete Contact” button on the contact edit page.

First things first, update the target of our “Delete” link to be the row that the link is in, rather than the entire body. We can once again take advantage of the relative positional `closest` feature to target the closest `tr`, like we did in our “Click To Load” and “Infinite Scroll” features:

    <td>
      <a href="/contacts/{{ contact.id }}/edit">Edita>
      <a href="/contacts/{{ contact.id }}">Viewa>
      <a href="#" hx-delete="/contacts/{{ contact.id }}"
        hx-swap="outerHTML"
        hx-confirm="Are you sure you want to delete this contact?"
        hx-target="closest tr">Deletea> <1>
    td>

The existing row actions

1.  Updated to target the closest enclosing `tr` (table row) of the link.

## Updating The Server Side

Now we need to update the server side. We want to keep the “Delete Contact” button working as well, and in that case the current logic is correct. So we’ll need some way to differentiate between `DELETE` requests that are triggered by the button and `DELETE` requests that come from this anchor.

The cleanest way to do this is to add an `id` attribute to the “Delete Contact” button, so that we can inspect the `HX-Trigger` HTTP Request header to determine if the delete button was the cause of the request. This is a simple change to the existing HTML:

    <button id="delete-btn" <1>
      hx-delete="/contacts/{{ contact.id }}"
      hx-push-url="true"
      hx-confirm="Are you sure you want to delete this contact?"
      hx-target="body">
      Delete Contact
    button>

Adding an `id` to the “delete contact” button

1.  An `id` attribute has been added to the button.

By giving this button an id attribute, we now have a mechanism for differentiating between the delete button in the `edit.html` template and the delete links in the `rows.html` template. When this button issues a request, it will look something like this:

    DELETE http://example.org/contacts/42 HTTP/1.1
    Accept: text/html,*/*
    Host: example.org
    ...
    HX-Trigger: delete-btn
    ...
    

You can see that the request now includes the `id` of the button. This allows us to write code very similar to what we did for the active search pattern, using a conditional on the `HX-Trigger` header to determine what we want to do. If that header has the value `delete-btn`, then we know the request came from the button on the edit page, and we can do what we are currently doing: delete the contact and redirect to `/contacts` page.

If it _does not_ have that value, then we can simply delete the contact and return an empty string. This empty string will replace the target, in this case the row for the given contact, thereby removing the row from the UI.

Let’s refactor our server-side code to do this:

    @app.route("/contacts/", methods=["DELETE"])
    def contacts_delete(contact_id=0):
        contact = Contact.find(contact_id)
        contact.delete()
        if request.headers.get('HX-Trigger') == 'delete-btn': <1>
            flash("Deleted Contact!")
            return redirect("/contacts", 303)
        else:
            return "" <2>

Updating our server code to handle two different delete) patterns

1.  If the delete button on the edit page submitted this request, then continue to do the previous logic.
    
2.  If not, simply return an empty string, which will delete the row.

And that’s our server-side implementation: when a user clicks “Delete” on a contact row and confirms the delete, the row will disappear from the UI. Once again, we have a situation where just changing a few lines of simple code gives us a dramatically different behavior. Hypermedia is powerful in this manner.

## The Htmx Swapping Model

This is pretty cool, but there is another improvement we can make if we take some time to understand the htmx content swapping model: it would be nice if, rather than just instantly deleting the row, we faded it out before we removed it. The fade would make it clear that the row is being removed, giving the user some nice visual feedback on the deletion.

It turns out we can do this pretty easily with htmx, but to do so we’ll need to dig in to exactly how htmx swaps content.

You might think that htmx simply puts the new content into the DOM, but that’s not in fact how it works. Instead, content goes through a series of steps as it is added to the DOM:

*   When content is received and about to be swapped into the DOM, the `htmx-swapping` CSS class is added to the target element.
    
*   A small delay then occurs (we will discuss why this delay exists in a moment).
    
*   Next, the `htmx-swapping` class is removed from the target and the `htmx-settling` class is added.
    
*   The new content is swapped into the DOM.
    
*   Another small delay occurs.
    
*   Finally, the `htmx-settling` class is removed from the target.

There is more to the swap mechanic (settling, for example, is a more advanced topic that we will discuss in a later chapter) but this is enough for now.

Now, there are small delays in the process here, typically on the order of a few milliseconds. Why so? It turns out that these small delays allow _CSS transitions_ to occur.

**CSS Transitions**

CSS transitions are a technology that allow you to animate a transition from one style to another. So, for example, if you changed the height of something from 10 pixels to 20 pixels, by using a CSS transition you can make the element smoothly animate to the new height. These sorts of animations are fun, often increase application usability, and are a great mechanism to add polish to your web application.

Unfortunately, CSS transitions are difficult to access in plain HTML: you usually have to use JavaScript and add or remove classes to get them to trigger. This is why the htmx swap model is more complicated than you might initially think. By swapping in classes and adding small delays, you can access CSS transitions purely within HTML, without needing to write any JavaScript!

## Taking Advantage of “htmx-swapping”

OK, so, let’s go back and look at our inline delete mechanic: we click an htmx-enhanced link which deletes the contact and then swaps some empty content in for the row. We know that before the `tr` element is removed, it will have the `htmx-swapping` class added to it. We can take advantage of that to write a CSS transition that fades the opacity of the row to 0. Here is what that CSS looks like:

    tr.htmx-swapping { <1>
      opacity: 0; <2>
      transition: opacity 1s ease-out; <3>
    }

Adding a fade out transition

1.  We want this style to apply to `tr` elements with the `htmx-swapping` class on them.
    
2.  The `opacity` will be 0, making it invisible.
    
3.  The `opacity` will transition to 0 over a 1 second time period, using the `ease-out` function.

Again, this is not a CSS book and we are not going to go deeply into the details of CSS transitions, but hopefully the above makes sense to you, even if this is the first time you’ve seen CSS transitions.

So, think about what this means from the htmx swapping model: when htmx gets content back to swap into the row it will put the `htmx-swapping` class on the row and wait a bit. This will allow the transition to a zero opacity to occur, fading the row out. Then the new (empty) content will be swapped in, which will effectively remove the row.

Sounds good, and we are nearly there. There is one more thing we need to do: the default “swap delay” for htmx is very short, a few milliseconds. That makes sense in most cases: you don’t want to have much of a delay before you put the new content into the DOM. But, in this case, we want to give the CSS animation time to complete before we do the swap, we want to give it a second, in fact.

Fortunately htmx has an option for the `hx-swap` annotation that allows you to set the swap delay: following the swap type you can add `swap:` followed by a timing value to tell htmx to wait a specific amount of time before it swaps. Let’s update our HTML to allow a one second delay before the swap is done for the delete action:

    <td>
      <a href="/contacts/{{ contact.id }}/edit">Edita>
      <a href="/contacts/{{ contact.id }}">Viewa>
      <a href="#" hx-delete="/contacts/{{ contact.id }}"
        hx-swap="outerHTML swap:1s" <1>
        hx-confirm="Are you sure you want to delete this contact?"
        hx-target="closest tr">Deletea>
    td>

The existing row actions

1.  A swap delay changes how long htmx waits before it swaps in new content.

With this modification, the existing row will stay in the DOM for an additional second, with the `htmx-swapping` class on it. This will give the row time to transition to an opacity of zero, giving the fade out effect we want.

Now, when a user clicks on a “Delete” link and confirms the delete, the row will slowly fade out and then, once it has faded to a 0 opacity, it will be removed. Pretty fancy, and all done in a declarative, hypermedia-oriented manner, no JavaScript required. (Well, obviously htmx is written in JavaScript, but you know what we mean: we didn’t have to write any JavaScript to implement the feature.)