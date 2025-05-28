# Updating Other Content

Above we saw how to use a server-triggered event, via the `HX-Trigger` HTTP response header, to update a piece of the DOM based on the response to another part of the DOM. This technique addresses the general problem that comes up in Hypermedia-Driven Applications: “How do I update other content?” After all, in normal HTTP requests, there is only one “target”, the entire screen, and, similarly, in htmx-based requests, there is only one target: either the explicit or implicit target of the element.

If you want to update other content in htmx, you have a few options:

## Expanding Your Selection

The first option, and the simplest, is to “expand the target.” That is, rather than simply replacing a small part of the screen, expand the target of your htmx-driven request until it is large enough to enclose all the elements that need to be updated on a screen. This has the tremendous advantage of being simple and reliable. The downside is that it may not provide the user experience that you want, and it may not play well with a particular server-side template layout. Regardless, we always recommend at least thinking about this approach first.

## Out of Band Swaps

A second option, a bit more complex, is to take advantage of “Out Of Band” content support in htmx. When htmx receives a response, it will inspect it for top-level content that includes the `hx-swap-oob` attribute. That content will be removed from the response, so it will not be swapped into the DOM in the normal manner. Instead, it will be swapped in for the content that it matches by id.

Let’s look at an example. Consider the situation we had earlier, where a contacts table needs to be updated if an integration pulls down any new contacts. Previously we solved this by using events and a server-triggered event via the `HX-Trigger` response header.

This time, we’ll use the `hx-swap-oob` attribute in the response to the `POST` to `/integrations/1`. The new contacts table content will “piggyback” on the response.

    <button hx-post="/integrations/1"> <1>
      Pull Contacts From Integration
    button>
    
      ...
    
    <table id="contacts-table"> <2>
      ...
    table>

The updated contacts table

1.  The button still issues a `POST` to `/integrations/1`.
    
2.  The table no longer listens for an event, but it now has an id.
    

Next, the response to the `POST` to `/integrations/1` will include the content that needs to be swapped into the button, per the usual htmx mechanism. But it will also include a new, updated version of the contacts table, which will be marked as `hx-swap-oob="true"`. This content will be removed from the response so that it is not inserted into the button. Instead, it is swapped into the DOM in place of the existing table since it has a matching id.

    HTTP/1.1 200 OK
    Content-Type: text/html; charset=utf-8
    ...
    
    Pull Contacts From Integration <1>
    
     <2>
      ...
    
    

A response with out-of-band content

1.  This content will be placed in the button.
    
2.  This content will be removed from the response and swapped by id.
    

Using this piggybacking technique, you can update content wherever needed on a page. The `hx-swap-oob` attribute supports other additional features, all of which are [documented](https://htmx.org/attributes/hx-swap-oob/).

Depending on how exactly your server-side templating technology works, and what level of interactivity your application requires, out of band swapping can be a powerful mechanism for content updates.

## Events

Finally, the most complex mechanism for updating content is the one we saw back in the events section: using server-triggered events to update elements. This approach can be very clean, but also requires a deeper conceptual knowledge of HTML and events, and a commitment to the event-driven approach. While we like this style of development, it isn’t for everyone. We typically recommend this pattern only if the htmx philosophy of event-driven hypermedia really speaks to you.

If it _does_ speak to you, however, we say: go for it. We’ve created some very complex and flexible user interfaces using this approach, and we are quite fond of it.

## Being Pragmatic

All of these approaches to the “Updating Other Content” problem will work, and will often work well. However, there may come a point where it would just be simpler to use a different approach for your UI, like the reactive one. As much as we like the hypermedia approach, the reality is that there are some UX patterns that simply cannot be implemented easily using it. The canonical example of this sort of pattern, which we have mentioned before, is something like a live online spreadsheet: it is simply too complex a user interface, with too many interdependencies, to be done well via exchanges of hypermedia with a server.

In cases like this, and any time you feel like an htmx-based solution is proving to be more complex than another approach might be, we recommend that you consider a different technology. Be pragmatic, and use the right tool for the job. You can always use htmx for the parts of your application that aren’t as complex and don’t need the full complexity of a reactive framework, and save that complexity budget for the parts that do.

We encourage you to learn many different web technologies, with an eye to the strengths and weaknesses of each one. This will give you a deep tool chest to reach into when problems present themselves. Our experience is that, with htmx, hypermedia is a tool you can reach for frequently.