# Configuring

There are a large number of configuration options available for htmx. Some examples of things you can configure are:

*   The default swap style
    
*   The default swap delay
    
*   The default timeout of AJAX requests
    

A full list of configuration options can be found in the config section of the [main htmx documentation](https://htmx.org/docs/#config).

Htmx is typically configured via a `meta` tag, found in the header of a page. The name of the meta tag should be `htmx-config`, and the content attribute should contain the configuration overrides, formatted as JSON. Here is an example:

    <meta name="htmx-config" content='{"defaultSwapStyle":"outerHTML"}'>

An htmx configuration via `meta` tag

In this case, we are overriding the default swap style from the usual `innerHTML` to `outerHTML`. This might be useful if you find yourself using `outerHTML` more frequently than `innerHTML` and want to avoid having to explicitly set that swap value throughout your application.

# HTML Notes: Semantic HTML

Telling people to “use semantic HTML” instead of “read the spec” has led to a lot of people guessing at the meaning of tags — “looks pretty semantic to me!” — instead of engaging with the spec.

> I think being asked to write _meaningful_ HTML better lights the path to realizing that it isn’t about what the text means to humans—​it’s about using tags for the purpose outlined in the specs to meet the needs of software like browsers, assistive technologies, and search engines.
> 
> ℄ [https://t-ravis.com/post/doc/semantic_the_8_letter_s-word/](https://t-ravis.com/post/doc/semantic_the_8_letter_s-word/)

We recommend talking about, and writing, _conformant_ HTML. (We can always bikeshed further). Use the elements to the full extent provided by the HTML specification, and let the software take from it whatever meaning they can.