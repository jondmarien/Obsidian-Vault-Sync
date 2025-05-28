# AJAX-ifying Our Application

To get our feet wet with htmx, the first feature we are going to take advantage of is known as “boosting.” This is a bit of a “magic” feature in that we don’t need to do much beyond adding a single attribute, `hx-boost`, to the application.

When you put `hx-boost` on a given element with the value `true`, it will “boost” all anchor and form elements within that element. “Boost”, here, means that htmx will convert all those anchors and forms from “normal” hypermedia controls into AJAX-powered hypermedia controls. Rather than issuing “normal” HTTP requests that replace the whole page, the links and forms will issue AJAX requests. Htmx then swaps the inner content of the tag in the response to these requests into the existing pages tag.

This makes navigation feel faster because the browser will not be re-interpreting most of the tags in the response and so forth.

## Boosted Links

Let’s take a look at an example of a boosted link. Below is a link to a hypothetical settings page for a web application. Because it has `hx-boost="true"` on it, htmx will halt the normal link behavior of issuing a request to the `/settings` path and replacing the entire page with the response. Instead, htmx will issue an AJAX request to `/settings`, take the result and replace the `body` element with the new content.

    <a href="/settings" hx-boost="true">Settingsa> <1>

A boosted link

1.  The `hx-boost` attribute makes this link AJAX-powered.
    

You might reasonably ask: what’s the advantage here? We are issuing an AJAX request and simply replacing the entire body.

Is that significantly different from just issuing a normal link request?

Yes, it is in fact different: with a boosted link, the browser is able to avoid any processing associated with the head tag. The head tag often contains many scripts and CSS file references. In the boosted scenario, it is not necessary to re-process those resources: the scripts and styles have already been processed and will continue to apply to the new content. This can often be a very easy way to speed up your hypermedia application.

A second question you might have is: does the response need to be formatted specially to work with `hx-boost`? After all, the settings page would normally render an `html` tag, with a `head` tag and so forth. Do you need to handle “boosted” requests specially?

The answer is no: htmx is smart enough to pull out only the content of the `body` tag to swap in to the new page. The `head` tag is mostly ignored: only the title tag, if it is present, will be processed. This means you don’t need to do anything special on the server side to render templates that `hx-boost` can handle: just return the normal HTML for your page, and it should work fine.

Note that boosted links (and forms) will also continue to update the navigation bar and history, just like normal links, so users will be able to use the browser back button, will be able to copy and paste URLs (or “deep links”) and so on. Links will act pretty much like “normal”, they will just be faster.

## Boosted Forms

Boosted form tags work in a similar way to boosted anchor tags: a boosted form will use an AJAX request rather than the usual browser-issued request, and will replace the entire body with the response.

Here is an example of a form that posts messages to the `/messages` endpoint using an HTTP `POST` request. By adding `hx-boost` to it, those requests will be done in AJAX, rather than the normal browser behavior.

    <form action="/messages" method="post" hx-boost="true"> <1>
      <input type="text" name="message" placeholder="Enter A Message...">
      <button>Post Your Messagebutton>
    form>

A boosted form

1.  As with the link, `hx-boost` makes this form AJAX-powered.
    

A big advantage of the AJAX-based request that `hx-boost` uses (and the lack of head processing that occurs) is that it avoids what is known as a _flash of unstyled content_:

Flash Of Unstyled Content (FOUC)

A situation where a browser renders a web page before all the styling information is available for the page. A FOUC causes a disconcerting momentary “flash” of the unstyled content, which is then restyled when all the style information is available. You will notice this as a flicker when you move around the internet: text, images and other content can “jump around” on the page as styles are applied to it.

With `hx-boost` the site’s styling is already loaded _before_ the new content is retrieved, so there is no such flash of unstyled content. This can make a “boosted” application feel both smoother and also snappier in general.

## Attribute Inheritance

Let’s expand on our previous example of a boosted link, and add a few more boosted links alongside it. We’ll add links so that we have one to the `/contacts` page, the `/settings` page, and the `/help` page. All these links are boosted and will behave in the manner that we have described above.

This feels a little redundant, doesn’t it? It seems silly to annotate all three links with the `hx-boost="true"` attribute right next to one another.

    <a href="/contacts" hx-boost="true">Contactsa>
    <a href="/settings" hx-boost="true">Settingsa>
    <a href="/help" hx-boost="true">Helpa>

A set of boosted links

Htmx offers a feature to help reduce this redundancy: attribute inheritance. With most attributes in htmx, if you place it on a parent, the attribute will also apply to children elements. This is how Cascading Style Sheets work, and that idea inspired htmx to adopt a similar “cascading htmx attributes” feature.

To avoid the redundancy in this example, let’s introduce a `div` element that encloses all the links and then “hoist” the `hx-boost` attribute up to that parent `div`. This will let us remove the redundant `hx-boost` attributes but ensure all the links are still boosted, inheriting that functionality from the parent `div`.

Note that any legal HTML element could be used here, we just use a `div` out of habit.

    <div hx-boost="true"> <1>
      <a href="/contacts">Contactsa>
      <a href="/settings">Settingsa>
      <a href="/help">Helpa>
    div>

Boosting links via the parent

1.  The `hx-boost` has been moved to the parent div.
    

Now we don’t have to put an `hx-boost="true"` on every link and, in fact, we can add more links alongside the existing ones, and they, too, will be boosted, without us needing to explicitly annotate them.

That’s fine, but what if you have a link that you _don’t_ want boosted within an element that has `hx-boost="true"` on it? A good example of this situation is when a link is to a resource to be downloaded, such as a PDF. Downloading a file can’t be handled well by an AJAX request, so you probably want that link to behave “normally”, issuing a full page request for the PDF, which the browser will then offer to save as a file on the user’s local system.

To handle this situation, you simply override the parent `hx-boost` value with `hx-boost="false"` on the anchor tag that you don’t want to boost:

    <div hx-boost="true"> <1>
      <a href="/contacts">Contactsa>
      <a href="/settings">Settingsa>
      <a href="/help">Helpa>
      <a href="/help/documentation.pdf" hx-boost="false"> <2>
        Download Docs
      a>
    div>

Disabling boosting

1.  The `hx-boost` is still on the parent div.
    
2.  The boosting behavior is overridden for this link.
    

Here we have a new link to a documentation PDF that we wish to function like a regular link. We have added `hx-boost="false"` to the link and this declaration will override the `hx-boost="true"` on the parent `div`, reverting it to regular link behavior and, thus, allowing for the file download behavior that we want.

## Progressive Enhancement

A nice aspect of `hx-boost` is that it is an example of _progressive enhancement_:

Progressive Enhancement

A software design philosophy that aims to provide as much essential content and functionality to as many users as possible, while delivering a better experience to users with more advanced web browsers.

Consider the links in the example above. What would happen if someone did not have JavaScript enabled?

No problem. The application would continue to work, but it would issue regular HTTP requests, rather than AJAX-based HTTP requests. This means that your web application will work for the maximum number of users; those with modern browsers (or users who have not turned off JavaScript) can take advantage of the benefits of the AJAX-style navigation that htmx offers, and others can still use the app just fine.

Compare the behavior of htmx’s `hx-boost` attribute with a JavaScript heavy Single Page Application: such an application often won’t function _at all_ without JavaScript enabled. It is often very difficult to adopt a progressive enhancement approach when you use an SPA framework.

This is _not_ to say that every htmx feature offers progressive enhancement. It is certainly possible to build features that do not offer a “No JS” fallback in htmx, and, in fact, many of the features we will build later in the book will fall into this category. We will note when a feature is progressive enhancement friendly and when it is not.

Ultimately, it is up to you, the developer, to decide if the trade-offs of progressive enhancement (a more basic UX, limited improvements over plain HTML) are worth the benefits for your application users.

## Adding “hx-boost” to Contact.app

For the contact app we are building, we want this htmx “boost” behavior…​ well, everywhere.

Right? Why not?

How could we accomplish that?

Well, it’s easy (and pretty common in htmx-powered web applications): we can just add `hx-boost` on the `body` tag of our `layout.html` template, and we are done.

    <html>
    ...
    <body hx-boost="true"> <1>
    ...
    body>
    html>

Boosting the entire contact.app

1.  All links and forms will be boosted now!
    

Now every link and form in our application will use AJAX by default, making it feel much snappier. Consider the “New Contact” link that we created on the main page:

    <a href="/contacts/new">Add Contacta>

A newly boosted “add contact” link

Even though we haven’t touched anything on this link or on the server-side handling of the URL it targets, it will now “just work” as a boosted link, using AJAX for a snappier user experience, including updating history, back button support and so on. And, if JavaScript isn’t enabled, it will fall back to the normal link behavior.

All this with one htmx attribute.

The `hx-boost` attribute is neat, but is different than other htmx attributes in that it is pretty “magical”: by making one small change you modify the behavior of a large number of elements on the page, turning them into AJAX-powered elements. Most other htmx attributes are generally lower level and require more explicit annotations in order to specify exactly what you want htmx to do. In general, this is the design philosophy of htmx: prefer explicit over implicit and obvious over “magic.”

However, the `hx-boost` attribute was too useful to allow dogma to override practicality, and so it is included as a feature in the library.