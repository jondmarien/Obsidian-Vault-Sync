# General Overview of Secure Software Development

Keep software secure, throughout the entire development process. Still, software is never 100% secure.
## Tricky Vulnerabilities
- Some undiscovered bugs (now patched)
	1. Rowhammer: DRAM vulnerability
	2. Meltdown: CPU vulnerability
	3. Bypassing pre-boot authentication passwords

Some vulnerabilities are introduced by development tools:
```c
memset(password, '\0', len(password)); 
free(password);
```
Some optimization compilers will remove the `memset` line.

## Refresh
- Software development methodologies: 
	- Waterfall,
	- Agile
- Testing: 
	- Unit testing,
	- Integration testing, 
	- Systems testing.
- Test Driven Design Documentation: 
	- Comments, 
	- Diagrams (UML)
- Version Control Coding Conventions 
- Design Patterns

## Secure SDLC Steps (and Microsoft's SD3+C)
1. **Secure by Design:** 
	- Include security from the start 
2. **Secure by Default:** 
	- The first state should be the safest
3. **Secure in Deployment:** 
	- Ease of administration, 
	- Change management, 
	- Patching
4. **Communication**

## Step 1: Secure by Design
- Application Threat Models: 
	- A process for identifying, quantifying and addressing the risks in an application.
- Define application's security requirements.
- Security testing of the application during development.
- Static code analysis (code reviews, linters, dependency security auditing)
- Dynamic code analysis (app pen tests, fuzzing)
- Learn from mistakes: 
	- If you find one bug, look for similar ones. Automate it.

- Create a hardened baseline application if you'll be developing similar applications in the future.
- Minimize the application's attack surface
	- Enumerate services, open ports, dynamic content sites, user accounts
	- Examine application's entry points
- Defense in Depth: Make each component as secure as possible. Assume all the other controls have failed.
	- Function level access control.
	- Revalidate for critical functions.
- Data validation!

## Step 2: Secure by Default
- Controlling feature creep
- Principle of least privilege
	- Does a bank teller need to be able to open the main vault?
	- Who's local admin on their laptop right now?
	- Sandboxes.
- The system's most secure state should be right after installation. (ex. PostgreSQL)
- Risk should be introduced when non-default properties are set or new features are enabled/introduced.
- Secure defaults because 80% of the time people will use 20% of your app
	- Simple mode vs Advanced/Power mode
- Don't implicitly trust other systems
- Apps should fail securely:
	- See example in https://owasp.org/www-community/Fail_securely

## Examples
What are these flaws?

```c
if (checkPassword(password) == BADPASSWORD){
	// access denied
} else {
	// access granted
}
```
No need for the if condition on checking the password. Default access denied, then check for good password and grant access.

```c
isAdmin = true; 
try { 
  codeWhichMayFail(); 
  isAdmin = isUserInRole( “Administrator” ); 
}
catch (Exception ex)
{
  log.write(ex.toString()); 
} 
```
Change `isAdmin` to default as `false`.

This example is also an example of the [Least privilege](https://owasp.org/www-community/vulnerabilities/Least_Privilege_Violation) principle, which states you should never grant more access than required. If `codeWhichMayFail()` requires admin access, we should be verifying that admin access before we run that code.
## Step 3: Secure in Deployment
- Ease of administration
- Change management
- Security patching capability
- Security features are not necessarily secure features & security software is not necessarily secure software.
	- Not seeding random number generator.
	- Android security settings/permissions auditing
- Don't depend only on security through obscurity (hiding security algorithms)
	- Proprietary cryptographic protocols are bad

## Step 4: Communication
- End user assistance
- Patch management
- Open vulnerability mindset
	- Bug bounties
	- Issue trackers and transparency
	- Disclosure policies
- Addressing and fixing critical issues
- CVE, CPE, CCE. Find and share!
- Determine/share vulnerability metrics like CVVS
- Participate in and use vulnerability feeds

## CIA !!! Confidentiality/Integrity/Availability
The CIA triangle applies to more than just network and systems security.

- Confidentiality: 
	- Authentication and Authorization 
- Integrity: 
	- Calculations
	- Data types
	- Encoding/Decoding 
- Availability: 
	- Redundancy
	- Concurrency
	- Scalability

