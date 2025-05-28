---
title: Hours Week 3
author:
  - Jon Marien
created: 2025-05-27
published: 2025-05-27
tags:
  - classes
  - capstone
---

| Title        | Author                       | Created      | Published    | Tags                                             |
| ------------ | ---------------------------- | ------------ | ------------ | ------------------------------------------------ |
| Hours Week 3 | <ul><li>Jon Marien</li></ul> | May 27, 2025 | May 27, 2025 | [[#classes\|#classes]], [[#capstone\|#capstone]] |

# Hours Week 3

| Jonathan Marien                     |
| ----------------------------------- |
| 991476393                           |
| Automotive Security - RF Monitoring |
| Group #7                            |

---

| Group            | Date       | Time           | Duration | Activity                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------- | ---------- | -------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Group #7         | 22/05/2025 | 9:00am-12:00pm | 1hr30min | **Addressed Professor's Technical Questions:**<br>- Documented three core filtering parameters: RSSI threshold (-60 dBm), duplicate detection threshold (2), and duplicate window (configurable seconds).<br>- Defined signal validity pipeline using frequency band validation (315-433 MHz, 13.56 MHz) and temporal analysis.<br>- Designed decision matrix for signal reporting logic with four alert levels based on RSSI, pattern match, and timing. |
| Group #7         | 22/05/2025 | 1:00pm-3:00pm  | 1hr30min | **System Resource Management Documentation:**<br>- Specified memory allocation: 512 MB ring buffer for SDR, 64 MB log buffer.<br>- Swapped over to MicroPython to better fit the Pi Pico.<br>- Documented power management strategy with active/standby modes and battery backup specifications.                                                                                                                                                          |
| Group #7         | 22/05/2025 | 6:00pm-8:00pm  | 2hrs     | **Weekly Team Meeting:**<br>- Met with group for weekly work breakdown, and planned for a time to meet and build the device in person.<br>- Organized a time to meet with Jill to pick-up the device parts in case she cannot come to class again due to being sick.                                                                                                                                                                                      |
| Group #7         | 23/05/2025 | 10:00am-1:00pm | 3hrs     | **Database and Storage Architecture:**<br>- Designed hierarchical storage: SQLite for on-device validation, and planned MongoDB for cloud fleet intelligence, like API remote health checks.<br>- Implemented local cache strategy for mobile app (50 MB encrypted storage).<br>- Planned to integrate Redis for in-memory signal pattern caching to achieve sub-3-second alert latency; Skeleton code exists                                             |
| Group #7         | 23/05/2025 | 2:00pm-4:00pm  | 2hrs     | **Updated System Architecture:**<br>- Clarified Edge MCU as Raspberry Pi Pico.<br>- Added Raspberry Pi Pico as dedicated real-time signal processor.<br>- Updated functional block diagram with dual-processor architecture.<br>- Documented new SPI interfaces between Pico and SDR for processed data transfer.                                                                                                                                         |
| Group #7         | 25/05/2025 | 9:00am-11:00am | 2hrs     | **Logic Engine Integration:**<br>- Added Logic Engine component to system architecture with SignalFilter, Validator, ResourceMgr, and DecisionTree modules.<br>- Updated data flow to show integration between hardware components and logic processing.<br>- Documented how HAL (Hardware Abstraction Layer, aka, how we interact with the device) implementation supports the new architecture requirements.                                            |
| **TOTAL HOURS:** |            |                | 12hrs    |                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

---

### **Notes:**  
- This week focused on addressing specific technical questions raised by our professor regarding system parameters, database strategy, and resource allocation.
- Successfully clarified the distinction between Edge MCU and Raspberry Pi Pico for real-time signal processing to improve system performance.
- The hierarchical storage strategy addresses both local real-time processing needs and optional cloud fleet intelligence requirements.
- Updated system architecture now clearly shows the logic engine integration with all filtering and validation parameters documented.

---

### **Technical Progress:**  
![[image-345.png]]
![[image-346.png]]
![[image-347.png]]

- Defined complete signal processing pipeline from antenna to mobile alert with all parameters quantified
- Established database technology stack supporting both local and cloud operations
- Created dual-processor architecture optimizing real-time performance while maintaining system complexity manageable
- Integrated all professor feedback into comprehensive technical documentation ready for implementation phases

---

### **Next Week Priorities:**  
- Begin Raspberry Pi Pico firmware development for real-time SDR processing
- Implement SQLite database schema for local signal validation
- Test SPI communication between Pico and SDR
- Validate memory allocation and CPU scheduling under load testing scenarios

---

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                             VEHICLE CABIN                                   │
│                                                                             │
│  ┌───────────┐   Coax    ┌────────────┐   IQ Stream   ┌────────────┐        │
│  │  Antenna  ├──────────►│  SDR Core  ├──────────────►│ Pi Pico    │        │
│  └───────────┘           └────────────┘               └─────┬──────┘        │
│                              ▲   USB                        │               │
│                              │                              │ SPI/I²C       │
│                      ┌────────────┐   SPI/I²C    ┌──────────┴─────┐         │
│                      │ Secure Elem│◄──────────── │ LOGIC ENGINE   │         │
│                      └────────────┘              │ ┌────────────┐ │         │
│                              ▲                   │ │SignalFilter│ │         │
│                              │                   │ │Validator   │ │         │
│                      ┌────────────┐              │ │ResourceMgr │ │         │
│                      │   SQLite   │◄─────────────│ │DecisionTree│ │         │
│                      │  Database  │              │ └────────────┘ │         │
│                      └────────────┘              └──────────┬─────┘         │
│                              ▲                              │               │
│                              │                              ▼               │
│                      ┌────────────┐   UART/BLE   ┌──────────────────┐       │
│                      │  NFC Coil  │              │  BLE/Wi-Fi SoC   │       │
│                      └────────────┘              └─────┬────────────┘       │
│                              ▲   NFC                   │                    │
│                              │                         │                    │
│                      ┌────────────┐                    │                    │
│                      │ Mobile App │◄───────────────────┘                    │
│                      │ (50MB Cache│   BLE/GATT                              │
│                      │ SQLite)    │                                         │
│                      └────────────┘                                         │
│                                                                             │
│                                            OTA / TLS1.3                     │
│                                                │                            │
│                                                ▼                            │
│                                         ┌────────────┐                      │
│                                         │ Cloud API  │                      │
│                                         │ (MongoDB)  │                      │
│                                         └────────────┘                      │
└─────────────────────────────────────────────────────────────────────────────┘

```