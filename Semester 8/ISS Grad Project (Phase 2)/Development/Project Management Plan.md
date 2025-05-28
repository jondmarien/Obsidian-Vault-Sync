---
title: Project Management Plan
author:
  - Jon Marien
created: 2025-05-20
published: 2025-05-20
tags:
  - capstone
---

| Title                   | Author                       | Created      | Published    | Tags                     |
| ----------------------- | ---------------------------- | ------------ | ------------ | ------------------------ |
| Project Management Plan | <ul><li>Jon Marien</li></ul> | May 20, 2025 | May 20, 2025 | [[#capstone\|#capstone]] |
# Group 7 – Enhancing Automotive Security
## Project Management Plan

* *Lead Programmer – Jonathan Marien, 991476393*<br>
* *Project Lead – Jillian Moorcroft, 991625656*<br>
* *Lead Researcher – Aaron Briand, 991644564* <br>
* *Researcher – Hala Alwash, 991471580*

---

# Purpose & Scope
This plan governs the 12-week Phase 2 development, test, and delivery cycle for the automotive RF-and-NFC monitoring dongle, following PMI PMBOK phases while satisfying ISO/SAE 21434 artefact expectations.

## Semester Timeline & Phase Gates (12 Weeks Remaining)
| Week(s) | Phase                   | Milestone                                         | Exit Criteria                 |
| ------- | ----------------------- | ------------------------------------------------- | ----------------------------- |
| 1       | Initiation              | Approved charter; hardware orders placed          | Stakeholder sign-off          |
| 2       | Planning                | Detailed schematics, updated BOM, sprint backlog  | DR-1 review complete          |
| 3       | Execution I             | Breadboard prototype (RTL-SDR + PN532) functional | Signal capture validated      |
| 4       | Execution II            | µC firmware alpha; logging pipeline operational   | 50 % unit-test coverage       |
| 5       | Signal Processing       | Anomaly-detection v0.1; NFC detection refined     | ≥70 % accuracy in bench tests |
| 6       | Alert System            | BLE/Wi-Fi alerts end-to-end; backend stubbed      | Notification latency ≤3 s     |
| 7       | Enclosure & Integration | 3-D printed shell; field-ready prototype          | Prototype survives 24-h soak  |
| 8       | Field Testing I         | Vehicle deployment; collect real-world data       | ≥20 GB logs captured          |
| 9       | Field Testing II        | Detection logic tuned; power tests                | False-positive rate <5 %      |
| 10      | Compliance & Security   | FCC Part 15B pre-scan; secure-boot reviewed       | All critical findings closed  |
| 11      | Documentation           | User manual draft; ISO/SAE matrices updated       | Docs 80 % complete            |
| 12      | Final Review & Handoff  | Capstone demo; professor acceptance               | Grade submission ready        |

##  Work Breakdown Structure (WBS)
*1.0 Project Management – Member #2 (lead)*  
  • Sprint planning & retrospectives  
  • ISO 21434 evidence tracking  
*2.0 Hardware – All* 
  • Antenna, PCB, power subsystem; FCC/IC pre-scan  
*3.0 Firmware – Member #1*
  • SDR drivers, detection pipeline, secure-boot & OTA  
*4.0 Mobile App – Member #1*  
  • BLE interface, UI/UX, alert logic, TestFlight release  
*5.0 Cloud (optional) – Member #1*  
  • MQTT API, fleet dashboards, IAM policies  
*6.0 QA & Testing – Member #4*  
  • Unit tests, HIL bench, pen-test with replay toolkit  
*7.0 Documentation & Delivery – All*  
  • User manual, install video, final poster  

## RACI Matrix (Excerpt)
*Responsible, Accountable, Consulted, and Informed*

| Task            | Lead | Support | Consult   | Inform       |
| --------------- | ---- | ------- | --------- | ------------ |
| PCB layout      | #3   | #1      | Advisor   | Team         |
| ML model        | #2   | #1      | Professor | Team         |
| Compliance docs | #1   | #2      | Library   | Stakeholders |

## Risk Register – Top Three
| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| RF false positives | Medium | Medium | Dynamic threshold + ML retrain |
| Component shortage | High | High | Dual vendors, pin-compatible alternates |
| FCC regulatory delay | Low | Medium | Pre-scan in Week 6; outsource remediation |

## Test & Quality Management
- Continuous Integration executes static-analysis, unit tests, and code-coverage on every push.  
- Nightly Hardware-in-the-Loop bench replays captured relay-attack waveforms to prevent regressions.  
- Traceability matrix ties every requirement to verification artefacts ensuring audit readiness.

## Deployment & Support
Final deliverables include a pre-flashed dongle in a 3-D-printed enclosure, QR-coded quick-start guide, and mobile-app links to TestFlight and Google Beta. Post-launch support spans 60 days with hot-patch OTA capability for emergent CVEs.

---

### Next-Week Action Items
1. Incorporate professor feedback on secure-element threat modelling into WP-10-05 draft.  
2. Validate component lead times against Mouser/Digi-Key inventory and update risk log.  
3. Prepare demo vehicle harness to streamline pilot installations during Week 10 validation.

