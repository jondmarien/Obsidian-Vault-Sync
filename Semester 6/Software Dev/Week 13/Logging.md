# Logging
>"Data!data!data! He Cried Impatiently. I Can't Make Bricks without clay"
>	Arthur Conan Doyle, The Adventure of the Copper Beeches.


## Application Logging
- An information system already has many logs
	- Network infrastructure logs
	- Firewall logs
	- IDS/IPS logs
	- Operating System logs
	- Web server, email server
- Why add more at the application level?
	- Look for security events at the application level
	- Audit policy
	- Determine and monitor baselines
	- Debug problems
	- Provide a more complete picture for an investigation
	- Detect attacks and thus mitigate app exploitation
	- Monitor performance & compliance

## Standard Log Formats
- CLFS (Common Log File System)
- CEF (Common Event Format)
- CEE (Common Event Expression)
- ELFF (Extended Log File Format)

## Events to Log
- User Input/System Output Validation failures
- Authentication success/failure
- Authorization failure
- Session management failure
- Application errors i.e.,
	- Exceptions
- "High-risk" operations i.e., 
	- Changing a password
	- System Access
	- Admin Access
- Legal checks and "opt-in" behaviour i.e.,
	- Accepting terms of use
- Excessive use i.e.,
	- Beyond the baseline
- Domain specific business logic i.e.,
	- Fraud
	- Criminal Activity
- Configuration changes

## What to Log?
**When**
- Timestamp
	- All that are available
		- Remote host
		- Server
- Sequence number
	- If applicable:
		- Allows you to tie events to a single user session
**Where**
- Application identifier
- Application server IP
- Service/protocol involved
- Geolocation
- Application entry point
	- URL
	- HTTP 
	- FTP
	- HTTPS
	- etc.
- Code location if possible
**Who**
- Source IP or other source identifier
- User identity
	- Username
	- PK
	- etc0
**What**
- Type of event
- Severity
	- Numeric, possibly
- Description
- Result/Actions taken, if any
- Reason
- Request headers and HTTP Status codes

## What NOT to Log
- _**Don't**_ include sensitive information in logs, such as:
	- Passwords
	- Authentication tokens
	- Credit Card numbers
	- Personal data
	- Encryption keys

## Where Should the Logs Go?
- Local file system
	- Log to a separate partition where possible
	- Enforce strict permission
	- Don't publicly expose the logs i.e.,
		- Not in the web directory
- Remote file system
	- Follow the same guidelines as local file system
	- Use a secure means of log transport i.e.,
		- Encrypt the transfer
- Database
	- Create an account just for logging

## Links
[Logging Cheat Sheet](https://www.owasp.org/index.php/Logging_Cheat_Sheet)