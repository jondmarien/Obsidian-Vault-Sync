---
title: POC Analysis
author:
  - Jon Marien
created: 2025-03-23
published: 2025-03-23
tags:
  - classes
---

| Title        | Author                       | Created        | Published      | Tags                   |
| ------------ | ---------------------------- | -------------- | -------------- | ---------------------- |
| POC Analysis | <ul><li>Jon Marien</li></ul> | March 23, 2025 | March 23, 2025 | [[#classes\|#classes]] |

# Analysis of RF Signal Detection Results

Based on the log file `integrated_detection_log_20250323_034913.txt`, I can provide the following analysis of our automotive security proof of concept:

## Overview
- Monitoring Duration: `15 seconds`.
- Alert Threshold: `-60 dBm` (signals stronger than this are flagged as anomalies).
- Attack Probability: `70%` (parameter used during simulation).
- Session Start Time:` 2025-03-23 03:49:13`.

## Key Findings
1. **High Rate of Suspicious Signals:** All detected signals were classified as "SUSPICIOUS" and triggered "Anomaly Detected!" alerts. This is consistent with the high attack probability (70%) setting we used.
2. **Signal Strength Analysis:**
	- All signals were significantly stronger than the -60 dBm threshold.
	- Strongest signal: *-45.36 dBm* (detected at 315.3 MHz at 03:49:25).
	- Weakest signal: *-54.89 dBm* (detected at 315.3 MHz at 03:49:17).
	- Average signal strength: approximately -50.2 dBm.
3. **Frequency Distribution:**
	- Two main frequency bands were detected:
	- 315 MHz band: *4 signals* (315.3-315.6 MHz).
	- 433 MHz band: *4 signals* (433.1-433.4 MHz).
	- This pattern suggests targeted transmissions in known automotive frequencies.
4. **Temporal Pattern:**
	- Signals alternated between the two frequency bands.
	- Consistent detection at 2-second intervals.
	- No gaps in detection throughout the 15-second period.

## Security Implications
The results indicate what appears to be a sophisticated simulation of a potential RF replay attack against a vehicle's remote keyless entry system. Both the 315 MHz and 433 MHz bands are commonly used for automotive remote controls.

The strong signal strengths (-45 to -55 dBm) suggest close proximity transmissions that could potentially override legitimate signals. This could represent either:
- A relay attack capturing and retransmitting legitimate key fob signals.
- A brute force attack attempting to find valid key codes.
- A replay attack using previously captured signals.

## Demo Effectiveness
We believe our POC successfully demonstrates:
1. Detection of potentially malicious RF signals in automotive frequency bands.
2. Real-time monitoring and alerting based on signal strength thresholds.
3. Proper logging and timestamp correlation of detected events.
4. Visual presentation of attack patterns through the terminal interface.

This data provides compelling evidence for our automotive security demonstration, showing how RF-based attacks against vehicles could be detected with appropriate monitoring tools.