# Polling

That’s definitely progress, but we don’t exactly have the best progress indicator here: just some static text telling the user that the process is running.

We want to make the content update as the process makes progress and, ideally, show a progress bar indicating how far along it is. How can we do that in htmx using plain old hypermedia?

The technique we want to use here is called “polling”, where we issue a request on an interval and update the UI based on the new state of the server.

**Polling? Really?**

Polling has a bit of a bad rap, and it isn’t the sexiest technique in the world: today developers might look at a more advanced technique like WebSockets or Server Sent Events (SSE) to address this situation.

But, say what one will, polling _works_ and it is drop-dead simple. You need to be careful not to overwhelm your system with polling requests, but, with a bit of care, you can create a reliable, passively updated component in your UI using it.

Htmx offers two types of polling. The first is “fixed rate polling”, which uses a special `hx-trigger` syntax to indicate that something should be polled on a fixed interval.

Here is an example:

    <div hx-get="/messages" hx-trigger="every 3s"> <1>
    div>

Fixed interval polling

1.  Trigger a `GET` to `/messages` every three seconds.

This works great in situations when you want to poll indefinitely, for example if you want to constantly poll for new messages to display to the user. However, fixed rate polling isn’t ideal when you have a definite process after which you want to stop polling: it keeps polling forever, until the element it is on is removed from the DOM.

In our case, we have a definite process with an ending to it. So, it will be better to use the second polling technique, known as “load polling.” In load polling, we take advantage of the fact that htmx triggers a `load` event when content is loaded into the DOM. We can create a trigger on this `load` event, and add a bit of a delay so that the request doesn’t trigger immediately.

With this, we can conditionally render the `hx-trigger` on every request: when a process has completed we simply do not include the `load` trigger, and the load polling stops. This offers a nice and simple way to poll until a definite process finishes.

## Using Polling To Update The Archive UI

Let’s use load polling to update our UI as the archiver makes progress. To show the progress, let’s use a CSS-based progress bar, taking advantage of the `progress()` method which returns a number between 0 and 1 indicating how close the archive process is to completion.

Here is the snippet of HTML we will use:

    <div class="progress">
        <div class="progress-bar"
             style="width:{{ archiver.progress() * 100 }}%">div> <1>
    div>

A CSS-based progress bar

1.  The width of the inner element corresponds to the progress.

This CSS-based progress bar has two components: an outer `div` that provides the wire frame for the progress bar, and an inner `div` that is the actual progress bar indicator. We set the width of the inner progress bar to some percentage (note we need to multiply the `progress()` result by 100 to get a percentage) and that will make the progress indicator the appropriate width within the parent div.

**What About The Element?**

We are perhaps dipping our toes into the “div soup” here, using a `div` tag when there is a perfectly good HTML5 tag, the [progress](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/progress) element, that is designed specifically for showing, well, progress.

We decided not to use the `progress` element for this example because we want our progress bar to update smoothly, and we will need to use a CSS technique not available for the `progress` element to make that happen. That’s unfortunate, but sometimes we have to play with the cards we are dealt.

We will, however, use the proper [progress bar roles](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/roles/progressbar_role) to make our `div`\-based progress bar play well with assistive technologies.

Let’s update our progress bar to have the proper ARIA roles and values:

    <div class="progress">
      <div class="progress-bar"
        role="progressbar" <1>
        aria-valuenow="{{ archiver.progress() * 100 }}" <2>
        style="width:{{ archiver.progress() * 100 }}%">div>
    div>

A CSS-based progress bar

1.  This element will act as a progress bar
    
2.  The progress will be the percentage completeness of the archiver, with 100 indicating fully complete

Finally, for completeness, here is the CSS we’ll use for this progress bar:

    .progress {
        height: 20px;
        margin-bottom: 20px;
        overflow: hidden;
        background-color: #f5f5f5;
        border-radius: 4px;
        box-shadow: inset 0 1px 2px rgba(0,0,0,.1);
    }
    
    .progress-bar {
        float: left;
        width: 0%;
        height: 100%;
        font-size: 12px;
        line-height: 20px;
        color: #fff;
        text-align: center;
        background-color: #337ab7;
        box-shadow: inset 0 -1px 0 rgba(0,0,0,.15);
        transition: width .6s ease;
    }

The CSS for our progress bar

Which ends up rendering like this:

![](file7.png)

Our CSS-Based Progress Bar

### Adding The Progress Bar UI

Let’s add the code for our progress bar into our `archive_ui.html` template for the case when the archiver is running, and let’s update the copy to say “Creating Archive…​”:

    <div id="archive-ui" hx-target="this" hx-swap="outerHTML">
      {% if archiver.status() == "Waiting" %}
        <button hx-post="/contacts/archive">
          Download Contact Archive
        button>
      {% elif archiver.status() == "Running" %}
        <div>
          Creating Archive...
          <div class="progress"> <1>
            <div class="progress-bar" role="progressbar"
              aria-valuenow="{{ archiver.progress() * 100}}"
              style="width:{{ archiver.progress() * 100 }}%">div>
          div>
        div>
      {% endif %}
    div>

Adding the progress bar

1.  Our shiny new progress bar

Now when we click the “Download Contact Archive” button, we get the progress bar. But it still doesn’t update because we haven’t implemented load polling yet: it just sits there, at zero.

To get the progress bar updating dynamically, we’ll need to implement load polling using `hx-trigger`. We can add this to pretty much any element inside the conditional block for when the archiver is running, so let’s add it to that `div` that is wrapping around the “Creating Archive…​” text and the progress bar.

Let’s make it poll by issuing an HTTP `GET` to the same path as the `POST`: `/contacts/archive`.

    <div id="archive-ui" hx-target="this" hx-swap="outerHTML">
      {% if archiver.status() == "Waiting" %}
        <button hx-post="/contacts/archive">
          Download Contact Archive
        button>
      {% elif archiver.status() == "Running" %}
        <div hx-get="/contacts/archive" hx-trigger="load delay:500ms"> <1>
          Creating Archive...
          <div class="progress" >
            <div class="progress-bar" role="progressbar"
              aria-valuenow="{{ archiver.progress() * 100}}"
              style="width:{{ archiver.progress() * 100 }}%">div>
          div>
        div>
      {% endif %}
    div>

Implementing load polling

1.  Issue a `GET` to `/contacts/archive` 500 milliseconds after the content loads.

When this `GET` is issued to `/contacts/archive`, it is going to replace the `div` with the id `archive-ui`, not just itself. The `hx-target` attribute on the `div` with the id `archive-ui` is _inherited_ by all child elements within that `div`, so the children will all target that outermost `div` in the `archive_ui.html` file.

Now we need to handle the `GET` to `/contacts/archive` on the server. Thankfully, this is quite easy: all we want to do is re-render `archive_ui.html` with the archiver:

    @app.route("/contacts/archive", methods=["GET"]) <1>
    def archive_status():
        archiver = Archiver.get()
        return render_template("archive_ui.html", archiver=archiver) <2>

Handling progress updates

1.  handle `GET` to the `/contacts/archive` path
    
2.  just re-render the `archive_ui.html` template

Like so much else with hypermedia, the code is very readable and not complicated.

Now, when we click the “Download Contact Archive”, sure enough, we get a progress bar that updates every 500 milliseconds. As the result of the call to `archiver.progress()` incrementally updates from 0 to 1, the progress bar moves across the screen for us. Very cool!

## Downloading The Result

We have one final state to handle, the case when `archiver.status()` is set to “Complete”, and there is a JSON archive of the data ready to download. When the archiver is complete, we can get the local JSON file on the server from the archiver via the `archive_file()` call.

Let’s add another case to our if statement to handle the “Complete” state, and, when the archive job is complete, lets render a link to a new path, `/contacts/archive/file`, which will respond with the archived JSON file. Here is the new code:

    <div id="archive-ui" hx-target="this" hx-swap="outerHTML">
      {% if archiver.status() == "Waiting" %}
        <button hx-post="/contacts/archive">
          Download Contact Archive
        button>
      {% elif archiver.status() == "Running" %}
        <div hx-get="/contacts/archive" hx-trigger="load delay:500ms">
          Creating Archive...
          <div class="progress" >
            <div class="progress-bar" role="progressbar"
              aria-valuenow="{{ archiver.progress() * 100}}"
              style="width:{{ archiver.progress() * 100 }}%">div>
          div>
        div>
      {% elif archiver.status() == "Complete" %} <1>
        <a hx-boost="false" href="/contacts/archive/file">
          Archive Ready! Click here to download. ↓
        a> <2>
      {% endif %}
    div>

Rendering A Download Link When Archiving Completes

1.  If the status is “Complete”, render a download link.
    
2.  The link will issue a `GET` to `/contacts/archive/file`.

Note that the link has `hx-boost` set to `false`. It has this so that the link will not inherit the boost behavior that is present for other links and, thus, will not be issued via AJAX. We want this “normal” link behavior because an AJAX request cannot download a file directly, whereas a plain anchor tag can.

## Downloading The Completed Archive

The final step is to handle the `GET` request to `/contacts/archive/file`. We want to send the file that the archiver created down to the client. We are in luck: Flask has a mechanism for sending a file as a downloaded response, the `send_file()` method.

As you see in the code that follows, we pass three arguments to `send_file()`: the path to the archive file that the archiver created, the name of the file that we want the browser to create, and if we want it sent “as an attachment.” This last argument tells Flask to set the HTTP response header `Content-Disposition` to `attachment` with the given filename; this is what triggers the browser’s file-downloading behavior.

    @app.route("/contacts/archive/file", methods=["GET"])
    def archive_content():
        manager = Archiver.get()
        return send_file(
          manager.archive_file(), "archive.json", as_attachment=True) <1>

Sending A File To The Client

1.  Send the file to the client via Flask’s `send_file()` method.

Perfect. Now we have an archive UI that is very slick. You click the “Download Contacts Archive” button and a progress bar appears. When the progress bar reaches 100%, it disappears and a link to download the archive file appears. The user can then click on that link and download their archive.

We’re offering a user experience that is much more user-friendly than the common click-and-wait experience of many websites.