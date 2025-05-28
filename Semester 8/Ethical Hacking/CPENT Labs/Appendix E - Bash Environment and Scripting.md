---
title: Appendix E - Bash Environment and Scripting
author:
  - Jon Marien
created: 2025-05-01
published: 2025-05-01
tags:
  - skillsontario
  - competitions
  - certifications
---

| Title                                       | Author                       | Created      | Published    | Tags                                                                                                       |
| ------------------------------------------- | ---------------------------- | ------------ | ------------ | ---------------------------------------------------------------------------------------------------------- |
| Appendix E - Bash Environment and Scripting | <ul><li>Jon Marien</li></ul> | May 01, 2025 | May 01, 2025 | [[#skillsontario\|#skillsontario]], [[#competitions\|#competitions]], [[#certifications\|#certifications]] |

# Bash Environment and Scripting

# Exercise 1: Basic BASH Queries

## Objectives

- Create basic BASH queries, extract data, and explore the features and components of BASH

# Steps

## Step 1

### Ubuntu OS

- create password lists
	- exists in ~
	- `cut -d' ' -f2 file.txt` to select all single words
	- `cat /proc/cpuinfo` to see cpu info.

![[image-226.png]]

![[image-227.png]]

![[image-228.png]]

to view all files modified in the last 24 hours: `sudo find /home -mtime -1`
![[image-229.png]]

![[image-230.png]]

converts 'A' into hex:
![[image-231.png]] 

to convert hex to ascii:
![[image-232.png]]

to output in binary:
![[image-233.png]]

`sudo egrep -a -o '\b[[:print:]]{2,}\b' somefile.exe - string search
`
for example, could show all files in `ifconfig`:
![[image-234.png]]

`sudo egrep -a -o '\b[[:print:]]{2,}\b' /sbin/ifconfig | sort -u`
![[image-235.png]]
![[image-236.png]]

> [!check answer]-
> i got it right, but they said no lol:![[image-237.png]]

# Exercise 2: Basic cURL Queries

## Objectives
- Create basic cURL queries, extract the data, and explore the features and components of cURL
- **cURL** is a command line tool and a library that can be used to receive and send data between a client and a server or any two machines connected over the internet. It supports a wide range of protocols such as HTTP, FTP, IMAP, LDAP, POP3, and SMTP.
-  Due to its **versatile nature**, cURL is used in many applications and for many use cases. For example, the command line tool can be used to download files, testing Application Program Interfaces (APIs), and debugging network problems. In this lab, we shall look at how the cURL command line tool can be used to perform various tasks.
-  As a penetration tester, you need to be familiar with this tool. We will cover some of the usage examples in this lab, but this tool can be used in many ways.
-  In this exercise, we will review the different methods of extracting data using **cURL**.
# Step

## Step 1

### Ubuntu OS
In this form, the cURL tool is acting as a simple client. We have the capability to do this using **Telnet** and **netcat**, but the tool makes it in one go.
![[image-238.png]]

`curl` can download with flag `-o`, and can download a partially complete file with `-C`.
![[image-239.png]]

Now, we swap to the `bash-web` machine.
## Step 2

### Bash Web
we login with `root` and `owaspbwa`:
![[image-240.png]]

we can use the following `dd` command to create a file:
`dd if=/dev/zero of=testfile_10MB bs=10485760 count=1
![[image-241.png]]

copy the file to the root folder for the web server, verify file exists:
![[image-242.png]]

then, copy it:
![[image-243.png]]

Now, back to the bash machine (ubuntu).
## Step 3

### Ubuntu
Now, we can download the file:
![[image-244.png]]

As per the RFC, to request a resource such as a web page or to submit data to a server, an HTTP client (such as a browser or `cURL`) makes an HTTP request to the server. The server responds with an HTTP response, which contains the "contents" of that page. An example of this is shown in the following screenshot.
![[fxou1bnz.jpg]]
HTTP requests contain the request method, URL, some headers, and some optional data as part of the "request body." The request method controls how a certain request should be processed. The most common types of request methods are `GET` and `POST`. Typically, we use `GET` requests to retrieve a resource from the server and `POST` to submit data to the server for processing. `POST` requests generally contain some data in the request body, which the server can use.

HTTP responses are similar and contain the status code, some headers, and a body. The body contains the actual data that clients can display or save to a file. The status code is a three-digit code, which tells the client if the request succeeded or failed, and how to proceed further. Common status codes are 2xx (success), 3xx (redirect to another page), and 4xx/5xx (for errors).

to see the request headers and connection details, you can `curl` the web server:
![[image-245.png]]

To perform the **recon** without seeing the output of errors, we can use the **-s** option, shown here, and redirect to `/dev/null`: 
`curl -svo /dev/null http://192.168.177.200/testfile_10MB`
![[image-246.png]]

This results in sending the response and garbage html data to `/dev/null`, essentially showing us just the connection data. Useful!

![[image-247.png]]
This does the same but hides the progress bar! `-S`.

![[image-248.png]]

ran out of time rip
![[image-249.png]]
![[image-250.png]]
![[image-251.png]]
![[image-252.png]]
![[image-253.png]]
![[image-254.png]]

# Exercise 3: Log Analysis with BASH

## Objectives

- Create BASH queries, extract data from log files, and modify log data

![[image-255.png]]

![[image-256.png]]

![[image-257.png]]

![[image-258.png]]

![[image-259.png]]

![[image-260.png]]
![[image-261.png]]

![[image-262.png]]

![[image-263.png]]

![[image-264.png]]

![[image-265.png]]

![[image-266.png]]