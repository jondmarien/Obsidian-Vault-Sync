## Same Origin Policy
Web content's origin is defined by the scheme (**protocol**), hostname (**domain**), and **port** of the URL used to access it.

- Two URLs may have the *same origin* if the **protocol**, **port**, and **host** are the same for both.
	- This may be referred as the *scheme/host/port*, or just a *tuple*
- Reduces attack vectors
- Restricts how a document or script loaded by one *origin* can interact with a resource from another origin

| URL                                             | Outcome     | Reason                |
| ----------------------------------------------- | ----------- | --------------------- |
| http://store.company.com/dir2/other.html        | Same Origin | Only the path differs |
| http://store.company.com/dir/inner/another.html | Same Origin | Only the path differs |
| https://store.company.com/page.html             | Failure     | Different protocol    |
| http://store.company.com:81/dir/page.html       | Failure     | Different port        |
| http://news.company.com/dir/page.html           | Failure     | Different host        |

## Cookies
- An **HTTP Cookie** (web cookie, browser cookie) is a small piece of data that a server sends back to a user's browser. The browser may store the cookie and send it back to the same server with later requests
- It remembers stateful information for the **stateless** HTTP protocol
- **Cookies** are mainly used for 3 things:
	- **Session Management**:
		- Logins, shopping carts, games scores, or anything else the server should remember
	- **Personalization**:
		- User preferences, themes, and other settings
	- **Tracking**:
		- Recording and analyzing user behaviour
- There are new technologies:
	- Web storage API
	- Indexed DB
- **HTTP**
	- *Stateless*
- **HTTPS**
	- *Stateful*
Setting a cookie: ![](Pasted%20image%2020240311131932.png)
![](Pasted%20image%2020240311131937.png)

## How to attack using Cookies
- **Secure**: A cookie with `secure` attribute is only sent to the server with an encrypted request over the HTTPS protocol
	- Helps to defeat **Man in the Middle** attack
- **HttpOnly**: A cookie with `HttpOnly` attribute is inaccessible to the JavaScriptDocument.cookie API
	- Helps to defeat **XSS** ![](Pasted%20image%2020240311132156.png)

## How to define where Cookies are sent
- **Domain**: The browser defaults the domain to the same **host** that set the cookie, *excluding subdomains*. If **Domain** is specified, then *the subdomains are always included*. 
	- Therefore, specifying **Domain** is less restrictive than omitting it
- For example, if you set **Domain=mozilla.org**, cookies are available for **developer.mozilla.org**

## Path Attribute
- The **Path** attribute indicates a *URL path* that must exist in the requested URL, in order to send the **Cookie** header. 
	- The `%x2F` character ("/") is considered a directory separator, and the subdirectories **must match** as well.
- For example, if you set **Path=/docs**, these requests paths match:
	- /docs
	- /docs/
	- /docs/Web/
	- /docs/Web/HTTP
- But these request paths don't:
	- /
	- /docsets/
	- /fr/docs

## Same site Attribute
- **SameSite** attribute lets servers specify whether or even when cookies are sent with cross-site requests
- This provides some protection against cross-site request forgery attacks (CSRF)
- It takes three possible values:
	- **Strict**
		- The browser only sends the cookie with requests from the cookie's origin site (i.e., bank withdrawal, that request must come from the bank's site, not some other site.)
	- **Lax**
		- Same as strict, but the browser ALSO sends the cookie when the user *navigates* to the cookie's origin site (i.e., following a link from an external site)
	- **None**
		- Specifies that cookies are sent on both originating and cross-site requests, but *only in secure contexts* (i.e., if **SameSite=None** then **Secure** must also be set. 
			- If **SameSite** is not set to anything, the cookie is treated as **Lax**) 
![](Pasted%20image%2020240311133829.png)



