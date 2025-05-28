---
title: System Architecture Report
author:
  - Jon Marien
created: 2025-05-20
published: 2025-05-20
tags:
  - capstone
---

| Title                      | Author                       | Created      | Published    | Tags                     |
| -------------------------- | ---------------------------- | ------------ | ------------ | ------------------------ |
| System Architecture Report | <ul><li>Jon Marien</li></ul> | May 20, 2025 | May 20, 2025 | [[#capstone\|#capstone]] |

# Group 7 – Enhancing Automotive Security
## System Architecture Report

* *Lead Programmer – Jonathan Marien, 991476393*<br>
* *Project Lead – Jillian Moorcroft, 991625656*<br>
* *Lead Researcher – Aaron Briand, 991644564* <br>
* *Researcher – Hala Alwash, 991471580*

---

# Overview
The capstone delivers a USB-powered radio-frequency (RF) monitoring dongle that listens on 315 MHz, 433 MHz, and 13.56 MHz to flag relay, cloning, and jamming attempts against keyless-entry vehicles. Alerts are forwarded to drivers through a mobile application while optionally streaming anonymized telemetry to a cloud dashboard for aggregated fleet analytics.

## High-Level System Architecture
The complete solution is composed of eight tightly-coupled functional blocks that exchange signed JSON messages across secure local or cloud channels.

```md
┌─────────────────────────────────────────────────────────────────────────────┐
│                             VEHICLE CABIN                                   │
│                                                                             │
│  ┌───────────┐   Coax    ┌────────────┐   IQ Stream   ┌────────────┐        │
│  │  Antenna  ├──────────►│  SDR Core  ├──────────────►│  Edge MCU  │        │
│  └───────────┘           └────────────┘               └─────┬──────┘        │
│                              ▲   USB                        │               │
│                              │                              │               │
│                      ┌────────────┐   SPI/I²C   ┌──────────┴─────┐          │
│                      │ Secure Elem│◄────────────│  BLE/Wi-Fi SoC │          │
│                      └────────────┘              └─────┬─────────┘          │
│                              ▲   UART/BLE              │                    │
│                              │                         │                    │
│                      ┌────────────┐                    │                    │
│                      │  NFC Coil  │                    │                    │
│                      └────────────┘                    │                    │
│                              ▲   NFC                   │                    │
│                              │                         │                    │
│                      ┌────────────┐                    │                    │
│                      │ Mobile App │◄───────────────────┘                    │
│                      └────────────┘   BLE/GATT or MQTT                      │
│                                                                             │
│                                            OTA / TLS1.3                     │
│                                                │                            │
│                                                ▼                            │
│                                         ┌────────────┐                      │
│                                         │  Cloud API │                      │
│                                         └────────────┘                      │
└─────────────────────────────────────────────────────────────────────────────┘

```

### **Key relationships**  
• Antenna feeds an SDR core that streams IQ data to a micro-controller for spectral analysis.  
• The micro-controller’s anomaly engine forwards events to the BLE/Wi-Fi module; this module bridges to the mobile app and (optionally) an MQTT broker in the cloud.  
• A hardware secure-element protects TLS keys used for firmware updates, mobile pairing, and cloud upload, guaranteeing provenance and preventing replay attacks.

## Functional Block Summary
| #   | Block                | Core Technology   | Principal Role                              | Notable Interfaces                |
| --- | -------------------- | ----------------- | ------------------------------------------- | --------------------------------- |
| 1   | Antenna & Front-End  | SAW filters + LNA | Capture 315/433 MHz & 13.56 MHz             | Coax → SDR                        |
| 2   | SDR Core             | RTL-SDR V3 (USB)  | Digitise baseband, 2 MS/s                   | USB 2.0 OTG → MCU                 |
| 3   | Edge Compute         | Raspberry Pi 4B   | FFT & lightweight CNN for anomaly detection | SPI to secure element; USB to SDR |
| 4   | Secure Storage       | ATECC608B         | Key vault, secure-boot attestation          | I²C to Pi                         |
| 5   | BLE/Wi-Fi SoC        | ESP32-C3          | Low-latency alert channel + OTA             | UART to Pi; BLE to phone          |
| 6   | Mobile Application   | Flutter           | Push notifications, logs, settings          | BLE; REST to cloud                |
| 7   | Cloud API (optional) | AWS IoT Core      | Fleet analytics & threat-intel share        | MQTT/TLS                          |
| 8   | Power Management     | 2 000 mAh Li-ion  | 48 h standby after USB loss                 | I²C fuel gauge                    |

## Data-Flow Description
1. Raw RF bursts enter the SDR, are digitized, and streamed to the Pi’s ring buffer where a lightweight CNN classifies patterns against a curated dataset of legitimate key-fob bursts.  
2. Any suspicious frame (e.g., high RSSI replay with abnormal preamble) is wrapped in a signed JSON object and queued to the ESP32.  
3. The ESP32 notifies the mobile app in ≤ 3 s via BLE GATT; parallel TLS 1.3 upload to the cloud enables fleet security-operation-centre dashboards.  
4. On receiving a critical alert, the app can sound an alarm, display direction-finding hints, and optionally trigger a CAN-bus immobilizer via OEM API partnerships.

## Security Controls Aligned to ISO/SAE 21434
| Clause | Control Implemented | Work Product |
|--------|--------------------|--------------|
| 10.5 | Secure-boot chain validates Pi & ESP32 firmware on power-up | WP-10-03 – Coding-guideline docs |
| 10.7 | Static-analysis + fuzzing to minimise residual weaknesses | WP-10-07 – Vulnerability report |
| 11.1 | Vehicle-level validation with replay attacks against demo cars | WP-11-01 – Validation report |
| 13 | Incident-response playbook for OTA hot-patches | WP-13-02 – Update procedure |

## Bill-of-Materials Snapshot

*What we have:*

| Category       | Part/Item           | Qty | Unit Cost (CAD) | Source           |
| -------------- | ------------------- | --- | --------------- | ---------------- |
| Board          | Board w Accessories | 1   | $48.30          | (as per receipt) |
| Board          | Back-up Board       | 1   | $11.95          | (as per receipt) |
| Misc.          | Dongle Ext. x2      | 2   | $8.50           | (as per receipt) |
| SDR            | RTL-SDR             | 1   | $69.95          | (as per receipt) |
| NFC            | NFC Module          | 1   | $15.99          | (as per receipt) |
| Shipping       | PiShop Shipping     | 1   | $17.12          | (as per receipt) |
| Tax            | PiShop Tax          | 1   | $8.94           | (as per receipt) |
| Import Fees    | Import Fees Amazon  | 1   | $11.18          | (as per receipt) |
| **Total**      |                     |     | **$191.93**     |                  |
| **Per Person** |                     |     | **$47.98**      | (4 people)       |
*What we may need:*

| Category       | Part                            | Qty | Unit Cost (CAD) | Source     |
| -------------- | ------------------------------- | --- | --------------- | ---------- |
| Secure Element | Microchip ATECC608B-MAHDA       | 1   | 1.20            | Mouser     |
| Power          | 2 000 mAh Li-ion cell + charger | 1   | 7.20            | AliExpress |
| Enclosure      | 3-D-printed PETG shell          | 1   | 3.00            | In-house   |
| Misc.          | Cables, headers, passives       | —   | 5.65            | —          |
| **Total**      |                                 |     | **CAN $17.05**  |            |
## Future Enhancements
* Direction-finding using AoA with dual coherent antennas  
* Integration with OEM telematics for automatic immobiliser engagement  
* Expansion to 868 MHz/915 MHz for European key-fobs  
* Integration of Tiny-ML-based classification directly on ESP32 C6 to remove Raspberry Pi dependency

---

### References
1. ISO/SAE 21434:2021 – Road Vehicles – Cybersecurity Engineering.
2. ETSI EN 303 204 V2.2.1 – Short Range Device Radio Equipment.
3. RTL-SDR Blog. “V4 Dongle Specifications,” 2024.

