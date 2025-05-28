# \_hyperscript

The final scripting technology we are going to look at is a bit further afield: [_hyperscript](https://hyperscript.org). The authors of this book initially created \_hyperscript as a sibling project to htmx. We felt that JavaScript wasn’t event-oriented enough, which made adding small scripting enhancements to htmx applications cumbersome.

While the previous two examples are JavaScript-oriented, \_hyperscript has a completely different syntax than JavaScript, based on an older language called HyperTalk. HyperTalk was the scripting language for a technology called HyperCard, an old hypermedia system available on early Macintosh Computers.

The most noticeable thing about \_hyperscript is that it resembles English prose more than it resembles other programming languages.

Like Alpine, \_hyperscript is a modern jQuery replacement. Also like Alpine, \_hyperscript allows you to write your scripting inline, in HTML.

Unlike Alpine, however, \_hyperscript is _not_ reactive. It instead focuses on making DOM manipulations in response to events easy to write and easy to read. It has built-in language constructs for many DOM operations, preventing you from needing to navigate the sometimes-verbose JavaScript DOM APIs.

We will give a small taste of what scripting in the \_hyperscript language is like, so you can pursue the language in more depth later if you find it interesting.

Like htmx and AlpineJS, \_hyperscript can be installed via a CDN or from npm (package name `hyperscript.org`):

    <script src="//unpkg.com/hyperscript.org">script>

Installing \_hyperscript via CDN

\_hyperscript uses the `_` (underscore) attribute for putting scripting on DOM elements. You may also use the `script` or `data-script` attributes, depending on your HTML validation needs.

Let’s look at how to implement the simple counter component we have been looking at using \_hyperscript. We will place an `output` element and a `button` inside of a `div`. To implement the counter, we will need to add a small bit of \_hyperscript to the button. On a click, the button should increment the text of the previous `output` tag.

As you’ll see, that last sentence is close to the actual \_hyperscript code:

    <div class="counter">
      <output>0output>
      <button _="on click
        increment the textContent of the previous <output/>"> <1>
        Increment
      button>
    div>

1.  The \_hyperscript code added inline to the button.
    

Let’s go through each component of this script:

*   `on click` is an event listener, telling the button to listen for a `click` event and then executing the remaining code.
    
*   `increment` is a “command” in \_hyperscript that “increments” things, similar to the `++` operator in JavaScript.
    
*   `the` doesn’t have any semantic meaning in \_hyperscript, but can be used to make scripts more readable.
    
*   `textContent of` is one form of _property access_ in \_hyperscript. You are probably familiar with the JavaScript syntax `a.b`, meaning “Get the property `b` on object `a`. \_hyperscript supports this syntax, but also supports the forms `b of a` and `a’s b`. Which one you use should depend on which one is most readable.
    
*   `previous` is an expression in \_hyperscript that finds the previous element in the DOM that matches some condition.
    
*   is a _query literal_, which is a CSS selector wrapped between `<` and `/>`.
    

In this code, the `previous` keyword (and the accompanying `next` keyword) is an example of how \_hyperscript makes DOM operations easier: there is no such native functionality to be found in the standard DOM API, and implementing this in VanillaJS is trickier than you might think!

So, you can see, \_hyperscript is very expressive, particularly when it comes to DOM manipulations. This makes it easier to embed scripts directly in HTML: since the scripting language is more powerful, scripts written in it tend to be shorter and easier to read.

**Natural Language Programming?**

Seasoned programmers may be suspicious of \_hyperscript: There have been many “natural language programming” (NLP) projects that target non-programmers and beginner programmers, assuming that being able to read code in their “natural language” will give them the ability to write it as well. This has led to some badly written and structured code and has failed to live up to the (often over the top) hype.

\_hyperscript is _not_ an NLP programming language. Yes, its syntax is inspired in many places by the speech patterns of web developers. But \_hyperscript’s readability is achieved not through complex heuristics or fuzzy NLP processing, but rather through judicious use of common parsing tricks, coupled with a culture of readability.

As you can see in the above example, with the use of a _query reference_,, \_hyperscript does not shy away from using DOM-specific, non-natural language when appropriate.

## \_hyperscript in Action: A Keyboard Shortcut

While the counter demo is a good way to compare various approaches to scripting, the rubber meets the road when you try to actually implement a useful feature with an approach. For \_hyperscript, let’s add a keyboard shortcut to Contact.app: when a user hits Alt+S in our app, we will focus the search field.

Since our keyboard shortcut focuses the search input, let’s put the code for it on that search input, satisfying locality.

Here is the original HTML for the search input:

    <input id="search" name="q" type="search" placeholder="Search Contacts">

We will add an event listener using the `on keydown` syntax, which will fire whenever a keydown occurs. Further, we can use an _event filter_ syntax in \_hyperscript using square brackets after the event. In the square brackets we can place a _filter expression_ that will filter out `keydown` events we aren’t interested in. In our case, we only want to consider events where the Alt key is held down and where the “S” key is being pressed. We can create a boolean expression that inspects the `altKey` property (to see if it is `true`) and the `code` property (to see if it is `"KeyS"`) of the event to achieve this.

So far our \_hyperscript looks like this:

    on keydown[altKey and code is 'KeyS'] ...
    

A start on our keyboard shortcut

Now, by default, \_hyperscript will listen for a given event _on the element where it is declared_. So, with the script we have, we would only get `keydown` events if the search box is already focused. That’s not what we want! We want to have this key work _globally_, no matter which element has focus.

Not a problem! We can listen for the `keyDown` event elsewhere by using a `from` clause in our event handler. In this case we want to listen for the `keyDown` from the window, and our code ends up looking, naturally, like this:

    on keydown[altKey and code is 'KeyS'] from window ...
    

Listening globally

Using the `from` clause, we can attach the listener to the window while, at the same time, keeping the code on the element it logically relates to.

Now that we’ve picked out the event we want to use to focus the search box, let’s implement the actual focusing by calling the standard `.focus()` method.

Here is the entire script, embedded in HTML:

    <input id="search" name="q" type="search" placeholder="Search Contacts"
      _="on keydown[altKey and code is 'KeyS'] from the window
        focus() me"> <1>

Our final script

1.  “me” refers to the element that the script is written on.
    

Given all the functionality, this is surprisingly terse, and, as an English-like programming language, pretty easy to read.

## Why a New Programming Language?

This is all well and good, but you may be thinking “An entirely new scripting language? That seems excessive.” And, at some level, you are right: JavaScript is a decent scripting language, is very well optimized and is widely understood in web development. On the other hand, by creating an entirely new front end scripting language, we had the freedom to address some problems that we saw generating ugly and verbose code in JavaScript:

Async transparency

In \_hyperscript, asynchronous functions (i.e., functions that return `Promise` instances) can be invoked _as if they were synchronous_. Changing a function from sync to async does not break any \_hyperscript code that calls it. This is achieved by checking for a Promise when evaluating any expression, and suspending the running script if one exists (only the current event handler is suspended and the main thread is not blocked). JavaScript, instead, requires either the explicit use of callbacks _or_ the use of explicit `async` annotations (which can’t be mixed with synchronous code).

Array property access

In \_hyperscript, accessing a property on an array (other than `length` or a number) will return an array of the values of property on each member of that array, making array property access act like a flat-map operation. jQuery has a similar feature, but only for its own data structure.

Native CSS Syntax

In \_hyperscript, you can use things like CSS class and ID literals, or CSS query literals, directly in the language, rather than needing to call out to a wordy DOM API, as you do in JavaScript.

Deep Event Support

Working with events in \_hyperscript is far more pleasant than working with them in JavaScript, with native support for responding to and sending events, as well as for common event-handling patterns such as “debouncing” or rate limiting events. \_hyperscript also provides declarative mechanisms for synchronizing events within a given element and across multiple elements.

Again we wish to stress that, in this example, we are not stepping outside the lines of a Hypermedia-Driven Application: we are only adding frontend, client-side functionality with our scripting. We are not creating and managing a large amount of state outside of the DOM itself, or communicating with the server in a non-hypermedia exchange.

Additionally, since \_hyperscript embeds so well in HTML, it keeps the focus _on the hypermedia_, rather than on the scripting logic.

It may not fit all scripting styles or needs, but \_hyperscript can provide an excellent scripting experience for Hypermedia-Driven Applications. It is a small and obscure programming language worth a look to understand what it is trying to achieve.