---
title: Student Feasibility
author:
  - Jon Marien
created: 2025-02-11
published: 2025-02-11
tags:
  - classes
---

| Title               | Author                       | Created           | Published         | Tags                   |
| ------------------- | ---------------------------- | ----------------- | ----------------- | ---------------------- |
| Student Feasibility | <ul><li>Jon Marien</li></ul> | February 11, 2025 | February 11, 2025 | [[#classes\|#classes]] |

# Feasibility Analysis: Implementing Key Fob Security Against Relay Attacks for a Student Capstone Project  

## **Project Scope & Timeline**  
Your proposed 8-month timeline (4 months planning, 4 months implementation) aligns well with academic capstone requirements. Below is a technical feasibility assessment of implementing relay attack countermeasures, considering student resource constraints, technical complexity, and alignment with industry standards like ISO 21434.  

---

### **1. Technical Feasibility of Proposed Countermeasures**  

| **Countermeasure**         | **Feasibility for Students**                                                                 | **Key Challenges**                                                                 |  
|------------------------------|---------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|  
| **Nonce Values**             | High: Requires firmware programming and AES-256 implementation. Compatible with Arduino/RPi. | Secure nonce generation; synchronization between fob and receiver.                |  
| **Time-Limited Tokens**       | High: Can be simulated with TOTP algorithms (e.g., HMAC-SHA1). Low hardware dependency.      | Clock synchronization; handling token expiration in real-time systems.             |  
| **Packet Counters**           | Moderate: Requires encrypted payload management. Ideal for software-based prototypes.         | Counter desynchronization risks; secure storage of counter states.                  |  
| **Motion-Sensor Activation** | Moderate: Low-cost accelerometers (e.g., MPU6050) can detect idle states.                    | False positives; power management for always-on sensors.                            |  
| **UWB/RTT Measurement**       | Low: Requires specialized UWB chips (e.g., DW1000) and precise timing hardware.              | Cost ($50–$100 per chip); complex signal processing; FCC compliance for testing.   |  
| **Biometric Verification**   | Low: Fingerprint sensors (e.g., R503) add cost ($20–$30/unit) and integration complexity.    | Biometric template storage security; limited processing power for ML algorithms.   |  

**Recommendation**: Prioritize cryptographic methods (nonce values, packet counters) and motion-sensor activation. These align with low-cost hardware (Arduino, ESP32) and software tools (Python, C++).  

---

### **2. Resource Constraints & Mitigations**  
- **Budget**:  
  - **Target**: <$500.  
  - **Cost Breakdown**:  
    - Microcontrollers (Arduino/RPi): $50  
    - RF modules (nRF24L01 for signal simulation): $20  
    - Sensors (MPU6050 accelerometer): $10  
    - Encryption libraries (AES-256): Free (OpenSSL/ArduinoLibs).  

- **Tools**:  
  - Use Software-Defined Radio (SDR) tools like HackRF ($300) or simulate relay attacks with MATLAB/Python.  
  - Leverage open-source automotive security frameworks: [CANalyze](https://github.com/EB-Car-Analytics/CANalyze) for CAN bus testing.  

- **Mentorship**:  
  - Seek advisors with embedded systems or cryptography expertise.  
  - Partner with automotive engineering departments for hardware access.  

---

### **3. Implementation Roadmap**  
#### **Phase 1: Planning (Months 1–4)**  
1. **Literature Review**: Map relay attack vectors (ISO 21434 Annex G) and existing solutions.  
2. **Scope Definition**: Focus on 2–3 countermeasures (e.g., nonce + motion sensor).  
3. **Simulation**: Model cryptographic protocols in Python/MATLAB.  
4. **Component Sourcing**: Procure microcontrollers, RF modules, and sensors.  

#### **Phase 2: Implementation (Months 5–8)**  
1. **Firmware Development**:  
   - Implement AES-256 with nonce values on Arduino.  
   - Integrate accelerometer for motion-based activation.  
2. **Testing**:  
   - Use SDR to simulate relay attacks.  
   - Validate latency thresholds (<10ms for RTT detection).  
3. **Validation**:  
   - Compare attack success rates before/after countermeasures.  
   - Benchmark against industry standards (e.g., Tesla’s UWB implementation).  

---

### **4. Risk Analysis**  

| **Risk**                      | **Mitigation Strategy**                                                                |
| ----------------------------- | -------------------------------------------------------------------------------------- |
| Hardware incompatibility      | Use modular design; test components early with vendor return policies.                 |
| Cryptographic vulnerabilities | Use pre-validated libraries (Arduino Crypto); avoid custom encryption implementations. |
| Time overruns                 | Adopt Agile sprints; prioritize MVP (e.g., basic nonce system) before enhancements.    |

---

### **5. Deliverables & Success Metrics**  
- **Minimum Viable Product (MVP)**:  
  - Functional key fob prototype with nonce-based authentication.  
  - Motion-sensor activation demonstrating reduced attack surface.  
- **Success Metrics**:  
  - ≥90% relay attack prevention in controlled tests.  
  - Documentation of ISO 21434-aligned risk assessments.  

---

### **6. Academic Alignment**  
- **Thesis Contribution**:  
  - Novelty: Hybrid approach combining cryptographic and sensor-based defenses.  
  - Relevance: Addresses ISO 21434 Clause 8 (Risk Assessment) and Clause 9 (Concept Phase).  
- **Validation**:  
  - Compare results with academic papers (e.g., [Dantas et al., 2020](https://arxiv.org/abs/2012.15080)).  

---

## **Conclusion**  
The project is **feasible** for a student team with careful scoping. Focus on cryptographic methods and sensor integration to balance innovation with resource limits. Prioritize iterative testing and leverage open-source tools to mitigate technical risks. Partnering with faculty or industry mentors for hardware access and validation will strengthen outcomes.

Citations:
[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_c1da1608-c142-40f5-ab2f-bba49eb1a97d/3bed165e-fe16-4747-824b-612ef8e741b8/security-engineering-iso-21434.pdf
[2] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_c1da1608-c142-40f5-ab2f-bba49eb1a97d/20a22adb-2c58-4092-8a55-c96f57c46df0/wp-setting-the-standard-for-connected-cars-cybersecurity.pdf
[3] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_c1da1608-c142-40f5-ab2f-bba49eb1a97d/71b7b423-7a66-4922-b91f-dd8e670a47b1/03-Martin-Schmiedecker-ISO21434.pdf
[4] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_c1da1608-c142-40f5-ab2f-bba49eb1a97d/78db3ed5-33cf-4893-a866-4419601b484e/Road-Vehicles-Cybersecurity-Engineering.pdf