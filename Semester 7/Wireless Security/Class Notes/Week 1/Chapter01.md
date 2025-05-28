SYST44998: Wireless Security

Chapter 1: WLAN Security Overview

![](Chapter01_0.png)

# Outline

- Standards organizations
- 802\.11 networking basics
- 802\.11 security basics
- 802\.11 security history

![](Chapter01_1.png)

# Learning Outcomes

Explain how security information can be gathered using various techniques \( <span style="color:#ff0000">1</span> \)

# Standards Organizations

- The Wi\-Fi Alliance
- International Organization for Standardization \( __ISO__ \)
- Institute of Electrical and Electronics Engineers \( __IEEE__ \)
- Internet Society \( __ISOC__ \)

---

The Wi-Fi Alliance is a global, nonprofit industry association of about 600 member companies devoted to promoting the growth of WLANs.

The International Organization for Standardization (ISO) created the Open Systems Interconnection (OSI) model, which is an architectural model for data communications. The Institute of Electrical and Electronics Engineers (IEEE) creates standards for compatibility and coexistence between networking equipment, not just wireless networking equipment. However, in this book we are concerned primarily with its role in wireless networking and more specifically wireless security. The Internet Engineering Task Force (IETF) is responsible for creating Internet standards. Many of these standards are integrated into the wireless networking and security protocols and standards. ISO is not a mistyped acronym. It is a word derived from the Greek word isos, meaning equal. The IEEE’s mission is to “foster technological innovation and excellence for the benefit of humanity.” The Internet Society (ISOC) is made up of several groups as you see in this slide.

<span style="color:#ff0000">Wi-Fi Alliance</span>
- Global\, nonprofit industry association of about 600 member companies
- Devoted to promoting the growth of WLANs
- Responsible for ensuring the interoperability of WLAN products by providing certification testing

![](Chapter01_2.png)

---

![](Chapter01_3.jpg)

https://www\.androidheadlines\.com/2018/05/alleged\-galaxy\-a8\-star\-gets\-certified\-by\-the\-wi\-fi\-alliance\.html

---
<span style="color:#ff0000">International Organization for Standardization \(</span>  <span style="color:#ff0000"> __ISO__ </span>  <span style="color:#ff0000">\)</span>

Created the  <span style="color:#7030a0">Open Systems Interconnection</span>  \(OSI\) model
<span style="color:#0070c0">OSI</span>  is an architectural model for data communications\.

![](Chapter01_4.png)

---

![](Chapter01_5.png)

---

* <span style="color:#ff0000">Institute of Electrical and Electronics Engineers \(</span>  <span style="color:#ff0000"> __IEEE__ </span>  <span style="color:#ff0000">\) </span>
* Create standards for compatibility and coexistence between networking equipment
  * Not just wireless networking equipment
* Mission is to “ _foster technological innovation and excellence for the benefit of humanity_ \.”

![](Chapter01_6.jpg)

---

<span style="color:#ff0000"> __https://t1\.daumcdn\.net/cfile/tistory/2169FB3D559179C720__ </span>

---
* <span style="color:#ff0000">Internet Society \(</span>  <span style="color:#ff0000"> __ISOC__ </span>  <span style="color:#ff0000">\)</span>
* RFC 3935
  * “…to produce high quality\, relevant technical and engineering document\. …These documents include protocol standards\, best current practices\, and informational documents of various kinds\.”
* Internet Engineering Task Force \( __IETF__ \)
* Internet Architecture Board \( __IAB__ \)
* Internet Corporation for Assigned Names and Numbers \( __ICANN__ \)
* Internet Engineering Steering Group \( __IESG__ \)
* Internet Research Task Force \( __IRTF__ \)
---

![](Chapter01_8.png)

---

# 802.11 Networking Basics

The OSI Model

TCP/IP

Routing

Switching

_A solid understanding of networking fundamentals is mandatory for an understanding 802\.11 networking and security\._

---

Students will need a solid understanding of Networking in general to be able to better understand 802.11 networking and security.

# 802.11 Security Basics

- Data privacy
- Authentication\, authorization\, and accounting \(AAA\)
- Segmentation
- Monitoring
- Policy

<span style="color:#ff0000">Data privacy</span>
For wireless networks\, data is transmitted openly and freely\, proper protection is needed to ensure privacy
Privacy is achieved by strong encryption

<span style="color:#ff0000">Data privacy</span>
* <span style="color:#7030a0">Encryption technologies</span>
  * Used to obscure the information
* <span style="color:#7030a0">Terminology:</span>
  * Cipher:
    * An algorithm used to perform the encryption
  * Cryptology:
    * Field of science that covers the encryption & decryption techniques

_Encryption & decryption processes_
![](Chapter01_9.jpg)

<span style="color:#ff0000">http://smartcardpoint\.com/all\-about\-the\-data\-encryption\-process/</span>
<span style="color:#ff0000">Data privacy</span>
<span style="color:#7030a0">Cryptanalysis: </span> The science of decrypting the cipher\-text without the knowledge of the key or cipher

<span style="color:#ff0000">Authentication\, authorization\, and accounting \(AAA\)</span>
  
* <span style="color:#7030a0">Authentication</span>
  * Verification of user identity and credentials
  * Users must identify themselves by presenting usernames and passwords\, etc\.
  * _Multifactor\-authentication _ is the most secure approach\.

* <span style="color:#7030a0">Authorization </span>
  * Determines if the device or user is authorize to have access to network resources
  * It might be device\-\, time\-\, and location\-dependent
  * It takes place after authentication

* <span style="color:#7030a0">Accounting  </span>
  * It keeps a historical trail of who used what\, when\, where\, and how\.
  * Keeping an accounting trail is a requirement is most industries\.

<span style="color:#ff0000">Segmentation</span>
- Process of separating user traffic within the network
- As important as  _strong encryption_  and  _AAA_
- It can be achieved through the use of routers\, VPNs\, and VLANs
- For 802\.11\, the most common technique is the creation of  _WVLANS_

* <span style="color:#ff0000">Monitoring</span>
* It is important for the sake of:
	* <span style="color:#7030a0">Performance analysis:</span>
	    * Certify that the system is responding as planned
	- <span style="color:#7030a0">Security analysis</span>
		- Certify that the system is secure against attacks and intrusion\- free

<span style="color:#ff0000">Monitoring</span>
- To monitor malicious wireless activity\,  <span style="color:#7030a0">wireless IDS </span> and  <span style="color:#7030a0">wireless IPS</span>  should be used
- _WIDS_  and  _WIPS_  classify valid and invalid devices on the network
- WIPS can also mitigate attacks from rogue AP and rogue users

<span style="color:#ff0000">Policy </span>
- Without security polices any effort to secure the network is worthless\.
- It must be clearly defined and enforced to solidify the effectiveness of the WLAN security components\.
# 802.11 Security History

![](Chapter01_10.png)

