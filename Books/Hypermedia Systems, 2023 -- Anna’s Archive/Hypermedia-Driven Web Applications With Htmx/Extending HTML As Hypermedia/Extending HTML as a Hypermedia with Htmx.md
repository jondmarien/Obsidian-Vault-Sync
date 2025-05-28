# Extending HTML as a Hypermedia with Htmx

These four opportunities present us a way to extend HTML well beyond its current abilities, but in a way that is _entirely within_ the hypermedia model of the web. The fundamentals of HTML, HTTP, the browser, and so on, won’t be changed dramatically. Rather, these generalizations of _existing functionality_ already found within HTML would simply let us accomplish _more_ using HTML.

Htmx is a JavaScript library that extends HTML in exactly this manner, and it will be the focus of the next few chapters of this book. Again, htmx is not the only JavaScript library that takes this hypermedia-oriented approach (other excellent examples are [Unpoly](https://unpoly.com) and [Hotwire](https://hotwire.dev)), but htmx is the purest in its pursuit of extending HTML as a hypermedia.

## Installing and Using Htmx

From a practical “getting started” perspective, htmx is a simple, dependency-free and stand-alone JavaScript library that can be added to a web application by simply including it via a `script` tag in your `head` element.

Because of this simple installation model, you can take advantage of tools like public CDNs to install the library.

Below is an example using the popular [unpkg](https://unpkg.com) Content Delivery Network (CDN) to install version `1.9.2` of the library. We use an integrity hash to ensure that the delivered JavaScript content matches what we expect. This SHA can be found on the htmx website.

We also mark the script as `crossorigin="anonymous"` so no credentials will be sent to the CDN.

    <head>
    <script src="https://unpkg.com/htmx.org@1.9.2"
      integrity="sha384-L6OqL9pRWyyFU3+/bjdSri+iIphTN/
        bvYyM37tICVyOJkWZLpP2vGn6VUEXgzg6h"
      crossorigin="anonymous">script>
    head>

Installing htmx

If you are used to modern JavaScript development, with complex build systems and large numbers of dependencies, it may be a pleasant surprise to find that that’s all it takes to install htmx.

This is in the spirit of the early web, when you could simply include a script tag and things would “just work.”

If you don’t want to use a CDN, you can download htmx to your local system and adjust the script tag to point to wherever you keep your static assets. Or, you may have a build system that automatically installs dependencies. In this case you can use the Node Package Manager (npm) name for the library: `htmx.org` and install it in the usual manner that your build system supports.

Once htmx has been installed, you can begin using it immediately.

## No JavaScript Required…​

And here we get to the interesting part of htmx: htmx does not require you, the user of htmx, to actually write any JavaScript.

Instead, you will use _attributes_ placed directly on elements in your HTML to drive more dynamic behavior. Htmx extends HTML as a hypermedia, and it is designed to make that extension feel as natural and consistent as possible with existing HTML concepts. Just as an anchor tag uses an `href` attribute to specify the URL to retrieve, and forms use an `action` attribute to specify the URL to submit the form to, htmx uses HTML _attributes_ to specify the URL that an HTTP request should be issued to.