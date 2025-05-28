---
title: Fast Secure Roaming
author:
  - Jon Marien
created: 2025-03-20
published: 2025-03-20
tags:
  - classes
  - SYST44998
---

| Title               | Author                       | Created        | Published      | Tags                                               |
| ------------------- | ---------------------------- | -------------- | -------------- | -------------------------------------------------- |
| Fast Secure Roaming | <ul><li>Jon Marien</li></ul> | March 20, 2025 | March 20, 2025 | [[#classes\|#classes]], [[#SYST44998\|#SYST44998]] |

# Outline
- Definitions
- Basic Procedures
- Client Roaming
- Security
- Auth Delay
- PMKSA
	- PMK Caching
- Fast Secure Roaming

## Definitions
-  Mobility is one of the most attractive features of wireless networks
	- It can increase productivity and profitability, if end users can access resources wirelessly.
- **Roaming**
	- The ability to transition between APs while keeping network connectivity for the upper-layer applications.
	- Reassociation services - **Layer 2**.
	- BSS Transition.
- **Handoff**
	- Network procedure that makes roaming possible.

## Basic Procedures
- To support the **BSS Transition**, the following process should be defined with restrictions, such as:
	- Client Roaming Thresholds.
	- AP-to-AP handoff communications.

## Client Roaming Decision
- Handoff/Roaming decisions are triggered by the **received signal strength indicator** (RSSI) **threshold**.
- RSSI **might** involve:
	- Signal strength.
	- Signal-to-noise ratio.
	- Bit-error rate.
- Proprietary algorithm and thresholds:
	- Varies by vendors.

![[image-142.png]]

## AP-to-AP Communications
- Primary task:
	- To support the communication from the target AP to the original AP.
		- The target AP informs the original AP that the client station is roaming.
		- The target AP requests the client's buffered packets from the original AP.
![[image-143.png]]

## Roaming & Security
- **RSNA** requires two 802.11 stations (STAs) to establish procedures to:
	- Authenticate and associate with each other
	- Create dynamic encryption keys through the **4-Way Handshake Process**.
- For a **mobile client STA**, a **RSNA** is required for every time a client makes a handoff.
- It means that:
	- **Unique encryption keys** must be generated using the 4-Way Handshake Process between the AP and the client STA.
	- ***Every time a client STA roams, it must re-authenticate.***

## Authentication Delay
- Multiple EAPOL frames are needed for 802.1X authentication:
	- 802.1X authentication requires > 700ms.
	- Delay-sensitive applications requires 150ms or less to keep the quality of the data.
	- Be aware that ***there is a trade off between security and performance***.
- The trade off implies that:
	- The higher the security is, the slower the process might be.
	- If the RADIUS server is **not in the local network**, the delay will be worse!
		- ***There is need to have a FASTER SECURE roaming procedure!***

## PMK Security Association (PKMSA)
- Created after authentication (802.1X or PSK)
	- Between a supplicant and authenticator (AP).
- PMKID is **assigned for each association**.
- RSN Information Element found in:
	- Association request.
	- Re-association request.
- Contains PMKID and the quantity of it.

![[image-146.png]]

This is a ***SLOW process***:
![[image-147.png]]

## Fast Secure Roaming
- Options:
	- [PMK Caching](#PMK%20Caching)
	- [Preauthentication](#Preauthentication)
	- [Opportunistic Key Caching](#Opportunistic%20Key%20Caching)
	- [Fast BSS Transition](#Fast%20BSS%20Transition)

### PMK Caching
- It keeps multiple PMKs and their IDs
- When the client stations roam to an AP that **already has** the PMK, then it skips the 802.1X/EAP exchange and goes to the 4-way handshake based on the cached PMK.
- There is no need to re-authenticate.
- Also called **Fast-Secure Roam Back**.
	- If I revisit an AP I have been to before, I can reuse the pairwise master key.

![[image-148.png]]
### Preauthentication
- Performs authentication with the target AP (RADIUS) before roaming to it.
	- While the client STA is in the original AP, it establishes a new 802.1X/EAP exchange with the RADIUS server.
		- Once the client STA is pre-authenticated, the new PMK is created and cached in the STA and the target AP.
			- When the STA moves to the target AP, **only the 4-way handshake** is done.

![[image-149.png]]
### Opportunistic Key Caching
- The computed PMK is forwarded from the original AP to multiple APs to avoid having to re-authenticate!
	- Takes advantage of the PMKID formula.

$$PMKID = HMAC-SHA1-128(PMK, \text{PMK Name}\;||\;AA||SPA)$$
### Fast BSS Transition
1. *PMK#1* and *PMKID* are created to be used by the original *AP* and *STA*.
2. Original *AP* caches *PMK#1* and forwards it to the target *AP*.
3. *STA* calculates the *PMKID#2* using `PMK + Target AP MAC + Client Mac`.
4. *STA* sends reassociation request to the target *AP* with the *PMKID#2*.
5. Target *AP* uses the same formula and computes the *PKMID#2*.
6. If there is a **MATCH**, then a **4-way handshake** is performed.

![[image-151.png]]

##### Fast BSS Transition (FT)
**Terminology:**
- **Basic Service Set** (BSS): WLAN with a single AP.
- **Extended Service Set** (ESS): Set of BSSs interconnected by a DS.
![[image-152.png]]

- **Mobility Domain:**
	- A set of BSS (within the same ESS) that supports fast BSS transitions between themselves.
		- Within this domain, the STAs can handoff in a faster and more secure method.
![[image-153.png]]

- **Key Hierarchy:**
	- *Pairwise Master Key R0* (`PMK-R0`):
		- 1st level key derived from the MSK.
	- *Pairwise Master Key R1* (`PMK-R1`):
		- 2nd level key "" "" "".
	- *Pairwise Transient Key* (`PTK`):
		- 3rd level key "" "" "".
$$MSK > PMK-R0 > PMK-R1 > PTK$$

- **Key Holders:**
	- *WLAN Controller or original AP:*
		- **PMK-R0** key holder (`R0KH`)
	- *Access Point:*
		- **PMK-R1** key holder (`R1KH`)
	- *Client Station:*
		- **PMK-S0** key holder (`S0KH`)
		- **PMK-S1** key holder (`S1KH`)

#### FT: First Level PMK
- After using 802.1X/EAP, the MSK is used to create the PMK-R0.
	- PMK-R0 is sent to the WLAN-C (could be to the AP) and Client STA.

![[image-155.png]]

#### FT Key Hierarchy: WLAN Controller Infrastructure
1. *PMK-R0* is cached at the **WLAN-C**.
	- **WLAN-C** is the key holder for *PMK-R0*.
2. *PMK-R1* is created at the **WLAN-C** and is sent to the target's APs.
	- **AP#1** and **AP#2** are the key holders for *PMK-R1*.
3. **PTKs** are computed from the *PMK-R1*.

![[image-156.png]]

#### FT Key Hierarchy: Supplicant 
1. Client STA caches the *PMK-R0*.
	- Supplicant is the key holder for *PMK-R0*.
2. *PMK-R1* is created at the STA and is then cached.
	- STA is the key holder for *PMK-R1*.
3. PTKs are computed from the *PMK-R1*.