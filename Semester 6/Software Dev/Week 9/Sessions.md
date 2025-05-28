## Storing Session Data
- A session is often represented as an associate array of keys and values for tracking web application data and objects
- Sessions are often used to track a user's authentication status
- Session data is stored on the **server-side** of a web application, NEVER on the client-side (since the additional data transfer would require additional security and bandwidth)
- There a 3 options (generally) for storing data on the server:
	- **RAM/Caching system** (provides fast access)
	- **Files in a** `/tmp` **directory** (this is usually the default)
	- **In a database** (provides persistent long term storage)

## Session ID Management
- The *session ID* is a large randomly generated number (or string)
- The *session ID* is exchanged between the client and server (client -> server) on **EACH transaction** so that the server can look up the **client's session data** 
- The *session ID* is managed in one of two ways:
	- In a cookie (the default)
		- Represented as a text file or in an SQLite database for some browsers
	- In the URL as a GET parameter (**VERY** unsafe)
- W3C Recommended Session ID Specification
```
SID:ANON:www.w3.org:j6oAOxCWZh/CD723LGeXlf-01:34
```

## Starting / Stopping / Using Sessions
The following PHP code demonstrates simple session use for refreshing and reference purpose:
```php
<?php session_start();
if ($_SESSION[‘authed’] == true) {
//display page
} else {
//redirect to login page
} ?>
```
For the logout page:
```php
<?php session_destroy(); ?>
```

## Session Security
- The main concern in session security is keeping the *session ID* **secret & random!!!**
- The *ID* should be a cryptographically secure large random sequence of digits and letters
- *Session ID* predictability should be avoided at all costs
- **DON'T USE** the URL/GET method of passing the *session ID*
- Any transmission of the *session ID* should be encrypted

## Hijacking (Attacks on Sessions)
- Hijacking is stealing the *session ID* with access to the cookie file by malicious code
	- Using XSS or CSRF to inject the JavaScript code to read the *session ID* and forward it to the attacker
- Two types of Hijacking:
	- **Fixation**:
		- "Injecting" the *ID* of a known session into a user's session
	- **Sidejacking**:
		- Packet sniffing the *session ID* when it is not encrypted with SSL/TLS, the *ID* can now be used in a reply attack
		- Two things happening simultaneously at the same time

## Session Safeguards
- Use **SSL/TLS** to encrypt the *session ID* during all communications between client and server
- Use a cryptographically secure random number/letter sequence for generating *session IDs*
- If using an insecure session for pre-login tracking, generate a *new session ID* after the user logs in and is transferred to the SSL/TLS site content
	- Unnecessary if the entire site is SSL/TLS encrypted


## Testing for Session Management Schema
- If the *session ID* is plain-text, the structure and pertinent data may be immediately known (such as 192.168.100.1:owaspuser:password:15:58)
- If part of or the entire token appears to be encoded or hashed, it should be compared to various techniques to check for obvious obfuscation
```Hex
3139322E3136382E3130302E313A6F77617370757365723A70617373776F72643A31353A3538
```
```Base64
MTkyLjE2OC4xMDAuMTpvd2FzcHVzZXI6cGFzc3dvcmQ6MTU6NTg=
```
```Md5
01c2fc4f0a817afd8366689bd29dd40a
```
- Having identified the type of obfuscation, it may be possible to decode back to the original data
	- However, this is unlikely:
		- Decoding takes a longer time than the expiry of the session

## Characteristics of a Cookie providing Session Management
1. Unpredictability
	Cookie must contain some amount of hard-to-guess data
2. Tamper resistance
	A cookie must resist malicious attempts of modification
3. Expiration
	Only valid for a period of time 
4. Secure Flag
	A cookie whose value is critical for the integrity of the session should have this flag enabled in order to allow its transmission only in an encrypted channel 


# HTML5 Local Storage

## Web App Local Storage
Web Apps store all kinds of data on the client-side:
- Session IDs
- Application state
- Temp results and preferences
- Device-level authentication caching
- Shopping carts
- Web-based video game personal high scores (local)
- etc...

Modern web standards provide 3 storage tools to developers:
- Cookies
- HTML5 Application Cache
- HTML5 Local Storage

## Cookies
```js
function setCookie(cname, cvalue, exdays) { 
var d = new Date();

d.setTime(d.getTime() + (exdays*24*60*60*1000)); var expires = "expires="+d.toUTCString(); document.cookie = cname+"="+cvalue+"; "+expires;

}

function getCookie(cname) { 

var name = cname + "=";
var ca = document.cookie.split(';'); 

for(var i=0; i<ca.length; i++) {
var c = ca[i];

while (c.charAt(0)==' ') c = c.substring(1);

if (c.indexOf(name) == 0)

return c.substring(name.length,c.length);

}

return "";

}
```

## HTML5 Application Cache
- Used to create offline versions of web apps by storing all the resources that the page needs to function
- Also reduces server load and increases speed of web applications
- Current security concerns are around the potentional for malicious cached apps
```HTML
<!DOCTYPE HTML>
<html manifest="demo.appcache">
...
</html>
```
![](Pasted%20image%2020240311142904.png)
## HTML Local Storage
- Used to speed up applications by storing large amounts of data client-side
- Unlike cookies, data does not have to be sent back-and-forth to the application server
- Larger storage limits than cookies (~5MB)
- Storage presented as a collection of `key=value`strings
- Comes in two varieties:
	- localStorage
		- No default expiration date
	- sessionStorage
		- Data only stored for current session, but lost when window/tab is closed
```js
// Store
localStorage.lastname = "Smith";

// Retrieve
document.getElementById("result").innerHTML = localStorage.lastname;
```
- Don't store sensitive data here! It is accessible by XSS.
- Browser domain-based restrictions prevent apps from accessing each other's local storage 

## More Information
https://www.w3schools.com/js/js_cookies.asp
https://www.w3schools.com/php/php_cookies.asp
https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/
![](Pasted%20image%2020240311143327.png)
