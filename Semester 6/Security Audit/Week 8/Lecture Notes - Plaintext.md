Week 8

Slide 1 - INFO SYSTEMS SECURITY AUDITING

Slide 2 - Windows Auditing
Windows Auditing
Windows auditing is a mechanism for capturing and tracking events.
Knowing when and where these events occurred and who triggered them.
It can also be very helpful with detecting certain types of problems like granting of unnecessary privileges and roles, monitoring user events, monitoring resources etc.

Slide 3 - Windows Auditing
Windows Auditing
A Windows system's audit policy determines which type of information about the system you'll find in the Security log.
Windows uses approximately 9 audit policy categories and 50 audit policy subcategories to give you more-granular control over which information is logged.

Slide 4 - Windows Auditing
Windows Auditing
Auditing policies enable you to capture and record a variety of activities to the Windows security log.
Then these auditing logs can be examined to identify issues that need further analysis and investigation.

Slide 5 - Windows Auditing Auditing provides information...
Windows Auditing
Auditing provides information about successful and unsuccessful events so that auditor can analyse and examine any events which can result in attack on the IT assets.
Logging failed/bad attempts can detect malicious users, attackers or unauthorized users to access IT enterprise resources.

Slide 6 - Windows Auditing
Windows Auditing
A security audit is a systematic monitoring of the security of a company's information system by measuring how well it complies with the existing security standards.
Windows security auditing is a Windows feature that helps to maintain the security on the computer and in corporate networks.

Slide 7 - Windows Auditing
Windows Auditing
Windows auditing is intended to monitor user activity, perform forensic analysis and incident investigation, and troubleshooting.
Security audit lets you implement security policies in your environment to fulfil corporate, governmental or industrial requirements.

Slide 8 - How to setup Windows security auditing?
How to setup Windows security auditing?

Windows security auditing can be enabled using either Group Policy (in Active Directory environment) or Local Security Policy (for a single computer).

Open Windows Control Panel, select Administrative Tools, and then run Local Security Policy.
Open Local Policies branch and select Audit Policy. In the right pane of Local Security Policy window, you will see a list of audit policies.
Double click on the required policy and choose what attempts (Success or Failure) to log. Here we described setting up basic audit policies.

Starting from Windows 2008 R2/Windows 7, you can use Advanced Security Audit Policy: Local Security Policy -> Advanced Audit Policy Configuration -> System Audit Policies.

Slide 9 - How to audit logon events?
How to audit logon events?

Windows security auditing lets you audit user logons and invalid logon attempts to your system.
Windows generate these events not only when a user physically logons the system,
but even when accessing a shared resource from a remote computer.
Auditing logon events help the administrator or investigator to review users’ activity and detect potential attacks.
To log logon events run Local Security Policy. Open Local Policies branch and select Audit Policy.
Double click on “Audit logon events” and enable Success and Failure options.
After that, all user logons and invalid logon attempts will be logged to security event log.
Here are some important logon events

Event ID Event message
4624      An account was successfully logged on
4625      An account failed to log on
4648      A logon was attempted using explicit credentials
4675      SIDs were filtered
How to audit file access events?
Windows security auditing lets you audit access to an object, e.g. file, folder, registry key and other system objects that have system access control list (SACL).

It is important task for a system administrator to organize file server auditing, but it may be reasonable to audit not only file servers

Auditing logon events help the administrator or investigator to review users’ activity, detect attempts of unauthorized access to files, and prevent software misconfiguration.
How to audit file access events?
To log file access events, run Local Security Policy. Open Local Policies branch and select Audit Policy. Double click on “Audit object access” and enable Success and Failure options.
This enables system-wide object access audit. Now we should select file objects, which will trigger this event.
Open Windows Explorer and browse for the required file or folder.
Click right mouse button on this object and select Properties. Switch to Security tab and click Advanced button. Switch to Auditing tab in Advanced Security Settings window.
Click Continue button. Now you can set the names of the users or groups whose access you want to audit (you can choose everyone for all users) and what type of access to the file will be audited.

Some important audit events:
Event ID Event message
4656      A handle to an object was requested
4658      The handle to an object was closed
4660      An object was deleted
4663      An attempt was made to access an object
4685      The state of a transaction has changed
4985      The state of a transaction has changed

Audit Policies and Event Viewer
Audit Policy Categories
Each Windows system on your network has nine audit policy categories and 50 policy subcategories, which you can enable or disable.

Audit Policies and Event Viewer
You will see policy settings for only the main categories:
• Audit account logon events
• Audit logon events
• Audit account management
• Audit directory service access
• Audit object access
• Audit policy change
• Audit privilege use
• Audit process tracking
• Audit system events

Audit Policies and Event Viewer
An event in the Windows Security log has a keyword for either Audit Success or Audit Failure. When you enable an audit policy (each of which corresponds to a top-level audit category), you can enable the policy to log Success events, Failure events, or both, depending on the policy. All nine audit policies generate Success events, but only some policies generate Failure events.

Audit Policies and Event Viewer
When you open an audit policy, you may or may not be able to modify it, depending on whether the policy has been defined in a GPO(Group Policy Objects) that has been applied to the local system. If the computer is a member of an AD domain, then the computer automatically applies appropriate GPOs from the domain. Any policy that is defined in a GPO overrides policies that are defined in the system’s Local Security Policy object and becomes the effective setting.

Audit Policies and Event Viewer
As with all security settings, the best practice is to use Group Policy to centrally manage your audit policy. Using local settings can be risky: A group policy could override the local policy settings. Microsoft warns you of this behavior on each policy’s Local Security Setting tab shown below.

Audit Policies and Event Viewer
Audit Policy Subcategories
What about subcategory settings?
The big advantage of using subcategories is the ability to limit the number of events that result from the related category, thus reducing (though not eliminating) unnecessary events.
You can control these policies in Group Policy under Advanced Audit Policy Configuration.

Audit Policy Subcategories
But by default, subcategory settings will take effect only if the top-level policy is undefined. However, you can reverse this behavior by enabling the Audit: Force audit policy subcategory settings to override audit policy category settings security option as shown below.

Audit Policy Subcategories
Note that the default installation of this option is actually Not defined rather than Disabled, as the option’s Explain tab states.
It is recommended that you set this option to be either Enabled or Disabled, for consistent auditing across your enterprise. If this option is enabled and you set a policy subcategory, then no category policy will override it. The subcategory setting will take over on Windows systems.
If this option is enabled but you haven’t specifically configured any subcategory settings for a policy, those subcategories will follow the main category policy.

Top-Level Auditing
Let’s examine the nine top-level audit policy settings one by one.

Audit Account Logon Events
Top-Level Auditing
Audit Account Management
The Audit account management policy, which you can use to monitor changes to user accounts and groups, is valuable for auditing the activity of administrators and Help desk staff. This policy logs password resets, newly created accounts, and changes to group membership

Top-Level Auditing
Audit Directory Service Access
The primary purpose of the Audit directory service access policy is to provide a low-level audit trail of changes to objects in AD. By using this policy, you can identify exactly which fields of a user account, or any other AD object, were accessed.
The policy tracks the same activity as does the Audit account management policy, but at a much lower level.

Top-Level Auditing
Audit Logon Events
The Audit logon events audit policy actually controls the Logon/Logoff category. The policy’s main objective is to record all attempts to use either a domain account or a local account to log on to or off of the local computer.

Top-Level Auditing
Audit Object Access
The Audit object access policy handles auditing access to all objects that reside outside of AD. The first use you might think of for this policy is file and folder auditing. You can also use the policy to audit access to any type of Windows object, including registry keys, printers, and services.

Top-Level Auditing
Audit Policy Change
The primary purpose of the Audit policy change policy is to notify you of changes to important security policies on the local system. Such changes include changes to the system’s audit policy

Top-Level Auditing
Audit Privilege Use
The Audit privilege use policy tracks the exercise of user rights. Microsoft uses the terms privilege, right, and permission inconsistency. In this policy's case, privilege refers to the user rights that you find in the Local Security Policy (under Security Settings\Local Policies\User Right Assignment).

Top-Level Auditing
Audit Process Tracking
The Audit process tracking policy records events in the Detailed Tracking category. This policy’s primary purpose is to track each program that is executed by either the system or by end users. You can even determine how long the program was open.

Top-Level Auditing
Audit System Events
The Audit system events policy logs several miscellaneous security events.

Using Event Viewer to View Events
The preceding audit policies allow you to start up the Windows auditing function. But when Windows starts sending events to the Security log, you need a way to view them. The only built-in tool for accessing the Security log is the MMC Event Viewer snap-in as seen below.

Using Event Viewer to View Events
By default, Event Viewer displays the local computer’s event logs, but you can easily use the console to view the logs of other computers on the network.

Using Event Viewer to View Events
Event Viewer Filter
The filter in the new Event Viewer is also a big improvement as shown in the screenshot below. In the action pane on the right of Event Viewer, click Filter current event log to access the filter. For the Security log, the only event source available is Microsoft Windows security auditing . You must choose this source in the Event sources drop- down box before you can see and choose which subcategories (called task categories in this GUI) to filter.

Searching for Events
The Find feature provides a useful way to correlate events. In the action pane on the right of Event Viewer, click Find to access this feature. For example, you can search for a logon ID to find when a user logged on, the audited objects that the user accessed, and when the user logged off as shown below. If the filter or Find functions are slow, try limiting the time period that is specified in the Logged drop-down box to reduce the number of events that must be processed.
Security Log Integrity
To protect the integrity of Security logs, you must export events from the Security log, as frequently as possible, to a separate server that is both physically and logically out of reach of the local server’s administrator and other operations staff.

Security specialists staff then can monitor the security activity that the servers report and can review the activity of operations staff, as needed.

Based on the findings of the report necessary corrective actions can be taken.
Using Event Viewer to Configure the Security Log
Aside from using Event Viewer to view security events, you use it to configure the maximum size of the Security log. Right-click Security in the left pane, then select Properties to open the Log Properties dialog box shown below.
Using Event Viewer to Configure the Security Log
Windows will not grow the log beyond the size you specify. Nowadays you can set log sizes very large - even in gigabytes.
No matter which maximum size you configure, the log will eventually reach it. You can configure Windows to do one of three things at that point. Don’t choose the Do not overwrite events (Clear logs manually)option; if you do, Windows will just stop logging events when the log reaches its maximum size.

Security Log Integrity
The Security log is very secure. To erase events or otherwise modify the Security log or audit policy, you need physical access to the target system, Administrator authority to that system, or Write access to a Group Policy Objects that applies to that system.

There should be separation of duty between operations and security- monitoring staff in production environments.

Slide 2 - Why DB Auditing?
Auditors typically have three main questions for database
administrators (DBAs ) :
1. Who has access to the sensitive data in a database?
2. Are the right people accessing the data ?
3. Is the audit trail that's being used to validate the access controls
reliable?
Why DB Auditing?

Slide 3 - Monitoring access to sensitive data
Monitoring access to sensitive data
At the start of a compliance audit, the auditors will want to know who has access to sensitive data? and how they gained that access?

Knowing exactly where relevant data resides in a database is the key
to determining who has access to it.

DBAs need to understand how user permissions are applied to the
parts of databases where sensitive data is stored.

For ex : In Oracle Databases tablespaces contains data files and all of the sensitive data
is stored in data files.

Slide 4 - Monitoring access to sensitive data
Monitoring access to sensitive data
DBAs need to isolate and identify users, as well as their privileges and
roles, maintaining a listing of access control levels on specific objects
in a database. 

Auditors typically will need to know that all this information has been
validated by an organization's compliance officer

Slide 5 - Data access for the privileged users
Data access for the privileged users
Auditors also want to make sure that employees are using critical data
properly.

Auditors ask for proof that the data is only being accessed by the
privileged users.

It's important to prove that the data can't be accessed by the
unprivileged users.

Slide 6 - Data access for the privileged users
Data access for the privileged users
To control the data, DB auditing aims to provide detailed records and
reports on when data was accessed and by whom 

The main challenge for the DBAs is not only keeping track of the who,
what, when and where of every transaction related to particular data
sets, but also maintaining those records and being able to retrieve
them as required 

Slide 7 - Maintaining Audit Trail
Maintaining Audit Trail
Auditors want to ensure that the audit trail being used to validate the
data access controls hasn't been tampered or modified by unauthorized users

Confidentiality and Integrity of audit data should also be maintained

DBAs collect and maintain a full audit trail for transactions relating to
the critical data in a database 

Slide 8 - Maintaining Audit Trail
Maintaining Audit Trail
Data should be kept in accordance with a standard data retention
policy -- typically, for a minimum of five years. It depends on the
organization’s data retention policy 

Slide 9 - Common Database Vulnerabilities
Common Database Vulnerabilities
• Default user accounts and passwords
• Easily identified passwords
• Missing database patches
• Misconfigurations
• Excessive Privileges
Common Database Vulnerabilities
External Threats:
• Web application attacks (SQL - injection)
• Poor Internal Control i.e. Insider mistakes
• Weak audit mechanisms
• Social engineering attacks
Common Database Vulnerabilities
Default and Weak Passwords

Oracle Defaults (hundreds of them)
User Account: system / Password: manager
User Account: sys / Password: change_on_install
User Account: dbsnmp / Password: dbsnmp

Microsoft SQL Server Defaults
User Account: SA / Password: null
Common Database Vulnerabilities
It is important that you have all of the proper safeguards against password attackers because:

Every DB account is not configured with lockout mechanism

Database Login activity is sometimes unmonitored 

Scripts and Tools for breaking weak passwords are
widely available 
Common Database Vulnerabilities
Missing Patches:
Privilege Escalation Attack – Become a DBA or
equivalent privileged user
Denial of Service Attacks – Result in the database
crashing or failing to respond to connect, application
requests or SQL queries by end users .
Common Database Vulnerabilities
Buffer Overflow Attacks – Result in an unauthorized user causing
the application to perform an action and it exceeds the maximum
buffer size and results in loss of transaction data .
Common Database Vulnerabilities: Misconfigurations

Oracle
• External Procedure Service
• Default HTTP Applications
• Privilege to Execute UTL_FILE

Microsoft SQL Server 
• Standard SQL Server Authentication Allowed 
• Permissions granted on xp_cmdshell

MySQL 
• Permissions on User Table ( mysql.user )
Database Protection Planning: Auditing and Monitoring
1. Authentication Auditing
Who accessed which systems, when, and how?
2. User Auditing
What activities were performed in the database by both users and administrators?
3. Security Activity Monitoring
Identify and flag any suspicious, malicious or unauthorized access to sensitive data or critical systems
4. Vulnerability & Threat Auditing
Detect vulnerabilities in the database, then identify users attempting to exploit them
5. Change Auditing
Establish a baseline policy/standard procedures for database; configuration, schema, users, privileges and structure, then monitor changes from that baseline.
Auditing: Vulnerability Assessment & Activity Monitoring

"Outside in" and "Inside out" scan of all database applications to assess:
Security strength
Database vulnerabilities
Application discovery and inventory

Fix security holes and misconfigurations

Develop policies based on results from scan to identify:
Database vulnerability
Roles and responsibilities functionality to segregate users
Compliance risk factors
Auditing: Vulnerability Assessment & Activity Monitoring

Auditing
Comprehensive reporting

Real - Time Monitoring
Defend against misuse, fraud, and abuse from internal and external
users 

Monitor all of the (DDL, DML and DCL statements) .
HOW TO AUDIT DATABASE SYSTEMS?

Check for object level and system level permissions:
• Check views, stored procedures, tables, etc.
permissions.

Check the permissions at the file, folder, registry and
data dictionary level.
HOW TO AUDIT DATABASE SYSTEMS?
Look for new database installations:
Newly installed database servers/instances and new installed servers
could be installed with blank or weak passwords, they could be un -
patched, mis - configured, etc. So apply patches immediately after the
database installation.
HOW TO AUDIT DATABASE SYSTEMS?
Search for users with DBA privileges:
This helps to detect misuse , elevation of privileges, etc.

Audit database configuration and settings:
If security configurations or settings are changed for instance by a
system upgrade, patch, etc., your databases could be open to attack 
HOW TO AUDIT DATABASE SYSTEMS?
Check database system objects against changes:
If you detect a change in any of the database objects like tables, views, procedures, functions, triggers etc., and you haven't applied a patch to your database server it could mean database can be compromised 
ENABLING DATABASE AUDITING
• Must be enabled and configured on each database server
individually.
• Auditing is mostly configured by DBA
• Can be managed and controlled with audit management tools (Audit Trail table etc.)

By default auditing is disabled in most of the databases.
Advantages of Database Systems Auditing
- Identifies potentially suspicious activity
- Operationally efficient
- Indicates possible need for action in case of policy violation
or compliance failure.
- Saves resources, staff, time and money
- Audit data is retained for future use.
Databases
• Warehouses of application data
• Many apps are built on DBs

• Relational Databases (RDBMS)
Subheading
• MSSQL
• PostgreSQL
• Oracle
• MySQL
• SQLite

• NoSQL
Application Data
• Most applications have internal auditing
• Financial applications may have a “Transactions” table
• Filtering applications may have an “Actions” table
• Most applications will have some form of “Log” table
Auditing within the app
• Admin consoles provide access to logs
• Every app implements this differently
• Some apps provide exporting

• Access via:
• The application itself
• A separate “admin” application
• A separate login to the webapp
Investigate the Schema
• What tables are in the DB?
• Most developers name things in helpful ways
• “Log” table is the most obvious
• “something_log ” occurs often too

• What views are in the DB?
• Perhaps a view joins 5 - 6 tables to make logs easy

• What functions/stored procedures exist?
Use their functions with caution!
• Your application may have functions or Stored Procedures to make logging easy
• Functions / Stored Procedures CAN change data
• Auditing entries could be added automatically
• Triggers are widely used as auditing objects
App Architecture
• Applications issue SQL statements to DBMS
• RDBMS processes statement, returns data
• RDBMS have their own auditing features, offering another way to find out
what happened
Write - Ahead Log (WAL)
• A Write - Ahead Log (WAL) is a file used by DBMS’s to maintain ACID compliance
• Every task is logged first, then performed, then logged again.
ACID “standard”
• ACID is a set of properties that guarantee transactions are processed
reliably:
• Atomicity – (All or nothing occurs)
• Consistency – (Known inputs always produce known outputs)
• Isolation – (Changes happen one - at - a - time)
• Durability – (Successful changes are permanent)
Write - Ahead Log (WAL)
WALs are used by RDBMSes to enforce ACID properties

1. Statement issued to RDBMS
2. Statement written to WAL, transaction opened
3. Statement processed within DB; changes recorded
4. Transaction closed; “Complete” written to WAL
All DBMSes have a WAL
• Each DBMS names it differently:

• Oracle
• Redo Log

• MS SQL
• Transaction Log Data File (LDF)

• PostgreSQL
• xlog (x = transaction)

• MySQL
• mysqlbinlog command on / var /log/mysql - bin.000001

• SQLite
• Write - Ahead Log
Write - Ahead Log (WAL)
• If a statement is interrupted before completing, the WAL will
show this
• The DBMS checks the WAL when starting and rolls - back any
incomplete transactions
• WAL can contain every statement ever issued to the DB
WAL Log Settings
• Each DBMS’s default settings for WALs are different
• Log size (MB) for rotation
• Date range (in days) for rotation
• Statement count (in #statements) for rotation
• In most cases, defaults record near - term statements
• Long - term history of statements can be found elsewhere
DBMS Backup Strategies
• Many DBMSes require log files to be backed up with data files
• Analyzing online backups, tape backups, and other archived databases can reveal statements issued near those backup dates
Database Permissions
• Even viewing permissions can alter the WAL
• SELECT * FROM Roles
• SELECT * FROM Users

• Consider backing up the log file before doing anything to the
database

Slide 2 - Auditing database management systems
Auditing database management systems
a) Types of databases
b) Data dictionaries
c) Controls provided by the DBMS
d) Application dependent controls
e) Audit considerations
f) Case study

Slide 3 - a. Types of Databases
a. Types of Databases
• Relational Database Management Systems (RDBMS): Stores data in tables with rows and columns. Examples include MySQL, Oracle, and SQL Server.

• NoSQL Databases: Designed for storing and retrieving data in formats other than tabular relations, such as key - value, document, column, and graph databases. Examples include MongoDB, Cassandra, and Neo4j.

• In - Memory Databases: Store data in the main memory to ensure faster access and processing. Examples include Redis and SAP HANA.

• Object - Oriented Databases: Store data in the form of objects, similar to object - oriented programming. Examples include db4o and ObjectDB.

• Example: A company might use an RDBMS like MySQL for structured data such as customer information and transactions, while using a NoSQL database like MongoDB for unstructured data like logs or social media posts.

Slide 4 - b. Data Dictionaries
b. Data Dictionaries
• A data dictionary is a centralized repository of metadata, providing details about database tables, views, columns, data types, and relationships. It helps in understanding the structure and constraints of the data.

• Example: In an RDBMS, the data dictionary might include information such as table names, column names, data types, primary and foreign keys, and constraints like NOT NULL or UNIQUE.

Slide 5 - c. Controls Provided by the DBMS
c. Controls Provided by the DBMS
• Access Controls: Determine who can access the database and what actions they can perform.

• Authentication and Authorization: Verify the identity of users and grant permissions based on roles.

• Data Integrity Controls: Ensure the accuracy and consistency of data through constraints like primary keys, foreign keys, and check constraints.

• Auditing and Logging: Record database activities to monitor and analyze access and changes.

• Example: A DBMS might enforce access controls by requiring users to log in with a username and password, and then restricting their actions based on their assigned roles.

Slide 6 - d. Application Dependent Controls
d. Application Dependent Controls
These are controls implemented at the application level that interact with the database, such as:
• Input Validation: Ensuring that only valid data is entered into the database.

• Parameterized Queries: Preventing SQL injection attacks by using parameters instead of embedding user input directly into SQL statements.

• Error Handling: Properly managing database errors to prevent information leakage.

• Example: A web application might use parameterized queries to safely insert user input into the database, avoiding SQL injection vulnerabilities.

Slide 7 - e. Audit Considerations
e. Audit Considerations
When auditing a database management system, consider the following:
• Compliance with Policies and Regulations: Ensure that the database management practices comply with relevant policies and regulations.

• Access Control and Authentication: Verify that access controls and authentication mechanisms are properly implemented and effective.

• Data Integrity and Security: Check that data integrity controls are in place and that data is protected from unauthorized access or manipulation.

• Backup and Recovery: Assess the adequacy of backup and recovery procedures to ensure data availability and continuity.

• Change Management: Evaluate the processes for managing changes to the database structure or contents.

Slide 8 - Case Study: Auditing a Healthcare Database
Case Study: Auditing a Healthcare Database
A healthcare organization uses an RDBMS to store patient records, treatment history, and billing information. An audit is conducted to ensure compliance with healthcare regulations and data protection standards.

• Access Controls: The audit checks that only authorized personnel can access sensitive patient data and that roles are defined to limit access based on job function.

• Data Encryption: It is verified that sensitive data, such as patient health information, is encrypted both at rest and in transit.

• Backup and Recovery: The organization's backup procedures are evaluated to ensure that data can be restored in case of a disaster or data loss.

• Audit Trails: The audit examines the database's logging mechanisms to ensure that all access and changes to patient data are recorded for future review.

• Compliance with Regulations: The auditor verifies that the database management practices comply with regulations such as HIPAA (Health Insurance Portability and Accountability Act) for protecting patient data.

Slide 9 - The audit findings help the organization...
The audit findings help the organization identify areas for improvement in their database management and security practices, ensuring the confidentiality, integrity, and availability of patient data.

Talking abut Project/Practical Midterm

Assignment 2

Project Pt. 2
Made with Glean