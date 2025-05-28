# Installing Htmx

The first thing we need to do is install htmx in our web application. We are going to do this by downloading the source and saving it locally in our application, so we aren’t dependent on any external systems. This is known as “vendoring” the library. We can grab the latest version of htmx by navigating our browser to `https://unpkg.com/htmx.org`, which will redirect us to the source of the latest version of the library.

We can save the content from this URL into the `static/js/htmx.js` file in our project.

You can, of course, use a more sophisticated JavaScript package manager such as Node Package Manager (NPM) or yarn to install htmx. You do this by referring to its package name, `htmx.org`, in the manner appropriate for your tool. However, htmx is very small (approximately 12kb when compressed and zipped) and is dependency free, so using it does not require an elaborate mechanism or build tool.

With htmx downloaded locally to our applications `/static/js` directory, we can now load it in to our application. We do this by adding the following `script` tag to the `head` tag in our `layout.html` file, which will make htmx available and active on every page in our application:

    <head>
      <script src="/js/htmx.js">script>
      ...
    head>

Installing htmx

Recall that the `layout.html` file is a _layout_ file included in most templates that wraps the content of those templates in common HTML, including a `head` element that we are using here to install htmx.

Believe it or not, that’s it! This simple script tag will make htmx’s functionality available across our entire application.