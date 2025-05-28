---
title: Chapter 2 - Legacy Security
author:
  - Jon Marien
created: 2025-01-16
published: 2025-01-16
tags:
  - classes
  - SYST4499
---

| Title                       | Author                       | Created          | Published        | Tags                                             |
| --------------------------- | ---------------------------- | ---------------- | ---------------- | ------------------------------------------------ |
| Chapter 2 - Legacy Security | <ul><li>Jon Marien</li></ul> | January 16, 2025 | January 16, 2025 | [[#classes\|#classes]], [[#SYST4499\|#SYST4499]] |

# Outline
- [Legacy Security (802.11)](Chapter%202%20-%20Legacy%20Security.md#Legacy%20Security%20(802.11))
- [Authentication](Authentication%20&%20Authorization.md#Authentication)
- [Wired Equivalent Privacy (WEP) Encryption](#Wired%20Equivalent%20Privacy%20(WEP)%20Encryption)
- [Virtual Private Networks (VPNs)](#Virtual%20Private%20Networks%20(VPNs))
- [MAC Filters](#MAC%20Filters)
- [SSID Cloaking/Hiding](#SSID%20Cloaking/Hiding)
- [SSID Segmentation](#SSID%20Segmentation)

## Legacy Security (802.11)
- It allows legacy client access.
- It provides backward compatibility with exiting equipment.
- It can be the weak spot of the network.

- Standard Legacy 802.11 security means:
	- Open System Authentication, Shared Key Authentication, WEP Encryption.
- Non-Standard Legacy 802.11 security means:
	- VPN over Wireless, MAC Filtering, SSID Segmentation, SSID Cloaking/Hiding.

## Legacy Authentication
- **Methods**
	- Open System Authentication
	- Shared Key Authentication
		- Wired Equivalent Privacy (WEP) Encryption
		- Pre-Shared Keys
- **Status**: Deprecated - **DO NOT USE THESE**

### Open System Authentication
- Two-way exchange between the client STAs and the AP:
	- Client STA sends an authentication request.
	- AP then sends an authentication response.
- It can use WEP for data encryption after authentication

### OS-Auth Messages
![](Chapter%202%20-%20Legacy%20Security-January-16th-2025-17-08-15.webp)

**Authentication Methods: Radio and User ^ v**
#### OSA and 802.11X/EAP Authentication
![](Chapter%202%20-%20Legacy%20Security-January-16th-2025-17-08-54.webp)

### Shared Key Authentication
- It uses WEP encryption for authentication.
- Client STA and AP should be configured with the static WEP key.
- Authentication will not work if the keys do not match.

#### SK-Auth Messages
![](Chapter%202%20-%20Legacy%20Security-January-16th-2025-17-18-09.webp)

##### SK-Auth: **Weaknesses**
- If the cleartext challenge phrase and encrypted challenge phrase in the response is captured, then the static WEP key *might* be derived
![](Chapter%202%20-%20Legacy%20Security-January-16th-2025-17-19-37.webp)

### Wired Equivalent Privacy (WEP) Encryption
- Layer 2 encryption method
- Use ARC4 (**RC4, Rivest Cipher 4, "Alleged RC4**) 
- Encrypts the **layers 3-7** & **LLC sublayer**
	- Payload of 802.11 data frame
		- MAC Service Data Unit (MSDU)

- Can use either a 40-bit or 104-bit user-supplied key
- Prepends a 24-bit **Initialization Vector (IV)** to user's key

![](Chapter%202%20-%20Legacy%20Security-January-16th-2025-17-33-51.webp)

- IV is sent in cleartext and new IV is created for every frame.
- There are "**only**" **16,777,216** possible IVs.
- Overtime, IVs are repeated.

- Static WEP key can be entered in hex or ASCII characters
- Some APs and STAs support up to 4 keys
- Use or select the default transmission key.
![](Chapter%202%20-%20Legacy%20Security-January-16th-2025-17-39-28.webp)

#### STAs and AP Encryption and Decryption
![](Chapter%202%20-%20Legacy%20Security-January-16th-2025-17-40-28.webp)
#### WEP Services
- [Data Integrity](#Data%20Integrity)
- [Confidentiality](#Confidentiality)
- [Access Control WEP](#Access%20Control%20WEP)
##### Data Integrity
A data integrity checksum known as the **Integrity Check Value (ICV)** is computed on data before encryption and used to prevent data from being modified.
##### Confidentiality
The primary goal of confidentiality was to provide data privacy by encryption the data before transmission.
##### Access Control WEP
Client stations that do not have the same matching static WEP key as an access point are refused access to network resources.

#### WEP Encryption Process
- RC4- Rivet Cipher
	- Stream Cipher
![](Chapter%202%20-%20Legacy%20Security-January-16th-2025-17-41-33.webp)

#### WEP Weaknesses
It has been deprecated since it is easily cracked using **freeware**!

### Temporal Key Integrity Protocol (TKIP)
- Designed to replace the WEP until strong encryption was available.
- No need for legacy equipment replacement, but a **firmware upgrade** instead.
	- Also based on ARC4 Encryption/Decryption.

- Temporal Keys
	- Uses dynamic keys instead of static ones.
- Sequencing
	- Uses a TKIP sequence counter (TSC) to avoid replay attacks.
- Key Mixing
	- Two-phase cryptographic mixing process to produce a stronger seed to ARC4.
- Enhanced data integrity
	- Uses a stronger data integrity check known as **Messaged Integrity Code (MIC)** < same as **MAC**.
- TKIP Countermeasures (IF MIC FAILS)
	- Alarm is raised!
		- Logging
		- 60-sec shutdown
		- New temporal keys
- Easily cracked with freeware tools

### MAC Filters
- Almost all wireless APs implement access control
	- Through **Media Access Control (MAC)** address filtering
- Implementing restrictions
	- A device can be *permitted* into the network
	- A device can be *prevented* from the network
- Vulnerable solution since MAC can be easily spoofed and impersonated.

### Virtual Private Networks (VPNs)
- No longer recommended practice for WLAN security, but often implemented since the VPN server is already deployed in the wired network.
- The solution calls for a Firewall (FW) between the WLAN client and the VPN server
	- FW allows only VPN traffic to pass
- VPN client encrypts (decrypts) traffic which is decrypted (encrypted) by the VPN server.

![](Chapter%202%20-%20Legacy%20Security-January-16th-2025-17-56-03.webp)

- VPN suffers from two major drawbacks for WLAN security
	- Configuration complexity
	- Scalability
- **Recommendations**
	- For remote access, when client STAs connect to the enterprise from a public WLAN.

### SSID Cloaking/Hiding
- SSID stands for **Service Set Identifier**.
	- Logical name of the WLAN.
- Removes the SSID from Beacon frames, then STAs that do not know the SSID will not associate to it.
- Passive Scan will not reveal the SSID, but active scans will.
- Do not secure the WLAN.
- Might cause problems for the WLAN Administration.

- **Recommendation**: Broadcast the SSID!

### SSID Segmentation
- It is a common practice to create different SSIDs for different types of users
- SSIDs are typically mapped into individual VLANs leading to multiple SSIDs per AP
- **Consequence** 
	- Users are segmented by the SSID/VLAN pair
- **Recommendation**
	- Enterprise APs might support up to 16 SSIDs, each of which is mapped into a VLAN.
	- Layer 2 overhead is considerable when 16 SSIDs are lifted, leading to a **40%** performance reduction.
	- **Best Practice**
		- 3-4 SSIDs.

#### SSID Segmentation Example
- **Guest SSID/VLAN**
	- Open access.
	- Deny access to local network resources.
	- Routed off to an Internet Gateway.
- **Voice SSID/VLAN**
	- Use WPA2 encryption.
	- VoWiFi clients are routed to VoIP server.
- **Employee SSID/VLAN**
	- Strong security solutions like WPA2 encryption.
	- ACLs or FWs to access network resources after authentication
![](Chapter%202%20-%20Legacy%20Security-January-16th-2025-18-05-36.webp)