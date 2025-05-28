
## Operating Systems
Perform three main tasks:  
- translates high-level languages into the machine-level language  
- allocates computer resources to user applications
- manages the tasks of job scheduling and   multiprogramming  


## OS Security
- Log on procedure
- Access Token
- Access Control List
- Discretionary Access Control

## OS Controls
- Access Privileges
- Password Control
- Malicious & Destructive Programs
- Audit Trail Controls

## Access Control Principles
RFC 4949 states that computer security is defined as:
	'Measures that implement and assure security services in a computer system, particularly those that assure access control service.'

- Discretionary Access Control (DAC)
![[Pasted image 20240223162252.png]]
- Role-based access control (RBAC)
- Mandatory access control (MAC)
- Attribute-based access control (ABAC)

![[Pasted image 20240223162238.png]]

## Account Security
- PAM (Pluggable Authentication Modules)
![[Pasted image 20240223162400.png]]
![[Pasted image 20240223162411.png]]

## Audit System Architecture
![[Pasted image 20240223162458.png]]
- the audit daemon collects the information from the kernel and creates log file entries in a log file
- audisp
	- audit dispatcher daemon that interacts with the main daemon and sends events to other apps for further processing
- auditctl
	- audit control utility interacts with the kernel audit component to interact with and control a number of settings and parameters of the event generation process
- aureport
	- generates a report of all recorded events

## Audit Rules
- Control rules
	- allow the audit systems behavior and some of its config to be changed
- File system rules
	- aka file watches, allowing the audit of access to a certain file or dir
- System call rules
	- allow logging of system calls that any one program makes

## Kernel Auditing
• the launch and completion of system jobs
• reading, writing, and changing a file's access rights
• initiating network connections
• failed authorization attempts
• changing network configurations
• changing user and group information
• launching and halting applications
• executing system calls

## Logging of Logins and Logouts
- `/var/run/utmp` and `/var/log/wtmp` contains logs for currently logged in users and current/past logins + additional system information about system reboots 
	- they are binary files, use `utmpdump`
- `/var/log/btmp` contains all bad login attempts


## /var/log/secure
- tracks authorization systems
	- sudo logins, ssh logins, other login errors
- All user auth events are logged here
	- can help to detect possible hacking attempts


`watch` command to repeat commands


## Displaying Memory + Cache
`/proc/meminfo`
![[Pasted image 20240223164338.png]]

## AIDE (Adv. Intrusion Detection Environment)
- Checks integrity of files
	- when files  are changed
- maintains a db of file statuses
- emails notifications of changes
- monitors last time a file was accessed

1. Run an initial scan
2. Schedule daily or weekly integrity check (cron job)
3. Check reports and investigate changes
4. Update db if changes occur (update baseline)


## Tecnet
1. Access Control
2. Data Protection
3. network security
4. malware protection
5. incident response
6. physical security
7. compliance and training


1. LOGGER
	1. COLLECTS DETAILED LOGS FROM VARIOUS SOURCES; EVERY ACTION IS LOGGED
2. ANALYZER
	1. CORE INTEL ENGINE, COLLECTS LOGS
3. NOTIFIER
	1. ALERTING RELEVANT PERSONNELL