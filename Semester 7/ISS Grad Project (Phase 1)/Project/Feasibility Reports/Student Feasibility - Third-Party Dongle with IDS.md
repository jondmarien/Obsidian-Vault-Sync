---
title: Student Feasibility - Third-Party Dongle with IDS
author:
  - Jon Marien
created: 2025-02-11
published: 2025-02-11
tags:
  - classes
---

| Title                                             | Author                       | Created           | Published         | Tags                   |
| ------------------------------------------------- | ---------------------------- | ----------------- | ----------------- | ---------------------- |
| Student Feasibility - Third-Party Dongle with IDS | <ul><li>Jon Marien</li></ul> | February 11, 2025 | February 11, 2025 | [[#classes\|#classes]] |

# Feasibility Analysis: Third-Party Anti-Theft Dongle with Intrusion Detection System (IDS)  

---

## **1. Introduction**  
Vehicle theft remains a critical challenge, with thieves increasingly exploiting vulnerabilities in modern cars' electronic systems. While key fob security enhancements are a primary focus, this report evaluates the feasibility of a secondary solution: a third-party dongle that connects via a USB port or 12V lighter socket to implement an Intrusion Detection System (IDS) and additional anti-theft measures. This device aims to detect and mitigate relay attacks, CAN bus intrusions, and unauthorized access through real-time monitoring and response mechanisms.  

---

## **2. Technical Design Overview**  
### **Core Components** 
#### **Hardware Interface** 
   - **12V Lighter Socket/USB Power**: Utilizes the car’s power supply for continuous operation.  
   - **CAN Bus Interfacing**: Requires an external CAN transceiver (e.g., MCP2515) to connect to the OBD-II port or direct wiring for CAN signal interception.  
   - **Microcontroller**: Raspberry Pi Pico W ($6) or ESP32 ($15) for real-time data processing.  

#### **Intrusion Detection System (IDS)**
   - **Anomaly Detection**: Machine learning models (e.g., Random Forest classifiers) trained on CAN bus traffic patterns to flag unauthorized commands (e.g., engine start requests).  
   - **Signature-Based Detection**: Predefined rules to block known attack patterns (e.g., replay attacks).  

#### **Security Features**
   - **Vehicle Immobilization**: Relay-based circuit to disrupt fuel pump/ignition signals when intrusions are detected.  
   - **GPS Tracking**: SIM800L GSM/GPS module ($20) for real-time location tracking.  

### **Data Flow**
```plaintext
[Vehicle CAN Bus] ↔ [CAN Transceiver] ↔ [Microcontroller (IDS Analysis)] → [Immobilizer Circuit/Cloud Alert]  
```

---

## **3. Technical Feasibility Assessment**  

| **Component**           | **Feasibility**                                                                  | **Challenges**                                                                 |
| ----------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **CAN Bus Interfacing** | Moderate: Requires reverse-engineering CAN IDs for critical systems (e.g., ECU). | Vehicle-specific protocols (e.g., Toyota vs. Ford) complicate standardization. |
| **IDS Implementation**  | High: Open-source tools (e.g., CANalyze, SavvyCAN) simplify traffic analysis.    | Limited processing power for ML models on low-cost MCUs.                       |
| **Immobilizer Circuit** | High: Relays can be wired to critical systems with basic electronics knowledge.  | Safety risks if improperly installed; potential liability concerns.            |
| **Wireless Alerts**     | High: GSM modules enable SMS alerts; BLE/Wi-Fi for app integration.              | Cellular data costs ($5/month per SIM); signal reliability in garages.         |

---

## **4. Competitive Analysis**  
### **Existing Solutions**
- **OBD-II Locks**: Physical port locks (e.g., MITI OBD Protector, $30) prevent device removal but lack active security.  
- **GPS Trackers**: Devices like CARLOCK ($99) offer tracking but no CAN bus monitoring.  
- **Aftermarket Immobilizers**: Traditional kill switches ($50–$200) require professional installation.  
### **Market Gap**
No low-cost, student-developed dongle combines IDS, immobilization, and GPS tracking without OBD-II dependency.  

---

## **5. Implementation Roadmap**  
### **Phase 1: Planning (Months 1–4)**  
1. **CAN Bus Reverse Engineering**: Use CAN sniffers to log traffic in test vehicles (e.g., Honda Civic, Toyota Corolla).  
2. **IDS Model Training**: Deploy pre-trained ML models (e.g., from [USENIX Study 19]) for anomaly detection.  
3. **Prototype Design**: Develop a modular PCB integrating ESP32, MCP2515, and relays.  

### **Phase 2: Build & Testing (Months 5–8)**  
1. **Hardware Validation**: Test immobilizer response times (<500ms) and GPS accuracy (<5m error).  
2. **Attack Simulation**: Use CAN injection tools (e.g., CANtact) to evaluate IDS effectiveness.  
3. **User Testing**: Deploy prototypes in 3–5 vehicles to assess false positives and usability.  

---

## **6. Cost Analysis**  

| **Component**           | **Cost** |
| ----------------------- | -------- |
| ESP32 Microcontroller   | $15      |
| MCP2515 CAN Transceiver | $8       |
| SIM800L GPS/GSM Module  | $20      |
| Relays & PCB            | $12      |
| **Total**               | **$55**  |

### **Additional Costs**:  
- 3D-printed enclosure: $10  
- Cellular data plan: $5/month  

---

## **7. Legal & Regulatory Challenges**  
- **Vehicle Modifications**: Immobilizer circuits may violate warranty terms if not installed by certified technicians. 
- **Data Privacy**: GPS tracking requires compliance with CCPA/GDPR for user consent and data anonymization.  
- **FCC Compliance**: Wireless modules must adhere to FCC Part 15 for unintentional radiators.  

---

## **8. Risk Mitigation**  
### **Safety Risks**:  
   - Use opto-isolators to prevent ECU damage during immobilization.  
   - Implement fail-safes to disable immobilization if the dongle loses power.  

### **Technical Limitations**:  
   - Prioritize signature-based detection over ML to reduce computational load.  
   - Partner with local mechanics for vehicle-specific CAN bus profiling.  

---

## **9. Market Potential**  
- **Target Audience**: Owners of pre-2010 vehicles lacking factory immobilizers (32% of US fleet).  
- **Price Point**: $120–$150 (vs. $200+ for commercial systems).  
- **Unique Value Proposition**: Plug-and-play installation without OBD-II port dependency.  

---

## **10. Academic Contribution**  
- **Novelty**: First student-developed, open-source IDS dongle for legacy vehicles.  
- **Validation Metrics**: Publish attack prevention rates and false-positive ratios compared to commercial solutions.  

---

## **Conclusion**  
This secondary approach is **highly feasible** for a student capstone project, with a total prototype cost under $100 and a clear 8-month timeline. While CAN bus interfacing poses standardization challenges, leveraging open-source tools and modular hardware simplifies development. Success hinges on iterative testing with multiple vehicle models and collaboration with automotive cybersecurity experts. By addressing the security needs of older vehicles and avoiding OBD-II port limitations, this solution fills a critical gap in the anti-theft device market.  

**Recommended Next Steps**:  
3. Secure test vehicles from local dealerships or faculty.  
4. Explore partnerships with open-source CAN bus communities (e.g., OpenGarages).  
5. Consult with university legal teams to draft liability disclaimers.  

--- 

This report demonstrates how the proposed dongle could complement or serve as an alternative to key fob security enhancements, providing a layered defense against modern vehicle theft techniques.

Citations:
[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/5025329/01e67e92-fa2c-4d00-bc10-9f4222304435/Vehicle-Theft-Prevention-Dongle.docx
[2] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/5025329/01e67e92-fa2c-4d00-bc10-9f4222304435/Vehicle-Theft-Prevention-Dongle.docx