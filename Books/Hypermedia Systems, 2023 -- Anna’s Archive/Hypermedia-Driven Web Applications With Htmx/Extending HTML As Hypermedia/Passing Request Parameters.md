# Passing Request Parameters

So far we have just looked at a situation where a button makes a simple `GET` request. This is conceptually very close to what an anchor tag might do. But there is that other native hypermedia control in HTML-based applications: forms. Forms are used to pass additional information beyond just a URL up to the server in a request.

This information is captured via input and input-like elements within the form via the various types of input tags available in HTML.

Htmx allows you include this additional information in a way that mirrors HTML itself.

## Enclosing Forms

The simplest way to pass input values with a request in htmx is to enclose the element making a request within a form tag.

Let’s take our original search form and convert it to use htmx instead:

    <form action="/contacts" method="get" class="tool-bar"> <1>
      <label for="search">Search Termlabel>
      <input id="search" type="search" name="q" 
        value="{{ request.args.get('q') or '' }}"
        placeholder="Search Contacts"/>
      <button hx-post="/contacts" hx-target="#main"> <2>
        Search
      button>
    form>

An htmx-powered search button

1.  When an htmx-powered element is withing an ancestor form tag, all input values within that form will be submitted for non-`GET` requests
    
2.  We have switched from an `input` of type `submit` to a `button` and added the `hx-post` attribute
    

Now, when a user clicks on this button, the value of the input with the id `search` will be included in the request. This is by virtue of the fact that there is a form tag enclosing both the button and the input: when an htmx-driven request is triggered, htmx will look up the DOM hierarchy for an enclosing form, and, if one is found, it will include all values from within that form. (This is sometimes referred to as “serializing” the form.)

You might have noticed that the button was switched from a `GET` request to a `POST` request. This is because, by default, htmx does _not_ include the closest enclosing form for `GET` requests, but it _does_ include the form for all other types of requests.

This may seem a little strange, but it avoids junking up URLs that are used within forms when dealing with history entries, which we will discuss in a bit. You can always include an enclosing form’s values with an element that uses a `GET` by using the `hx-include` attribute, which we will discuss next.

Note also that we could have added the `hx-post` attribute to the form, rather than to the button but that would create a somewhat awkward duplication of the search URL in the `action` and `hx-post` attributes. This can be avoided by using the `hx-boost` attribute, which we discuss in the next chapter.

## Including Inputs

While enclosing all the inputs you want included in a request within a form is the most common approach for serializing inputs for htmx requests, it isn’t always possible or desirable: form tags can have layout consequences and simply cannot be placed in some spots in HTML documents. A good example of the latter situation is in table row (`tr`) elements: the `form` tag is not a valid child or parent of table rows, so you can’t place a form within or around a row of data in a table.

To address this issue, htmx provides a mechanism for including input values in requests: the `hx-include` attribute. The `hx-include` attribute allows you to select input values that you wish to include in a request via CSS selectors.

Here is the above example reworked to include the input, dropping the form:

    <div id="main">
    
      <label for="search">Search Contacts:label>
      <input id="search" name="q"  type="search" 
        value="{{ request.args.get('q') or '' }}"
        placeholder="Search Contacts"/>
      <button hx-post="/contacts" hx-target="#main" hx-include="#search"> <1>
        Search
      button>
    
    div>

An htmx-powered search button with `hx-include`

1.  `hx-include` can be used to include values directly in a request.
    

The `hx-include` attribute takes a CSS selector value and allows you to specify exactly which values to send along with the request. This can be useful if it is difficult to colocate an element issuing a request with all the desired inputs.

It is also useful when you do, in fact, want to submit values with a `GET` request and overcome the default behavior of htmx.

### Relative CSS selectors

The `hx-include` attribute and, in fact, most attributes that take a CSS selector, also support _relative_ CSS selectors. These allow you to specify a CSS selector _relative_ to the element it is declared on. Here are some examples:

`closest`

Find the closest parent

element matching the given selector, e.g., `closest form`.

`next`

Find the next element (scanning

forward) matching the given selector, e.g., `next input`.

`previous`

Find the previous element

(scanning backwards) matching the given selector, e.g., `previous input`.

`find`

Find the next element within this

element matching the given selector, e.g., `find input`.

`this`

The current element.

Using relative CSS selectors often allows you to avoid generating ids for elements, since you can take advantage of their local structural layout instead.

## Inline Values

A final way to include values in htmx-driven requests is to use the `hx-vals` attribute, which allows you to include “static” values in the request. This can be useful if you have additional information that you want to include in requests, but you don’t want to have this information embedded in, for example, hidden inputs (which would be the standard mechanism for including additional, hidden information in HTML.)

Here is an example of `hx-vals`:

    <button hx-get="/contacts" hx-vals='{"state":"MT"}'> <1>
      Get The Contacts In Montana
    button>

An htmx-powered button with `hx-vals`

1.  `hx-vals`, a JSON value to include in the request.
    

The parameter `state` with the value `MT` will be included in the `GET` request, resulting in a path and parameters that looks like this: `/contacts?state=MT`. Note that we switched the `hx-vals` attribute to use single quotes around its value. This is because JSON strictly requires double quotes and, therefore, to avoid escaping we needed to use the single-quote form for the attribute value.

You can also prefix `hx-vals` with a `js:` and pass values evaluated at the time of the request, which can be useful for including things like a dynamically maintained variable, or value from a third party JavaScript library.

For example, if the `state` variable were maintained dynamically, via some JavaScript, and there existed a JavaScript function, `getCurrentState()`, that returned the currently selected state, it could be included dynamically in htmx requests like so:

    <button hx-get="/contacts"
      hx-vals='js:{"state":getCurrentState()}'> <1>
      Get The Contacts In The Selected State
    button>

A dynamic value

1.  With the `js:` prefix, this expression will evaluate at submit time.
    

These three mechanisms, using `form` tags, using the `hx-include` attribute and using the `hx-vals` attribute, allow you to include values in your hypermedia requests with htmx in a manner that should feel very familiar and in keeping with the spirit of HTML, while also giving you the flexibility to achieve what you want.