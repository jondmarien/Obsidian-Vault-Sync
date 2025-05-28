# SQLi's Bigger Badder Sibling

## What is Command Injection?
- A vulnerability in an application which can lead to arbitrary code being run on the target system
	- Command injection attacks are attempts by attackers to execute arbitrary shell commands against the system hosting the vulnerable application
- Less common but potentially more dangerous type of injection attack than SQL injection
- Command injection can be used for information gathering, application installation, system modification, privilege escalation, persistence, and general data destruction

## What Causes Command Injection Vulnerabilities?
 - User input data not validated
- Incorrect data validation technique
- Incorrect application of the principle of least privilege
- Insufficient restrictions at the data layer
- Trivial to exploit
- High profile example happened in 2014 called [Shellshock](https://en.wikipedia.org/wiki/Shellshock_(software_bug))

## Usages
![](Pasted%20image%2020240325144243.png)

## Exploitation
- Similar to SQL Injection exploitation
- Expect command is terminated using a known termination character sequence
	- Bash, for example, separates commands with a semicolon
- Malicious command is inserted after terminator
- Severity of exploitation depends on permissions of executing user (this is generally the web server "user")
- Alternate method:
	- If the command executes a supplied script by name, an attacker could insert malicious program name (see example below)
```java
String script = System.getProperty("SCRIPTNAME");  
if (script != null) System.exec(script);
```

## Command Injection Remediation Strategies
- Escape sequences and regular expression pattern matching
	- Good place to implement "whitelist" matching technique, based on expected script function
- If possible, modify input method to something other than an open text field
- Sadly, no stored procedure or prepared statement mechanisms available
- Some CGI (Common Gateway Interface) languages allow a version of exec which specifically requires an executable name and list of arguments as an array leaving no room for injection

- Other mitigation strategies
	- Apply least privilege concepts
	- chroot jails
	- Run the web server as a custom user to control available executable programs

## Links
[OWASP Command Injection](https://owasp.org/www-community/attacks/Command_Injection)
[MITRE Top 25]([http://cwe.mitre.org/top25/index.html#CWE-78](http://cwe.mitre.org/top25/index.html))


## Examples
### catWrapper
```c
#include <stdio.h>
#include <unistd.h>

int main(int argc, char **argv) {
 char cat[] = "cat ";
 char *command;
 size_t commandLength;

 commandLength = strlen(cat) + strlen(argv[1]) + 1;
 command = (char *) malloc(commandLength);
 strncpy(command, cat, commandLength);
 strncat(command, argv[1], (commandLength - strlen(cat)) );

 system(command);
 return (0);
}
```

Used normally, the output is simply the contents of the file requested:
```cli
$ ./catWrapper Story.txt
When last we left our heroes...
```

However, if we add a semicolon and another command to the end of this line, the command is executed by `catWrapper` with no complaint:
```cli
$ ./catWrapper "Story.txt; ls"
When last we left our heroes...
Story.txt               doubFree.c              nullpointer.c
unstosig.c              www*                    a.out*
format.c                strlen.c                useFree*
catWrapper*             misnull.c               strlength.c             useFree.c
commandinjection.c      nodefault.c             trunc.c                 writeWhatWhere.c
```
If `catWrapper` had been set to have a higher privilege level than the standard user, arbitrary commands could be executed with that higher privilege.

### Filename as a CLI Argument
   The following simple program accepts a filename as a command line argument, and displays the contents of the file back to the user. The program is installed setuid root because it is intended for use as a learning tool to allow system administrators in-training to inspect privileged system files without giving them the ability to modify them or damage the system.
```c
int main(char* argc, char** argv) {
 char cmd[CMD_MAX] = "/usr/bin/cat ";
 strcat(cmd, argv[1]);
 system(cmd);
}
```

### Using Environment Variable
   The following code from a privileged program uses the environment variable $APPHOME to determine the application's installation directory, and then executes an initialization script in that directory.
```c
...
char* home=getenv("APPHOME");
char* cmd=(char*)malloc(strlen(home)+strlen(INITCMD));
if (cmd) {
 strcpy(cmd,home);
 strcat(cmd,INITCMD);
 execl(cmd, NULL);
}
...
```

### Make File
The code below is from a web-based CGI utility that allows users to change their passwords. The password update process under NIS includes running `make` in the `/var/yp` directory. Note that since the program updates password records, it has been installed `setuid` root.
```c
system("cd /var/yp && make &> /dev/null");
```
Unlike the previous examples, the command in this example is hardcoded, so an attacker cannot control the argument passed to system(). 
- However, since the program does not specify an absolute path for make, and does not scrub any environment variables prior to invoking the command, the attacker can modify their $PATH variable to point to a malicious binary named make and execute the CGI script from a shell prompt. 
	- And since the program has been installed setuid root, the attacker's version of make now runs with root privileges.

### Unix/Linux Command Injection
```c
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
     char command[256];

     if(argc != 2) {
          printf("Error: Please enter a program to time!\n");
          return -1;
     }

     memset(&command, 0, sizeof(command));

     strcat(command, "time ./");
     strcat(command, argv[1]);

     system(command);
     return 0;
}
```
If this were a suid binary, consider the case when an attacker enters the following: `ls; cat /etc/shadow`. In the Unix environment, shell commands are separated by a semi-colon. We now can execute system commands at will!

 **suid: Set owner User ID up on execution**

### PHP Command Injection
```php
<?php
print("Please specify the name of the file to delete");
print("<p>");
$file=$_GET['filename'];
system("rm $file");
?>
```
The following request and response is an example of a successful attack:
Request: 
`http://127.0.0.1/delete.php?filename=bob.txt;id`
Response:
```
Please specify the name of the file to delete

uid=33(www-data) gid=33(www-data) groups=33(www-data)
```
Sanitizing Input
```
Replace or Ban arguments with “;”
Other shell escapes available
Example:
–  &&
–  |
–  ...
```