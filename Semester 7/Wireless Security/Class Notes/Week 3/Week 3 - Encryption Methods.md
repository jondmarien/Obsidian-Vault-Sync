---
title: Week 3 - Encryption Methods
author:
  - Jon Marien
created: 2025-01-23
published: 2025-01-23
tags:
  - classes
  - SYST4499
---

| Title                       | Author                       | Created          | Published        | Tags                                             |
| --------------------------- | ---------------------------- | ---------------- | ---------------- | ------------------------------------------------ |
| Week 3 - Encryption Methods | <ul><li>Jon Marien</li></ul> | January 23, 2025 | January 23, 2025 | [[#classes\|#classes]], [[#SYST4499\|#SYST4499]] |

# Outline
- [Encryption Basics](#Encryption%20Basics)
- [Cipher Types](#Cipher%20Types)
- [Wired Equivalent Privacy (WEP)](#Wired%20Equivalent%20Privacy%20(WEP))
- [Temporal Key Integrity Protocol (TKIP)](#Temporal%20Key%20Integrity%20Protocol%20(TKIP))
- [CCMP](#CCMP)
- [Wi-Fi Protected Access (WPA/WPA2)](#Wi-Fi%20Protected%20Access%20(WPA/WPA2))

## Encryption Basics 
### Scenarios
- Transmitting a secure message:
![](Week%203%20-%20Encryption%20Methods-January-23rd-2025-17-15-38.webp)
- Receiving a secure message:
![](Week%203%20-%20Encryption%20Methods-January-23rd-2025-17-16-04.webp)
### Keyed Crypto Systems
![](Week%203%20-%20Encryption%20Methods-January-23rd-2025-17-16-37.webp)
### Taxonomy
![](Week%203%20-%20Encryption%20Methods-January-23rd-2025-17-16-59.webp)

### Symmetric Algorithms
- Same key for encryption and decryption: pre shared key (**PSK**).
	- Key must be shared between the parties prior establishing the secure communications channel.
- Simple, ease of implementation, and computationally fast.
- Example:
	- RC4/ARC4.
	- AES.
![](Week%203%20-%20Encryption%20Methods-January-23rd-2025-17-17-51.webp)

### Asymmetric Algorithms
- Separate key for encryption and decryption: public and private key
- Computationally intensive and slow
- Key distribution can be done through **public key infrastructure** (PKI)
![](Week%203%20-%20Encryption%20Methods-January-23rd-2025-17-19-05.webp)

## Cipher Types
- [Stream Cipher](#Stream%20Cipher)
- [Block Cipher](#Block%20Cipher)
- [RC4/ARC4](#RC4/ARC4)
- [AES](#AES)

### Stream Cipher
- Symmetric key method.
- Bit-by-bit operation.
- Data stream is XORed with keystream.
- Example:
	- ARC4 is used in WEP & TKIP.
### Block Cipher
- Symmetric key method.
- Block ciphers process messages in into blocks, each of which is then en/decrypted:
	- Fixed length block-by-block operation.
	- One block cipher text is produced from one block of data.
- Example:
	- AES is used in WPA2.

![](Week%203%20-%20Encryption%20Methods-January-23rd-2025-17-25-23.webp)

### RC4/ARC4
- Rivest Cipher
- Unofficial version, that is publicly available, called ARC4 (alleged RC4)
- Features 
	- Fast and simple 
	- Stream cipher: generates pseudorandom stream of bits (keystream) 
	- Symmetric key cipher 
- Examples: 
	- Used in WEP and TKIP
### AES
- Advanced Encryption Standard
- Symmetric Block Cipher
- Features
	- Based on Rijandael Algorithm
	- Key sizes: **128 (AES-128)**, 192 (AES-192), 256 (AES-256)
	- Multiple Applications: IPsec VPN, WPA2 Security
- Encryption protocol used by **CCMP** (802.11-2012 standard)

![](Week%203%20-%20Encryption%20Methods-January-23rd-2025-17-30-05.webp)

### Mac Authentication Code
- MAC (**tag**) is used to authenticate a message.
	- Used to provide **authenticity** and **integrity**.
	- Key must be somehow agreed between sender and receiver.
![](Week%203%20-%20Encryption%20Methods-January-23rd-2025-17-31-29.webp)

## WLAN Encryption Systems
- The 802.11‐2012 standard defines three encryption methods that operate at Layer 2 
	- **WEP:** Wired Equivalent Privacy 
		- *(A)RC4* 
	- **TKIP**: Temporal Key Integrity Protocol 
		- *(A)RC4* 
	- **CCMP**: Counter Mode (CM) with Cipher Block Chaining (CBC) 
		- *AES*
	- **Message Authentication Code** (MAC) Protocol 
		- *AES*

## Wired Equivalent Privacy (WEP)
- Legacy security
- Features
	- ARC4 stream cipher
	- Static key (64 bit or 128 bit)
		- Static bit initialization vector (IV)
		- Static WEP key (40 bit or 104 bit)
	- Integrity check value (ICV)
		- Cyclic redundancy check (CRC32)

![](Chapter%202%20-%20Legacy%20Security-January-16th-2025-17-33-51.webp)

### WEP Encryption Process
- **Confidentiality** by RC4
- **Integrity** by CRC32

- RC4 seed =
	- (24 IV + 40 bit user key)
	- or
	- (24 IV + 104 bit user key)

![](Week%203%20-%20Encryption%20Methods-January-23rd-2025-17-39-38.webp)

### 802.11 MAC Protocol Data Unit (MSDU)
- Data frames that carry MSDU are encrypted
- Frame types that are not encrypted
	- Management frames
	- Control frames

![](Week%203%20-%20Encryption%20Methods-January-23rd-2025-17-41-30.webp)

### WEP MPDU
![](Week%203%20-%20Encryption%20Methods-January-23rd-2025-17-41-59.webp)

## Temporal Key Integrity Protocol (TKIP)
- A stopgap measure to improve on the security offered by WEP
	- An enhancement of WEP
	- A legacy security measure, by today's security standards
	- Uses the same **ARC4 algorithm** as WEP

### TKIP Features
- Temporal keys
	- 128 bits
	- **Dynamically created**
- Sequencing
	- MPDUs are sequenced with **per-MDU TKIP Sequence Counter** (TSC)
- Key Mixing 
	- Stronger key mixing process **for seeding to RC4**
- Enhanced Data Integrity
	- Stronger data integrity method: **Message Integrity Check** (MIC)

### TKIP Data Flow
![](Week%203%20-%20Encryption%20Methods-January-23rd-2025-17-45-43.webp)

![](Week%203%20-%20Encryption%20Methods-January-23rd-2025-17-45-55.webp)

### TKIP MPDU
![](Week%203%20-%20Encryption%20Methods-January-23rd-2025-17-46-21.webp)

## CCMP
- Counter Mode with Cipher‐Block Chaining Message Authentication Code Protocol (CCMP)
	- Designed to replace WEP *and* TKIP.
	- Uses the stronger **AES Block Cipher** (vs. ARC4).
	- Required in Robust Security Networks (RSNs).

### Key Terms in CCMP
- **Counter Mode** with Cipher‐Block Chaining Message Authentication Code Protocol (CCMP)
- **Counter Mode (CTR)**
	- Provides *data confidentiality*.
	- Featured by the application of the AES.
- Cipher Block Chaining (CBC) or **CBC-MAC** (Message Authentication Code)
	- Provides *authentication and data integrity*.

- CCMP is also called **Counter Mode with CBC-MAC**
	- Provides both *authentication and confidentiality*.
	- Same key is used for both purposes
	- 128-bit block size (block cipher)

### Features of CCMP
- 128-bit temporal keys:
	- Pairwise Transient key (PTK) for unicast traffic.
	- Group Temporal key (GTK) for multicast traffic.
- Key ID:
	- Corresponds to the Extended IV bit in TKIP.
	- Set 1 indicates that the frame format is RSN rather than the WEP.
- Packet Number (PN):
	- Works like the TKIP sequence number.
	- Protects against replay and injection attacks.
- Nonce:
	- Random number that is created *only one time* and used *only one time*.
	- Created from PN, priority data used in QoS, and transmitter address (**TA**).
	- *f(**PN**, **TA**, **priority of data in QOS**)*.
- Additional Authentication Data (**AAD**)
	- Constructed from portions of the MAC header.
	- Used for data integrity.
	- Receiving STAs can validate the integrity of the MAC header

### Process Steps for CCMP
1. Starts with 128-bit temporal key (**PTK** or **GTK**).
2. 48-bit PN is created; incremented for each **MPDU.**
3. **AAD** is created.
4. **Nonce** is created; *f(**PN**, **TA**, **priority of data in QOS**)*.
5. 8-byte CCMP header is created; *f(**Key ID**, **PN**)*.
6. CCM (AES Block Cipher) module is used to:
	1. Create 8-byte **MIC:** *f(**TK**, **AAD**, **nonce**, **data**)*.
	2. Create 128-bit blocks of encrypted data: *f(**MIC**, **data**)*.
7. **MPDU** is created:
	1. *(**MAC header** || **CCMP header** || **Encrypted MSDU** || **Encrypted MIC**) || **FCS***
	2. **Frame Check Sequence** (FCS) is calculated on the whole MAC

### CCMP Encryption and Data Integrity Process
![](Week%203%20-%20Encryption%20Methods-January-23rd-2025-18-11-05.webp)

![](Week%203%20-%20Encryption%20Methods-January-23rd-2025-18-11-15.webp)

### CCMP MPDU
![](Week%203%20-%20Encryption%20Methods-January-23rd-2025-18-11-40.webp)

## Wi-Fi Protected Access (WPA/WPA2)
![](Week%203%20-%20Encryption%20Methods-January-23rd-2025-18-11-55.webp)

## Summary of Encryption Methods in 802.11
![](Week%203%20-%20Encryption%20Methods-January-23rd-2025-18-12-20.webp)