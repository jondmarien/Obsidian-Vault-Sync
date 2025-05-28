# Security Considerations

In general, htmx and hypermedia tends to be more secure than JavaScript heavy approaches to building web applications. This is because, by moving much of the processing to the back end, the hypermedia approach tends not to expose as much surface area of your system to end users for manipulation and shenanigans.

However, even with hypermedia, there are still situations that require care when doing development. Of particular concern are situations where user-generated content is shown to other users: a clever user might try to insert htmx code that tricks the other users into clicking on content that triggers actions they don’t want to take.

In general, all user-generated content should be escaped on the server-side, and most server-side rendering frameworks provide functionality for handling this situation. But there is always a risk that something slips through the cracks.

In order to help you sleep better at night, htmx provides the `hx-disable` attribute. When this attribute is placed on an element, all htmx attributes within that element will be ignored.

## Content Security Policies & Htmx

A Content Security Policy (CSP) is a browser technology that allows you to detect and prevent certain types of content injection-based attacks. A full discussion of CSPs is beyond the scope of this book, but we refer you to the [Mozilla Developer Network article](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) on the topic for more information.

A common feature to disable using a CSP is the `eval()` feature of JavaScript, which allows you to evaluate arbitrary JavaScript code from a string. This has proven to be a security issue and many teams have decided that it is not worth the risk to keep it enabled in their web applications.

Htmx does not make heavy use of `eval()` and, thus, a CSP with this restriction in place will be fine. The one feature that does rely on `eval()` is event filters, discussed above. If you decide to disable `eval()` for your web application, you will not be able to use the event filtering syntax.