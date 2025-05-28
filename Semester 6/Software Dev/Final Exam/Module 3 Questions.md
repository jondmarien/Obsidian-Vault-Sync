# Web Applications

1. Name three types of XSS.
	- **Dom-based XSS**
		- This is a malicious script that modifies the client-side Document Object Model (**DOM**). There is no server interaction.
	- **Reflected XSS**
		- This is a malicious script which is embedded in a URL or user input, which is **reflected** back by the server in response
	- **Stored XSS (Persistent)**
		- This is a malicious script that is permanently (**persistently**) stored on the server, which is later executed when victims view infected content 
2. What type of XSS does not need the malicious script to be sent to the server and reflected back?
	- **DOM-based XSS** does not need the server to respond. It manipulates the client-side code.
3.  What is the vulnerability of web applications in reflected XSS?
	- **Reflected XSS** has an easy vulnerability in the form of un-sanitized user input, which would allow an attacker to inject a script into the generated response page by the server.
4. Explain how the stored XSS works.
	- **Stored XSS** 
		- Core Mechanics:
			1. Injection
				- The attacker finds a way to inject their malicious JS code into a vulnerable website. Common injection points are, but no limited to:
					- **Comment Fields**
					- **Message Fields**
					- **Profile Fields**
					- **Any Input Field**
						- Any form field that does not validate or sanitize user data
			2. Storage
				- Once the malicious code is injected, it gets stored persistently on the website's server. Typically when this happens it is saved in a database in relation to that application on the website's server.
			3. Execution
				- Every time a user visits a page that loads the stored malicious code, their browser unknowingly retrieves and executes the malicious JS.
5.  Among the three types of XSS, which one can affect a large number of end users?
	-  Out of the 3 types of XSS (Persistence, Reflected, DOM-Based), **Persistence** has the potential to affect the largest number of end users.
		- This is because in Stored XSS (Persistent), the malicious script becomes a part of the websites content permanently, which is stored in a database or something similar. Every time a user loads an infected page, the script executes on the browser. Also, since the malicious script is embedded within the site's data, any who user who comes across this content will trigger the attack repeatedly. As you can tell, the impact would grow exponentially as more and more users visit the site. Finally, unlike in Reflected XSS, where the payload is part of a specific request, or like with DOM-based XSS, where it lives in the browser's DOM, removing **Stored XSS** requires you to know where the infected data is in the server's storage, and removing it -- which is harder than it sounds.
6. What is the main difference between CSRF and SSRF?
	- **CSRF vs SSRF**
		- **Definitions**:
			- A **CSRF** attack exploits the trust a website has in a user's browser to trick the user into unknowingly sending requests that change their account state (e.g., transfer funds, modify settings), often by embedding malicious actions within seemingly harmless links or forms on attacker-controlled websites.
			- An **SSRF** attack tricks a web server into making requests to unintended locations (often internal or otherwise inaccessible resources) by manipulating the target of a URL fetch or web request made by the server itself. This can lead to data exposure, unauthorized actions on internal systems, or attacks on other systems within the server's network.
		- **CSRF**
			- Exploits a user's _trust in a website_ to execute unintended actions on their behalf 
		- **SSRF**
			- Exploits a server's _trust in itself_ to make requests to internal resources or external systems
7. Which one can be more harmful: CSRF or SSRF? Why?
	-  **SSRF** is more harmful because it can access internal networks and systems that are typically inaccessible to external attackers, potentially leading to data breaches or server compromise.
8. Explain a setting for cookies to mitigate CSRF? Answer: Explain `SameSite`.
	- **SameSite** is an attribute that can be added to cookies to control when they are sent alongside requests to other websites.
		- **Strict**: Cookie is only sent if the request origin is the same site as the target 
		- **Lax**: Cookie is only sent for clicking on links that use a safe HTTP method (like GET, not POST)
		- **None**: Cookies are sent in all contexts, **BUT** only with the **Secure** attribute also set.
9. What is the usage of `Httponly` setting in cookies? How it can mitigate XSS?
	- The attribute **Httponly** prevents access to cookies by client-side JavaScript, aka the JavaScriptDocument.cookie API. This reduces the impact of XSS attacks that try to steal cookies.
10. What is the usage of `Secure` setting in cookies?
	- The attribute **Secure** ensures cookies are only transmitted over HTTPS connections, making sure the requests are encrypted.
11. What is the usage of `Domain` setting in Cookies?
	- The attribute **Domain** specifies the domains for which the cookie is valid, which limits its scope to specific subdomains. The browser defaults the domain to the same **host** that set the cookie, _excluding subdomains_. If **Domain** is specified, then _the subdomains are always included_. 
		- Therefore, specifying **Domain** is less restrictive than omitting it
			- For example, if you set **Domain=mozilla.org**, cookies are available for **developer.mozilla.org**
12. Which one of the following links has the same origin with 
`http://store.company.com/dir/page.html`
![](Pasted%20image%2020240409190948.png)
	- Out of the URLs in the list, the second link, `http://store.company.com/dir/inner/another.html` has the same origin as `http://store.company.com/dir/page.html`
		-  `http://store.company.com:81/dir/page.html` - Different port (81 instead of the standard 80).
		- `https://store.company.com/dir/page.html` - Different protocol (https instead of http).
		- `http://news.company.com/dir/page.html` - Different hostname ([invalid URL removed] instead of store.company.com).
	- The **same origin policy** is a critical security concept that restricts how documents or scripts loaded from one origin can interact with resources from another origin. An origin is defined by a combination of the protocol, port (if not standard), and hostname.
13. How attacker can use `localstorage` for DOM based XSS?
	- An attacker would inject malicious JS into a vulnerable page. This script then writes malicious data to the victim's `localstorage` . Later, when the victim visits the page again, the malicious script is retrieved from `localstorage` and executed.
14. Where does the session data get stored?
	- Sessions can be stored in a server-side database, in memory (like cache), or in files.
15. What type of attack you can see in the following code? How can you mitigate it?
![](Pasted%20image%2020240409191756.png)
- This looks to be as a **Stored XSS** attack, because if you look in the code above, it seems to be inserting user input directly inside a form, via `$name`. An attacker can inject malicious code into `$name` , which would then be embedded into the HTML and executed by the user's browser when the page loads. INESECURE FILE UPLOAD
16. What type of attack it is showing? Write the solutions to mitigate it.
![](Pasted%20image%2020240409191803.png)
- **CSRF attack**
	- The attacker sets up a malicious website ([www.somesite.com](http://www.somesite.com/)) that contains a malicious IMG tag pointing to the victim's bank website (fictitious.com).
		- When the victim visits the attacker's website, the browser automatically sends a request to the bank's website, including any valid session cookies the victim has.
			- The bank's web application validates the session, and then completes the transaction requested by the attacker (transferring money to the attacker's account).
17. What type of attack does not need end-user's intervention? CSRF or SSRF?
	- **CSRF** does NOT need the end-user's intervention to be successful. This is because CSRF exploits an already logged in account with some hidden link or form which exploits the victim's existing authenticated session 
18. Explain the type of vulnerability in the following code and how an attacker can take advantage of it.
![](Pasted%20image%2020240409191807.png)
- This appears to be a **String Injection Vulnerability**. This happens when user-supplied data is inserted into the string without any/proper validation or encoding. This can lead to an attacker supplying malicious code that can then be executed by the application
19. Discuss which one is more practical. input validation based on black-list or white-list?
	- **White-list** input validation is more practical because it defines a specific set of allowed characters, which reduces the attack surface.  
20. Explain click jacking?
	- How **Clickjacking** works is that an attacker tricks a user into click on invisible UI elements on a legitimate site, like mediafire, or zippyshare, which leads to unintended actions on a malicious site.
21. Write a solution for mitigating click jacking in a benign site.
	- Use the `X-Frame-Options` header with `deny` or `sameorigin` to prevent the site from being embedded in an `iframe`.
22. What does obscurity mean? Does it provide extra security for cryptography algorithms?
	- Security through Obscurity means to rely on secrecy of design or implementation for security. It's a flawed approach, as anything can be reverse engineered given enough time. **Cryptography algorithms should not rely on obscurity for security.**
23. Discuss which one of the following codes are secure against SQLi?
![](Pasted%20image%2020240409191816.png)
or
![](Pasted%20image%2020240409191822.png)
- The first code is more secure as it uses Parameterized Queries, and is more secure against SQLi. Parameterization ensures that user input is treated as data, not executable code. Whereas in the second image, the code is concatenating user input directly into the SQL query string. The attacker could inject malicious SQL into `userName` and it would not get validated, and end up getting executed as part of the SQL query.
24. Write a simple input for the following code to show it is vulnerable to SQLi? 
![](Pasted%20image%2020240409191827.png)
- The attacker could provide the following input for the `userName` parameter:
```sql
' OR '1'='1
```
- When constructed, the entire SQL query would now be:
```sql
SELECT * FROM items WHERE owner = '' OR '1'='1' AND itemname = '' AND ItemName.Text = ''
```
- This query will return all rows from the `items` table, and as the condition `'1'='1'` is always true, it will effectively bypass any intended restrictions on the data being retrieved.