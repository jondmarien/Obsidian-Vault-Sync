---
title: Dynamic Encryption Key Generation
author:
  - Jon Marien
created: 2025-02-11
published: 2025-02-11
tags:
  - classes
  - SYST44998
---

| Title                             | Author                       | Created           | Published         | Tags                                               |
| --------------------------------- | ---------------------------- | ----------------- | ----------------- | -------------------------------------------------- |
| Dynamic Encryption Key Generation | <ul><li>Jon Marien</li></ul> | February 11, 2025 | February 11, 2025 | [[#classes\|#classes]], [[#SYST44998\|#SYST44998]] |
# 802.11 Layer 2 Dynamic Encryption Key Generation

## 802.1X/EAP and Dynamic Keys
- Dynamic keys are a **by-product** of the 802.1X/EAP process.
- EAP protocols that utilize mutual authentication provide the seeding material used to generate the keys.
 - Benefits of dynamic keys:
	 - They cannot be compromised by SE.
	 - Every user has a different key.
		 - **Outcome**: if the key is compromised, other supplicants will not be exposed.

![[image-1.png]]

## Robust Security Network (RSN)
- A **robust security network** (RSN) is a network that allows the creation of only **robust security network associations** (RSNAs).
	- Two 802.11 radios must have established procedure to: 
		- **Authenticate**. 
		- **Associate**.
		- **Create** unique dynamic keys by means a 4-way handshake process. 
- **CCMP/AES** is the mandated encryption method and TKIP is optional.
	- Anything else would be called a legacy secure network.

## RSNA within a BSS
- Terminology and procedures: 
	- **Pairwise Transient Key** (PTK): 
		- **Unicast** traffic.
		- **Unique** between a client STA and the AP.
		- **CCMP/AES** or **TKIP/ARC4**.
	- **Group Temporal Key** (GTK): 
		- Broadcast and multicast traffic.
		- Determined by the **lowest common denominator** (LCD) method. 
		- E.g.: 
			- *LCD (CCMP, CCMP)* = **CCMP** 
			- *LCD (CCMP, TKIP)* = **TKIP** 
			- *LCD (CCMP, CCMP, WEP)* = **WEP**
		- Weakest encryption technique among the client STAs is chosen as the GTK.

![[image-2.png]]

## Robust Security Network Criteria
- In a **RSN**, only **RSNAs** are allowed:
	- **TKIP/ARC4**.
	- **CCMP/AES**.

*GTK=LCD (CCMP, TKIP) = TKIP*
![[image-3.png]]

## Transition Security Network (TSN)
- Allows **WEP**.
 GTK=LCD (CCMP, TKIP,WEP) = WEP
 ![[image-4.png]]

## Pre-RSN, RSN, TSN Coexistence
- BSS is featured by: 
	- Service set identifier (SSID)            = **logical name** 
	- Basic service set identifier (BSSID) = **MAC address**
- It is possible to have multiple SSIDs within the same AP. 
- Each SSID is associated with a virtual MAC address.
- Each SSID and vBSSS might be associated to a security level.
![|326x291](blue.png)
![|326x291](red-1.png)
![|326x291](green.png)

## The RSN Information Element
- AP send frames to inform client STAs about its RSN capabilities.
![[image-5.png]]
- Client STA use the association frame request to inform the AP about its security capabilities.
![[image-7.png]]
- When a client STA is performing a handoff, it uses the re-association frame to inform the new AP about its security capabilities.
![[image-8.png]]

## Authentication and Key Management (AKM)
- **AKM** is defined in **802.11-2012** standard.
- Consists of a set of algorithms designed to provide:
	- **Authentication**.
	- **Key management**:
		- Individually.
		- In combination with higher-layer authentication and key-management algorithms.
- **Key point:** 
	- **Authentication** and **Key generation** are mixed.
		- An **authentication** process is necessary to generate dynamic encryption keys.
		- **802.1X/EAP** and **PSK** authentication processes generate the seeding material needed to create dynamic encryption keys.
		- **Authorization** is not finalized until encryption keys are created, and encryption keys **cannot be created without authentication**.

### AKM Steps
1. Discovery
2. Authentication
3. Master Key Creation
4. Temporal Key Creation
5. Authorization
6. Encryption
*(steps can be seen in the image below)*
![[image-9.png|419x321]]

## Discovery Component
![[image-10.png]]
## Authentication and Master Key Generation
![[image-11.png]]

### Temporal Key Generation and Authorization
![[image-12.png]]

## RSNA Key Hierarchy
- Each upper tier key acts as the seeding material for lower keys.
	- [**Master Session Key (MSK)**](#**Master%20Session%20Key%20(MSK)**)
		- [**Group Master Key (GMK)**](#**Group%20Master%20Key%20(GMK)**)
			- [Temporal Keys](#Temporal%20Keys)
	- [**Pairwise Master Key (PMK)**](#**Pairwise%20Master%20Key%20(PMK)**) 
		- **Pairwise Transient Key**
![[image-23.png]]

---
### Master Keys
#### **Master Session Key (MSK)** 
- **MSK** is also called **AAA key**.
- It is generated either from the **802.1X/EAP** or **PSK authentication**.
- **64 octets** in length.
- **MSK generation is out of the scope** of the 802.11-2012 standard and is EAP specific.
![[image-22.png]]

---

#### **Pairwise Master Key (PMK)** 
- MSK is the seeding material for the PMK.
- PMK resides on supplicant and authentication server.
- PMK is unique and is generated every time there is an authentication or re-authentication.
- It is sent from the server to the authenticator.
##### **Group Master Key (GMK)** 
- Randomly generated at the authenticator.
![[image-20.png]]

---
#### **Master Keys Overview**
![[image-16.png]]

### Temporal Keys
- Outcome of the 4-way handshake.
- **Pairwise Temporal Key (PTK)**
	- It is **created from the PMK**.
	- It is used to **protect the payload of the 802.11 data frame**.
	- **Unicast traffic** from/to STA to/from AP.
	- **Unique** for every STA.
- **Group Temporal Key (GTK)** 
	- It is **derived from the GMK**. 
	- Encrypt all the broadcast and multicast traffic.
	- Shared among all client STAs and a single authenticator.

![[image-17.png]]

## Purpose of 4-Way Handshake Process
- It uses 4 EAPOL‐Key frame messages between the authenticator and the supplicant for six major purposes: 
	1. **Confirms the existence of the PMK** at the peer station.
	2. **Ensures that the PMK is current**.
	3. **Derives a new Pairwise Transient Key (PTK)** from the PMK.
	4. **Installs the PTK** on the supplicant **and** the authenticator.
	5. **Transfers the GTK** from the authenticator to the supplicant and **installs the GTK** on the supplicant **and, if necessary**, the authenticator.
	6. **Confirms the selection** of the cipher suites.

### 4‐Way Handshake
> Final process used to generate PTK for encryption of unicast transmissions and a GTK for encryption of broadcast/multicast transmissions

#### Key Terms
- **Pseudo-random function (PRF)**:
	- It hashes input values to create a pseudo-random value.
- **Nonce**:
	- Random numerical value generated one time only.
	- Authenticator nonce (**ANonce**) 
	- Supplicant nonce (**SNonce**) 
	- Authenticator MAC add (**AA**) 
	- Supplicant MAC add (**SPA**)

- **Pairwise Transient Key** is given by this formula: 
$$ PTK=PRF(PMK+ANonce+SNonce+AA+SPA)$$
- To **generate the PTK**, both the supplicant and authenticator need all 5 parameters.

### How the Handshake Works
- **MSG #1:** AP sends the `ANonce`, then STA can generate the PTK.
- **MSG #2:** 
	- STA sends the `SNonce`.
	- MIC. 
- **MSG #3:** 
	- AP sends the GTK encrypted using the PTK.
	- Command to install the PTK. 
	- MIC.
- **MSG #4:** 
	- Ack that the temporal keys are installed.
	- MIC.

![[image-24.png]]

## Group Handshake
- The Group Key Handshake is used only to issue a new GTK to client STA that have previously formed security associations. 
	- E.g., the GTK should change: 
		- **after a client STA disassociation or de-authentication**.
		- **in a certain period of time**.

- **MSG #1:** 
	- AP sends the new generated GTK to STA encrypted using its PTK.
	- MIC.
- **MSG #2:** 
	- ACK the installation of the new GTK.
	- MIC.

![[image-25.png]]
