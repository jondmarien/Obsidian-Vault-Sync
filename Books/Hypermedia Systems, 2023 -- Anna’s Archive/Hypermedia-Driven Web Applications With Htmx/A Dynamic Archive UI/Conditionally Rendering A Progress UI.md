# Conditionally Rendering A Progress UI

Now let’s turn our attention to updating our archiving UI by setting `archive_ui.html` to conditionally render different content depending on the state of the archive process.

Recall that the archiver has a `status()` method. When we pass the archiver through as a variable to the template, we can consult this `status()` method to see the status of the archive process.

If the archiver has the status `Waiting`, we want to render the “Download Contact Archive” button. If the status is `Running`, we want to render a message indicating that progress is happening. Let’s update our template code to do just that:

    <div id="archive-ui" hx-target="this" hx-swap="outerHTML">
      {% if archiver.status() == "Waiting" %} <1>
        <button hx-post="/contacts/archive">
          Download Contact Archive
        button>
      {% elif archiver.status() == "Running" %} <2>
        Running... <3>
      {% endif %}
    div>

Adding conditional rendering

1.  Only render the archive button if the status is “Waiting.”
    
2.  Render different content when status is “Running.”
    
3.  For now, just some text saying the process is running.
    

OK, great, we have some conditional logic in our template view, and the server-side logic to support kicking off the archive process. We don’t have a progress bar yet, but we’ll get there! Let’s see how this works as it stands, and refresh the main page of our application…​

    UndefinedError
    jinja2.exceptions.UndefinedError: 'archiver' is undefined
    

Something Went Wrong

Ouch!

We get an error message right out of the box. Why? Ah, we are including the `archive_ui.html` in the `index.html` template, but now the `archive_ui.html` template expects the archiver to be passed through to it, so it can conditionally render the correct UI.

That’s an easy fix: we just need to pass the archiver through when we render the `index.html` template as well:

    @app.route("/contacts")
    def contacts():
        search = request.args.get("q")
        if search is not None:
            contacts_set = Contact.search(search)
            if request.headers.get('HX-Trigger') == 'search':
                return render_template("rows.html", contacts=contacts_set)
        else:
            contacts_set = Contact.all()
        return render_template("index.html",
          contacts=contacts_set, archiver=Archiver.get()) <1>

Including the archiver when we render index.html

1.  Pass through archiver to the main template
    

Now with that done, we can load up the page. And, sure enough, we can see the “Download Contact Archive” button.

When we click on it, the button is replaced with the content “Running…​”, and we can see in our development console on the server-side that the job is indeed getting kicked off properly.