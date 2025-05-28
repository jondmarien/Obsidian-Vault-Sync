# Debugging

We are not ashamed to admit: we are big fans of events. They are the underlying technology of almost any interesting user interface, and are particularly useful in the DOM once they have been unlocked for general use in HTML. They let you build nicely decoupled software while often preserving the locality of behavior we like so much.

However, events are not perfect. One area where events can be particularly tricky to deal with is _debugging_: you often want to know why an event _isn’t_ happening. But where can you set a break point for something that _isn’t_ happening? The answer, as of right now, is: you can’t.

There are two techniques that can help in this regard, one provided by htmx, the other provided by Chrome, the browser by Google.

## Logging Htmx Events

The first technique, provided by htmx itself, is to call the `htmx.logAll()` method. When you do this, htmx will log all the internal events that occur as it goes about its business, loading up content, responding to events and so forth.

This can be overwhelming, but with judicious filtering can help you zero in on a problem. Here are what (a bit of) the logs look like when clicking on the “docs” link on [https://htmx.org](https://htmx.org), with `logAll()` enabled:

    htmx:configRequest
    
    Object { parameters: {}, unfilteredParameters: {}, headers: {…}, target: body, verb: "get", errors: [], withCredentials: false, timeout: 0, path: "/docs/", triggeringEvent: a
    , … }
    htmx.js:439:29
    htmx:beforeRequest
    
    Object { xhr: XMLHttpRequest, target: body, requestConfig: {…}, etc: {}, pathInfo: {…}, elt: a
     }
    htmx.js:439:29
    htmx:beforeSend
    
    Object { xhr: XMLHttpRequest, target: body, requestConfig: {…}, etc: {}, pathInfo: {…}, elt: a.htmx-request
     }
    htmx.js:439:29
    htmx:xhr:loadstart
    
    Object { lengthComputable: false, loaded: 0, total: 0, elt: a.htmx-request
     }
    htmx.js:439:29
    htmx:xhr:progress
    
    Object { lengthComputable: true, loaded: 4096, total: 19915, elt: a.htmx-request
     }
    htmx.js:439:29
    htmx:xhr:progress
    
    Object { lengthComputable: true, loaded: 19915, total: 19915, elt: a.htmx-request
     }
    htmx.js:439:29
    htmx:beforeOnLoad
    
    Object { xhr: XMLHttpRequest, target: body, requestConfig: {…}, etc: {}, pathInfo: {…}, elt: a.htmx-request
     }
    htmx.js:439:29
    htmx:beforeSwap
    
    

[[/docs/|Htmx logs]]

[[/docs/|Not exactly easy on the eyes, is it?But, if you take a deep breath and squint, you can see that it isn’t that bad: a series of htmx events, some of which we have seen before (there’s htmx:configRequest!), get logged to the console, along with the element they are triggered on.After a bit of reading and filtering, you will be able to make sense of the event stream, and it can help you debug htmx-related issues.]]

[[/docs/|]]

[[/docs/|Monitoring Events in ChromeThe preceding technique is useful if the problem is occurring somewhere within htmx, but what if htmx is never getting triggered at all? This comes up some times, like when, for example, you have accidentally typed an event name incorrectly somewhere.In cases like this you will need recourse to a tool available in the browser itself. Fortunately, the Chrome browser by Google provides a very useful function, monitorEvents(), that allows you to monitor all events that are triggered on an element.This feature is available only in the console, so you can’t use it in code on your page. But, if you are working with htmx in Chrome, and are curious why an event isn’t triggering on an element, you can open the developers console and type the following:]]

[[/docs/|]]

[[/docs/|]]

[[/docs/|]]`[[#cb122-1|]]monitorEvents(document.getElementById("some-element"));`

Htmx logs

This will then print _all_ the events that are triggered on the element with the id `some-element` to the console. This can be very useful for understanding exactly which events you want to respond to with htmx, or troubleshooting why an expected event isn’t occurring.

Using these two techniques will help you as you (infrequently, we hope) troubleshoot event-related issues when developing with htmx.