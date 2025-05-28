---
title: Chapter 1 - WLAN Security Overiew
author:
  - Jon Marien
created: 2025-01-19
published: 2025-01-19
tags:
  - classes
  - SYST4499
---

| Title                             | Author                       | Created          | Published        | Tags                                             |
| --------------------------------- | ---------------------------- | ---------------- | ---------------- | ------------------------------------------------ |
| Chapter 1 - WLAN Security Overiew | <ul><li>Jon Marien</li></ul> | January 19, 2025 | January 19, 2025 | [[#classes\|#classes]], [[#SYST4499\|#SYST4499]] |

# Outline
- Standards organizations
- 802.11 networking basics
- 802.11 security basics
- 802.11 security history

## Standards Organizations
- The Wi-Fi Alliance
- ISO (International Organization for Standardization)
- IEEE (Institute of Electrical and Electronics Engineers)
- ISOC (Internet Society)

### The Wi-Fi Alliance
- Global nonprofit industry association of about 600 member companies.
- Devoted to promoting the growth of WLANs.
- Ensures the certification testing.

	![|170](Chapter01_2.png)
### ISO
- Created the Open Systems Interconnection (OSI) Model.
- OSI is an architectural model for data communication.

	![|122](Chapter01_4.png)

OSI Model:
	![|280](Chapter01_5.png)

## IEEE
- Institute of Electrical and Electronics Engineers
- Create standards for compatibility and coexistence between networking equipment
	- Not jus for wireless networking equipment
- Mission is to *"foster technological innovation and excellence for the benefit of humanity"*.

	![|175](Chapter01_6.jpg)

	![|346](2169FB3D559179C720.jpg)

### ISOC

RFC 3935
  * “…to produce high quality relevant technical and engineering document. …These documents include protocol standards, best current practices, and informational documents of various kinds.”
* Internet Engineering Task Force  (**IETF**)
* Internet Architecture Board (__IAB__)
* Internet Corporation for Assigned Names and Numbers (__ICANN__)
* Internet Engineering Steering Group (__IESG__)
* Internet Research Task Force (__IRTF__)E

	![|439](Chapter01_8.png)

## 802.11 Networking Basics
- The OSI Model
- TCP/IP
- Routing
- Switching
*A solid understanding of networking fundamentals is mandatory for an understanding 802.11 networking and security.*

## 802.11 Security Basics
- Data privacy
- Authentication, Authorization, and Accounting (AAA)
- Segmentation
- Monitoring
- Policy

### Data Privacy
For wireless networks, data is transmitted openly and freely, proper protection is needed to ensure privacy. **Privacy is achieved by strong encryption!!**

- **Encryption technologies are:**
	- Used to obscure the information.
- **Terminology**
	- *Cipher*
		- An algorithm used to perform the encryption.
	- *Cryptology*
		- Field of science that covers the encryption & decryption techniques.
	- *Cryptanalysis*
		- The science of decrypting the cipher-text without the knowledge of the key or cipher

**Data Encryption Process**
	![|439](Chapter01_9.jpg)

### AAA (Authentication, Authorization, and Accounting)
- Authentication
	- Verification of user identity and credentials
	- Users must identify themselves by presenting usernames and passwords, etc.
	- **MFA** (Multifactor Authentication) is the most secure approach.
	- This is the first step, so *it takes place first*!
- Authorization
	- Determines if the device or use is authorized to have access to network resources.
	- It might be device, time, and location-dependent.
	- It takes place *after authentication*.
- Accounting
	- It keeps a historical trail of who used what, when, where, and how!
	- Keeping an accounting trail is a requirement in most industries.
	- This the final step, *it takes place last*!

### Segmentation
- Process of separating *user traffic* within the network.
- As important as *strong encryption* and *AAA*.
- It can be achieved through the use of *routers*, *VPNs*, and *VLANs*.
- For 802.11, the most common technique is the creation of *WVLANs*.
  
### Monitoring
- It is important for the sake of:
	- Performance analysis:
		- Certify that the system is responding as planned.
	- Security analysis:
		- Certify that the system is *secure against attacks* and also *intrusion-free*.

- To monitor malicious wireless activity, *wireless IDS* and *wireless IPS* should be used!
- *WIDS* and *WIPS* classify valid and invalid devices on the network.
- *WIPS* can also mitigate attacks from rogue APs and rogue users.
  
### Policy
- Without security policies, any effort to secure the network is *worthless*.
- It must be clearly defined and enforced to solidify the effectiveness of the WLAN security components.

## 802.11 Security History
![|450](Chapter01_10.png)