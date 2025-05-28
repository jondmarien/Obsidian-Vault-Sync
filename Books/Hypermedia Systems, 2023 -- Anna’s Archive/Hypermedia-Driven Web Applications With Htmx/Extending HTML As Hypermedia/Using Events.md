# Using Events

Thus far we have been using a button to issue a request with htmx. You have probably intuitively understood that the button would issue its request when you clicked on the button since, well, that’s what you do with buttons: you click on them.

And, yes, by default when an `hx-get` or another request-driving annotation from htmx is placed on a button, the request will be issued when the button is clicked.

However, htmx generalizes this notion of an event triggering a request by using, you guessed it, another attribute: `hx-trigger`. The `hx-trigger` attribute allows you to specify one or more events that will cause the element to trigger an HTTP request.

Often you don’t need to use `hx-trigger` because the default triggering event will be what you want. The default triggering event depends on the element type, and should be fairly intuitive:

*   Requests on `input`, `textarea` & `select` elements are triggered by the `change` event.
    
*   Requests on `form` elements are triggered on the `submit` event.
    
*   Requests on all other elements are triggered by the `click` event.
    

To demonstrate how `hx-trigger` works, consider the following situation: we want to trigger the request on our button when the mouse enters it. Now, this is certainly not a _good_ UX pattern, but bear with us: we are just using this as an example.

To respond to a mouse entering the button, we would add the following attribute to our button:

    <div id="main">
    
      <button hx-get="/contacts" hx-target="#main" hx-swap="outerHTML"
        hx-trigger="mouseenter"> <1>
        Get The Contacts
      button>
    
    div>

A (bad?) button that triggers on mouse entry

1.  Issue a request on the… `mouseenter` event.
    

Now, with this `hx-trigger` attribute in place, whenever the mouse enters this button, a request will be triggered. Silly, but it works.

Let’s try something a bit more realistic and potentially useful: let’s add support for a keyboard shortcut for loading the contacts, `Ctrl-L` (for “Load”). To do this we will need to take advantage of additional syntax that the `hx-trigger` attribute supports: event filters and additional arguments.

Event filters are a mechanism for determining if a given event should trigger a request or not. They are applied to an event by adding square brackets after it: `someEvent[someFilter]`. The filter itself is a JavaScript expression that will be evaluated when the given event occurs. If the result is truthy, in the JavaScript sense, it will trigger the request. If not, the request will not be triggered.

In the case of keyboard shortcuts, we want to catch the `keyup` event in addition to the click event:

    <div id="main">
    
      <button hx-get="/contacts" hx-target="#main" hx-swap="outerHTML"
        hx-trigger="click, keyup"> <1>
        Get The Contacts
      button>
    
    div>

A start, trigger on keyup

1.  A trigger with two events.
    

Note that we have a comma separated list of events that can trigger this element, allowing us to respond to more than one potential triggering event. We still want to respond to the `click` event and load the contacts, in addition to handling the `Ctrl-L` keyboard shortcut.

Unfortunately there are two problems with our `keyup` addition: As it stands, it will trigger requests on _any_ keyup event that occurs. And, worse, it will only trigger when a keyup occurs _within_ this button. The user would need to tab onto the button to make it active and then begin typing.

Let’s fix these two issues. To fix the first one, we will use a trigger filter to test that Control key and the “L” key are pressed together:

    <div id="main">
    
      <button hx-get="/contacts" hx-target="#main" hx-swap="outerHTML"
        hx-trigger="click, keyup[ctrlKey && key == 'l']"> <1>
        Get The Contacts
      button>
    
    div>

Getting better with filter on keyup

1.  `keyup` now has a filter, so the control key and L must be pressed.
    

The trigger filter in this case is `ctrlKey && key == 'l'`. This can be read as “A key up event, where the ctrlKey property is true and the key property is equal to l.” Note that the properties `ctrlKey` and `key` are resolved against the event rather than the global name space, so you can easily filter on the properties of a given event. You can use any expression you like for a filter, however: calling a global JavaScript function, for example, is perfectly acceptable.

OK, so this filter limits the keyup events that will trigger the request to only `Ctrl-L` presses. However, we still have the problem that, as it stands, only `keyup` events _within_ the button will trigger the request.

If you are not familiar with the JavaScript event bubbling model: events typically “bubble” up to parent elements. So an event like `keyup` will be triggered first on the focused element, and then on its parent (enclosing) element, and so on, until it reaches the top level `document` object that is the root of all other elements.

To support a global keyboard shortcut that works regardless of what element has focus, we will take advantage of event bubbling and a feature that the `hx-trigger` attribute supports: the ability to listen to _other elements_ for events. The syntax for doing this is the `from:` modifier, which is added after an event name and that allows you to specify a specific element to listen for the given event on using a CSS selector.

In this case, we want to listen to the `body` element, which is the parent element of all visible elements on the page.

Here is what our updated `hx-trigger` attribute looks like:

    <div id="main">
    
      <button hx-get="/contacts" hx-target="#main" hx-swap="outerHTML"
        hx-trigger="click, keyup[ctrlKey && key == 'l'] from:body"> <1>
        Get The Contacts
      button>
    
    div>

Even better, listen for keyup on the body

1.  Listen to the ‘keyup” event on the `body` tag.
    

Now, in addition to clicks, the button will listen for `keyup` events on the body of the page. So it will issue a request when it is clicked on and also whenever someone hits `Ctrl-L` within the body of the page.

And now we have a nice keyboard shortcut for our Hypermedia-Driven Application.

The `hx-trigger` attribute supports many more modifiers, and it is more elaborate than other htmx attributes. This is because events, in general, are complicated and require a lot of details to get just right. The default trigger will often suffice, however, and you typically don’t need to reach for complicated `hx-trigger` features when using htmx.

Even with more sophisticated trigger specifications like the keyboard shortcut we just added, the overall feel of htmx is _declarative_ rather than _imperative_. That keeps htmx-powered applications “feeling like” standard web 1.0 applications in a way that adding significant amounts of JavaScript does not.