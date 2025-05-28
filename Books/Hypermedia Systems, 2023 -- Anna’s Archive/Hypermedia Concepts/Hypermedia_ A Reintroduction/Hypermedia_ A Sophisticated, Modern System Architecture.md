# Hypermedia: A Sophisticated, Modern System Architecture

Hypermedia is often regarded as an old and antiquated technology in web development circles, useful perhaps for static websites but certainly not a realistic choice for modern, sophisticated web applications.

Seriously? Are we claiming that modern web applications can be built using it?

Yes, seriously.

Contrary to current popular opinion, hypermedia is an _innovative_ and _modern_ system architecture for building applications, in some ways _more modern_ than the prevailing Single Page Application approaches. In the remainder of this book we will reintroduce you to the core, practical concepts of hypermedia and then demonstrate exactly how you can take advantage of this system architecture in your own software.

In the coming chapters you will develop a firm understanding of all the benefits and techniques enabled by this approach. We hope that, in addition, you will also become as passionate about it as we are.

# HTML Notes:

Soup

The best-known kind of messy HTML is

soup.

When developers fall back on the generic

and elements instead of more meaningful tags, we either degrade the quality of our websites or create more work for ourselves — probably both.

For example, instead of adding a button using the dedicated element, a

element might have a `click` event listener added to it.

    <div class="bg-accent padding-4 rounded-2" onclick="doStuff()">
      Do stuff
    div>

There are two main issues with this button:

*   It’s not focusable — the Tab key won’t get you to it.
    
*   There’s no way for assistive tools to tell that it’s a button.
    

Yes, we can fix that by adding `role="button"` and `tabindex="0"`:

    <div class="bg-accent padding-4 rounded-2"
      role="button"
      tabindex="0"
      onclick="doStuff()">Do stuffdiv>

These are easy fixes, but they’re things you have to _remember_. It’s also not obvious from the HTML source that this is a button, making the source harder to read and the absence of these attributes harder to spot. The source code of pages with div soup is difficult to edit and debug.

To avoid div soup, become friendly with the HTML spec of available tags, and consider each tag another tool in your tool chest. There might be things there you don’t remember from before! (With the 113 elements currently defined in the spec, it’s more of a tool _shed_).

Of course, not every UI pattern has a designated HTML element. We often need to compose elements and augment them with attributes. Before you do, though, rummage through the HTML tool chest. Sometimes you might be surprised by how much is available.