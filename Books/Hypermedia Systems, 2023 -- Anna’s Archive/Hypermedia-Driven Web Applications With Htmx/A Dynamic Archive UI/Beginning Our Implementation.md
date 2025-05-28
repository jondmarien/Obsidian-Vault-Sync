# Beginning Our Implementation

We now have everything we need to begin implementing our UI: a reasonable outline of what it is going to look like, and the domain logic to support it.

So, to start, note that this UI is largely self-contained: we want to replace the button with the download progress bar, and then the progress bar with a link to download the results of the completed archive process.

The fact that our archive user interface is all going to be within a specific part of the UI is a strong hint that we will want to create a new template to handle it. Let’s call this template `archive_ui.html`.

Also note that we are going to want to replace the entire download UI in multiple cases:

*   When we start the download, we will want to replace the button with a progress bar.
    
*   As the archive process proceeds, we will want to replace/update the progress bar.
    
*   When the archive process completes, we will want to replace the progress bar with a download link.
    

To update the UI in this way, we need to set a good target for the updates. So, let’s wrap the entire UI in a `div` tag, and then use that `div` as the target for all our operations.

Here is the start of the template for our new archive user interface:

    <div id="archive-ui"
      hx-target="this" <1>
      hx-swap="outerHTML"> <2>
    div>

Our initial archive UI template

1.  This div will be the target for all elements within it.
    
2.  Replace the entire div every time using `outerHTML`.
    

Next, lets add the “Download Contact Archive” button to the `div` that will kick off the archive-then-download process. We’ll use a `POST` to the path `/contacts/archive` to trigger the start of the archiving process:

    <div id="archive-ui" hx-target="this" hx-swap="outerHTML">
      <button hx-post="/contacts/archive"> <1>
        Download Contact Archive
      button>
    div>

Adding the archive button

1.  This button will issue a `POST` to `/contacts/archive`.
    

Finally, let’s include this new template in our main `index.html` template, above the contacts table:

    {% block content %}
      {% include 'archive_ui.html' %} <1>
    
      <form action="/contacts" method="get" class="tool-bar">

Our initial archive UI template

1.  This template will now be included in the main template.
    

With that done, we now have a button showing up in our web application to get the download going. Since the enclosing `div` has an `hx-target="this"` on it, the button will inherit that target and replace that enclosing `div` with whatever HTML comes back from the `POST` to `/contacts/archive`.