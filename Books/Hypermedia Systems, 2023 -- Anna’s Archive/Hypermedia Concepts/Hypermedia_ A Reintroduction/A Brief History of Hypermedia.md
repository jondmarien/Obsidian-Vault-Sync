# A Brief History of Hypermedia

Where did the idea of hypermedia come from?

While there were many precursors to the modern idea of hypertext and the more general hypermedia, many people point to the 1945 article _As We May Think_ written by Vannevar Bush in The Atlantic as a starting point for looking at what has become modern hypermedia.

In this article Bush described a device called a Memex, which, using a complex mechanical system of reels and microfilm, along with an encoding system, would allow users to jump between related frames of content. The Memex was never actually implemented, but it was an inspiration for later work on the idea of hypermedia.

The terms “hypertext” and “hypermedia” were coined in 1963 by Ted Nelson, who would go on to work on the _Hypertext Editing System_ at Brown University and who later created the _File Retrieval and Editing System (FRESS)_, a shockingly advanced hypermedia system for its time. (This was perhaps the first digital system to have a notion of “undo”.)

While Nelson was working on his ideas, Douglas Engelbart was busy at work at the Stanford Research Institute, explicitly attempting to make Vannevar Bush’s Memex a reality. In 1968, Englebart gave “The Mother of All Demos” in San Francisco, California.

Englebart demonstrated an unbelievable amount of technology:- Remote, collaborative text editing with his peers in Menlo Park- Video and audio chat- An integrated windowing system, with window resizing, etc- A recognizable hypertext, whereby clicking on underlined text navigated to new content.

Despite receiving a standing ovation from a shocked audience after his talk, it was decades before the technologies Englebart demonstrated became mainstream.

## Modern Implementation

In 1990, Tim Berners-Lee, working at CERN, published the first website. He had been working on the idea of hypertext for a decade and had finally, out of desperation at the fact it was so hard for researchers to share their research, found the right moment and institutional support to create the World Wide Web:

> Creating the web was really an act of desperation, because the situation without it was very difficult when I was working at CERN later. Most of the technology involved in the web, like the hypertext, like the Internet, multifont text objects, had all been designed already. I just had to put them together. It was a step of generalising, going to a higher level of abstraction, thinking about all the documentation systems out there as being possibly part of a larger imaginary documentation system.
> 
> ℄ Tim Berners-Lee, https://britishheritage.org/tim-berners-lee-the-world-wide-web

By 1994 his creation was taking off so quickly that Berners-Lee founded the W3C, a working group of companies and researchers tasked with improving the web. All standards created by the W3C were royalty-free and could be adopted and implemented by anyone, cementing the open, collaborative nature of the web.

In 2000, Roy Fielding, then at U.C. Irvine, published a seminal PhD dissertation on the web: “Architectural Styles and the Design of Network-based Software Architectures.” Fielding had been working on the open source Apache HTTP Server and his thesis was a description of what he felt was a _new and distinct networking architecture_ that had emerged in the early web. Fielding had worked on the initial HTTP specifications and, in the paper, defined the web’s hypermedia network model using the term _REpresentational State Transfer (REST)_.

Fielding’s work became a major touchstone for early web developers, giving them a language to discuss the new technical medium they were building applications in.

We will discuss Fielding’s key ideas in depth in Chapter 2, and try to correct the record with respect to REST, HATEOAS and hypermedia.