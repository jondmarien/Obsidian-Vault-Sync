# HTTP Requests & Responses

We have just seen an advanced feature of HTTP responses supported by htmx, the `HX-Trigger` response header, but htmx supports quite a few more headers for both requests and responses. In chapter 4 we discussed the headers present in HTTP Requests. Here are some of the more important headers you can use to change htmx behavior with HTTP responses:

`HX-Location`

Causes a client-side redirection to a new location

`HX-Push-Url`

Pushes a new URL into the location bar

`HX-Refresh`

Refreshes the current page

`HX-Retarget`

Allows you to specify a new target to swap the response content into on the client side

You can find a reference for all requests and response headers in the [htmx documentation](https://htmx.org/reference/#headers).

## HTTP Response Codes

Even more important than response headers, in terms of information conveyed to the client, is the _HTTP Response Code_. We discussed HTTP Response Codes in Chapter 3. By and large htmx handles various response codes in the manner that you would expect: it swaps content for all 200-level response codes and does nothing for others. There are, however, two “special” 200-level response codes:

*   `204 No Content` - When htmx receives this response code, it will _not_ swap any content into the DOM (even if the response has a body)
    
*   `286` - When htmx receives this response code to a request that is polling, it will stop the polling
    

You can override the behavior of htmx with respect to response codes by, you guessed it, responding to an event! The `htmx:beforeSwap` event allows you to change the behavior of htmx with respect to various status codes.

Let’s say that, rather than doing nothing when a `404` occurred, you wanted to alert the user that an error had occurred. To do so, you want to invoke a JavaScript method, `showNotFoundError()`. Let’s add some code to use the `htmx:beforeSwap` event to make this happen:

    document.body.addEventListener('htmx:beforeSwap', evt => { <1>
      if (evt.detail.xhr.status === 404) { <2>
        showNotFoundError();
      }
    });

Showing a 404 dialog

1.  Hook into the `htmx:beforeSwap` event.
    
2.  If the response code is a `404`, show the user a dialog.
    

You can also use the `htmx:beforeSwap` event to configure if the response should be swapped into the DOM and what element the response should target. This gives you quite a bit of flexibility in choosing how you want to use HTTP Response codes in your application. Full documentation on the `htmx:beforeSwap` event can be found at [htmx.org](https://htmx.org/events/#htmx:beforeSwap).