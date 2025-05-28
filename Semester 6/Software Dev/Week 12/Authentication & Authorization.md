# Authentication

## What is Authentication?
- Authentication (from the Greek for real or  genuine, from authentes; author) is the act of confirming the truth of an attribute of a datum or entity.
	- "Is someone who they say they are?"

- Factors of authentication
	- SMS
	- MFA
		- 2 approaches in use
	- Bio

## Basic HTTP Authentication

| Pros                                                        | Cons                   |
| ----------------------------------------------------------- | ---------------------- |
| No cookies, sessions                                        | No confidentiality     |
| No handshakes, SSL                                          | No encryption, hashing |
| Implemented by the web server and browser via HTTP protocol | No logout function     |
Browser response is a Base65 Encoded string containing `username:password`
Authorization: Basic
QWxhZGRpbjpvcGVuIHNlc2FtZQ==
![](Pasted%20image%2020240401143644.png)


## Digest HTTP Authentication
- Basic HTTP authentication with hashing using MD5 and a nonce to prevent replay attacks
- Cons: MD5 is broken (ie. Easy to find collisions) and there is no option to specify a more advanced algorithm. Also, no man-in-the-middle (MITM) protection due to  lack of digital certificate support.
- Both Digest and Basic HTTP authentication are  implemented in Apache with the use of `.htaccess` and `.htdigest` files placed in the web application folders or configured at the virtual host level in the server configuration
- These authentication techniques are not recommended and do not meet most certification or audit requirements

## Modern Web App Authentication
- Most web applications implement single-factor (more on  multifactor later) username/password authentication using  the following set of techniques:
	- SSL/TLS login page accessed using HTTPS restrictions  at the web server and web application levels (ie. You  cannot access [http://yoursite/login.php](http://yoursite/login.php), you are  redirected to [https://yoursite/login.php](https://yoursite.login.php/))
	- Login form implements xss/csrf/clickjacking protection
	- Username/password fields are validated using standard  xss/sqli prevention techniques
	- Passwords are salted (with a strong random number)  and hashed using a strong hash algorithm (not MD5!),  not reversible encryption.

## Password Management
- Implementing password reset functionality
	- Don't use reversible function
	- Don't send a new password in an email
		- User likely won't change the password
		- The password is now sitting in plaintext in their email inbox or likely saved to some folder
		- A temporary one is fine as long as the user is forced to change their password on next login
- Generate a secure nonce (random number) and store in a field of the user table
- Send the user an email with the nonce (lets call it a reset token) as a URL parameter in a clickable link to an SSL/TLS encrypted password reset page
- Perform additional authentication on the reset page
- When in doubt, follow the reset workflow of a solid/secure site
- The reset window should also timeout to prevent DoS, race conditions or other security concerns that could  arise from stale reset emails (someone accesses your company email backups?)
- If you are going to implement security questions as part of the password recovery, don't use information that can be found on Facebook/LinkedIn or other social networks

## Lightweight Directory Access Protocol (LDAP)
- "LDAP is an application protocol for and maintaining distributed directory information services over an IP network"
- Protocol defined in IETF RFC 5411
- A "phonebook" style directory to track records of mostly flat data (like CSV)
- Optimize for read operations, but not for the more complicated querying capabilities of a RDBMS
- Supports SSL/TLS encrypted communications
- Typical operations are:
	- add, modify, delete, search, compare
- OpenLDAP is an open source LDAP server for Linux
- Microsoft uses Active Directory to provide LDAP-like services

### Sample LDAP Entry
- An LDAP Distinguished Name (DN)
```LDAP
dn: cn=John Doe,dc=example,dc=com  cn: John Doe
givenName: John  sn: Doe
telephoneNumber: +1 888 555 6789
telephoneNumber: +1 888 555 1232  mail: [john@example.com](mailto:john@example.com)
manager: cn=Barbara Doe,dc=example,dc=com  objectClass: inetOrgPerson
objectClass: organizationalPerson  objectClass: person
objectClass: top
```
## LDAP Authentication
- LDAP systems are typically used for storing user information that may be required across different systems like web applications and infrastructure identity  (like a domain login)
- This makes LDAP well suited for centralizing authentication operations
- The username and (encrypted) password for a user simply become LDAP entry attributes for a DN assigned to that user
- Query an LDAP server in PHP
```php
$ds = ldap_connect($ldap_server_ip);
ldap_bind($ds); //anonymous read-only connection to ldap
$result = ldap_search($ds, “dc=example,dc=com”, “uid=$username”);
$records = ldap_get_entries($ds, $result);
$password = $records[0][“password”][0]; //first record field, then password field
ldap_close($ds);
```
## Single Sign-On (SSO) Authentication
- Single-Sign On (SSO) is the capability for an information system to allow users to use a single set of credentials to access many different services (i.e., Google, Microsoft)
- True SSO should support different types of authentication
	- Web applications
	- Network access (ex. wifi)
	- Thick client applications (ex. Accounting systems)
	- OS logins
- SSO should not be confused with shared authentication, where another entity manages the authentication portion
	- OAuth
	- OAuth2
	- Facebook Connect
	- OpenID
- LDAP is a natural choice for SSO
	- Fast read access
	- Standardized data formats
	- Supports SSL/TLS
	- Bindings for most programming languages
	- PAM capabilities for OS & thick applications (**application that performs a significant portion of its processing on the user's device**)
	- LDAP logs centralize authentication attempts 

## Web Applications - MFA
- Going beyond "something you have" is tricky
	- Most users don't have access to biometric scanners so  "something you are" is no feasible
	- Must rely on "something you have", traditionally a  hardware token (hardware gets lost)
- "Web 2.0" multi-factor authentication
	- Use an existing product like Google Authenticator, Authy or Duo but if you MUST roll your own:
		- Generate a token (more on this later)
		- Store the server-side token in a session or the user's table
		- Send the token to the user (or user generates it)
		- User sends the token along with username and password
		- User token compared to stored token for final  authentication
## Generating/Sending Tokens
- Two standardized token generation algorithms
	- [Counter-based](https://tools.ietf.org/html/rfc4226)
		- A counter-based algorithm that generates a hash value with a secret combined with a constantly incrementing counter.
		- The token's counter scales up each time the button on the device is clicked, the server counter scales up with each validated OTP.
![](Pasted%20image%2020240401145348.png)

- [Time-based](https://tools.ietf.org/html/rfc6238)
	- A time-based algorithm that generates a hash value using  a secret combined with a timestamp, typically only good  for 30 seconds
	- Tokens can be generated by a user's smartphone app, via  email, via SMS (though SIM hijacking is a risk)
	- Users can also be provided with a list of generated tokens  to choose from where each token is used once
	- Full hash is not sent, just the last 6 chars.
![](Pasted%20image%2020240401145320.png)


## SaaS MFA
- A number of companies have surfaced that solve the multi-factor authentication implementation for a fee.
- Duo Security, for example, has a web application module that you can use to build multi-factor authentication in  your apps.
- Their service is free for the first 10 users, so is well suited to development and small proofs of concept.

[Python Example ]( [https://www.duosecurity.com/docs/duoweb#first-steps](https://www.duosecurity.com/docs/duoweb))
1. Create a key
2. Call sign_request()
3. Show a custom form
4. Call verify_response()
5. Done!

-----
# Authorization