# Alpine.js

OK, so that’s an in-depth look at how to structure plain VanillaJS-style JavaScript. Let’s turn our attention to an actual JavaScript framework that enables a different approach for adding dynamic behavior to your application, [Alpine.js](https://alpinejs.dev).

Alpine is a relatively new JavaScript library that allows developers to embed JavaScript code directly in HTML, akin to the `on*` attributes available in plain HTML and JavaScript. However, Alpine takes this concept of embedded scripting much further than `on*` attributes.

Alpine bills itself as a modern replacement for jQuery, the widely used, older JavaScript library. As you will see, it definitely lives up to this promise.

Installing Alpine is very easy: it is a single file and is dependency-free, so you can simply include it via a CDN:

    <script src="https://unpkg.com/alpinejs">script>

Installing Alpine

You can also install it via a package manager such as NPM, or vendor it from your own server.

Alpine provides a set of HTML attributes, all of which begin with the `x-` prefix, the main one of which is `x-data`. The content of `x-data` is a JavaScript expression which evaluates to an object. The properties of this object can, then, be accessed within the element that the `x-data` attribute is located.

To get a flavor of AlpineJS, let’s look at how to implement our counter example using it.

For the counter, the only state we need to keep track of is the current number, so let’s declare a JavaScript object with one property, `count`, in an `x-data` attribute on the div for our counter:

    <div class="counter" x-data="{ count: 0 }">

Counter with Alpine, line 1

This defines our state, that is, the data we are going to be using to drive dynamic updates to the DOM. With the state declared like this, we can now use it _within_ the div element it is declared on. Let’s add an `output` element with an `x-text` attribute.

Next, we will _bind_ the `x-text` attribute to the `count` attribute we declared in the `x-data` attribute on the parent `div` element. This will have the effect of setting the text of the `output` element to whatever the value of `count` is: if `count` is updated, so will the text of the `output`. This is “reactive” programming, in that the DOM will “react” to changes to the backing data.

    <div x-data="{ count: 0 }">
      <output x-text="count">output> <1>

Counter with Alpine, lines 1-2

1.  The `x-text` attribute.
    

Next, we need to update the count, using a button. Alpine allows you to attach event listeners with the `x-on` attribute.

To specify the event to listen for, you add a colon and then the event name after the `x-on` attribute name. Then, the value of the attribute is the JavaScript you wish to execute. This is similar to the plain `on*` attributes we discussed earlier, but it turns out to be much more flexible.

We want to listen for a `click` event, and we want to increment `count` when a click occurs, so here is what the Alpine code will look like:

    <div x-data="{ count: 0 }">
      <output x-text="count">output>
    
      <button x-on:click="count++">Incrementbutton> <1>
    div>

Counter with Alpine, the full thing

1.  With `x-on`, we specify the event in the attribute _name_.
    

And that’s all it takes. A simple component like a counter should be simple to code, and Alpine delivers.

## “x-on:click” vs. “onclick”

As we said, the Alpine `x-on:click` attribute (or its shorthand, the `@click` attribute) is similar to the built-in `onclick` attribute. However, it has additional features that make it significantly more useful:

*   You can listen for events from other elements. For example, the `.outside` modifier lets you listen to any click event that is _not_ within the element.
    
*   You can use other modifiers to:
    
    *   throttle or debounce event listeners
        
    *   ignore events that are bubbled up from descendant elements
        
    *   attach passive listeners
        
*   You can listen to custom events. For example, if you wanted to listen for the `htmx:after-request` event you could write `x-on:htmx:after-request="doSomething()"`.
    

## Reactivity and Templating

We hope you’ll agree that the AlpineJS version of the counter widget is better, in general, than the VanillaJS implementation, which was either somewhat hacky or spread out over multiple files.

A big part of the power of AlpineJS is that it supports a notion of “reactive” variables, allowing you to bind the count of the `div` element to a variable that both the `output` and the `button` can reference, and properly updating all the dependencies when a mutation occurs. Alpine allows for much more elaborate data bindings than we have demonstrated here, and it is an excellent general purpose client-side scripting library.

## Alpine.js in Action: A Bulk Action Toolbar

Let’s implement a feature in Contact.app with Alpine. As it stands currently, Contact.app has a “Delete Selected Contacts” button at the very bottom of the page. This button has a long name, is not easy to find and takes up a lot of room. If we wanted to add additional “bulk” actions, this wouldn’t scale well visually.

In this section, we’ll replace this single button with a toolbar. Furthermore, the toolbar will only appear when the user starts selecting contacts. Finally, it will show how many contacts are selected and let you select all contacts in one go.

The first thing we will need to add is an `x-data` attribute, to hold the state that we will use to determine if the toolbar is visible or not. We will need to place this on an ancestor element of both the toolbar that we are going to add, as well as the checkboxes, which will be updating the state when they are checked and unchecked. The best option given our current HTML is to place the attribute on the `form` element that surrounds the contacts table. We will declare a property, `selected`, which will be an array that holds the selected contact ids, based on the checkboxes that are selected.

Here is what our form tag will look like:

    <form x-data="{ selected: [] }"> <1>

1.  This form wraps around the contacts table.
    

Next, at the top of the contacts table, we are going to add a `template` tag. A template tag is _not_ rendered by a browser, by default, so you might be surprised that we are using it. However, by adding an Alpine `x-if` attribute, we can tell Alpine: if a condition is true, show the HTML within this template.

Recall that we want to show the toolbar if and only if one or more contacts are selected. But we know that we will have the ids of the selected contacts in the `selected` property. Therefore, we can check the _length_ of that array to see if there are any selected contacts, quite easily:

    <template x-if="selected.length > 0"> <1>
      <div class="box info tool-bar">
        <slot x-text="selected.length">slot>
        contacts selected
    
        <button type="button" class="bad bg color border">Deletebutton> <2>
        <hr aria-orientation="vertical">
        <button type="button">Cancelbutton> <2>
      div>
    template>

1.  Show this HTML if there are 1 or more selected contacts.
    
2.  We will implement these buttons in just a moment.
    

The next step is to ensure that toggling a checkbox for a given contact adds (or removes) a given contact’s id from the `selected` property. To do this, we will need to use a new Alpine attribute, `x-model`. The `x-model` attribute allows you to _bind_ a given element to some underlying data, or its “model.”

In this case, we want to bind the value of the checkbox inputs to the `selected` property. This is how we do this:

    <td>
      <input type="checkbox" name="selected_contact_ids"
        value="{{ contact.id }}" x-model="selected"> <1>
    td>

1.  The `x-model` attribute binds the `value` of this input to the `selected` property
    

Now, when a checkbox is checked or unchecked, the `selected` array will be updated with the given row’s contact id. Furthermore, mutations we make to the `selected` array will similarly be reflected in the checkboxes” state. This is known as a _two-way_ binding.

With this code written, we can make the toolbar appear and disappear, based on whether contact checkboxes are selected.

Very slick.

Before we move on, you may have noticed our code here includes some “class=” references. These are for css styling, and are not part of Alpine.js. We’ve included them only as a reminder that the menu bar we’re building will require css to work well. The classes in the code above refer to a minimal css library called Missing.css. If you use other css libraries, such as Bootstrap, Tailwind, Bulma, Pico.css, etc., your styling code will be different.

### Implementing actions

Now that we have the mechanics of showing and hiding the toolbar, let’s look at how to implement the buttons within the toolbar.

Let’s first implement the “Clear” button, because it is quite easy. All we need to do is, when the button is clicked, clear out the `selected` array. Because of the two-way binding that Alpine provides, this will uncheck all the selected contacts (and then hide the toolbar)!

For the _Cancel_ button, our job is simple:

    <button type="button" @click="selected = []">Cancelbutton> <1>

1.  Reset the `selected` array.
    

Once again, AlpineJS makes this very easy.

The “Delete” button, however, will be a bit more complicated. It will need to do two things: first it will confirm if the user indeed intends to delete the contacts selected. Then, if the user confirms the action, it will use the htmx JavaScript API to issue a `DELETE` request.

    <button type="button" class="bad bg color border"
      @click="
        confirm(`Delete ${selected.length} contacts?`) && <1>
        htmx.ajax('DELETE', '/contacts',
          { source: $root, target: document.body }) <2>
      ">
      Delete
    button>

1.  Confirm the user wishes to delete the selected number of contacts.
    
2.  Issue a `DELETE` using the htmx JavaScript API.
    

Note that we are using the short-circuiting behavior of the `&&` operator in JavaScript to avoid the call to `htmx.ajax()` if the `confirm()` call returns false.

The `htmx.ajax()` function is just a way to access the normal, HTML-driven hypermedia exchange that htmx’s HTML attributes give you directly from JavaScript.

Looking at how we call `htmx.ajax`, we first pass in that we want to issue a `DELETE` to `/contacts`. We then pass in two additional pieces of information: `source` and `target`. The `source` property is the element from which htmx will collect data to include in the request. We set this to `$root`, which is a special symbol in Alpine that will be the element that has the `x-data` attribute declared on it. In this case, it will be the form containing all of our contacts. The `target`, or where the response HTML will be placed, is just the entire document’s body, since the `DELETE` handler returns a whole page when it completes.

Note that we are using Alpine here in a Hypermedia-Driven Application compatible manner. We _could_ have issued an AJAX request directly from Alpine and perhaps updated an `x-data` property depending on the results of that request. But, instead, we delegated to htmx’s JavaScript API, which made a _hypermedia exchange_ with the server.

This is the key to scripting in a hypermedia-friendly manner within a Hypermedia-Driven Application.

So, with all of this in place, we now have a much improved experience for performing bulk actions on contacts: less visual clutter and the toolbar can be extended with more options without creating bloat in the main interface of our app.