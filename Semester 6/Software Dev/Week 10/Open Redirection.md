# Open Redirection
## What is It?
- A vulnerability in a web application's attempt to redirect the user when a page loads
- Allows an attacker to send a legitimate user to a website or URL of the attacker's choosing
- Exploited when a web application sends a destination URL as a parameter in an HTTP request
- The attacker can replace the intended destination URL with a malicious one to force the user to a malicious site
- Commonly used in phishing or as part of a CSRF attack


## What is the Source of Vulnerability?
- HTTP request data not properly validated
	- Didn't check the parameter
	- Used an incorrect data validation technique to validate parameter
- Difficult to locate in an application since redirections are not always managed through request parameters
- Trivial to exploit when located
- Usually occurs when a user tries to visit a secure page before logging in. The user will be redirected to the login page

## Exploitation
- Simply replace the intended URL in the HTTP request field with a malicious one
- Send the modified request link to an unsuspecting victim
- Victim clicks on the link and is automatically redirected to attacker's site of choice
```php
//Redirect.php

<?php

if ($_SESSION[‘status’] != ‘loggedin’) {
$redirect = $_GET[‘url’]; 
header(Location:$redirect);
}

?>

Address bar:  www.mysite.com/redirect.php?url=login.php

Malicious bar: www.mysite.com/redirect.php?url=http://myevilsite.com
```

## Open Redirection Defense
- Rather than sending the whole URL, send an Id number which maps to a list of known redirects
Example: [http://www.mysite.com/redirect.php?redirid=1]

| $_GET['redirid] | URL          |
| --------------- | ------------ |
| 1               | login.php    |
| 2               | userhome.php |
- Use a whitelist validation to ensure the URL goes to an expected domain
- Attach a verification hash to the URL which is a combination of intended destination URL and a nonce (arbitrary number).
	- Verification hash can be checked by redirection page
### Links
[Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html)
[Open Redirect on OWASP](●[https://cwe.mitre.org/data/definitions/601.html](https://cwe.mitre.org/data/definitions/601.html))
