# Why Use Hypermedia?

> The emerging norm for web development is to build a React single-page application, with server rendering. The two key elements of this architecture are something like:
> 
> 1.  The main UI is built & updated in JavaScript using React or something similar.
>     
> 2.  The backend is an API that that application makes requests against.
>     
> 
> This idea has really swept the internet. It started with a few major popular websites and has crept into corners like marketing sites and blogs.
> 
> ℄ Tom MacWright, [https://macwright.com/2020/05/10/spa-fatigue.html](https://macwright.com/2020/05/10/spa-fatigue.html)

The JavaScript-based Single Page Application approach has taken the web development world by storm, and if there was one single reason for its wild success it was this: The Single Page Application offers a far more interactive and immersive experience than the old, gronky, Web 1.0 hypermedia-based applications could. SPAs had the ability to smoothly update elements inline on a page without a dramatic reload of the entire document, they had the ability to use CSS transitions to create nice visual effects, and the ability to hook into arbitrary events like mouse movements.

All of these abilities give JavaScript-based applications a huge advantage in building sophisticated user experiences.

Given the popularity, power and success of this modern approach to building web applications, why on earth would you consider an older, clunkier and less popular approach like hypermedia?

## JavaScript Fatigue

We are glad you asked!

It turns out that the hypermedia architecture, even in its original Web 1.0 form, has a number of advantages when compared with the Single Page Application + JSON Data API approach. Three of the biggest are:

*   It is an extremely _simple_ approach to building web applications.- It is extremely tolerant of content and API changes. In fact, it thrives on them!- It leverages tried and true features of web browsers, such as caching.
    

The first two advantages, in particular, address major pain points in modern web development:

*   Single Page Application infrastructure has become extremely complex, often requiring an entire team to manage.- JSON API churn — constant changes made to JSON APIs to support application needs — has become a major pain point for many application teams.
    

The combination of these two problems, along with other issues such as JavaScript library churn, has led to a phenomenon known as “JavaScript Fatigue.” This refers to a general sense of exhaustion with all the hoops that are necessary to jump through to get anything done in modern-day web applications.

We believe that a hypermedia architecture can help cure JavaScript Fatigue for many developers and teams.

But if hypermedia is so great, and if it addresses so many of the problems that beset the web development industry, why was it set aside in the first place? After all, hypermedia was there first. Why didn’t web developers just stick with it?

There are two major reasons hypermedia hasn’t made a comeback in web development.

The first is this: the expressiveness of HTML _as a hypermedia_ hasn’t changed much, if at all, since HTML 2.0, which was released _in the mid 1990s_. Many new _features_ have been added to HTML, of course, but there haven’t been _any_ major new ways to interact with a server in HTML in almost three decades.

HTML developers still only have anchor tags and forms available as hypermedia controls, and those hypermedia controls can still only issue `GET` and `POST` requests.

This baffling lack of progress by HTML leads immediately to the second, and perhaps more practical reason that HTML-as-hypermedia has fallen on hard times: as the interactivity and expressiveness of HTML has remained frozen, the demands of web users have continued to increase, calling for more and more interactive web applications.

JavaScript-based applications coupled to data-oriented JSON APIs have stepped in as a way to provide these more sophisticated user interfaces. It was the _user experience_ that you could achieve in JavaScript, and that you couldn’t achieve in plain HTML, that drove the web development community to the JavaScript-based Single Page Application approach. The shift was not driven by any inherent superiority of the Single Page Application as a system architecture.

It didn’t have to be this way. There is nothing _intrinsic_ to the idea of hypermedia that prevents it from having a richer, more expressive interactivity model than vanilla HTML. Rather than moving away from a hypermedia-based approach, the industry could have demanded more interactivity from HTML.

Instead, building thick-client style applications within web browsers became the standard, in an understandable move to a more familiar model for building rich applications.

Not everyone set aside hypermedia, of course. There have been heroic efforts to continue to advance hypermedia outside of HTML, efforts like HyTime, VoiceXML, and HAL.

But HTML, the most widely used hypermedia in the world, stopped making progress as a hypermedia. The web development world moved on, solving the interactivity problems with HTML by adopting JavaScript-based SPAs and, mostly inadvertently, a completely different system architecture.