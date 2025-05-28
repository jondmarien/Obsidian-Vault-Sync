# Targeting Other Elements

Now, given that htmx has issued a request and gotten back some HTML as a response, and that we are going to swap this content into the existing page (rather than replacing the entire page), the question becomes: where should this new content be placed?

It turns out that the default htmx behavior is to simply put the returned content inside the element that triggered the request. That’s _not_ a good thing in the case of our button: we will end up with a list of contacts awkwardly embedded within the button element. That will look pretty silly and is obviously not what we want.

Fortunately htmx provides another attribute, `hx-target` which can be used to specify exactly _where_ in the DOM the new content should be placed. The value of the `hx-target` attribute is a Cascading Style Sheet (CSS) _selector_ that allows you to specify the element to put the new hypermedia content into.

Let’s add a `div` tag that encloses the button with the id `main`. We will then target this `div` with the response:

    <div id="main"> <1>
    
      <button hx-get="/contacts" hx-target="#main"> <2>
        Get The Contacts
      button>
    
    div>

A simple htmx-powered button

1.  A `div` element that wraps the button.
    
2.  The `hx-target` attribute that specifies the target of the response.
    

We have added `hx-target="#main"` to our button, where `#main` is a CSS selector that says “The thing with the ID ‘main’.”

By using CSS selectors, htmx builds on top of familiar and standard HTML concepts. This keeps the additional conceptual load for working with htmx to a minimum.

Given this new configuration, what would the HTML on the client look like after a user clicks on this button and a response has been received and processed?

It would look something like this:

    <div id="main">
      <ul>
        <li><a href="mailto:joe@example.com">Joea>li>
        <li><a href="mailto:sarah@example.com">Saraha>li>
        <li><a href="mailto:fred@example.com">Freda>li>
      ul>
    div>

Our HTML after the htmx request finishes

The response HTML has been swapped into the `div`, replacing the button that triggered the request. Transclusion! And this has happened “in the background” via AJAX, without a clunky page refresh.