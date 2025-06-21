---
title: Midterm Study - Questions Answered
author: Jon Marien
created: 2025-06-16
published: 2025-06-16
tags: 
---

| Title                              | Author     | Created       | Published     | Tags |
| ---------------------------------- | ---------- | ------------- | ------------- | ---- |
| Midterm Study - Questions Answered | Jon Marien | June 16, 2025 | June 16, 2025 | \-   |

---
### INTRODUCTION

1. **What is Penetration Testing? Discuss.** Penetration testing is a type of security testing that evaluates an organization's ability to protect its infrastructure, including networks, applications, systems, and users, against both external and internal threats. It is an effective method for determining the efficacy of an organization's security policies, controls, and technologies. During a penetration test, security measures are actively analyzed for design weaknesses, technical flaws, and vulnerabilities by simulating attacks similar to those performed by real attackers. The results of the test are documented and delivered in a comprehensive report to both executive management and technical audiences. Penetration testing focuses on achieving specific security goals rather than merely ticking checkboxes or just finding vulnerabilities.
    
2. **Discuss the benefits of conducting a penetration testing.** Conducting a penetration test offers several benefits to an organization:
    
    - It proactively identifies threats and determines the probability of an attack on information assets.
    - It assures the organization that it operates within an acceptable limit of information security risks.
    - It helps determine the feasibility of various attack vectors and the potential business impact of a successful attack, providing a comprehensive approach for preparation steps to prevent future exploitation.
    - It ensures the effective implementation of security controls, leading to a better return on investment (ROI) on IT security.
    - It helps achieve compliance with regulations and industry standards such as ISO/IEC 27001:2013, PCI-DSS, HIPAA, and FISMA.
    - It focuses on high-severity vulnerabilities and emphasizes application-level security issues for development teams and management.
    - It evaluates the efficiency of network security devices like firewalls, routers, and web servers.
    - For network penetration testing specifically, it helps administrators close unnecessary ports and services, hide or customize banners, troubleshoot services, and calibrate firewall/IDS rules for robust security. It also helps organizations avoid huge fines for noncompliance and protects them from heavy financial losses due to security breaches.
3. **What is meaning of ROI in the context of penetration testing? Discuss.** ROI, or Return on Investment, in the context of penetration testing means that the testing helps companies identify, understand, and address vulnerabilities, which ultimately saves them a significant amount of money. Demonstrating ROI is a critical process for successfully "selling" a penetration test to an organization. The ROI for a penetration test is shown through a business case scenario that includes both the expenditure on the test and the involved profits (or avoided losses). Companies typically invest resources in a penetration test only if they have proper knowledge of its benefits, which include preventing costly security breaches. The formula for ROI is (Expected Returns - Cost of Investment) / Cost of Investment.
    
4. **Compare and contrast ‘security audit’, ‘vulnerability assessment’, and ‘penetration testing’.** These three security assessments differ in their scope and objectives:
    
    - **Security Audit**: A security audit checks whether an organization follows a set of standard security policies and procedures. It focuses on policy adherence.
    - **Vulnerability Assessment**: A vulnerability assessment concentrates on discovering vulnerabilities within an information system. However, it does not indicate whether these vulnerabilities can be exploited or the potential damage from successful exploitation. It's about finding flaws but not proving exploitability.
    - **Penetration Testing**: Penetration testing is a methodical approach to security assessment that encompasses both a security audit and a vulnerability assessment. Crucially, it goes further by demonstrating whether the vulnerabilities in a system can be successfully exploited by attackers. Unlike vulnerability scanning, which is part of a pentesting program but not a substitute, penetration testing focuses on achieving specific goals rather than just finding vulnerabilities.
5. **What is the meaning of ‘blind testing’ and ‘double bind testing’ in black box testing? Explain.** Black-box testing assumes the penetration tester has no previous knowledge of the infrastructure to be tested and limited information about the target company. It simulates a real hacking process, requiring extensive information gathering. Within black-box testing, there are further classifications:
    
    - **Blind Testing**: This type simulates the methodologies of a real hacker, where limited or no information is provided to the penetration testing team. It is a time-consuming and expensive process.
    - **Double-blind Testing**: In this approach, very few people in the organization are aware that the penetration test is being conducted. It specifically involves testing an organization’s security monitoring, incident identification, and response procedures.
6. **What are the common areas of penetration testing?** Common areas of penetration testing include:
    
    - Network Penetration Testing
    - Web Application Penetration Testing
    - Social Engineering Penetration Testing
    - Wireless Network Penetration in Testing
    - Mobile Device Penetration Testing
    - Cloud Penetration Testing
    - Virtual Private Network (VPN) Penetration Testing
    - Application Programming Interface (API) Penetration Testing
7. **What are the common network security issues?** Common network security issues identified during network penetration testing include:
    
    - Use of insecure protocols
    - Unused open ports and services
    - Unpatched operating system (OS) and software
    - Misconfiguration in firewalls, intrusion detection systems (IDS), servers, workstations, and network services
8. **What are the common security issues in web application?** Common web application security issues detected due to insecure design and development practices include:
    
    - Injection vulnerabilities
    - Broken authentication and authorization
    - Broken session management
    - Weak cryptography
    - Improper error handling
9. **What are the common security issues in wireless network infrastructure?** Common security issues found in wireless network infrastructure include:
    
    - Unauthorized/rogue/open access points
    - Insecure wireless encryption standards
    - Weak encryption passphrases
    - Unsupported wireless technology
10. **What are the six steps of EC-Council’s LPT methodology?** The EC-Council’s Licensed Penetration Tester (LPT) methodology involves custom penetration testing tools, techniques, and procedures (TTPs). While the question asks for six steps, the source provides **eleven** distinct steps:
    
    1. Planning and Scoping
    2. Reconnaissance and Information Gathering
    3. Vulnerability Assessment
    4. Gaining Access
    5. Privilege Escalation
    6. Lateral Movement
    7. Maintaining Access
    8. Data Exfiltration
    9. Clearing Tracks
    10. Documentation and Reporting
    11. Remediation Testing

---

### SCOPING AND ENGAGEMENT

1. **Discuss the importance of pre-engagement activities.** Pre-engagement activities are crucial as they set the foundation for managing and successfully executing a penetration testing engagement. These activities are an important component that should not be overlooked by either the pen tester or the client. Failing to properly follow pre-engagement activities can lead to issues such as scope creep, unsatisfied customers, and even legal problems in the penetration testing engagement. The pre-engagement process begins with determining the goal of the test.
    
2. **What are the primary objectives of conducting pre-engagement activities?** The primary objectives for conducting pre-engagement activities include:
    
    - Evaluating the scope of penetration testing.
    - Understanding the type of penetration testing required.
    - Determining the penetration test procedure.
    - Identifying the amount of resources needed for the test.
    - Outlining the rules of engagement (ROE).
    - Determining the metrics for estimating the time and cost of the test.
    - Estimating the overall cost.
    - Ascertaining the limits of engagement.
    - Learning about the laws in the jurisdiction of the test location.
3. **What is an RFP? What are the typical contents of an RFP?** An RFP, or Request for Proposal, is an invitation distributed by a client to various penetration testing vendors, asking them to submit proposals for penetration testing services before a specified due date. The typical contents of an RFP include:
    
    - **Purpose of the RFP**: States why the RFP is being issued.
    - **Goals of the organization in relation to penetration testing**: Outlines objectives such as evaluating the organization's security, identifying security issues that will impact the business, and requiring submission of findings and recommendations.
    - **Technical & Contractual Contact**: Provides contact details for individuals to reach regarding proposal submission, specifications, Statement of Work (SOW) requirements, contract terms, conditions, etc..
    - **Schedule of Events**: Specifies the timetable for events leading up to the engagement.
4. **What are the typical contents of a proposal?** A proposal submitted in response to an RFP should typically contain the following elements:
    
    1. **Executive Summary**: A high-level synopsis, features, and benefits of the proposed engagement.
    2. **Project Deliverables**: Describes the types of reports that will be provided (e.g., executive summary report, technical report).
    3. **Itemized Pricing**: Details on how charges will be calculated.
    4. **Team Strength**: Biographies and relevant experience of team members.
    5. **Approach and Methodology**: Detailed testing procedures and technical expertise needed for the engagement.
    6. **Project Management**: Explains the method and approach for project management and how the engagement will proceed from start to end.
    7. **References**: Relevant references for similar work performed in the past.
    8. **Company Briefing**: Information on the company, including its official address, contact details, and expertise in offering similar services.
5. **What is ‘scoping’? Elaborate its function.** Scoping in penetration testing involves assessing the possible elements of the target organization to define clear objectives, determine the approach and speed of tests, and identify the tools required. It helps define what will be tested, how it should be tested, what resources will be allocated, what limitations will be applied, what business objectives will be achieved, and how the test project will be planned and scheduled. Its functions include:
    
    - Ensuring the consistency and high success rate of the penetration test.
    - Helping to prevent collateral damage from intrusive scans or exploits.
    - Addressing all required attributes to start the penetration testing project in a professionally sound manner.
    - A lack of scoping can lead to a high chance of failure because assessment requirements will lack proper definitions or procedures to follow.
6. **For a scoping questionnaire, give some example questions for ‘Social Engineering’.** For a social engineering scoping questionnaire, example questions include:
    
    - Does the client have a list of email addresses against which a social engineering attack needs to be performed?
    - Does the client have a list of phone numbers against which a social engineering attack needs to be performed?
    - Is the social engineering attack being performed for gaining unauthorized physical access? If so, how many people will be targeted?
7. **Elaborate the ‘SMARTER’ approach of penetration testing.** The SMARTER approach is used, particularly in goal/objective-based testing, to ensure the test goals are clearly understood and well-defined. SMARTER stands for:
    
    - **S** - SPECIFIC: Goals must be clear and precise.
    - **M** - MEASURABLE: The progress and outcome of the goal should be quantifiable.
    - **A** - ATTAINABLE: The goals should be realistic and achievable.
    - **R** - RELEVANT: The goals should align with the organization's broader security objectives.
    - **T** - TIMEBOUND: There should be a defined timeframe for achieving the goals.
    - **E** - EVALUATE: The process involves evaluating the progress and results.
    - **R** - REEVALUATE: Continuous reevaluation of the goals and approach as needed.
8. **List some examples of pentesting targets.** Examples of penetration testing targets include:
    
    - Network
    - Applications
    - URLs
    - Servers (IIS, Windows, Linux/Unix, application servers)
    - Workstations and desktops
    - Network devices (Routers, switches, gateways, LAN cards, modems, network load balancers, hubs)
    - Users/employees
    - Whitelisted/blacklisted IPs configured on IPS/firewall
    - Access-control lists (ACLs) assigned on resources
    - Organization’s security policies
    - Certificate pinning
9. **Give some example types of tests that may be identified as off-limits of pentesting.** During the scoping phase, certain types of tests may be identified as off-limits and should not be performed on the client organization without explicit written approval. Examples include:
    
    - **Denial of Service (DoS) Testing**: This type of test may render the client organization’s services unavailable to its users. If the client is an e-commerce company, they may not want a DoS test on their website. It should only be performed if explicitly requested and approved in writing.
    - **Social Engineering Penetration Testing (with certain pretexts)**: Specific pretexts related to sex, drugs, or pornography may not be allowed in a corporate environment. Approval for acceptable pretexts should be obtained in writing before the test.
10. **What is ROE? Elaborate.** ROE, or Rules of Engagement, is the formal permission to conduct penetration testing. It is a separate formalized document that states the rules to be followed during the execution of the engagement. ROE helps testers overcome legal, federal, and policy-related restrictions that might otherwise prevent the use of certain penetration testing tools and techniques. While scoping defines what should be tested, ROE defines the agreement on _how_ testing should be performed within certain limitations and rules during the penetration testing. Both the tester and client should sign the documented ROE. Key aspects discussed in drafting an ROE include establishing communication lines (how often and in what manner), identifying time/location for progress updates, establishing timelines for milestones, deciding meeting frequency, defining the time of day for testing, identifying personnel for assistance, and deciding the evidence handling process.
    
11. **What is the purpose of an ‘Indemnification clause’ in a pentesting contract?** An 'Indemnification clause' in a penetration testing contract is a provision designed to protect one party (the penetration testing organization) from liability for damages or losses incurred by the other party (the client) during the course of the engagement. It's typically included in the broader penetration testing "rules of behavior" or contract. This clause ensures that the penetration testing organization will be held harmless and not criminally liable for unintentional interruptions, loss, or damage to equipment that may occur as a result of the testing.
    
12. **What is the meaning of ‘scope creeping’? Elaborate.** Scope creeping occurs when a client asks for additional tests or tasks to be included during the engagement that go beyond the scope initially defined and agreed upon. This is a common issue in penetration testing engagements. Scope creeping can lead to legal problems and consume a significant portion of the estimated time and resources that were allocated for the original scope. To battle scope creep, pen testers should strive to help the client but request payment for any extra work. If the client agrees to pay an additional amount and legally allows for the extra time and resources, the tester can agree to the work; otherwise, they should politely refuse.

---

### OPEN SOURCE INTELLIGENCE

1. **“Open Source Intelligence (OSINT) gathering is required for all types of penetration tests."- Discuss.** Yes, Open Source Intelligence (OSINT) gathering is required for all types of penetration tests. It is the first phase of penetration testing, often referred to as "footprinting," where primary information about a potential target is gained. For external network penetration testing, the penetration tester performs a survey to gather all possible information about the target network, such as IP addresses, domain names, device type, applications and their versions, and implemented security tools (IDS, IPS, firewalls). This intelligence helps in developing effective testing methods. Even for black-box network penetration testing, where no information is provided, the tester relies on OSINT to gather target network information like domain names, IP range, live hosts, OS details, network map, device types, and security defenses. OSINT is also crucial in the black-box social engineering penetration test, where the tester must obtain information about the target using OSINT techniques.
    
2. **What is the purpose of finding similar or parallel domain names?** Finding similar or parallel domain names serves several purposes in penetration testing:
    
    - **Detecting typosquatters**: It helps detect entities profiting from typos in a legitimate domain name.
    - **Brand protection**: It aids in protecting a brand by identifying and potentially registering popular typos that users might make.
    - **Identifying traffic redirection**: It helps identify typo domain names that will receive traffic intended for another domain, which could be malicious.
    - **Conducting phishing attacks**: During a penetration test, this information can be used to conduct realistic phishing attacks by crafting convincing fake domains that resemble the target's actual domain.
3. **In a google advanced search with ‘intitle:index.of xyz’, what you expect to get?** Using the Google advanced search operator `intitle:` restricts search results to pages containing the search keyword in their title. When combined with `index.of`, such as `intitle:index.of xyz`, you would expect to get results pointing to publicly accessible web server directories that have directory listing enabled for "xyz" related content. These are often misconfigured servers that expose directory contents, potentially revealing sensitive files or information. This is part of "Google hacking" or "dorking," where specific queries are used to find sensitive information inadvertently exposed online.
    
4. **What services are provided by ‘Shodan’? Elaborate.** Shodan is a search engine designed for finding specific devices and device types that are connected to the internet and are openly accessible online. It allows penetration testers to identify a wide range of devices, including:
    
    - Webcams
    - Routers
    - Switches
    - Internet of Things (IoT) devices It can be used to search for specific devices, like Cisco routers worldwide by their public IP addresses, or webcams with their public IP addresses. This helps in identifying potential attack surfaces that are exposed to the internet.
5. **How can you use OSINT to find out what type of networking devices are used in the organization?** OSINT can be used to identify the type of networking devices used in an organization through several methods:
    
    - **Analyzing online documentation**: Examine the organization’s publicly available documentation for mentions of specific device vendors or technologies.
    - **Job postings**: Search for the company’s job postings in major newspapers, classifieds, and job search engines. Job requirements for roles like system administrators, database operators, or security administrators often list the required experience with specific technologies or device types, indicating the organization's existing infrastructure.
    - **Technical forums and professional profiles**: These results may include links to professional profiles or social networking sites, offering valuable details about the network devices and configurations in use.
    - **Google searches with keywords**: Google specific keywords along with the organization’s name (e.g., "ASA firewall with [Company Name]") to find relevant information from job sites, professional or social networking sites.
6. **What kind of sensitive information you may find in the source code of a company’s web pages?** By examining the HTML source code of web pages, sensitive information can often be found in comments or other exposed elements. This may yield information about:
    
    - Back-end technologies being used.
    - External links.
    - File system structure.
    - Script types. This information can potentially be exploited by an attacker.
7. **What information you may expect to find using DNS interrogation?** DNS interrogation, which involves querying DNS records, can provide important information about the location and type of servers associated with a target domain. Expected information includes:
    
    - **Subdomains**: Different applications and parts of the attack surface.
    - **DNS records**: Such as A (IPv4 address), AAAA (IPv6 address), MX (mail servers), NS (name servers), CNAME (aliases), SOA (start of authority), SRV (service records), PTR (IP to hostname mapping), HINFO (host information like CPU type and OS), and TXT (unstructured text records, e.g., SPF, DKIM).
    - **Hostnames and machine names**: Especially through DNS zone transfers.
    - **Usernames and aliases**: Potentially exposed through zone transfers.
    - **IP addresses**: Including net blocks allocated to the organization.
    - **Publicly accessible services**: Indicated by various DNS entries. Tools like Nmap (with dns-brute), SubBrute, dnsmap, dnsenum, fierce, sublist3r, and dig are used for DNS interrogation.
8. **Who provides the ‘whois’ service? What information you may get using ‘whois’ service?** Whois databases are maintained by Regional Internet Registries (RIRs). Examples of RIRs include AFRINIC, ARIN, APNIC, LACNIC, and RIPE NCC. The Whois tool sends a query to these databases and can obtain personal and technical details about domain owners and their associated resources. Information obtainable via Whois includes:
    
    - Domain name details.
    - Contact details of the domain owner.
    - Domain name servers.
    - IP address and NetRange (IP address block allocated).
    - Domain creation date and expiry records.
    - Physical location.
    - Telephone number and email address.
    - Technical and administrative contacts.
9. **Why would you perform reverse DNS lookups (PTR) in penetesting?** Performing reverse DNS lookups (PTR) on a target’s IP range is valuable in penetration testing for several reasons:
    
    - **Locating DNS PTR records**: It specifically helps to find a DNS PTR record for those IP addresses, which maps an IP address back to a hostname.
    - **Identifying other domains on shared servers**: It allows discovery of other domains that might share the same web server. This is important for understanding potential attack vectors, especially in shared web hosting environments, as a vulnerability in one domain could impact others on the same server.
    - **Mapping infrastructure**: It aids in mapping out the network infrastructure more completely by revealing hostnames associated with IP addresses, which might not be immediately apparent from forward DNS lookups.
10. **During information gathering phase of pentesting, why would you use ‘maltego’?** During the information gathering (OSINT) phase of penetration testing, Maltego is a valuable tool because it is an OSINT and forensics application designed to deliver a clear threat picture of an organization's environment. It is useful for:
    
    - Determining relationships and real-world links among various entities such as people, groups of people (social networks), companies, organizations, websites, internet infrastructure, phrases, documents, and files.
    - Visualizing these relationships in a clear, graph-based format, making complex connections easier to understand. This helps penetration testers gain a comprehensive understanding of the target's external footprint and interconnected entities, which is crucial for planning subsequent attack phases.

---

### NETWORK PENETRATION TESTING – EXTERNAL, INTERNAL

1. **Discuss the steps of network pentesting process.** The network penetration testing process generally follows a structured methodology to ensure thorough assessment. The typical steps are:
    
    1. **Information Gathering (OSINT)**: The penetration tester collects all possible information about the target network, including IP addresses, domain names, device types, applications and their versions, and security tools like IDS, IPS, and firewalls. This information is used to develop testing methods.
    2. **Port Scanning**: Testers use port scanning techniques to find live IP addresses, open ports on network devices, and fingerprint running services. Vulnerability scanners and port scanning tools are employed here.
    3. **OS and Service Fingerprinting**: The operating system (OS) running on the target device is identified to find and exploit known vulnerabilities. This step also identifies protocols, brands, and versions of servers running on specific ports.
    4. **Vulnerability Research**: After identifying live IP addresses, open ports, services, applications, and OSs, testers scan the host for known vulnerabilities using vulnerability scanning tools with built-in databases.
    5. **Exploit Verification**: In this step, testers analyze available exploits through manual verification and password cracking to validate the findings before reporting.
    6. **Reporting**: Finally, a comprehensive report is prepared, detailing findings, suggesting solutions, and making recommendations.
2. **Explain the differences of (i) Connect scan, and (ii) SYN scan.** Both Connect scan and SYN scan are port scanning techniques used to determine if a port is open on a target.
    
    - **(i) Connect Scan (Full Open Scan)**: This scan uses the operating system's `connect()` system call to attempt to establish a full TCP connection with the target at all specified ports. If the connection is successfully established (completing the three-way handshake: SYN, SYN/ACK, ACK), it indicates the port is open. This type of scan is less stealthy as it completes the connection, which can be logged by the target system. Nmap uses the `-sT` switch for this scan.
    - **(ii) SYN Scan (Half-open Scan)**: This is a stealthier scanning technique designed to bypass firewall rules and logging mechanisms. The client sends a SYN packet to the target and waits for a response. If the target responds with SYN/ACK, it indicates the port is open, but the scanner immediately sends an RST (reset) packet instead of completing the three-way handshake. This means the connection is never fully established, often making it less likely to be logged by the application layer. If the target responds with an RST, the port is closed. Nmap uses the `-sS` switch for this scan.
3. **Explain how ACK Flag probe scan works.** The ACK Flag probe scan works by sending TCP probe packets with the ACK flag set to a remote device. The goal is to analyze the header information, specifically the WINDOW field, of any received RST (reset) packets to determine whether a port is open or closed.
    
    - On some systems, the WINDOW value of RST packets from closed ports is always zero.
    - If the WINDOW value on a particular port has a non-zero value in the RST response, it suggests that the port is open. However, the source notes that this technique alone cannot be entirely relied upon to determine the state of ports, as its effectiveness depends on the specific TCP/IP implementation details used by a minority of systems. It is primarily useful for probing for the presence of stateful firewalls.
4. **Explain how you would interpret the response from a UDP scan.** When performing a UDP scan, the interpretation of the response helps determine the state of a port:
    
    - **No response**: This indicates that the port is either **open** or **filtered** (e.g., by a firewall). The absence of a response means the UDP packet was likely received by an open port, or it was blocked by a filtering device.
    - **ICMP "port unreachable" error message (Type 3 with Code 3)**: This explicitly indicates a **closed port**.
    - **ICMP Type 3 error with codes 0, 1, 2, 9, 10, or 13**: These codes indicate a **filtered port**, meaning a firewall or another filtering device is blocking the traffic.
5. **What is the purpose of fragmentation in scanning. Elaborate.** The purpose of fragmentation in scanning is to evade detection by packet filters and intrusion detection systems (IDS). Instead of sending a complete probe packet, it is broken into several smaller IP fragments. This technique splits up the TCP header over multiple packets, making it harder for firewalls and packet filters to reassemble and detect the true nature of the scan (e.g., a SYN scan or FIN scan). In Nmap, the `-f` switch is used to instruct the specified scan (like SYN or FIN) to use tiny fragmented packets. This makes the scan appear less suspicious to security devices that might be looking for complete, identifiable packet headers.
    
6. **What are the typical sources of information about the details of vulnerabilities, once OS and service fingerprinting is done?** Once OS and service fingerprinting are complete, and the specific versions of operating systems, services, and devices running on the target are known, typical sources for finding detailed information about associated security vulnerabilities include:
    
    - **Google hacking database (GHDB)**: A database of queries that penetration testers use to identify exploitable targets and sensitive data through search engines. It can reveal advisories, server vulnerabilities, error messages, files with passwords, sensitive directories, and login portals.
    - **National Vulnerability Database (NVD)**: A U.S. government repository of standards-based vulnerability management data represented using the Security Content Automation Protocol (SCAP). (Though not detailed, mentioned as a source).
    - **Exploit Database**: A comprehensive archive of exploits and vulnerable software, often used to find known exploits for specific vulnerabilities.
    - **CVE Details (www.cvedetails.com)**: Provides detailed information on Common Vulnerabilities and Exposures (CVEs).
    - **BugtraqID**: Can also show exploits.
    - **Nessus scan results**: When performing vulnerability assessments, Nessus provides detailed reports including vulnerability descriptions, risk information (CVSS), exploitable status, and references to external databases like CVE and BID.
7. **Explain the distinguishing features of internal network penetration testing.** Internal network penetration testing focuses on assessing the security from an "insider's perspective". Its distinguishing features include:
    
    - **Testing from within the corporate network**: The assessment is conducted inside the organization's network, meaning the tester is already "past the perimeter firewall". This contrasts with external testing, which assesses from across the internet and must break through firewalls and IDS/IPS systems.
    - **Focus on internal assets**: It involves testing computers and devices _within_ the company or organization, examining internal IT systems for weaknesses that could disrupt confidentiality, availability, or integrity.
    - **Perspective of an inside attacker**: The test is performed to discover and exploit known and unknown vulnerabilities from the viewpoint of an insider, whether malicious or accidental.
    - **Complementary to external testing**: While external penetration testing ensures external ports and services are blocked, internal testing ensures that the organization's internal assets are properly secured.
8. **Why should you perform internal network penetration testing?** Internal network penetration testing is crucial for several reasons:
    
    - **Evaluate internal security measures**: It checks existing internal security controls to determine what information and access an insider could obtain.
    - **Understand insider risk**: It helps management understand the level of risk posed by malicious or negligent users within the organization's internal network.
    - **Detailed internal network insights**: It provides comprehensive details about the organization's internal network, enabling the suggestion of cost-effective and targeted mitigation approaches.
    - **Basis for future security strategy**: It creates a foundation for future decisions regarding the organization’s information security strategy and resource allocation, ensuring internal assets are properly secured.
9. **What is the meaning ‘enumeration’ in network pentesting? Explain why we should perform service enumeration.** In network penetration testing, **enumeration** refers to the process of creating active connections with computer systems and performing directed queries to gain more detailed information about the organization’s network. The extracted information is used to identify system attack points and potentially perform password attacks to gain unauthorized access to information system resources. It gathers information about network resources and shares, routing tables, audit and service settings, SNMP and DNS details, machine names, users and groups, applications, and banners. **Service enumeration** is performed to identify the services running on open ports and their specific versions. We should perform service enumeration because:
    
    - Knowing the exact service and its version allows penetration testers to research known vulnerabilities specific to that software, which are far more likely to be exploitable.
    - It helps in identifying unknown services, which might not use well-known ports or use other protocols as wrappers, and probes them aggressively.
    - It helps identify specific devices and configurations, such as IPsec-enabled devices (by identifying ISAKMP on UDP port 500) or VoIP-enabled devices (by identifying SIP on UDP/TCP ports 2000, 2001, 5050, 5061).
    - This detailed information is critical for developing precise and effective exploit strategies.
10. **List the services that are typically targeted for enumeration. For each, mention what information is expected to be extracted?** Services typically targeted for enumeration and the information expected to be extracted are:
    
    - **TCP 53 / DNS Zone Transfer**: List of DNS server names, hostnames, machine names, usernames, IP addresses, aliases, etc., assigned within a target domain.
    - **UDP 137 / NetBIOS Name Service**: List of computers in a domain, shares on individual hosts, policies, and passwords.
    - **TCP 139 / NetBIOS Session Service (SMB over NetBIOS)**: SMB shares.
    - **UDP 161 / Simple Network Management Protocol (SNMP)**: Information about network resources like hosts, routers, devices, shares, and potentially even read-write access to device configurations if default community strings are present.
    - **TCP/UDP 389 / Lightweight Directory Access Protocol (LDAP)**: Valid usernames, addresses, departmental details, and other directory service data.
    - **TCP 445 / SMB over TCP/IP**: SMB shares.
    - **TCP/UDP 3268 / Global Catalog Service**: Similar to LDAP, further directory information.
    - **Network Time Protocol (NTP)**: List of hosts connected to the NTP server, client IP addresses in a network, their system names, and OSs. Internal IPs can also be obtained if the NTP server is in the DMZ.
    - **Simple Mail Transfer Protocol (SMTP)**: List of valid users on the SMTP server.
    - **IPSec**: Encryption and hashing algorithms, authentication type, key distribution algorithm, Security Associations (SA), and LifeDuration.
    - **Voice over IP (VoIP)**: VoIP gateway/servers, IP-PBX systems, client software (softphones)/VoIP phones, user-agent, IP addresses, and user extensions.
    - **Remote Procedure Call (RPC)**: RPC endpoints and services running.
    - **Unix/Linux User Enumeration**: User’s login name, real name, terminal name, idle time, login time, office location, office phone numbers, and list of logged-in users.
11. **What are the objectives of vulnerability scanning?** The objectives of vulnerability scanning are to:
    
    - Identify the attack surface.
    - Determine the risk.
    - Assess the severity of the findings.
    - Draft a report of the findings.
    - Develop a remediation plan. Essentially, it aims to identify network devices open to known vulnerabilities before actual penetration testing or as part of it.
12. **What activities a typical network vulnerability scanner will carry out while scanning?** A typical network vulnerability scanner will carry out several activities while scanning to identify vulnerabilities:
    
    - **Review data at the network level**: It assesses services accessible to the scanner.
    - **Investigate DMZ and other accessible zones**: It examines these areas for potential weaknesses.
    - **Review protocol and traffic**: It analyzes the protocols and traffic on the subnet, including routing.
    - **Determine attack surface**: It specifically identifies the attack surface at the network layer and transport layer (TCP and UDP).
    - **Host-level assessment**: For host vulnerability scanning, it reviews the attack surface on the host machine, assesses installed applications, and investigates running processes. This often works best with credentials provided.
    - **Scanning various vulnerabilities**: Tools like Nessus scan for misconfigurations, password attacks, denial of service conditions, and common vulnerabilities. They also check for compliance with standards like PCI-DSS.
    - **Using plugins**: Scanners like Nessus and OpenVAS use extensive databases of plugins (over 80,000 for Nessus) to check for specific vulnerabilities, each representing an audit check.
    - **Reporting**: They produce reports detailing new vulnerabilities, open ports, detected services, and suggestions for remediation.

