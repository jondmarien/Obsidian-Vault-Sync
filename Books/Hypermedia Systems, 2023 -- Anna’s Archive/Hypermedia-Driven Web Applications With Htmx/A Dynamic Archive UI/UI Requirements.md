# UI Requirements

Before we dive into the implementation, let’s discuss in broad terms what our new UI should look like: we want a button in the application labeled “Download Contact Archive.” When a user clicks on that button, we want to replace that button with a UI that shows the progress of the archiving process, ideally with a progress bar. As the archive job makes progress, we want to move the progress bar along towards completion. Then, when the archive job is done, we want to show a link to the user to download the contact archive file.

In order to actually do the archiving, we are going to use a python class, `Archiver`, that implements all the functionality that we need. As with the `Contact` class, we aren’t going to go into the implementation details of `Archiver`, because that’s beyond the scope of this book. For now you just need to know is that it provides all the server-side behavior necessary to start a contact archive process and get the results when that process is done.

`Archiver` gives us the following methods to work with:

*   `status()` - A string representing the status of the download, either `Waiting`, `Running` or `Complete`
    
*   `progress()` - A number between 0 and 1, indicating how much progress the archive job has made
    
*   `run()` - Starts a new archive job (if the current status is `Waiting`)
    
*   `reset()` - Cancels the current archive job, if any, and resets to the “Waiting” state
    
*   `archive_file()` - The path to the archive file that has been created on the server, so we can send it to the client
    
*   `get()` - A class method that lets us get the Archiver for the current user
    

A fairly uncomplicated API.

The only somewhat tricky aspect to the whole API is that the `run()` method is _non-blocking_. This means that it does not _immediately_ create the archive file, but rather it starts a background job (as a thread) to do the actual archiving. This can be confusing if you aren’t used to multithreading in code: you might be expecting the `run()` method to “block”, that is, to actually execute the entire export and only return when it is finished. But, if it did that, we wouldn’t be able to start the archive process and immediately render our desired archive progress UI.