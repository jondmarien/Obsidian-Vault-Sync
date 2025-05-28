---
title: EAP Authentication
author:
  - Jon Marien
created: 2025-01-30
published: 2025-01-30
tags:
  - classes
  - SYST4499
---

| Title              | Author                       | Created          | Published        | Tags                                             |
| ------------------ | ---------------------------- | ---------------- | ---------------- | ------------------------------------------------ |
| EAP Authentication | <ul><li>Jon Marien</li></ul> | January 30, 2025 | January 30, 2025 | [[#classes\|#classes]], [[#SYST4499\|#SYST4499]] |

# EAP Authentication

## Outline
- [WLAN Authentication Overview](#WLAN%20Authentication%20Overview)
- [IEEE802.1X](#IEEE802.1X)
- [Supplicant Credentials](#Supplicant%20Credentials)
- [802.1X/EAP and Certificates](#802.1X/EAP%20and%20Certificates)
- [Shared Secrets](#Shared%20Secrets)
- [Legacy Authentication Protocols](#Authentication%20Protocols)
- [EAP Authentication (Extensible Authentication Protocol)](#EAP%20Authentication)

## WLAN Authentication Overview
- Authentication occurs before association
- Authentication can include:
	- Something you know (user/pass)
	- Something you have (certificate/ID card)
	- Something you are (biometrics)

#### AAA
- [Authentication](#Authentication)
- [Authorization](#Authorization)
- [Accounting](#Accounting)

- These services are provided by the RADIUS server (AAA-Server)
	- Remote Authentication Dial-In User Service

##### Authentication
- Authentication is the verification of users' identity and credentials
- WLAN Authentication
	- What needs to occur before an individual or a device is allowed to access network resources.
- Requires presenting credentials:
	- Something you know.
	- Something you have.
	- Something you are.
- Authentication process may be multifactor
	- Requires two or more credentials.
	- More secure but costly.

###### Authentication Credentials
- Some common examples of authentication credentials used in enterprise WLAN today are:
	- Usernames and passwords.
	- Digital certificates.
	- Dynamic/OTPs.
	- Smart cards or credentials stored on USB devices.
	- Machine authentication (based on an embedded machine identity).
		- A unique identifier distinguishing software code, applications, virtual machines or even physical IoT devices from others on a network.
##### Authorization
- Authorization involves granting access to network resources and services.
	- WLAN is a portal to wired network resources.
	- Before authorization to network resources can be granted, proper authentication must occur.
- Typically RADIUS server provides authentication.
- IEEE802.11i does not dictate the use of RADIUS server.
	- But dictates the use of IEEE802.1X framework.
		- RADIUS server is one of the main components of 802.1X.
##### Accounting
- Accounting is tracking the use of network resources by users.
- Important aspect of network security.
	- Network forensics and daily network activity.
- Keeps a trail of:
	- **Who** used **what**, **when** and **where**!!
- RADUIS server can be used to Accounting.

## IEEE802.1X
- Port-based access control standard.
	- **Authorization framework** that allows/disallows traffic to pass through a port and access network resources.
- It can be implemented in wireless and wired environment.
- EAP (**Extensible Authentication Protocol**) is used to validate users at **Layer 2**.

- Three main components: 
	- [Supplicant](#Supplicant) 
	- [Authenticator](#Authenticator) 
	- [Authentication Server](#Authentication%20Server)
### Supplicant
- Supplicant
	- Host with a software that is requesting access to network resources.
	- It has a unique credentials that are verified before the supplicant getting access to the network resources.
	- Laptop or handheld device.
### Authenticator
- Device that blocks the traffic to pass through its ports entity.
- Two virtual ports:
	-  Uncontrolled:
		- Let the EAP authentication traffic (Layer 2) pass through it.
	- Controlled:
		- Block upper layer traffic until the supplicant has been authenticated.
- Take the form of either the **AP** or **WLAN controller**.

- Using Standalone AP 
	- AP is the authenticator 
- Using WLAN Controller 
	- WLC is the authenticator

![](EAP%20Authentication-January-30th-2025-17-54-34.webp)

### Authentication Server
- Server that validates the credentials and notifies the authenticator that supplicant has been authenticated.
- Role played by RADIUS server.
![](EAP%20Authentication-January-30th-2025-17-55-37.webp)

- Validates the credentials of a supplicant.
- Maintain a user database or may proxy with an external user database to authenticate user credentials.
	- Lightweight Directory Access Protocol (LDAP)-compliant database can be used as the authentication server.

**LDAP Server Figure:**
![](EAP%20Authentication-January-30th-2025-17-56-46.webp)

## Credentials + Certificates
- [Supplicant Credentials](#Supplicant%20Credentials)
- [Authentication Server Credentials](#Authentication%20Server%20Credentials)
- [Server Certificate](#Server%20Certificate)
- [802.1X/EAP and Certificates](#802.1X/EAP%20and%20Certificates)

### Supplicant Credentials
- Usernames and passwords:
	- {Domainname/Username, Password}
- Digital certificates:
	- Contains public key.
	- Validated by Certificate Authority (CA).
- Protected Access Credentials (PACs):
	- Kind of digital certificate without PKI.
	- Developed by Cisco.
- One-time passwords.
- Smart cards and USB tokens.
- Machine authentication.

![](EAP%20Authentication-January-30th-2025-18-01-25.webp)
### Authentication Server Credentials
- EAP allows for mutual authentication.
- Uses server-side certificate.
	- Issued by "trusted certificate authority".
- Certificate of issuing root authority (**Root CA cert**) must be installed in the supplicant.
### Server Certificate
- Validates the Authentication Server
- Creates an Encrypted TLS Tunnel in EAP 
	- Pass supplicant credential through the tunnel
- TLS - **TRANSPORT LAYER SECURITY**:
	- Usually used in transport layer.
		- In EAP, TLS is used in L2.
	- Provides end-to-end encryption.
		- Between supplicant and AS.
### 802.1X/EAP and Certificates
- Server certificates.
- Client certificates.
- Root CA certificates.

![](EAP%20Authentication-January-30th-2025-18-03-29.webp)

## Shared Secrets
- Between Authenticator and Authentication Server.
- Used by:
	- RADIUS Client (Authenticator).
	- RADIUS Server (AS).

	![](EAP%20Authentication-January-30th-2025-18-05-19.webp)
![](EAP%20Authentication-January-30th-2025-18-04-53.webp)

## Authentication Protocols
- Legacy Authentication Protocols:
	- PAP (Password Authentication Protocol) 
	- CHAP (Challenge Handshake Authentication Protocol) 
	- MSCHAP (Microsoft Challenge Handshake Authentication Protocol) 
	- MSCHAPv2 (Microsoft Challenge Handshake Authentication Protocol Version 2)

### PAP
- Password-based authentication protocol used by Point to Point Protocol (PPP) to validate users.
- Unencrypted password is transmitted.
### CHAP
- Better than PAP.
- Use the hash of the password in the transmission. 
- Relies on MD5 hash technology.
- MD5 is not secure, it should not be used out of a tunnel.
- Its variations created by Microsoft (**MS-CHAP** & **MS-CHAPv2**) are also vulnerable and should not be use outside of a tunnel.

## Extensible Authentication Protocol (EAP)
- Layer 2 protocol 
- Defined for use with 802.1X port-based access control
![](EAP%20Authentication-January-30th-2025-18-23-47.webp)

### Key Features of EAP
- Extensible 
	- Anyone can extend it to customize 
		- Standard-based (e.g. EAP-TLS)
		- Proprietary (e.g. Cisco’s LEAP) 
- Can provide both one-way and mutual authentication
- May use username/password or digital certificate
- Server-side certificate creates a TLS tunnel EAP messages are encapsulated in **EAP over LAN** (EAPOL) frames in WLAN

## EAP/EAPOL Messages
| **Name**                           | **Description**                                                                                                |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **EAP-Packet**                     | This is an encapsulated EAP frame. The majority of EAP frames are EAP Packet frames.                           |
| **EAPOL-Start**                    | This is an optional frame that the supplicant can use to start the EAP process.                                |
| **EAPOL-Logoff**                   | This frame terminates an EAP session and shuts down the virtual ports.                                         |
| **EAPOL-Key**                      | This frame is used to exchange dynamic keying information. For example, it is used during the 4-Way Handshake. |
| **EAPOL-Encapsulated - ASF-Alert** | This frame is used to send alerts.                                                                             |
![](EAP%20Authentication-January-30th-2025-18-27-11.webp)

### Generic EAP Process
![](EAP%20Authentication-January-30th-2025-18-29-41.webp)

### Weaknesses
- One-way authentication.
- Username in clear text.
- Examples: 
	- EAP-MD5.
	- EAP-LEAP (MS-CHAP, MS-CHAPv2) - CISCO.

### Strong EAP Protocols
- Uses TLS-tunneled authentication.
- Two authentications by supplicant.
	- Outer identity: 
		- Fake identity.
		- Sent in clear text.
	- Inner identity: 
		- Real identity.
		- Sent through tunnel.

### EAP-PEAP
- **EAP-Protected Extensible Authentication Protocol (EAP-PEAP)**
- Most widely supported EAP method used in WLAN security.
- ‘EAP inside EAP’:
	- Uses TLS tunnel.
		- 2 phases.

#### EAP-PEAP0 Process
- **EAP-PEAP0 (EAP-MSCHAPv2)** 
- **Phase 1**:
	- Uses bogus username.
	- Server certificate creates tunnel for phase 2.
- **Phase 2**:
	- Real identity of supplicant is used within the tunnel.
	- MS-CHAPv2 is used for authentication.

![](EAP%20Authentication-January-30th-2025-18-32-59.webp)

### EAP-TTLS
- **EAP-Tunneled Transport Layer Security (EAP-TTLS)**. 
- Very similar to EAP-PEAP.
- Support more inner EAP protocols inside the TLS tunnel: 
	- PEAP supports only MS-CHAPv2, TLS and GTC.
	- Differ from PEAP in other mirror details.
### EAP-TLS
- **EAP Transport Layer Security (EAP-TLS)** 
	- Most secure, but costly to implement.
- Mutual Authentication.
- Uses both server-side and client-side certificate.
- Requires PKI: expensive solution.
- Used in banking industry.