# Secure Software
1. What are some examples of security vulnerabilities that cannot be known at development time?
	- Attacks that cannot be known at development time would be things like:
		- **Zero-day vulnerabilities**
		- **Vulnerabilities in Dependencies**
		- **Evolving attack techniques**
2. What is the purpose of "application threat models" and how do they help identify and address risks?
	- **Application threat models** provide a structured way to analyze your application's design, systematically identify threats, and prioritize security risks based on severity. They **benefit** us by providing proactive security which uncovers vulnerabilities early on in the development process. You can also add security controls to address any risk mitigations. 
3. What is the principle of "least privilege" and why is it important for security?
	- **Least Privilege** means to grant users and processes only the absolute minimum permissions they need to perform their tasks.
4. What is "defense in depth" and how does it work to ensure security?
	-  **Defense in Depth** is a layered security approach with multiple, overlapping security controls. The idea is that if one layer fails, others remain to prevent or mitigate an attack.
5. What is the concept of "secure by default" and why is it important for security?
	- **Secure by Default** means that systems and applications should should with the most secure settings out of the box, with no user configuration required, especially for basic security measures. It is important because it reduces user error, and reduces the attack surface of the machine or application.
6. What component of the CIA triangle is concerned with ensuring availability and scalability of systems?
	- **Availability** is the component of the CIA triad that is focused on keeping systems & resources accessible to authorized users.
7. What is data validation?
	- Ensuring that a program operates on clean, correct, and useful data.
8.  What are the two serious issues that can occur due to non-validation of data?
	- **Injection attacks**: where malicious data alters program behaviour
	- **Buffer overflows**: when input exceeds expected storage, leading to code execution
9. Which approach is better for data validation: whitelist or blacklist?
	- **Whitelisting** is generally better, because it explicitly defines what's allowed. Blacklists can miss new patterns not defined in the ruleset.
10. What does sanitizing mean in the context of data validation?
	- **Sanitizing** data means to modify untrusted data to make it comply with expected formats, which would remove harmful elements.
11. What is the purpose of SSL? 
	- **SSL**'s purpose is to secure data transmission over the internet using encryption and authentication
12. Which protocol is commonly used in SSL?
	- **TLS**. Transport Layer Security.
13. What is the HTML 5 iframe sandbox used for?
	- The **Sandbox** is used to restrict embedded content, which prevents it from interacting maliciously within the main page.
14. What is the primary purpose of a sandbox for developers?
	- **Sandbox** provides a safe, isolated environment for developers to test code.
15. What are "dangerous" functions? 
	- **Dangerous functions** are functions that can introduce security vulnerabilities if used incorrectly, even though they can also be used safely.
		- Example: `gets()` and `>>`, or `strcpy()`
16. What are the categories of dangerous functions?
	- **Information Disclosure**
	- **Importing an External Resource**
	- **Connecting to an Domain Outside Trust (Domain)**
	- **Running System Commands**
17. Which PHP function is an example of a dangerous function that leads to information disclosure? 
	- `phpinfo()` dumps all PHP configuration information which could reveal sensitive details about the system and installed modules.
18. What should be done if a function on the prohibited list is required for a programming project? 
	- **Thorough justification**
	- **Strict Input Validation**
	- **Code Isolation**
	- **Extensive Code Review**
19. How can the use of prohibited functions be prevented and mitigated in a programming project?
	- **Train devs to not use unsafe function**
	- **Use coding standards and secure libraries**
	- **Prioritize security**
	- **Use static code analysis tools**