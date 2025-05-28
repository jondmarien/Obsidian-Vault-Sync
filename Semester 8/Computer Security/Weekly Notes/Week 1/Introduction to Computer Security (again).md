---
title: Introduction to Computer Security (again)
author:
  - Jon Marien
created: 2025-05-05
published: 2025-05-05
tags:
  - INFO47721
  - classes
---

| Title                                     | Author                       | Created      | Published    | Tags                       |
| ----------------------------------------- | ---------------------------- | ------------ | ------------ | -------------------------- |
| Introduction to Computer Security (again) | <ul><li>Jon Marien</li></ul> | May 05, 2025 | May 05, 2025 | [[#INFO47721\|#INFO47721]] |

# Introduction to Computer Security

# Outline
- [Components of Computer Security](#Basic%20Components)
- [Classes of Threats](#Classes%20of%20Threats)
- [Policies & Mechanisms](#Policies%20&%20Mechanisms)
- [Role of Trust](#Trust%20&%20Assumptions)
- [Assurance](#Assurance)
- [Operational Issues](#Operational%20Issues)
- [Human Issues](#Human%20Issues)

## Basic Components
- Confidentiality:
	- Keeping data and resources hidden.
- Integrity:
	- Data integrity (integrity).
	- Origin integrity (authentication).
- Availability:
	- Enabling access to data and resources.

## Classes of Threats
- Disclosure:
	- Snooping
- Deception:
	- Modification.
	- Spoofing.
	- Repudiation of Origin. (denial of truth)
	- Denial of Receipt.
- Disruption:
	- Modification.
- Usurpation (taking by force):
	- Modification.
	- Spoofing.
	- Delay.
	- Denial of Service.

## Policies & Mechanisms
- Policy says what is, and is not, allowed:
	- This defines "security" for the site/system/etc.
- Mechanisms enforce policies.
- Composition of policies:
	- If polices conflict, discrepancies may create security vulnerabilities.
### Types of Mechanisms
![[image-268.png]]

## Goals of Security
- Prevention:
	- Prevent attackers from violating security policy.
- Detection:
	- Detect attackers' violation of security policy.
- Recovery:
	- Stop attack, assess and repair damage.
	- Continue to function correctly even if attack succeeds.

## Trust & Assumptions
- Underlie *all* aspects of security.
- Policies:
	- Unambiguously partition system states.
	- Correctly capture security requirements.
- Mechanisms:
	- Assumed to enforce policy.
	- Support mechanisms work correctly.

## Assurance
- Specification:
	- Requirements analysis.
	- Statement of desired functionality.
- Design:
	- How system will meet specification.
- Implementation:
	- Programs/systems that carry out design.

## Operational Issues
- Cost-Benefit Analysis:
	- Is it cheaper to prevent or recover?
- Risk Analysis:
	- Should we protect something?
	- How much should we protect this thing?
- Laws & Customs:
	- Are desired security measures illegal?
	- Will people do them?

## Human Issues
- Organizational Problems:
	- Power & Responsibility.
	- Financial Benefits.
- People Problems:
	- Outsiders & Insiders.
	- Social Engineering.

## Tying it all Together
![[image-269.png]]

# Key Points
- Policy **defines** security, and mechanisms **enforces** security.
	- Confidentiality.
	- Integrity.
	- Availability.
- Trust & knowing assumptions.
- Importance of assurance.
- The human factor.