# Pragmatic Scripting

> In case of conflict, consider users over authors over implementors over specifiers over theoretical purity.
> 
> ℄ W3C, HTML Design Principles § 3.2 Priority of Constituencies

We have looked at several tools and techniques for scripting in a Hypermedia-Driven Application. How should you pick between them? The sad truth is that there will never be a single, always correct answer to this question.

Are you committed to vanilla JavaScript-only, perhaps due to company policy? Well, you can use vanilla JavaScript effectively to script your Hypermedia-Driven Application.

Do you have more leeway and like the look of Alpine.js? That’s a great way to add more structured, localized JavaScript to your application, and offers some nice reactive features as well.

Are you a bit more bold in your technical choices? Maybe \_hyperscript is worth a look. (We certainly think so.)

Sometimes you might even consider picking two (or more) of these approaches within an application. Each has its own strengths and weaknesses, and all of them are relatively small and self-contained, so picking the right tool for the job at hand might be the best approach.

In general, we encourage a _pragmatic_ approach to scripting: whatever feels right is probably right (or, at least, right _enough_) for you. Rather than being concerned about which particular approach is taken for your scripting, we would focus on these more general concerns:

*   Avoid communicating with the server via JSON data APIs.
    
*   Avoid storing large amounts of state outside of the DOM.
    
*   Favor using events, rather than hard-coded callbacks or method calls.
    

And even on these topics, sometimes a web developer has to do what a web developer has to do. If the perfect widget for your application exists but uses a JSON data API? That’s OK.

Just don’t make it a habit.

# HTML Notes: HTML is for Applications

A prevalent meme among developers suggests that HTML was designed for “documents” and is unsuitable for “applications.” In reality, hypermedia is not only a sophisticated, modern architecture for applications, but it can allow us to do away with this artificial app/document split for good.

> When I say Hypertext, I mean the simultaneous presentation of information and controls such that the information becomes the affordance through which the user obtains choices and selects actions.
> 
> ℄ Roy Fielding, [A little REST and Relaxation](https://www.slideshare.net/royfielding/a-little-rest-and-relaxation)

HTML allows documents to contain rich multimedia including images, audio, video, JavaScript programs, vector graphics and (with some help) 3D environments. More importantly, however, it allows interactive controls to be embedded within these documents, allowing the information itself to be the app through which it is accessed.

Consider: Is it not mind-boggling that a single application — which works on all types of computers and OSs — can let you read news, place video calls, compose documents, enter virtual worlds, and do almost any other everyday computing task?

Unfortunately, it is the interactive capabilities of HTML that is its least developed aspect. For reasons unknown to us, while HTML made it to version 5 and became a Living Standard, accreting many game-changing features on the way, the data interactions in it are still mainly restricted to links and forms. It’s up to developers to extend HTML, and we want to do so in a way that doesn’t abstract over its simplicity with an imitation of classical “native” toolkits.

> *   Software was not supposed to use native toolkits
>     
> *   Years of windows UI libraries yet no real-world use found for going lower level than the Web
>     
> *   Wanted a window anyway for a laugh? We had a tool for that: It was called “Electron”
>     
> *   “yes I would love to write 4 different copies of the same UI” - Statements dreamed up by the Utterly Deranged
>     
> 
> ℄ Leah Clark, @leah@tilde.zone