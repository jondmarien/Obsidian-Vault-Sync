---
title: Appendix J - Database Penetration Testing Methodology
author:
  - Jon Marien
created: 2025-04-30
published: 2025-04-30
tags:
  - skillsontario
  - competitions
  - certifications
---

| Title                                                 | Author                       | Created        | Published      | Tags                                                                                                       |
| ----------------------------------------------------- | ---------------------------- | -------------- | -------------- | ---------------------------------------------------------------------------------------------------------- |
| Appendix J - Database Penetration Testing Methodology | <ul><li>Jon Marien</li></ul> | April 30, 2025 | April 30, 2025 | [[#skillsontario\|#skillsontario]], [[#competitions\|#competitions]], [[#certifications\|#certifications]] |

# Database Penetration Testing Methodology

## Objective
The Objective of this lab is to extract database's, crack user credentials, manipulate databases and create user accounts using SQL injection technique.

## Scenario
Penetration testers and advisors will mimic an assault in the same way a programmer would do to gain access to the database utilizing industry best practice strategies and our own particular extra methods, recognizing access focuses and giving direction on the best way to secure down your database in the case of a genuine assault.

A database penetration test will show if your database is appropriately outlined, designed and kept up and if it complies with industry and seller best practice.

Databases hold important business resources, for example, client's sensitive information, payment card's subtle elements, item and estimating information, employee records, outlines, blueprints, licensed innovation and supplier data. Should this information end up on the wrong hands or be traded off in different ways then you may be left confronting with money-related problems in addition to harm to your reputation.

# Exercise 1: Pentesting MySQL Database

## Scenario
MySQL database is one of the extensively used open source databases and freely available with unrestricted redistribution, providing users with full access to the source code. The database can contain different pluggable storage engines to suit the application. Being one of the extensively used open source databases, MySQL becomes a prime target for the attackers in order to gain access to sensitive information.

As a pentester, you need to be aware of MySQL databases and their related queries. In this lab, you will learn to perform the following:

- Obtain information regarding the version of MySQL
- Perform dictionary attack on the database server and gain access to it

# Steps

## Step 1

### Parrot OS
First step is running a terminal with `nmap -sP 172.19.19.1-255`. This performs a ping sweep scan on the internal network. In our lab, we will be targeting `172.19.19.17`, which is the sales department.
![[image-193.png]]

Then, we perform an **intense scan** for **nmap -T4 -A 172.19.19.17**, which is the Sales Dept.
![[image-194.png]]

Once the scan is finished, we can see that port **3306** is open, which is the **MySQL** service on the remote machine.
![[image-195.png]]

Now, we launch `msfconsole`:
![[image-196.png]]

We will then use the **auxiliary script** for `mysql_login` and show the options:
![[image-197.png]]

Following that, we set the `host address` and the `password file` to use:
![[image-198.png]]

Then, we run the exploit:
![[image-199.png]]

Eventually, the script with complete successfully and show us the `username:password` combination that is valid to login:
![[image-200.png]]

Now that we have the password, we will set the auxiliary script to be `admin/mysql/mysql_sql`, and set the proper values to use the host, username, password, and the sql show db command.
![[image-201.png]]

 Then, we `run` the script.
![[image-202.png]]

Now, we can see all of the databases stored inside the MySQL DB server!

> [!check answer]-
> ![[image-203.png]]

# Exercise 2: Performing Automated Database Penetration Testing Using Havij

## Scenario
Database Vulnerability Assessments are essential to a methodical and proactive way to deal with database security and diminish the danger connected with both web and database particular assaults and bolster agreeability with significant norms, laws & regulations.

Database Vulnerability Assessments are best utilized:

- As a fast and economical method for surveying the danger connected with a database that is in operation yet has not (as of late) experienced a more extensive database security appraisal.
- As a major aspect of a progressing defenselessness/design administration program, particularly in the backing of show of continuous agreeability with important models/regulations.
- To evaluate less basic databases (i.e., databases with a moderate danger profile where the danger does not legitimize more prominent degree and meticulousness.
- As a data gathering instrument to center entrance testing or code surveys.

# Steps

## Step 1

### Windows Server 2019
We install Havij, and analyze the target url @ `http://172.19.19.21/queenhotel/about.aspx?name=coffee`.

![[image-204.png]]
![[image-205.png]]

We can also see this info in the `Info` tab, as shown here:
![[image-206.png]]

If we click the `Get` button, we get a more complete detailed list of information about the DB server:
![[image-207.png]]

In this lab, we are focusing on the `Real_Home` table in the tables section, and will attempt to retrieve the data from it:
![[image-208.png]]

If we click `Get Tables`, followed by `Get Columns`, we will discover more information about `Real_Home`:
![[image-209.png]]

We will focus on the `Login` table. We can select the `password` and `login_username` fields and click `Get Data`.
![[image-210.png]]

We can verify that these credentials are valid by browsing to the url that we searched originally in this lab + the `realhome` route, so `http://172.19.19.21/realhome`.

We then use the `smith` login:
![[image-211.png]]

It worked!
![[image-212.png]]

Done!

> [!check answer]-
> ![[image-213.png]]

# Exercise 3: SQL Injection Attacks on MS SQL Database

## Scenario
Today, SQL injection is one of the most common and perilous attacks that a website undergoes. This attack is performed on SQL databases that have weak codes. A website’s vulnerability can be used by an attacker to execute database queries to collect sensitive information, modify the database entries, or attach a malicious code resulting in total compromise of the most sensitive data.

As an **Expert Penetration Tester** and **Security Administrator**, you need to test web applications running on the MS SQL Server database of vulnerabilities and flaws.

# Steps

## Step 1

### Windows Server 2019

Browse to a url, and try to login by making the password field always true:
![[image-215.png]]

Done!
![[image-216.png]]

Then, we try to login with a user using this command:
`blah';insert into login values ('sandra','sandra123'); --`
![[image-217.png]]

It also works!
This is basically telling the application that we created login details as follows:
> Username: sandra
> Password: sandra123

![[image-218.png]]
![[image-219.png]]

It works!!

## Step 2

### Windows Server 2012 (ECSAv10)
We start by launching SQL Server Management Studio and connect.
![[image-220.png]]

Then we select the top 1000 rows from `goodshopping`.
![[image-221.png]]

We can see that our `sandra` user was successfully created in the database:
![[image-222.png]]

## Step 3
### Windows Server 2019
We go back to the Windows Server 2019 and attempt to create a new database. If we get no visual error, the query worked.
![[image-223.png]]

## Step 4

### Windows Server 2012
Once we connect back the 2012 Windows Server, and re-connect to the workspace, we can see a new entry in databases called `Stevemartin`, exactly how we created it.
![[image-224.png]]

All done!

>[!check answer]-
>![[image-225.png]]

