# Scripting Tools for the Web

The primary scripting language for the web is, of course, JavaScript, which is ubiquitous in web development today.

A bit of interesting internet lore, however, is that JavaScript was not always the only built-in option. As the quote from Roy Fielding at the start of this chapter hints, “applets” written in other languages such as Java were considered to be part of the scripting infrastructure of the web. In addition, there was a time period when Internet Explorer supported VBScript, a scripting language based on Visual Basic.

Today, we have a variety of _transcompilers_ (often shortened to _transpilers_) that convert many languages to JavaScript, such as TypeScript, Dart, Kotlin, ClojureScript, F# and more. There is also the WebAssembly (WASM) bytecode format, which is supported as a compilation target for C, Rust, and the WASM-first language AssemblyScript.

However, most of these options are not geared towards a hypermedia-friendly style of scripting. Compile-to-JS languages are often paired with SPA-oriented libraries (Dart and AngularDart, ClojureScript and Reagent, F# and Elm), and WASM is currently mainly geared toward linking to C/C++ libraries from JavaScript.

We will instead focus on three client-side scripting technologies that _are_ hypermedia-friendly:

*   VanillaJS, that is, using JavaScript without depending on any framework.
    
*   Alpine.js, a JavaScript library for adding behavior directly in HTML.
    
*   \_hyperscript, a non-JavaScript scripting language created alongside htmx. Like AlpineJS, \_hyperscript is usually embedded in HTML.
    

Let’s take a quick look at each of these scripting options, so we know what we are dealing with.

Note that, as with CSS, we are going to show you just enough of each of these options to give a flavor of how they work and, we hope, spark your interest in looking into any of them more extensively.