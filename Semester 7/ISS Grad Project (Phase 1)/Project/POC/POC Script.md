---
title: POC Script
author:
  - Jon Marien
created: 2025-03-24
published: 2025-03-24
tags:
  - classes
  - capstone
---

| Title      | Author                       | Created        | Published      | Tags                                             |
| ---------- | ---------------------------- | -------------- | -------------- | ------------------------------------------------ |
| POC Script | <ul><li>Jon Marien</li></ul> | March 24, 2025 | March 24, 2025 | [[#classes\|#classes]], [[#capstone\|#capstone]] |

# Script

## Introduction
### Opening Scene
- Brief introduction of yourself
- "Today I'm demonstrating the Automotive Security Proof of Concept - a system designed to detect and alert on suspicious RF signals that could compromise vehicle security."

### Project Overview
- "This system combines OpenXC vehicle data with HackRF One SDR technology to provide real-time monitoring and detection of potential security threats."
- "It's specifically designed to detect key fob relay attacks, cloning attempts, and signal jamming in the 315MHz and 433MHz frequency bands."

## System Setup

### Show Terminal
- "Let's start by setting up the environment:"
- Run: `source venv/bin/activate`
- Run: `cd src`
- Run: `python main_application.py`

### Show Main Menu
- "Here we have our main menu with several options:"
- "Let's start with the integrated RF detector to see the system in action."

## Real-Time Monitoring Demo
### Show Integrated RF Detector
- "This is our real-time monitoring interface. It's currently scanning the automotive frequency bands."
- "Let me explain the key components of this interface:"
  - Signal strength indicators.
  - Frequency spectrum display.
  - Vehicle data integration (if available).
  - Alert indicators.

### Simulate Attack Scenario
- "Let's simulate a key fob relay attack scenario to demonstrate the system's detection capabilities."
- "I'll use a pre-recorded signal to simulate this attack..."
- "As you can see, the system has immediately detected the suspicious signal pattern and triggered an alert."

### Show Alert Details
- "The alert includes:"
  - Time of detection.
  - Signal characteristics.
  - Potential threat level.
  - Recommended actions.

## Dashboard Demonstration
### Switch to Dashboard
- "Let's take a look at our comprehensive dashboard view by selecting 'Show Dashboard' from the main menu."
- "This dashboard provides a more detailed view of the system's monitoring capabilities."

### Show Key Features
- "Let me highlight some key features:"
  - Historical signal patterns
  - Vehicle data correlation
  - Alert history
  - Configuration settings

### Show Detection History
- "Here we can see the history of all detected signals and alerts, making it easy to track potential security incidents over time."

## Mobile App Integration
### Show Mobile App
- "The system also includes a mobile companion app for on-the-go monitoring."
- "Let me demonstrate how it works:"
  - Real-time alerts.
  - Current status.
  - Quick access to recent incidents.

## Conclusion
### Summary
- "To summarize, this proof of concept demonstrates how we can use modern SDR technology combined with vehicle data to detect and prevent automotive security threats."
- "The system provides real-time monitoring, intelligent detection, and comprehensive alerting capabilities."

### Future Potential
- "While this is a proof of concept, it shows the potential for developing more advanced vehicle security systems that can protect against emerging threats."

### Closing
- "Thank you for watching this demonstration. I hope you found it informative and interesting."
- "For more information about the technical details and implementation, please refer to the project documentation."

# Demo Setup
**Before starting the demo:**
1. Ensure HackRF One is connected and properly configured
2. Have pre-recorded signal samples ready for demonstration
3. Test the alert system to ensure it's functioning
4. Have the mobile app ready for demonstration
5. Prepare any necessary documentation or additional materials
**Recommended recording setup:**
6. Use a screen recording software to capture both the terminal and GUI interfaces.
7. Use a secondary camera to capture your face for a picture-in-picture effect.
8. Ensure good lighting and a clean background.
9. Test audio levels to ensure clear narration.
10. Have a backup plan in case of technical issues.