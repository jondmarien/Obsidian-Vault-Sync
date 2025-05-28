---
title: Scoping and Pre-engagement
author:
  - Jon Marien
created: 2025-05-12
published: 2025-05-12
tags:
  - classes
  - INFO40587
---

| Title                      | Author                       | Created      | Published    | Tags                                               |
| -------------------------- | ---------------------------- | ------------ | ------------ | -------------------------------------------------- |
| Scoping and Pre-engagement | <ul><li>Jon Marien</li></ul> | May 12, 2025 | May 12, 2025 | [[#classes\|#classes]], [[#INFO40587\|#INFO40587]] |

# Scoping and Pre-Engagement

# Outline
- [Pentesting Request for Proposal (RFP)](#Request%20for%20Proposal%20(RFP))
- Rules of Engagement (ROE)
- Legal and Regulatory Considerations
- Resource and Tools for Pentesting
- Scope Creep

## Pre-Engagement Activities
- They set the foundation for managing and *successfully* executing a pentesting engagement.
- The activities constitute an important component and should not be overlooked.
- If the client and pentester fail to properly follow said activities, they may face issues like:
	- **Scope Creeping**
	- **Unsatisfied Customers**
	- **Legal Issues**
- The activities start with determining the **goal of the test**.

### Objectives for Conducting
- Evaluate the **scope**.
- Understand the **type** of pentesting.
- Determine the testing **procedure**.
- Identify **resources** needed.
- Outline **rules of engagement**.
- Determine metrics for estimating **time and cost**.
- Estimate **overall cost**.
- Ascertain **the limits** of what you can engage with.
- Learn about the **laws in the jurisdiction** of the test location.

## Request for Proposal (RFP)

### Initiation of a Pentesting Engagement Process
- The client first distributes a request for proposal (RFP) document to various pentesting vendors, or, publishes one, and asks the vendors to submit proposals before a due date.
- An RFP is an invitation to pentesters to submit their proposals for pentesting services to the client organization.
#### Contents of an RFP
- Purpose of the RFP.
	- Goals of the org in relation to pentesting:
		- Evaluate the security of the organization.
		- Identify any security issues that will impact the business.
		- Submit the findings and recomendations.
	- Technical & Contractual Contact:
		- Contact details of individuals to contact for proposal submissions, specifications, SOW requirements, contract terms, conditions, and more.
	- Schedule of Events:
		- Specifies the timetable for events before engagement.

Example:
![[image-299.png]]

### Proposal Submission
- A proposal in response to an RFP should contain the following elements:
	1. Executive Summary.
	2. Project Deliverable.
	3. Itemized Pricing.
	4. Team Strength.
	5. Approach & Methodology.
	6. Project Management.
	7. References.
	8. Company Briefing.

#### Common Evaluation Criteria for Proposals
- The decision on selecting a proposal is based on the following:
	- What has been taking into consideration while deciding operational, technical, cost, and management requirements.
	- Responsivness to the RFP
	- Price quotes for all items mentioned in RFP
- The following primary considerations are also considered for evaluating proposals:
	- Completion of responses in the correct format.
	- Ability to propose an effective solution based on the stated requirements.
	- Ability to deliver the proposed service against specification.
	- Experience, stability, and past record, etc.
	- Ability and availability of sufficient highly skilled team members.

## Preparing for Proposal Submission
![[image-301.png]]

### (1) Identifying Scope, Approach, and Methodology
1. Sending a preliminary information request document to the client.
2. Listing the goals of penetration testing.
3. Scoping the penetration test.
4. Scheduling a pen test scoping meeting with the client.
5. Identifying the types of penetration testing assessment to perform.
6. Identifying the testing strategy.
7. Identifying the areas of infrastructure to test.
8. Identifying the targets to test.
9. Identifying any targets that require dealing with third parties/other countries.
10. Understanding client assessment requirements.
11. Obtaining a detailed proposal of tests to conduct and not conduct.
12. Deciding on the desired depth for penetration testing.

#### 1. Sending a Preliminary Information Request 
- This document contains the client's contact details, objectives and scope of pentesting, list of networks and devices to tests, etc.

#### 2. Listing the Goals of Pentesting
- Identify the organization’s goal from the purpose section of the RPF and preliminary information request document.
- List the primary and secondary goals of the organization along with what the target organization wants tested.
- The primary goals are driven by business risk, while secondary goals are driven by compliance.

![[image-302.png]]

#### 3. Scoping the Pentest
- Scoping the target helps in assessing the possible elements and determining the approach and speed of tests, as well as the tools required.
- It ensures the consistency and high success rate of the penetration test.
- Scoping helps define clear objectives, with which the following can be identified:
	- What will be tested?
	- How it should be tested?
	- What resources will be allocated?
	- What limitations will be applied?
	- What business objectives will be achieved?
	- How the test project will be planned and scheduled?

##### Key Factors to Consider when Scoping
- Target's Criticality:
	- Criticality may vary based on business services or activities it offers. Mission-critical systems, networks, services, and applications should be determined ahead of time.
- Test Location:
	- Some clients allow work on-site, some prefer off-site locations, as employees are not aware of the test.
- Test Volume:
	- Number of systems involved in the test, like number of IPs, a list of web pages and parameters, etc.

###### Advantages of Scoping
- Scoping ensures the consistency and high success rate of the pentest.
- Carefully determined scope helps in preventing collateral damage from intrusive scans or exploits.
- A lack of scoping can lead to a huge chance of failure of the pentest as no proper defintions or procedures have been determined.
- Scoping helps address all the required attributes to start the pentesting project in a professional manner.

#### 4. Scheduling a Pentest Scoping Meeting
- Once goal is identified, schedule a scoping meeting with the client to define the scope of the proposed pentest.
- In many cases, the scoping meeting can be arranged after the contract has been signed.
- However, there is a chance of the client arranging the scoping meeting before the contract is signed.
	- In such cases, the client may ask the tester to sign an NDA before any in-depth scoping discussion.
- **Rules of Engagement (ROE)** and **cost** are not **discussed** in this meeting.
- The scoping meting covers:
	- **Reviewing the RFP Document**.
	- **Questionnaires**.

Sample Questionnaire:
![[image-303.png]]
![[image-304.png]]
![[image-305.png]]
![[image-306.png]]
![[image-307.png]]
![[image-308.png]]
![[image-309.png]]

#### 5. Identifying Types of Pentesting to Perform
- Identify the types of penetration testing assessment that the organization wants performed.
	- Factors: Requirement (Outcome), Budget, Compliance requirements,
- Goal/Objective-based testing:
	- Clearly understand the goal of the test and ensure that it is specific, measurable, attainable, relevant, time-bound, evaluate, and re-evaluate (**SMARTER**)
- Compliance-based testing:
	- Clearly understand the requirements of standards, frameworks, laws, acts, etc. with which the organization wishes to comply
	- For example, in PCI DSS, it is important to limit the PCI DSS scope by reducing/eliminating cardholder data from the environment. Otherwise, cardholder data may be exposed, making the organization incompliant
- Red-team assessment approach:
	- Ensure specificity and accuracy in quantifying the testing environment, e.g., IPs within the scope
		- Prioritize testing efforts based on the objectives, importance, and risk level.

##### SMARTER
![[image-310.png]]

###### Limit the PCI DSS Scope
- It is important to limit the PCI DSS scope by reducing/eliminating cardholder data from the environment.
- Approaches:
	- Implement firewalls to restrict inbound and outbound traffic. Firewalls restrict external users from accessing the internal network and limit internal users’ access to necessary data.
	- Implement point-to-point encryption. Encrypt payment card and cardholder information beginning from the client end throughout the processing of the sensitive data.
	- Use devices approved by the PCI Council.
	- While using third-party vendors for payment processing, ensure that they are PCI DSS compliant.
	- Segment the network and separate the cardholder data environment from the rest of the network.
	- Implement methods approved by the PCI Security Council for timely disposal of cardholder information when not in use.
 - Important points for a **red-team assessment**:
	 - Ensure specificity and accuracy in quantifying the testing environment, e.g., IPs within the scope.
	 - Prioritize testing efforts based on the objectives, importance, and risk level.
	 - Have a good understanding of the risk threshold.
	 - Determine whether the budget matches the testing requirements.

#### 6. Identifying the Testing Strategy
- The appropriate testing strategy **depends on the scenario** in which the testing is to be commissioned:
	- Black-box or white-box testing.
	- Announced or Unannounced testing.
	- Blind or double-blind testing.
- **Determine** if the approach is a black/white/greybox or (un)announced or (double-)blind approach **before starting the pentest**.

#### 7. Identifying Areas of Infrastructure to Test
- Network Penetration Testing.
- Application Penetration Testing.
- Social Engineering Penetration Testing.
- Wireless Network Penetration Testing.
- Mobile Device Penetration Testing.
- Cloud Penetration Testing.
- Virtual Private Network (VPN) Penetration Testing.
- Application programming interface (API) Penetration Testing.

#### 8. Identifying the Targets to Test
- Based on the initial questionnaire phase with the clients in the scoping meeting, identify all the required targets.
- Identify what exactly to test for a specific type of test.
- Identify what targets in the form of specific IPs, network ranges, domain names, devices to be tested, etc.

- **Examples of targets**:
	- Network.
	- Applications.
	- URLs.
	- Servers (IIS, Windows, Linux/Unix, application servers).
	- Workstations and desktops.
	- Network devices (Routers, switches, gateways, LAN cards).
	- Users/employees.
	- Whitelisted/blacklisted IPs configured on IPS/firewall.
	- Access-control lists (ACLs) assigned on resources.
	- Organization’s security policies.
	- Certificate pinning.

##### Identifying the Internal/External Targets to Test Within/Outside the Organization
- Persistent penetration testing of servers, workstations and desktops, and network devices can benefit enterprises in hardening the security and integrity of their infrastructure components.
- Servers:
	- Internet Information Services (IIS) servers.
	- Application servers:
		- Client application servers.
		- Web application servers.
	- Windows servers Unix/Linux server.
- Network Devices:
	- Network Devices.
	- Routers.
	- Hubs.
	- Switches.
	- Modems.
	- Network load balancers.
	- Local area network (LAN) cards.
	- Gateway.
- Workstations and Desktops:
	- Number of workstations per department, in case there are multiple departments in the organization.

![[image-311.png]]

#### 9. Identifying any Targets that Require Dealing with Third Parties
- Identify the services or applications hosted by a third party such as cloud service providers, ISPs, and managed security service providers (MSSP) that need to be tested.
- Take permission from the service provider before starting the test.
- Special permission should be obtained from such third parties to avoid any legal issues.

##### Identifying Targets that Require Dealing with Other Countries
- Identify the countries where targets, e.g., servers, are located. 
- Review all the laws and regulations of that country.
- Do not rely on the client taking legal responsibility for any laws violated.

#### 10. Understanding Client Assessment Requirements
- Create a checklist of assessment requirements.
- Identify the time frame and testing hours.
- Identify who will be involved in reporting and document delivery.

#### 11. Obtaining a Detailed Proposal of Tests (of which to Conduct/Not Conduct)
- Ask the client to submit a detailed proposal for the penetration tests to be conducted and those that should not be conducted.

##### Listing Tests That Will Not be Performed
- Identify the types of tests that should not be performed on the client organization before testing begins.

- Denial of Service (DoS) Testing:
	- DoS pentesting may render the client organization’s services unavailable to its users.
	- If the client is an ecommerce company, then they may not want to get a DoS test performed on their website.
	- DoS penetration testing should be performed only if the organization explicitly wants its infrastructure to be tested against the availability of services; this test should be approved in writing before it begins.
	- AWS and Google Cloud allows remote DDoS with specific clients/programs (from GPT).
- Social Engineering Penetration Testing:
	- Identify the pretexts that should not be used while performing a social engineering penetration test.
	- Pretexts related to sex, drugs, porn, etc. may not be allowed in a corporate environment.
	- Obtain approval in writing for acceptable pretexts before the test.

#### 12. Deciding on the Desired Path for Pentesting
- Decide the depth of the proposed penetration test based on the scope identified during the penetration test scoping.
- The depth provides an estimate of the time, resources, and expenses required for the test.

- Consider the following **factors for deciding the depth** of the proposed penetration test:
	- Type of testing required (black box/white box/announced/unannounced/blind/double blind).
	- Areas of infrastructure to test .(network/application/wireless network/cloud/DoS)
	- Number of targets to test (IP addresses, network ranges, domain names, and devices.

### (2) Determining Project Deliverables

#### Preparing for Proposal Submission
![[image-312.png]]

##### Identifying How the Final Report will be Delivered
- The final report is prepared using the **test performed** in the organization.
- Discuss with the client organization the type of **report format** it expects to receive upon completion of the pentest.
- The detailed report should contain the following:
	- Vulnerabilities in the Organization:
		- Countermeasures to reduce vulnerabilities.
		- Recommendations.
		- Document the result.
		- Final Summary.

###### Identifying the Reports to Deliver after the Pentest
- The following are various reports provided after the completion of the penetration testing process:
	- Network test reports.
	- Client-side test reports.
	- Web-application test reports.
	- ...and more!

### (3) Determining the Project Schedule/Specifying the Test Duration
- After the scope has been identified, specify and agree on the **start** and **end** for an engagement.
- This allows for ending the engagement at a **predetermined time**. 
- It also helps overcome **scope creep**.

### (4) Understanding Staffing Requirements
- Identify a group of experts required in the penetration testing team based on the area and type of penetration testing.
- Specify the details of expertise in the team along with the skills and experience of team members.
	- Network Penetration Testers.
	- Policy Penetration Testers.
	- Application Penetration Testers.
	- Database Penetration Testers.
	- Report Writers.

### (5) Proposing Detailed & Itemized Pricing
- The estimated cost depends on the estimated scope, resources, and time required for the pentest engagement.
- If the estimated scope, resources, and time required are high, then the cost will also be high.
- Negotiate Per Day/Per Hour Fee for the Penetration Testing Project:
	- Based on the work performed by the testing team, negotiate the nature of payments as hourly or daily.
	- Salary negotiation is handled by the chief penetration tester, and the salary is distributed as per the rules of the client organization.
- How Much to Charge?
- Penetration test pricing varies based on the scope and number of man-days required to cover the scope of the project.

### (6) Submitting the Proposal
- Prepare an executive summary with a high-level synopsis that briefs the client on the engagement, features, and benefits of the proposed work.
- Before submitting the proposal, have a discussion with different experts in the team and generate a draft proposal to be sent to the client for discussion.
- Draft the proposal with the expected response requirements.
- Submit the proposal before the due date specified by the client.

## Setting the Rules of Engagement

### Rules of Engagement (ROE)
- ROE is the **formal permission** to conduct pentesting.
- ROE helps testers overcome **legal, federal,** and **policy-related restrictions** to use different pentesting tools and techniques.
- **Scoping** and **ROE** are two aspects that need to be handled independently while engaging in a pentesting assignment.
- Scoping defines **what** should be tested, while ROE **defines** the agreement on **how testing should be performed** within **certain limitations and rules** during pentesting.

### Drafting a ROE
- Conduct a meeting with the top management and techincal teams to discuss said ROE.
- Rules are created based on the following directives:
	- Establishing communication lines:
		- How often and in which manner will the test team and client communicate with each other?
		- Who will be the point of contact (POC) for both the client and test team?
	- Identifying Time/Location:
		- When and where will the progress of the test be informed?
	- Establishing the Timeline:
		- When will specific milestones in the engagement be completed?
	- Deciding the Frequency of Meetings:
		- What will be the frequency of meetings for briefing the client on the progress of the test?
	- Time of day to conduct testing:
		- At what time of the day should testing be performed?
	- Identifying Personnel for Assistance:
		- Who will conduct the pen test assessment?
	- Deciding the Evidence Handling Process:
		- What care should be taken while handling the evidence for the test?

#### Work Breakdown Structure (WBS) or Task List
- Developing a task list means breaking down a piece of work into its component tasks.
- The task status must be measurable.
- Each task must be a clearly defined event with a clear start and a clear end.
- Every task must have a deliverable.
- Example:
	- Where the tasks start and end.
	- Time estimates.
	- Task dependencies.
	- Resources assigned to each task.

#### Pentesting Schedule
- A penetration test schedule details the timing and duration of various tasks involved in testing.
- It provides a thorough design of the tasks performed during penetration testing.
- Details of the test schedule must be documented in a separate deliverable and generated with the assistance of a project scheduling tool. 
- The following tools may help in creating a penetration test schedule:
	- Microsoft Project Professional.
	- Zoho Projects.
	- GanttProject.

#### Meeting with the Client
- A pen tester should keep the client continuously informed about the project.
- Decide how often meetings should be held with the client regarding the progress of test: daily, weekly, etc.

#### Deciding the Time of Day for the Test
- Decide the time of the day at which testing should be performed.
	- Business hours.
	- After business hours.
	- Weekends.

#### Identifying the Local HR Resources Required for the Pentest
- Study and understand the pen testing requirements to identify the human resources required to perform a successful pen test.
- The local human resource requirements to perform the penetration testing are as follows:
	- Application Administrator.
	- Database Administrator.
	- Network Administrator.
	- OS Administration.

#### Identifying the Client's IT Security Admin
- To make the penetration testing successful, the tester must have an understanding of the security related issues of the organization.
- The information security administrator is the person responsible for the data and application security of the organization.
- The administrator of the organization should be identified.
- The security administrator can provide an understanding of the core parts of security and is accountable for network and system updates.
- Security administrators can assist in installing tools, testing services, etc.

##### ROE Document
- ROE is a separate formalized document that states the rules to be followed during the execution of the engagement.
- The ROE established between the tester and client should be documented, and both the parties should sign it

![[image-314.png]]

### Engagement Letter (EL) from the Client
- A pen testing engagement begins with the **receipt of the EL**. 
- Once all agreements on **scope** and ROE **are** completed, the client sends the final EL.
- Scan the EL into an electronic format. Produce an **MD5 hash** of the document for integrity purposes.

## Legal and Regulatory Considerations Critical to Pentesting

### Hiring a Lawyer
-  Hire a lawyer who can understand technology and related matters.
- Sign a legal document related to the penetration testing before starting the penetration testing assignment. 
- Have the document vetted by the lawyer before signing. 
- A lawyer who understands information technology and the risks associated with testing can render professional services more efficiently.

### Pentesting Contract
- The penetration testing contract must be **drafted by a lawyer** and **signed** by the penetration tester and the client company.
- The contract must clearly state the following:
	- Non-disclosure clause.
	- Objective of the penetration test.
	- Fees and project schedule.
	- Sensitive information.
	- Confidential information.
	- Indemnification clause. (not legally liable for breaking something, if you have "protection")
	- Reporting and responsibilities.

#### Drafting Contracts
- The pen test contract is the most important document to define and regulate the legal relationship between the penetration tester and client.
- It protects both parties from misunderstandings and includes agreements such as the following:
	- Scope of the Test.
	- Performance Standards.
	- Security and Confidentiality.
	- Audit Information.
	- Reporting and Cost.
	- Ownership and License.
	- Dispute Resolution and Indemnification.

#### Pentesting "Rules of Behaviour"
- Penetration testing “**rules of behavior**” is a penetration testing agreement that outlines the framework for external and internal penetration testing.
- Prior to testing, this agreement is signed by representatives from both the target organization and penetration testing organization to ensure a mutual understanding of the limitations, constraints, liabilities, and indemnification considerations.
- A **release and authorization** form may be required (in addition to the rules of behavior) that states the penetration testing organization will be **held harmless** and **not criminally liable** for unintentional interruptions and loss or damage to equipment.

#### Create a Get-Out-of-Jail-Free Card
- A **get-out-of-jail-free card** is an element that helps a person or organization emerge from an undesirable situation.
- The agreement **outlines** the types of **activities** to be performed and indemnifies the tester against any loss or damage that may result from the testing.
- The **get-out-of-jail-free card** entails a **legal agreement** signed by an authorized representative of the organization.
- The card is a **part of the penetration testing contract** and should include an incident response plan and appropriate client contact who can be alerted should an issue arise.

##### Listing the Permitted Items in the Legal Agreement
- Before performing the test, the pen tester must necessarily know and seek written permission for the following essential elements:
![[image-315.png]]

### Confidentiality and NDA Clauses
- Many documents and other information regarding the pen test contain critical information that could **damage one or both parties** if improperly disclosed.
- The tester also signs an agreement guaranteeing that the company’s information will be treated confidentially.
- It **provides cover** for a number of other key areas, such as negligence and liability, in the event of an untoward incident.
- Agreements are designed to be used by both the parties to protect sensitive information from disclosure.
- Both parties **bear the responsibility to protect** tools, techniques, vulnerabilities, and information from disclosure beyond the terms specified by a written agreement.
- NDAs should be **narrowly drawn** to protect sensitive information.
- Specific areas to consider include the following:
	- Ownership.
	- Use of the evaluation reports.
	- Results and the use of the testing methodology in client documentation.

#### Preparing an NDA and Having the Client Sign
- An NDA is an agreement that **contains confidential information**.
- The NDA should also be aimed at **protecting** the penetration tester’s interests.
- The lawyer should **vet the NDA form** before the client is asked to sign it.
- Include clauses highlighting the fact that the tester and their team **will not disclose any information** divulged by the client during the penetration test.

### Defining Liability Issues
