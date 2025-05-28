# Dismissing The Download UI

Some users may change their mind, and decide not to download the archive. They may never witness our glorious progress bar, but that’s OK. We’re going to give these users a button to dismiss the download link and return to the original export UI state.

To do this, we’ll add a button that issues a `DELETE` to the path `/contacts/archive`, indicating that the current archive can be removed or cleaned up.

We’ll add it after the download link, like so:

    <a hx-boost="false" href="/contacts/archive/file">
     Archive Ready! Click here to download. ↓
    a>
    <button hx-delete="/contacts/archive">Clear Downloadbutton> <1>

Clearing the download

1.  A simple button that issues a `DELETE` to `/contacts/archive`.
    

Now the user has a button that they can click on to dismiss the archive download link. But we will need to hook it up on the server side. As usual, this is pretty straightforward: we create a new handler for the `DELETE` HTTP Action, invoke the `reset()` method on the archiver, and re-render the `archive_ui.html` template.

Since this button is picking up the same `hx-target` and `hx-swap` configuration as everything else, it “just works.”

Here is the server-side code:

    @app.route("/contacts/archive", methods=["DELETE"])
    def reset_archive():
        archiver = Archiver.get()
        archiver.reset() <1>
        return render_template("archive_ui.html", archiver=archiver)

The handler to reset the download

1.  Call `reset()` on the archiver
    

This looks pretty similar to our other handlers, doesn’t it?

Sure does! That’s the idea!