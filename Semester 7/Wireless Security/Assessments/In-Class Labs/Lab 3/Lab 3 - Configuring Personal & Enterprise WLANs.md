---
title: Lab 3 - Configuring Personal & Enterprise WLANs
author:
  - Jon Marien
created: 2025-04-01
published: 2025-04-01
tags:
  - classes
  - SYST44998
---
# **Lab. 3: Configuring Personal & Enterprise WLAN systems**

|                         |               |
| ----------------------- | ------------- |
| **Administrative Info** |               |
| Mode of delivery        | Slate         |
| Due                     | Look at slate |
| Group                   | Individual    |
| Points                  | 7.5           |
| Time                    | N/A           |

## **Material(s)**

- - Cisco Packet Tracer ([https://www.netacad.com/courses/packet-tracer](https://www.netacad.com/courses/packet-tracer))
    - Lecture notes: Introduction to Lab3

## **Assignment Requirements**
1. Use the slides **_Introduction to the Lab 3_** as a major guideline for this lab.
2. Use the Section D in this document to report on your activities.
3. **Screenshot** every step of the process. Name the figure accordingly.
4. Submission must be in doc, docx, or pdf. Out of that, 2.0 marks will be deducted.

### **PART 1: WPA Personal**
- Deploy and configure a WLAN for a SOHO environment with four (4) laptops.
- Use DHCP to provide IP connectivity at the AP device
- Test the network connectivity by pinging from the laptop _1 to 2_, _2 to 3_, and _3 to 4_. Show the laptops (IP addresses) in the screenshots.
- Select a laptop and connect it to the AP.
- Change the name of the AP remotely using the AP’s Linksys to your _full name without space_.

### **PART 2: WLAN Enterprise**
- Create an enterprise-based BSS design with four (4) laptops
- Deploy the AP and configure it. Make it to point to the Server
- Configure the Server and make it point to the AP. Test the network connectivity between the Server and the AP. Screenshot it.
- Populate the Server with the info of all users (use your _fullname+counter_) for each profile. Example, _ABC1_, _ABC2_, etc. Screenshot the profile ensuring that all the 4 users are shown.
- Go to the laptops and create their profiles
- Test the connectivity among the laptops: _1 to 2_, _2 to 3_, and _3 to 4_. Screenshot all of them (ping results).

## **Marking Scheme**

|           |              |
| --------- | ------------ |
| **Items** | **Max Mark** |
| Part 1    | 3.0          |
| Part 2    | 4.5          |

## **Report**

*Student Name: Jonathan Marien*
*Student Number: 991476393*

##### **PART 1: WLAN Personal**

Setup:
![[image-157.png]]

Laptop0 IP Address:
![[image-158.png]]

Or we can use *ipconfig*:
![[image-159.png]]

Pinging from `Laptop0` to `Laptop1`:
![[image-160.png]]

Set the SSID:
![[image-161.png]]

##### **PART 2: WLAN Enterprise**

Setting up cabling:
![[image-162.png]]

Setting up WPA2 Enterprise (w/ RADIUS Server and shared secret):
![[image-163.png]]

Populate server info:
![[image-164.png]]

Turning on AAA Service and adding a network configuration, plus user setup:
![[image-166.png]]

Ping from the server to the AP:
![[image-167.png]]

Attempted to connect to AP from laptop, need to create a profile:
![[image-168.png]]

Advanced setup mode:
![[image-169.png]]

Chose WPA-Enterprise for Security level:
![[image-170.png]]

Used the `user1` and `user1_pass` for profile details:
![[image-171.png]]

Saved Profile:
![[image-172.png]]
![[image-173.png]]

I couldn't get the final connection to work from the Laptop the Wireless Router:
![[image-174.png]]

