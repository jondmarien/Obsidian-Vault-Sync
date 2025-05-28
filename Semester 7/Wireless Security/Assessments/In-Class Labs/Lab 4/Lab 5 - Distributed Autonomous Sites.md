---
title: Lab 5 - Distributed Autonomous Sites
author:
  - Jon Marien
created: 2025-04-01
published: 2025-04-01
tags:
  - classes
  - SYST44998
---
## **Lab 5: Centralized WLAN Architecture with Distributed Autonomous Sites Deployment**

|   |   |
|---|---|
|**Administrative Info**|   |
|Mode of delivery|Slate|
|Due|Look at slate|
|Group|Individual|
|Points|7.5|
|Time|N/A|

## **Material**
- - Cisco Packet Tracer ([https://www.netacad.com/courses/packet-tracer](https://www.netacad.com/courses/packet-tracer))
    - Lecture notes: Introduction to Lab5
    - Initial Configuration file: Lab5_Seed.pkt

## **Assignment Description and Requirements**
1. Use the slides **_Introduction to the Lab 5_** as a major guideline for this lab.
2. Use the Section D in this document to report on your activities.
3. **Screenshot** the requested steps. Name the figure using accordingly.

## **Assignment Description**
In this lab, you are receiving the Lab5_Seed.pkt file that contains an Enterprise network with two sites: headquarters and branch office. The deployment model followed by the organization was the distributed autonomous sites where the RADIUS server uses its native database for usernames and passwords. In this sense, there was no need for a LDPA database. Additionally, the design uses a centralized WLAN architecture. In this sense, the wireless controller is the client of the RADIUS server. Also, controller-based lightweight APs are used.

The headquarters is already configured (see Introduction to the Lab5) and can be used to guide you as well. The routers (R1 and R2) connecting both offices are configured using the RIP protocol. The branch office is partially configured and the **goal of the lab is to complete the configuration of the branch office and make a connectivity test with the computers of the headquarters**.

Fig. 1 shows a solution of the configuration where the system is fully connected including the wireless devices (printer and a laptop) in the branch office. Fig.2 shows a connectivity test using the ping utility from a laptop in the branch office to the AAA server in the headquarters.

The branch office uses the 192.168.1.0 (/24) network. It means that 256 addresses are supported where the .0 and the .255 are network and broadcast addresses. Additionally, the router R2 in the branch office is already configured as the 192.168.1.1 (default gateway for the branch office). Also, the VLAN 1 in the switch SW2 in the branch office is configured with the 192.168.1.2 address. The AP is also operational and named AP1. Considering the range of available IP addresses, you are free to select the ones that you want to configure the wireless controller and the RADIUS server as static ones. Note that the wireless controller in the branch office MUST BE the DHCP server. In this sense, it will assign the IP addresses to the wireless devices in the branch office as it is done at the headquarters. The security solution for the branch office to authenticate the wireless clients is the WPA2 as shown in Fig.5. If the IP address of the DNS server is asked, you can use the one of the RADIUS server in the branch office.

In this respect, your task is to configure the wireless controller (static IP address), the RADIUS server (static IP address), the printer, and the laptop of the branch office and connect them wirelessly with the enterprise wired system. Last but not least, the two offices must be connected considering the Lab5_Seed.pkt file.

![](<Semester 7/Wireless Security/Assessments/In-Class Labs/Lab 4/Attachments/Attachment.png>)
**Fig.1-Distributed Autonomous Sites with a headquarters and a branch office.**

![](<Semester 7/Wireless Security/Assessments/In-Class Labs/Lab 4/Attachments/Attachment 1.png>)
**Fig.2 - Connectivity test from the Laptop 0 in the branch office to the RADIUS server on the headquarters.**

![](<Semester 7/Wireless Security/Assessments/In-Class Labs/Lab 4/Attachments/Attachment 2.png>)
**Fig.3-Place Note**

![](<Semester 7/Wireless Security/Assessments/In-Class Labs/Lab 4/Attachments/Attachment 3.png>)
**Fig.4-Screenshot for each of the highlighted options**

![](<Semester 7/Wireless Security/Assessments/In-Class Labs/Lab 4/Attachments/Attachment 4.png>)
**Fig.5-Authetication solution in the branch office**

## **Marking Scheme**
The following screenshots are mandatory:

- A screenshot of the network fully connected as shown in Fig.1. For your design you MUST use the _place note_ as shown in Fig.3 to place your full name and student number in it.
- A screenshot of the RADIUS server with the usernames and passwords of the laptop and printer following the rule: _StudentLastName_StudentNumber_Laptop and StudentLastName_StudentNumber_Printer._ The screenshot MUST also show the wireless controller as the client. The **secret** used between the RADIUS and wireless controller MUST be _StudentLastName_StudentNumber_WC._
- A screenshot of the laptop and printer with the usernames and passwords of the laptop and printer following the rule: _StudentLastName_StudentNumber_Laptop and StudentLastName_StudentNumber_Printer._
- Three screenshots of the wireless controller showing the Wireless LANs, DHCP, and management configurations that are indicated in Fig.4 and the **_Introduction to the Lab 5_**.
- A screenshot of the connectivity test using the ping utility between the RADIUS server in the branch office to the RADIUS server in the headquarters.
- A screenshot of the connectivity test using the ping utility between the laptop in the branch office to a laptop in the headquarters. The screenshot must show the laptop chosen as shown in Fig2.

## **Report**
*Student Name: Jonathan Marien*
*Student Number: 991476393*

