---
title: Module 11 - OT&SCADA Penetesting
author:
  - Jon Marien
created: 2025-07-26
published: 2025-07-26
tags:
  - skillsontario
  - competitions
  - certifications
  - classes
---

| Title                            | Author                       | Created       | Published     | Tags                                                                                                                               |
| -------------------------------- | ---------------------------- | ------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Module 11 - OT&SCADA Penetesting | <ul><li>Jon Marien</li></ul> | July 26, 2025 | July 26, 2025 | [[#skillsontario\|#skillsontario]], [[#competitions\|#competitions]], [[#certifications\|#certifications]], [[#classes\|#classes]] |
# Task - Lab 9
**CyberQ Module 11 Lab (OT / SCADA Pentesting)**  
1) Capture all flags  
2) Complete the following exercises  
	- Exercise 1: ModBus Protocol Analysis - I  
	- Exercise 2: ModBus Protocol Analysis - II  
Output/Report:  
3) Screenshot of finished lab score  
4) Screen captures of the following steps from the CyberQ Lab Instructions document. 
	- [Exercise 1: ModBus Protocol Analysis - I (Steps: 18, 32, 36)](#Exercise%201%20ModBus%20Protocol%20Analysis%20-%20I%20(Steps%2018,%2032,%2036))
	- [Exercise 2: ModBus Protocol Analysis – II (Steps: 37, 44, 47, 59, 60)](#Exercise%202%20ModBus%20Protocol%20Analysis%20–%20II%20(Steps%2037,%2044,%2047,%2059,%2060))
Use the Lab Guide for preparing the report.

---
# Module 11: OT/SCADA Penetration Testing Methodology

## Objective

The process of penetrating testing with ICS and SCADA is not the same as that of a normal IT pen test. With ICS/SCADA, penetration testers must determine the attack surface largely without sending data into the target, which results in a different type of process to follow for testing ICS and SCADA systems and, consequently, OT networks.

With this type of testing, penetration testers must ensure that they have accurate asset inventory and identification, this can be obtained from the client in the initial data call or from Open Source Intelligence gathering. SCADA penetration testing should be limited to test-bed or development systems and executed in a passive manner to avoid disrupting operations.

## Scenario

Industrial protocols have evolved over time from simplistic networks that collect information from remote devices to complicated networks of systems that have redundancy built into the devices. Protocols utilized inside industrial control systems are occasionally very specific to the application.

Over the years, many efforts have been made by standards organizations such as IEC, ISO, and ANSI to standardize protocols. There is an abundance of proprietary protocols as well. In most cases, these protocols are built by vendors to require specific software and hardware to create vendor-centric systems. Irrespective of the origin of the protocol, most industrial protocols have one aspect in common: they were not designed with security in mind and are inherently insecure.

This has become a significant problem since their convergence with IT networks and the now-dominant Transmission Control Protocol (TCP)/Internet Protocol (IP)-based protocols. Understanding these security flaws and how they are exploited is crucial for penetration testing and threat modeling in industrial control system (ICS) environments.

---

# Exercise 1: ModBus Protocol Analysis - I (Steps: 18, 32, 36)

### Step 18
![[image-793.png]]

### Step 32
![[image-794.png]]

### Step 36
![[image-796.png]]

## Answer:

> [!check]-
> ![[image-797.png]]
> ![[image-798.png]]

---
# Exercise 2: ModBus Protocol Analysis – II (Steps: 37, 44, 47, 59, 60)

### Step 37
![[image-799.png]]
### Step 44
![[image-800.png]]
### Step 47
![[image-801.png]]
### Step 59
![[image-802.png]]
### Step 60
![[image-804.png]]
![[image-805.png]]
## Answer
> [!check]-
> ![[image-803.png]]

---
