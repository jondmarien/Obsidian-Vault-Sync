---
title: Module 3 - Open Source Intelligence
author:
  - Jon Marien
created: 2025-05-11
published: 2025-05-11
tags:
  - skillsontario
  - competitions
  - certifications
  - classes
---

| Title                               | Author                       | Created      | Published    | Tags                                                                                                       |
| ----------------------------------- | ---------------------------- | ------------ | ------------ | ---------------------------------------------------------------------------------------------------------- |
| Module 3 - Open Source Intelligence | <ul><li>Jon Marien</li></ul> | May 11, 2025 | May 11, 2025 | [[#skillsontario\|#skillsontario]], [[#competitions\|#competitions]], [[#certifications\|#certifications]] |

---

# Open Source Intelligence (OSINT) Methodology

## Objective
The objective of this lab is to help students learn different techniques to gather information about a company; you will learn how to:

- Extract a company's information
- Perform network tracerouting
- Perform passive OS fingerprinting

## Scenario
Penetration testing is much more than just running exploits against vulnerable systems. In fact, a penetration test begins before penetration testers have even contacted the victim's systems. Rather than blindly throwing out exploits and praying that one of them returns a shell, a penetration tester meticulously studies the environment for potential weaknesses and their mitigating factors. By the time a penetration tester runs an exploit, he or she is nearly certain that it will be successful. Since failed exploits can in some cases cause a crash or even damage to the target system, or at the very least make the target un-exploitable in the future, penetration testers won't get the best results, or deliver the most thorough report to their clients, if they blindly turn an automated exploit machine on the target network with no preparation.

A penetration tester collects the information of a company such as internal and external links of the company's website, people working in the company, geographical location, DNS information, competitive intelligence, network range etc. This information is collected in order to search for vulnerabilities, to exploit and sniff valuable information. In order to become an expert penetration tester and security auditor, you must know various techniques to gather a company's information.

# Steps

## Step 1

### Windows Server 2019
First, we open google chrome, and browse to `osintframework.com`, and open up this specific graph, and click on "Domain Dossier".
![[image-277.png]]

That leads us to a new page:
![[image-278.png]]

We can check off the records we want scanned, and enter in a site like so, @`certifiedhacker.com`:
![[image-279.png]]
![[image-280.png]]
![[image-281.png]]

We get all of the options we selected to view.

Now, we browse to `Robtex`, which is a way to investigate IP numbers, domain names, etc.
![[image-282.png]]
![[image-283.png]]

> [!answer]-
> ![[image-284.png]]

Done Part 1!

# Exercise 2: Footprinting a Target using Maltego

## Scenario
Maltego is a footprinting tool used to gather maximum information for the purpose of ethical hacking, computer forensics, and pentesting. It provides a library of transforms to discover data from open sources and visualizes that information in a graph format, suitable for link analysis and data mining. Maltego provides you with a graphical interface that makes seeing these relationships instant and accurate, and even making it possible to see hidden connections.

Here, we will gather a variety of information about the target organization using Maltego.

# Steps

## Step 1

### Parrot OS
First thing we need to tackle is launching maltego! 

I already had a Maltego account, so I signed in, and now we can get started.
First, we create a new graph:
![[image-285.png]]

We then drag a `website` component and point it to `www.certifiedhacker.com`
![[image-286.png]]

Once done, if we right-click on the component, and choose **All Transforms -> To Domains [DNS]**, we get some domains corresponding to the website we picked.
![[image-287.png]]

The UI is a bit small, but we can see all the other subdomains that are valid. The Transform -> To DNS Name [Using Name Schema] attempts to test various names against known name schemas to try and identify specific subdomains.
![[image-288.png]]
Attackers attempt to simulate various exploitation techniques to gain sensitive information related to the resultant name schemas. For example, an attacker may implement a brute-force or dictionary attack to log in to **ftp.certifiedhacker.com** and gain confidential information.

Then, if we try again to Transform the data, but this time -> To DNS Name - SOA (Start of Authority), we get some new information:
![[image-289.png]]

If we remove the name schemas, we get an easier view:
![[image-290.png]]
By extracting the SOA related information, attackers attempt to find vulnerabilities in their services and architectures and exploit them.

After we log that information, we can get more screen real-estate and attempt to transform the MX Servers:
![[image-291.png]]
By identifying the mail exchanger server, attackers attempt to exploit the vulnerabilities in the server and, thereby, use it to perform malicious activities such as sending spam e-mails.

Now we can attempt to transform the data into resolving the name servers!
![[image-292.png]]
By identifying the primary name server, an attacker can implement various techniques to exploit the server and thereby perform malicious activities such as DNS Hijacking and URL redirection.

After that step, we delete all the items except the original website component. We have more to do! We attempt to Transform -> To IP Address [DNS].
![[image-293.png]]
This displays the IP address of the website. By obtaining the IP address of the website, an attacker can simulate various scanning techniques to find open ports and vulnerabilities and, thereby, attempt to intrude in the network and exploit them.

We can now attempt to get the city and country of the IP address by selecting the Transform -> To location [city, country].
![[image-294.png]]
By obtaining the information related to geographical location, attackers can perform social engineering attacks by making voice calls (**vishing**) to an individual in an attempt to leverage sensitive information.

Apart from the aforementioned methods, you can perform footprinting on the critical employee from the target organization to gather additional personal information such as email addresses, phone numbers, personal information, image, alias, phrase, etc.

Apart from the transforms mentioned above, other transforms can track accounts and conversations of individuals who are registered on social networking sites such as Twitter. Extract all possible information.

By extracting all this information, you can simulate actions such as **enumeration, web application hacking, social engineering,** etc., which may allow you access to a **system or network, gain credentials,** etc.

**Question 3.2.1**

Use the Maltego tool in the Parrot machine to gather information about the target organization (www.certifiedhacker.com). Enter the domain administrator email associated with the domain certifiedhacker.com.

To answer this question, I transformed the domain into "To Email Address [from whois]" and received these:
![[image-295.png]]
Both seem to be incorrect, though? Let's continue.

By Transforming the data into "To Email Address [using Search Engine]", we get more emails:
![[image-296.png]]
But still, they do not work.

If we go back to near beginning of the report, when we transform the original MX records after doing the DNS transformations, we see:
![[image-316.png]]
I would wager to guess that this is the correct answer. TODO: Try before submission

TODO: New Pics to add:
![[image-317.png]]

**Question 3.2.2**

Use the Maltego tool in the Parrot machine to gather information about the target organization (www.certifiedhacker.com). Enter the geographical location of the domain certifiedhacker.com.

To answer this question, we actually already have this information :))

> [!answer]-
> ![[image-297.png]]
