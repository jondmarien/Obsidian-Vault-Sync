# Htmx: HTML eXtended

And hey, check it out! With `hx-trigger` we have addressed the final opportunity for improvement of HTML that we outlined at the start of this chapter:

*   Opportunity 2: We can use _any_ event to trigger an HTTP request.
    

That’s a grand total of eight, count ‘em, _eight_ attributes that all fall squarely within the same conceptual model as normal HTML and that, by extending HTML as a hypermedia, open up a whole new world of user interaction possibilities within it.

Here is a table summarizing those opportunities and which htmx attributes address them:

Any element should be able to make HTTP requests

`hx-get`, `hx-post`, `hx-put`, `hx-patch`, `hx-delete`

Any event should be able to trigger an HTTP request

`hx-trigger`

Any HTTP Action should be available

`hx-put`, `hx-patch`, `hx-delete`

Any place on the page should be replaceable (transclusion)

`hx-target`, `hx-swap`