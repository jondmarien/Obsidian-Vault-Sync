---
title: Lab 1 - Answers
author:
  - Jon Marien
created: 2025-02-05
published: 2025-02-05
tags:
  - classes
  - "#SYST4499"
---

| Title           | Author                       | Created           | Published         | Tags                   |
| --------------- | ---------------------------- | ----------------- | ----------------- | ---------------------- |
| Lab 1 - Answers | <ul><li>Jon Marien</li></ul> | February 05, 2025 | February 05, 2025 | [[#classes\|#classes]] |
# Lab 1: Cover the Encryption and Legacy Systems

## Materials
- Wireshark.
- `File1.pcap` & `File2.pcap`.
## Questions
1. Open the File1.PCAP file and click on one of the beacons with the source address 00:1A:1E:94:4C:32 (Line#3). 
	- Locate and expand the IEEE 802.11 Wireless LAN Management Frame section. 
	- After performing a detailed analysis of all the fields and subfields of it, respond the following question: 
		- What is the cipher that is used to avoid loss of confidentiality over the wireless transmission?
		- **CWSP-AES - Advanced Encryption Standard**![](Lab%201%20-%20Answers-February-5th-2025-14-15-10.webp)

2. Open the File1.PCAP file and click on one of the beacons with the source address 00:1A:1E:94:4C:31 (Line#2). 
	- Locate and expand the IEEE 802.11 Wireless LAN Management Frame section. 
	- After performing a detailed analysis of all the fields and subfields of it, respond the following question: 
		- What is the cipher that is used to avoid loss of confidentiality over the wireless transmission?
		- **CWSP-TKIP - Temporal Key Integrity Protocol**![](Lab%201%20-%20Answers-February-5th-2025-14-17-12.webp)

3. Open the File2.PCAP file and click on the Line#1. 
	- Locate and expand the IEEE 802.11 Wireless LAN Management Frame section. 
	- After performing a detailed analysis of all the fields and subfields of it, respond the following question: 
		- What is the legacy nonstandard technology used to secure the transmission?
		- **CISCO CKIP - Cisco Key Integrity Protocol**![](Lab%201%20-%20Answers-February-5th-2025-14-18-48.webp)
## Answers
1. What is the cipher that is used to avoid loss of confidentiality over the wireless transmission?
	The cipher that is used to avoid loss of confidentiality over the wireless transmission is: **CWSP-AES - Advanced Encryption Standard**.
2. What is the cipher that is used to avoid loss of confidentiality over the wireless transmission?
	The cipher that is used to avoid loss of confidentiality over the wireless transmission is: **CWSP-TKIP - Temporal Key Integrity Protocol**.
3. What is the legacy nonstandard technology used to secure the transmission?
	The legacy non-standard technology used to secure the transmission is: **CKIP - Cisco Key Integrity Protocol**.