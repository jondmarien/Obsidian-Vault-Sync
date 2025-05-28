# An Alternative UX: Auto-Download

While we prefer the current user experience for archiving contacts, there are other alternatives. Currently, a progress bar shows the progress of the process and, when it completes, the user is presented with a link to actually download the file. Another pattern that we see on the web is “auto-downloading”, where the file downloads immediately without the user needing to click a link.

We can add this functionality quite easily to our application with just a bit of scripting. We will discuss scripting in a Hypermedia-Driven Application in more depth in chapter 9, but, put briefly: scripting is perfectly acceptable in a HDA, as long as it doesn’t replace the core hypermedia mechanics of the application.

For our auto-download feature we will use [_hyperscript](https://hyperscript.org), our preferred scripting option. JavaScript would also work here, and would be nearly as simple; again, we’ll discuss scripting options in detail in Chapter 9.

All we need to do to implement the auto-download feature is the following: when the download link renders, automatically click on the link for the user.

The \_hyperscript code reads almost the same as the previous sentence (which is a major reason why we love hyperscript):

    <a hx-boost="false" href="/contacts/archive/file"
      _="on load click() me"> <1>
      Archive Downloading! Click here if the download does not start.
    a>

Auto-downloading

1.  A bit of \_hyperscript to make the file auto-download.
    

Crucially, the scripting here is simply _enhancing_ the existing hypermedia, rather than replacing it with a non-hypermedia request. This is hypermedia-friendly scripting, as we will cover in more depth in a bit.