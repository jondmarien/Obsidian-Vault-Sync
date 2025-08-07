---
title: Appendix K - Mobile Device Penetration Testing Methodology
author:
  - Jon Marien
created: 2025-04-30
published: 2025-04-30
tags:
  - skillsontario
  - competitions
  - certifications
---

| Title                                                      | Author                       | Created        | Published      | Tags                                                                                                       |
| ---------------------------------------------------------- | ---------------------------- | -------------- | -------------- | ---------------------------------------------------------------------------------------------------------- |
| Appendix K - Mobile Device Penetration Testing Methodology | <ul><li>Jon Marien</li></ul> | April 30, 2025 | April 30, 2025 | [[#skillsontario\|#skillsontario]], [[#competitions\|#competitions]], [[#certifications\|#certifications]] |

# Mobile Device Penetration Testing Methodology

## Objective
The labs in this module are designed to make you familiar with pen testing methodology to audit a wireless network infrastructure consisting of mobile devices by creating a malicious apk file and executing it.

## Scenario
By finding a secure spot in the vicinity of a building, hackers can exploit a wireless signal and gain entry into an organization’s internal network. Starting from the SSID of the wireless network to its strength in different areas of its radius, everything is critical to wireless security. Password for the wireless signal, encryption methodology and protocols used, devices interacting with the network are all potential weak points for the hackers to exploit. As a wireless penetration tester, you have to ensure that all the vulnerable points of a network are either secured or strengthened. You also have to identify the users who can easily be enticed to click on links or execute the malicious files you built.

# Exercise 1: Gaining Complete Access to an Android Device Using SpyNote

## Scenario
SpyNote is a client/server application developed in Java Android for the client side and in Java/Swing for the Server side. The goal of the application is to provide the control of the Android system remotely and retrieve information from it. 

Personnel working in an organization might carry their mobile devices to the workplace and use them to access enterprise data and systems. Hence, it is evident that mobile devices contain sensitive information related to organizations. This might open doors for attackers to perform attacks and get control over the personnel’ devices and access them to gain sensible information related to the organizations. This might reveal information related to the policies of the organization, payrolls of its personnel, HR policies, quotations signed by clients, and so on.  

Being a penetration tester or an information security auditor, you should have knowledge of how to develop a malicious apk file and merge it with a genuine apk file. When this file is shared with an employee in an organization and he/she installs it, the apk gives complete access to the pentester.  

In this lab, you will learn how to gain remote access to a device by using a remote access Trojan.

# Steps
## Step 1:
### Windows Server 2019
In this VM, we created a malicious `Twitter.apk` file by using the real `.apk` file for Twitter, and patched it with a malicious application, a backdoor using a trojan. The file was outputted in a build folder, and we renamed it to `Twitter.apk` to seem more genuine. Then, we moved over to the other VM

## Step 2:
### Marketing Dept
In this VM, we ran an AVD, and enabled installation of `APKs` from unknown sources. Then, we browsed the network and accessed the Windows Server 2019 files. We copied over the malicious `Twitter.apk` file and ran `adb install Twitter.apk` on the AVD. 

Then, we browse to the app launcher, and launch `Twitter`, the application. After a few seconds, the application disappears! This is okay, as the `SpyNote Client` on the Windows Server has established a remote connection with the device. Now we swap back over.

## Step 3:
### Windows Server 2019
Now, back in Windows Server, in `SpyNote Client`, we see the device details in the connection list:
![[image-189.png]]

By right clicking on the device, we get options for many actions/settings:
![[image-190.png]]

You can see info about the phone, change the volume of alerts on the phone, use or modify the actions in the phone bar, and even fool around with the Device Policy Manager.
![[image-191.png]]

We then check the filesystem, and download a file to test. Then, we check the Contacts Manager, then the SMS Manager.

> [!check answer]-
> ![[image-192.png]]