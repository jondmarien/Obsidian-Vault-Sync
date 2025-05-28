# How the Web Works
![](Pasted%20image%2020240318131954.png)

# Cross-Site Request Forgery (CSRF)
## About CSRF
- Discovered in 2001
- Incredibly easy to exploit
- CSRF attacks are known as:
	- XSRF
	- "Sea Surf"
	- Session Riding
	- Cross-Site Reference Forgery
	- Hostile Linking
- Can also be referred to as a One-Click attack
## What is CSRF?
- An attack that forces a user's browser to send requests they didn't indent to make
	- To a website that the user is currently authenticated to
	- To trigger an action without the user's consent
		- Transfer of money, change of password, etc…
- Typically requires an attacker to have prior access to and knowledge of the vulnerable application
### Invisible IMG Tags (GET)
```HTML
<img src[=http://fictitiousbank.com/transfer?](http://fictitiousbank.com/transfer) fromaccount=Bob&toaccount=MrHacker&Amount=1000 width=“1” height=“1”>
```
```HTML
<a href="http://bank.com/transfer.do? fromaccount=Bob&toaccount=MrHacker&Amount=1000 ">View my Pictures!</a>
```
### Form (POST)
```HTML
<form name=“badform” method=“post” acti[on=“h](http://fictitiousbank.com/transfer)ttp[://fictitiousbank.com/transfer>](http://fictitiousbank.com/transfer)

<input type=“hidden” name=“fromaccount” value=“Bob”>

<input type=“hidden” name=“toaccount” value=“MrHacker”>

<input type=“hidden” name=“Amount” value=“1000”>

</form>

<script>document.badform.submit()</script>
```
- Executing a POST-based CSRF requires JS
```JS
<body onload="document.forms[0].submit()"> <form...
```
#### Anatomy of a CSRF Attack
![](Pasted%20image%2020240318132118.png)
#### Example CSRF
![](Pasted%20image%2020240318133738.png)
#### Real World Example - Gmail Filters
- Email hijacking technique using Gmail Filters
	1. User logs into Gmail
	2. User visits a site hosting Gmail CSRF attack code
	3. User submits request to Gmail, creating a filter to forward all mail to hacker
	[Real World Example]([http://www.davidairey.com/google-gmail-security-](http://www.davidairey.com/google-gmail-security-hijack/)[hijack/](http://www.davidairey.com/google-gmail-security-hijack/))





## XSS Vs CSRF
- CSRF
	- **When a malicious website causes a user's browser to perform unwanted actions on a trusted website**
		- Examples
			- Transfer money out of user's account
			- Harvest user IDs
			- Compromise user accounts
- XSS
	- **Malicious website leverages bugs in trusted website to cause unwanted action on user's browser (which circumvents the same-origin policy)**
		- Examples
			- Reading cookies
			- Authentication information
			- Code injection
- Unlike XSS, which **exploits the trust that a user has for a particular site**, while CSRF **exploits the trust that a site has in the user's browser**
- Techniques that protect against XSS **will not necessarily work** for CSRF

## CSRF Mitigation - Users
- Logoff when you are done using a site
- Use multiple browsers
	- One for accessing sensitive data/sites/applications
	- One for surfing freely without worry

## CSRF Mitigation - Developers
- Session time outs
	- After some period of inactivity, logoff the user
- Confirmation pages
	- _Are you sure you want to transfer $1000?_
- CAPTCHA
- Add Session-related information to URLs
	- Makes it extremely difficult for an attacker to know/predict the structure of the URLs to attack
- Random, One-time tokens used in forms


### Can the Use of SSL Prevent CSRF?
- **Not necessarily**
- Goes back to implicit authentication
	- The user's browsers records session information when she is connected to the trusted site for the first time
	- Any subsequent requests sent by the browser are "helpfully" appended with session information
		- Username, password, or SSL certificates
	- Hence, SSL does not necessarily protect the user against CSRF
	- A sure shot way is for the user to authenticate every request. **No implicit authentication.**

#### Links
[OWASP](< [https://owasp.org/www-community/attacks/csrf](https://owasp.org/www-community/attacks/csrf))
[Gmail CSRF]([http://jeremiahgrossman.blogspot.com/2007/01/gmai](http://jeremiahgrossman.blogspot.com/2007/01/gmai))
[Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

# Server-Side Request Forgery (SSRF)
## What is SSRF?
- Among the top 10 OWASP Vulnerabilities in 2021
- SSRF is not limited to HTTP
	- In cases where the application itself performs the second request, it could use different protocols:
		- FTP
		- SMB
		- SMTP
		- etc…
	- and schemes:
		- file://
		- phar://
		- gopher://
		- data://
		- dict://
		- etc…

## What Happens in SSRF?
- The attacker can **abuse functionality on the server** to **read or update internal resources**
	- The victim application (server-side) may have functionality for **importing data from a URL,** **publishing data to a URL or otherwise reading data from a URL** that can be tampered with
		- The attacker then **sends the manipulated request to the server**, and the **server-side code picks up the manipulated URL**. Finally, it tries to **read the data from the manipulated URL**.
![](Pasted%20image%2020240318142249.png)

## Example SSRF
- A web application that receives and uses personal information from a user, such as their first name, last name, birth date etc. to create a profile in an internal HR system. 

- By design, that web application will have to communicate using a protocol that the HR system understands to process that data. 

- Basically, the user cannot reach the HR system directly, but, if the web application in charge of receiving user information is vulnerable to SSRF, the user can leverage it to access the HR system. The user leverages the web application as a proxy to the HR system.

## SSRF Protection
- Input validation in Application Layer
	- Apply the "allow list approach" when input validation is used because most of the time the format of the information expected from the user is globally known
	- Validations can be added to ensure that the input string respects the business/technical format expected
	- IP address and domain validation
- Network Layer
	- Create an "allow list" of hostnames (DNS names) or IP addresses the application needs to access. Thus, other internal services will not be accessible by a vulnerable server.
	- Many caching services and NoSQL databases do not require authentication by default. An attacker could use SSRF to access these services without authentication. Therefore, to protect sensitive information and secure web applications, it is critical to enable authentication for all services within your local network.