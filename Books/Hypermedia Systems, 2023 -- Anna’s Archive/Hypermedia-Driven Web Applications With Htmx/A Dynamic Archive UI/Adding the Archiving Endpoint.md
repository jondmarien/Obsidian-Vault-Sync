# Adding the Archiving Endpoint

Our next step is to handle the `POST` that our button is making. We want to get the `Archiver` for the current user and invoke the `run()` method on it. This will start the archive process running. Then we will render some new content indicating that the process is running.

To do that, we want to reuse the `archive_ui` template to handle rendering the archive UI for both states, when the archiver is “Waiting” and when it is “Running.” (We will handle the “Complete” state in a bit).

This is a very common pattern: we put all the different potential UIs for a given chunk of the user interface into a single template, and conditionally render the appropriate interface. By keeping everything in one file, it makes it much easier for other developers (or for us, if we come back after a while!) to understand exactly how the UI works on the client side.

Since we are going to conditionally render different user interfaces based on the state of the archiver, we will need to pass the archiver out to the template as a parameter. So, again: we need to invoke `run()` on the archiver in our controller and then pass the archiver along to the template, so it can render the UI appropriate for the current status of the archive process.

Here is what the code looks like:

    @app.route("/contacts/archive", methods=["POST"]) <1>
    def start_archive():
        archiver = Archiver.get() <2>
        archiver.run() <3>
        return render_template("archive_ui.html", archiver=archiver) <4>

Server-side code to start the archive process

1.  Handle `POST` to `/contacts/archive`.
    
2.  Look up the Archiver.
    
3.  Invoke the non-blocking `run()` method on it.
    
4.  Render the `archive_ui.html` template, passing in the archiver.