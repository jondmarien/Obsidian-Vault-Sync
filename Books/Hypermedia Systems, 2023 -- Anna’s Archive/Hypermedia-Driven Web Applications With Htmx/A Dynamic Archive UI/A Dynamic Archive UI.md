# A Dynamic Archive UI

Contact.app has come a long way from a traditional web 1.0-style web application: we’ve added active search, bulk delete, some nice animations, and a slew of other features. We have reached a level of interactivity that most web developers would assume requires some sort of Single-Page Application JavaScript framework, but we’ve done it using htmx-powered hypermedia instead.

Let’s look at how we can add a final significant feature to Contact.app: downloading an archive of all the contacts.

From a hypermedia perspective, downloading a file isn’t exactly rocket science: using the HTTP `Content-Disposition` response header, we can easily tell the browser to download and save a file to the local computer.

However, let’s make this problem more interesting: let’s add in the fact that the export can take a bit of time, from five to ten seconds, or sometimes even longer, to complete.

This means that if we implemented the download as a “normal” HTTP request, driven by a link or a button, the user might sit with very little visual feedback, wondering if the download is actually happening, while the export is being completed. They might even give up in frustration and click the download hypermedia control again, causing a _second_ archive request. Not good.

This turns out to be a classic problem in web app development. When faced with potentially long-running process like this, we ultimately have two options:

*   When the user triggers the action, block until it is complete and then respond with the result.
    
*   Begin the action and return immediately, showing some sort of UI indicating that things are in progress.

Blocking and waiting for the action to complete is certainly the simpler way to handle it, but it can be a bad user experience, especially if the action takes a while to complete. If you’ve ever clicked on something in a web 1.0-style application and then had to sit there for what seems like an eternity before anything happens, you’ve seen the practical results of this choice.

The second option, starting the action asynchronously (say, by creating a thread, or submitting it to a job runner system) is much nicer from a user experience perspective: the server can respond immediately and the user doesn’t need to sit there wondering what’s going on.

But the question is, what do you respond _with_? The job probably isn’t complete yet, so you can’t provide a link to the results.

We have seen a few different “simple” approaches in this scenario in various web applications:

*   Let the user know that the process has started and that they will be emailed a link to the completed process results when it is finished.
    
*   Let the user know that the process has started and recommend that they should manually refresh the page to see the status of the process.
    
*   Let the user know that the process has started and automatically refresh the page every few seconds using some JavaScript.

All of these will work, but none of them is a great user experience.

What we’d _really_ like in this scenario is something more like what you see when, for example, you download a large file via the browser: a nice progress bar indicating where in the process you are, and, when the process is complete, a link to click immediately to view the result of the process.

This may sound like something impossible to implement with hypermedia, and, to be honest, we’ll need to push htmx pretty hard to make this all work, but, when it is done, it won’t be _that_ much code, and we will be able to achieve the user experience we want for this archiving feature.