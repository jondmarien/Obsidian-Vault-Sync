# Htmx Attributes

Thus far we have used about fifteen different attributes from htmx in our application. The most important ones have been:

`hx-get`, `hx-post`, etc.

To specify the AJAX request an element should make

`hx-trigger`

To specify the event that triggers a request

`hx-swap`

To specify how to swap the returned HTML content into the DOM

`hx-target`

To specify where in the DOM to swap the returned HTML content

Two of these attributes, `hx-swap` and `hx-trigger`, support a number of useful options for creating more advanced Hypermedia-Driven Applications.

## hx-swap

We’ll start with the hx-swap attribute. This is often not included on elements that issue htmx-driven requests because its default behavior — `innerHTML`, which swaps the inner HTML of the element — tends to cover most use cases.

We earlier saw situations where we wanted to override the default behavior and use `outerHTML`, for example. And, in chapter 2, we discussed some other swap options beyond these two, `beforebegin`, `afterend`, etc.

In chapter 5, we also looked at the `swap` delay modifier for `hx-swap`, which allowed us to fade some content out before it was removed from the DOM.

In addition to these, `hx-swap` offers further control with the following modifiers:

`settle`

Like `swap`, this allows you to apply a specific delay between when the content has been swapped into the DOM and when its attributes are “settled”, that is, updated from their old values (if any) to their new values. This can give you fine-grained control over CSS transitions.

`show`

Allows you to specify an element that should be shown — that is, scrolled into the viewport of the browser if necessary — when a request is completed.

`scroll`

Allows you to specify a scrollable element (that is, an element with scrollbars), that should be scrolled to the top or bottom when a request is completed.

`focus-scroll`

Allows you to specify that htmx should scroll to the focused element when a request completes. The default for this modifier is “false.”

So, for example, if we had a button that issued a `GET` request, and we wished to scroll to the top of the `body` element when the request completed, we would write the following HTML:

    <button hx-get="/contacts" hx-target="#content-div"
      hx-swap="innerHTML show:body:top"> <1>
      Get Contacts
    button>

Scrolling to the top of the page

1.  This tells htmx to show the top of the body after the swap occurs.
    

More details and examples can be found online in the `hx-swap` [documentation](https://htmx.org/attributes/hx-swap/).

## hx-trigger

Like `hx-swap`, `hx-trigger` can often be omitted when you are using htmx, because the default behavior is typically what you want. Recall the default triggering events are determined by an element’s type:

*   Requests on `input`, `textarea` & `select` elements are triggered by the `change` event.
    
*   Requests on `form` elements are triggered on the `submit` event.
    
*   Requests on all other elements are triggered by the `click` event.
    

There are times, however, when you want a more elaborate trigger specification. A classic example is the active search example we implemented in Contact.app:

    <input id="search" type="search" name="q"
      value="{{ request.args.get('q') or '' }}"
      hx-get="/contacts"
      hx-trigger="search, keyup delay:200ms changed"/> <1>

The active search input

1.  An elaborate trigger specification.
    

This example took advantage of two modifiers available for the `hx-trigger` attribute:

`delay`

Allows you to specify a delay to wait before a request is issued. If the event occurs again, the first event is discarded and the timer resets. This allows you to “debounce” requests.

`changed`

Allows you to specify that a request should only be issued when the `value` property of the given element has changed.

`hx-trigger` has several additional modifiers. This makes sense, because events are fairly complex and we want to be able to take advantage of all the power they offer. We will discuss events in more detail below.

Here are the other modifiers available on `hx-trigger`:

`once`

The given event will only trigger a request once.

`throttle`

Allows you to throttle events, only issuing them once every certain interval. This is different than `delay` in that the first event will trigger immediately, but any following events will not trigger until the throttle time period has elapsed.

`from`

A CSS selector that allows you to pick another element to listen for events on. We will see an example of this used later in the chapter.

`target`

A CSS selector that allows you to filter events to only those that occur directly on a given element. In the DOM, events “bubble” to their ancestor elements, so a `click` event on a button will also trigger a `click` event on an enclosing `div`, all the way up to the `body` element. Sometimes you want to specify an event directly on a given element, and this attribute allows you to do that.

`consume`

If this option is set to `true`, the triggering event will be cancelled and not propagate to ancestor elements.

`queue`

This option allows you to specify how events are queued in htmx. By default, when htmx receives a triggering event, it will issue a request and start an event queue. If the request is still in flight when another event is received, it will queue the event and, when the request finishes, trigger a new request. By default, it only keeps the last event it receives, but you can modify that behavior using this option: for example, you can set it to `none` and ignore all triggering events that occur during a request.

### Trigger filters

The `hx-trigger` attribute also allows you to specify a _filter_ for events by using square brackets enclosing a JavaScript expression after the event name.

Let’s say you have a complex situation where contacts should only be retrievable in certain situations. You have a JavaScript function, `contactRetrievalEnabled()` that returns a boolean, `true` if contacts can be retrieved and `false` otherwise. How could you use this function to place a gate on a button that issues a request to `/contacts`?

To do this using an event filter in htmx, you would write the following HTML:

    <script>
      function contactRetrievalEnabled() {
        // code to test if contact retrieval is enabled
        ...
      }
    script>
    <button hx-get="/contacts"
      hx-trigger="click[contactRetrievalEnabled()]"> <1>
      Get Contacts
    button>

The active search input

1.  A request is issued on click only when `contactRetrievalEnabled()` returns `true`.
    

The button will not issue a request if `contactRetrievalEnabled()` returns false, allowing you to dynamically control when the request will be made. There are common situations that call for an event trigger, when you only want to issue a request under specific circumstances:

*   if a certain element has focus
    
*   if a given form is valid
    
*   if a set of inputs have specific values
    

Using event filters, you can use whatever logic you’d like to filter requests by htmx.

### Synthetic events

In addition to these modifiers, `hx-trigger` offers a few “synthetic” events, that is events that are not part of the regular DOM API. We have already seen `load` and `revealed` in our lazy loading and infinite scroll examples, but htmx also gives you an `intersect` event that triggers when an element intersects its a viewport.

This synthetic event uses the modern Intersection Observer API, which you can read more about at [MDN](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API).

Intersection gives you fine-grained control over exactly when a request should be triggered. For example, you can set a threshold and specify that the request be issued only when an element is 50% visible.

The `hx-trigger` attribute certainly is the most complex in htmx. More details and examples can be found in its [documentation](https://htmx.org/attributes/hx-trigger/).

## Other Attributes

Htmx offers many other less commonly used attributes for fine-tuning the behavior of your Hypermedia-Driven Application.

Here are some of the most useful ones:

hx-push-url

“Pushes” the request URL (or some other value) into the navigation bar.

hx-preserve

Preserves a bit of the DOM between requests; the original content will be kept, regardless of what is returned.

hx-sync

Synchronized requests between two or more elements.

hx-disable

Disables htmx behavior on this element and any children. We will come back to this when we discuss the topic of security.

Let’s take a look at `hx-sync`, which allows us to synchronize AJAX requests between two or more elements. Consider a simple case where we have two buttons that both target the same element on the screen:

    <button hx-get="/contacts" hx-target="body">
      Get Contacts
    button>
    <button hx-get="/settings" hx-target="body">
      Get Settings
    button>

Two competing buttons

This is fine and will work, but what if a user clicks the “Get Contacts” button and then the request takes a while to respond? And, in the meantime the user clicks the “Get Settings” button? In this case we would have two requests in flight at the same time.

If the `/settings` request finished first and displayed the user’s setting information, they might be very surprised if they began making changes and then, suddenly, the `/contacts` request finished and replaced the entire body with the contacts instead!

To deal with this situation, we might consider using an `hx-indicator` to alert the user that something is going on, making it less likely that they click the second button. But if we really want to guarantee that there is only one request at a time issued between these two buttons, the right thing to do is to use the `hx-sync` attribute. Let’s enclose both buttons in a `div` and eliminate the redundant `hx-target` specification by hoisting the attribute up to that `div`. We can then use `hx-sync` on that div to coordinate requests between the two buttons.

Here is our updated code:

    <div hx-target="body" <1>
      hx-sync="this"> <2>
      <button hx-get="/contacts">
        Get Contacts
      button>
      <button hx-get="/settings">
        Get Settings
      button>
    div>

Syncing two buttons

1.  Hoist the duplicate `hx-target` attributes to the parent `div`.
    
2.  Synchronize on the parent `div`.
    

By placing the `hx-sync` attribute on the `div` with the value `this`, we are saying “Synchronize all htmx requests that occur within this `div` element with one another.” This means that if one button already has a request in flight, other buttons within the `div` will not issue requests until that has finished.

The `hx-sync` attribute supports a few different strategies that allow you to, for example, replace an existing request in flight, or queue requests with a particular queuing strategy. You can find complete documentation, as well as examples, at the htmx.org page for [hx-sync](https://htmx.org/attributes/hx-sync/).

As you can see, htmx offers a lot of attribute-driven functionality for more advanced Hypermedia-Driven Applications. A complete reference for all htmx attributes can be found [on the htmx website](https://htmx.org/reference/#attributes).