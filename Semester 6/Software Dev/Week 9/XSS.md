# XSS
## Cross Site Scripting
- What is XSS?
	- **Cross Site Scripting (XSS)** is a common attack vector that injects malicious code into a vulnerable web application
	- It is a web security vulnerability that allows and attacker to compromise the interactions that users have with a vulnerable application

- **XSS** differs from other web attack vectors (i.e., **SQL Injections**), in that it does not directly target the application itself.
	- Instead, the users of the web application are the ones at risk.

A successful cross-site scripting attack can have devastating consequences for an online business's reputation and its relationship with its clients.
![](Pasted%20image%2020240311145133.png)

## Types of XSS
- There are **three** main different types of Cross-Site Scripting Vulnerabilities:
	- **Reflected XSS**
		- A reflected XSS vulnerability happens when the user input from a URL or POST data is reflected on the page without being stored
	- **Persistent or Stored XSS**
		- Stored Cross-Site Scripting vulnerabilities happens when the payload is saved, for example, in a database and then is executed when a user opens the page.
			- Stored cross-site scripting is very dangerous for many reasons
	- **DOM-based XSS**
		- The DOM-based XSS vulnerability happens in the DOM (Document Object Model) instead of part of the HTML
- These are not mutually exclusive, either. You can have Stored, Reflected DOM-based XSS.

- You can also have Stored, Reflected Non-DOM-based XSS too.

**New Types of XSS (easier to understand)**
1. Server XSS
2. Client XSS


## Client XSS
![](Pasted%20image%2020240311145811.png)
```HTML
https://insecure-website.com/status?message=All+is+well. 
<p>Status: All is well.</p>
```
While the web server does not do anything for protection for XSS, the attacked can create the following attack link and email it to the victim:
```HTML
https://insecure-website.com/status?message=<script>/*+Bad+stuff+here...+*/</script>
<p>Status: <script>/* Bad stuff here... */</script></p>
```
## Server XSS
![](Pasted%20image%2020240311145820.png)
A message board application lets users submit messages, which can get displayed to other users:
```HTML
<p>Hello, this is my message!</p>
```
The application doesn't perform any other processing of the data, so an attacker can easily send a message that attacks other users:
```HTML
<p><script>/* Bad stuff here... */</script></p>
```

## DOM XSS
An attack wherein **the attack payload is executed** as a result of modifying the DOM "environment" in the victim's browser used by the original client-side script, so that the client-side code runs in an "unexpected" manner.
	That is, the page itself does not change, but the client-side code contained in the page **executes differently** due to the **malicious modifications** that have occurred **in the DOM environment**.
This is in contrast to other XSS attacks like stored, or reflected, wherein the **attack payload is placed in the response page**, due to a **server-side flaw**.

Suppose the following code is used to create a form to let the user choose their preferred language. A default language is also provided in the query string, as the parameter "default".

```HTML
… Select your language: <select><script> document.write("<OPTION value=1>"+decodeURIComponent(document.location.href.substring(document.location.href.indexOf("default=")+8))+"</OPTION>"); document.write("<OPTION value=2>English</OPTION>"); </script></select> …
```

The page is invoked with a URL such as:
```HTML
http://www.some.site/page.html?default=French
```

If the following link is sent, a successful DOM-based XSS attack will happen against this page:
```HTML
http://www.some.site/page.html?default=<script>alert(document.cookie)</script>
```

When the victim clicks on above link, the browser sends a request for:
```HTML
/page.html?default=<script>alert(document.cookie)</script>
```
to `www.some.site`. The server responds with the page containing the above JS code. The browser creates a DOM object for the page, where the document.location object contains the string:
```HTML
http://www.some.site/page.html?default=<script>alert(document.cookie)</script>
```

The browser then renders the resulting page and executes the attacker's script:
```HTML
alert(document.cookie)
```
## Impact of XSS
Impact of an exploited vulnerability ranges a lot:
- Redirection
- Session Hijacking
- Cross-Site Request Forgery
- Keylogging
- Phishing

If the victim has admin rights, it might even lead to code execution on the server
## Ways to Identify and Verify XSS Vulnerabilities
XSS vulnerabilities can be identified in 2 ways:
- **Static Analysis** (Source code review)
- **Dynamic Analysis** (Fuzzing)

**Static Analysis Tools**
- OWASP WAP - Web Application Protection Project
- RIPS - A static source code analyzer
- Codacy - Automated code reviews + code analytics

**Dynamic Analysis Tools**
- Burp Suite
- Hackbar or burp addon
- Automated vulnerability scanner (Arachni)
## Preventing Cross-Site Scripting
_**PREVENTION????**_

-Never trust user input
-Never trust user input
-Never trust user input
-Never trust user input
-Never trust user input
-Never trust user input
-Never trust user input
-Never trust user input
-Never trust user input

An XSS attack is a type of code injection:
	User input is mistakenly interpreted as malicious program code. Prevention would require secure input handling. There are **two fundamentally different** ways:
		**Encoding**, which escapes the user input so that the browser interprets it _only_ as data, _not as code_.
		**Validation**, which _filters the user input_ so that the browser interprets it as code _without malicious commands_.

## Preventing XSS - Encoding
```pseudocode
print "<html>"
print "Latest comment: "
print encodeHtml(userInput)
print "</html>"
```

If the user input were the string `<script>…</script>`, the resulting HTML would be as follows:
```psuedocode
<html>
Latest comment:
&lt;script&gt;...&lt;/script&gt;
<html>
```
`< = &lt` and `> = &gt`
## Preventing XSS - Validating
One of the most recognizable types of validation in web development is allowing some HTML elements (such as `<em>` and `<strong>`) but disallowing others (such as `<script>`)

There are two main characteristics of validation that differ between implementations:

**Classification Strategy**
	User input can be classified using either blacklisting or whitelisting.
**Validation Outcome**
	User input identified as malicious can either be rejected or sanitized.
## FAQ
- How common are XSS vulnerabilities? 
	- XSS vulnerabilities are very common, and XSS is probably the most frequently occurring web security vulnerability.

- How common are XSS attacks? 
	- It is difficult to get reliable data about real-world XSS attacks, but it is probably less frequently exploited than other vulnerabilities.

- What is the difference between XSS and CSRF? 
	- XSS involves causing a web site to return malicious JavaScript, while CSRF involves inducing a victim user to perform actions they do not intend to do.

- What is the difference between XSS and SQL injection? 
	- XSS is a client-side vulnerability that targets other application users, while SQL injection is a server-side vulnerability that targets the application's database.

- How do I prevent XSS in PHP? 
	- Filter your inputs with a whitelist of allowed characters and use type hints or type casting. Escape your outputs with `htmlentities` and `ENT_QUOTES` for HTML contexts, or JavaScript Unicode escapes for JavaScript contexts.

- How do I prevent XSS in Java? 
	- Filter your inputs with a whitelist of allowed characters and use a library such as Google Guava to HTML-encode your output for HTML contexts, or use JavaScript Unicode escapes for JavaScript contexts

## Lab (Optional)
https://portswigger.net/web-security/cross-site-scripting