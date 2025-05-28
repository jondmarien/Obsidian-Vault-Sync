# Hypermedia: A New Generation

Hypermedia isn’t a frequent topic of discussion these days. Even many older programmers who grew up with the web in the late 1990s and early 2000s haven’t thought much about these ideas in years. Many younger web developers have grown up knowing nothing but Single Page Applications and the frameworks that are used to build them.

In particular, many young web developers began their careers by building React.js applications that interact with a Node server using a JSON API; they may never have learned about hypermedia as a system at all.

This is a tragedy, and, frankly, a failure on the part of the thought leaders in the web development community to properly communicate and advocate for the hypermedia approach.

Hypermedia was a great idea! It still is!

By the end of this book, you will have the tools and the _language_ to put this great idea to work in your own applications. And, further, you will be able to bring the ideas and concepts of hypermedia systems to the broader web development community.

Hypermedia can compete, hypermedia _can win_, hypermedia _has won_ as an architectural choice against the Single Page Application approach, but _only_ if smart people (like you) learn about it, build with it and then tell the world about it.

> Remember the message? “The future is not set. There is no fate but what we make for ourselves.”
> 
> ℄ Kyle Reese, Terminator 2: Judgement Day

# HTML Notes: Hypermedia In Practice

Clearly, HTML plays a central role in the story we tell here. At the end of each chapter we will share what we have learned about writing HTML for hypermedia-driven web applications.

To start, remember that our web applications are not islands. We’re writing HTML not just for a particular application, but also to play along with other members of the web. When we write with the hypermedia _system_ in mind, we’re better able to tap the range of abilities available to the web.

HTML is hypermedia-friendly when it is written for the full range of constituents of the hypermedia system. It conveys the state of an application to people viewing our sites with a browser, as well as to people listening to screen readers that read sites aloud. It conveys the aims of our sites to search engines that scrape sites programmatically. It also conveys its behavior as clearly as possible to other developers.

No, we can’t fix every problem with good HTML. The mantra that HTML is “accessible by default” is misleading. We would miss out on important opportunities if we shunned other technologies like JavaScript. And we still need to test, a lot, everywhere, to ensure things work as expected.

But good HTML lets browsers do a _lot_ of work for us.