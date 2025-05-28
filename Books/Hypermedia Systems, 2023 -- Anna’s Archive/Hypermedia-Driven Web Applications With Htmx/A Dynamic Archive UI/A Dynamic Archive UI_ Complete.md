# A Dynamic Archive UI: Complete

In this chapter we’ve managed to create a dynamic UI for our contact archive functionality, with a progress bar and auto-downloading, and we’ve done nearly all of it — with the exception of a small bit of scripting for auto-download — in pure hypermedia. It took about 16 lines of front end code and 16 lines of backend code to build the whole thing.

HTML, with a bit of help from a hypermedia-oriented JavaScript library such as htmx, can in fact be extremely powerful and expressive.

# HTML Notes: Markdown soup

_Markdown soup_ is the lesser known sibling of

soup. This is the result of web developers limiting themselves to the set of elements that the Markdown language provides shorthand for, even when these elements are incorrect. More seriously, it’s important to be aware of the full power of our tools, including HTML. Consider the following example of an IEEE-style citation:

    [1] C.H. Gross, A. Stepinski, and D. Akşimşek, <1>
      _Hypermedia Systems_, <2>
      Bozeman, MT, USA: Big Sky Software.
      Available: 

1.  The reference number is written in brackets.
    
2.  Underscores around the book title creates an _element._
    

_

Here, _is used because it’s the only Markdown element that is presented in italics by default. This indicates that the book title is being stressed, but the purpose is to mark it as the title of a work. HTML has the element that’s intended for this exact purpose._

_

Furthermore, even though this is a numbered list perfect for the

element, which Markdown supports, plain text is used for the reference numbers instead. Why could this be? The IEEE citation style requires that these numbers are presented in square brackets. This could be achieved on an

with CSS, but Markdown doesn’t have a way to add a class to elements meaning the square brackets would apply to all ordered lists.

Don’t shy away from using embedded HTML in Markdown. For larger sites, also consider Markdown extensions.

    {.ieee-reference-list} <1>
    1. C.H. Gross, A. Stepinski, and D. Akşimşek, <2>
      <cite>Hypermedia Systemscite>, <3>
      Bozeman, MT, USA: Big Sky Software.
      Available: 

1.  Many Markdown dialects let us add ids, classes and attributes using curly braces.
    
2.  We can now use the
    
    element, and create the brackets in CSS.
    
    2.  We use to mark the title of the work being cited (not the whole citation!)
        
    
    You can also use custom processors to produce extra-detailed HTML instead of writing it by hand:
    
        {% reference_list %} <1>
        [hypers2023]: <2>
          C.H. Gross, A. Stepinski, and D. Akşimşek, _Hypermedia Systems_,
          Bozeman, MT, USA: Big Sky Software, 2023.
          Available: 
        {% end %}
    
    1.  `reference_list` is a macro that will transform the plain text to highly-detailed HTML.
        
    2.  A processor can also resolve identifiers, so we don’t have to manually keep the reference list in order and the in-text citations in sync.
        





__