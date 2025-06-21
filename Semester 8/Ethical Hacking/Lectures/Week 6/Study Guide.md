---
title: Study Guide
author:
  - Jon Marien
created: 2025-06-14
published: 2025-06-14
tags:
  - classes
---

| Title       | Author                       | Created       | Published     | Tags                   |
| ----------- | ---------------------------- | ------------- | ------------- | ---------------------- |
| Study Guide | <ul><li>Jon Marien</li></ul> | June 14, 2025 | June 14, 2025 | [[#classes\|#classes]] |

# Internal Network Penetration Testing Study Guide

## Key Points Summary

-  **Internal vs External Testing**: Internal testing focuses on securing internal assets while external testing blocks unnecessary ports/services
-  **Footprinting Phase**: Identifies domains, hosts, subnets, IP ranges using commands like `net view`
-  **Network Scanning**: Uses tools like Nmap, Angry IP Scanner for host discovery and port scanning
-  **OS Fingerprinting**: TTL values identify operating systems (Windows=128, Linux=64)
-  **Enumeration Targets**: TCP/UDP ports 53, 137, 139, 161, 389, 445, 3268 for various services
-  **Vulnerability Assessment**: Uses Nessus, OpenVAS, GFI LanGuard for comprehensive scanning
-  **Metasploit Integration**: Database management with workspaces for organized testing

---

## **Footprinting Phase**

**Internal Domain Discovery**
- **Primary Command**: `net view /domain` - Lists all domains in network
- **Domain-Specific**: `net view /domain:[domain name]` - Shows servers on specific domain
- **Share Enumeration**: `net view \\computerName` - Lists file/printer shares
- **Hidden Shares**: `net view \\computername /all` - Displays hidden shares

**IP Range Identification**
- Use `ipconfig` to determine your IP and subnet mask
- Calculate broadcast IP (e.g., 192.168.1.255 for 192.168.1.0/24)
- **ARP Discovery**: `ping [broadcast IP]` then `arp -a` for MAC addresses
- **Tools**: SoftPerfect Network Scanner, MyLanViewer, Solarwinds IP Network Browser

🧠 The footprinting phase is critical because it establishes your network reconnaissance baseline. Think of it as mapping the digital terrain before launching your attack. The `net view` commands are Windows-specific and incredibly revealing - they're often overlooked by defenders but provide massive intelligence value.

---

## **Network Scanning Methodology**

**Scanning Objectives & Analysis**
- **TCP SYN Response Analysis**:
  - SYN → RST = Port closed
  - SYN → SYN+ACK = Port open
  - SYN → ICMP Unreachable = Filtering device present

**Nmap Essential Commands**
- **Single Host**: `nmap 10.10.10.10`
- **Multiple Hosts**: `nmap 10.10.10.10,11,12`
- **Subnet Scan**: `nmap 10.10.10.0/24`
- **Range Scan**: `nmap 10.10.10.10-155`
- **Quick Scan**: `nmap -F [IP Address]`
- **Live Host Discovery**: `nmap -sn 10.10.10.0/24`

**Advanced Scanning Techniques**
- **Source Port Bypass**: Use `-g` with ports 20 (FTP), 53 (DNS), 80 (HTTP) to bypass stateless filters
- **TCP Connect Scan**: `nmap -sT [IP Address]`
- **UDP Scan**: `nmap -sU [IP Address]`
- **All Ports**: `nmap -p "*" [IP Address]`

🧠 Source port scanning is a brilliant evasion technique that exploits the trust relationship many firewalls have with "return traffic" from well-known services. This is why port 80 source scanning often works - firewalls expect HTTP responses to come back through.

---

## **OS and Service Fingerprinting**

**TTL-Based OS Identification**
Critical TTL values to memorize:
- **Windows (all versions)**: TTL = 128
- **Linux/Unix**: TTL = 64  
- **Cisco**: TTL = 254
- **AIX**: TTL = 60

**Nmap OS Detection**
- **Standard**: `nmap -sV -O -v [target IP]`
- **Aggressive**: `nmap -T4 -A -v [target IP]`
- **Options**: `--osscan-limit`, `--osscan-guess`, `--max-os-tries`

**Banner Grabbing Techniques**
- **Telnet**: `telnet [IP] [port]`
- **Netcat**: `nc -vn [IP] [port]`
- **Python Socket Programming**
- **Dmitry**: `dmitry -pb [IP]`

🧠 TTL fingerprinting is incredibly reliable because it's baked into the TCP/IP stack implementation. Windows has consistently used 128, Linux 64. This is often more reliable than Nmap's OS detection algorithms because it can't be easily spoofed without breaking connectivity.

---

## **Enumeration - Critical Ports & Services**

**Primary Enumeration Targets**
- **TCP 53**: DNS Zone Transfer
- **UDP 137**: NetBIOS Name Service  
- **TCP 139**: NetBIOS Session Service (SMB over NetBIOS)
- **UDP 161**: SNMP
- **TCP/UDP 389**: LDAP
- **TCP 445**: SMB over TCP/IP
- **TCP/UDP 3268**: Global Catalog Service

## **Memory Techniques by Port**

**Port 53 - DNS**
- **"Dad! No Salt! You're 53!"** - Classic mnemonic for DNS
- Think: "Domain Name System = Do Not Stress at 53"
- Visual: A 53-year-old refusing salt for health reasons, just like DNS refuses bad domain requests

**Port 137 - NetBIOS Name Service**
- **"Net BIOS = Net (3 letters) BIOS (4 letters) = 134, but it's really 137"**
- Think: "NetBIOS Name = 137 Neighbors"
- Visual: A network neighborhood with 137 houses, each with a nameplate

**Port 139 - NetBIOS Session Service**
- **"139 = 137 + 2 more for Sessions"**
- Think: "NetBIOS Session = 139 Students in Session"
- Memory link: It's just 2 ports after 137, for the session layer

**Port 161 - SNMP**
- **"SNMP = Simple Network Management Protocol = 161 was when Marcus Aurelius became emperor"**
- Think: "Simple Network = 161 Sensors"
- Visual: An emperor managing a simple network with 161 monitoring devices

**Port 389 - LDAP**
- **"LDAP = Lightweight Directory = 389-page phonebook"**
- Think: "LDAP Directory = 389 Directory entries"
- Visual: A lightweight directory book with exactly 389 pages

**Port 445 - SMB**
- **"SMB = Server Message Block = 4x4 Safe with 5 locks"**
- Think: "SMB sharing = 445 Shared files"
- Visual: A 4x4 safe (secure) with 5 combination locks for file sharing

**Port 3268 - Global Catalog**
- **"Global Catalog = 3268 Global contacts"**
- Think: "3268 = 32 countries, 68 catalogs each"
- Visual: A global catalog spanning 3,268 entries worldwide

**NetBIOS Enumeration**
- **Windows**: `nbtstat -a [IP]` - Remote machine name table
- **Linux**: `nbtscan [IP range]` - Network NetBIOS scanning
- **Information Gathered**: Computer lists, shares, policies, passwords

**SNMP Enumeration**
- **Default Communities**: public (read-only), private (read-write)
- **Port**: UDP 161
- **Detection**: `nmap -sU -p 161 [IP]`
- **Enumeration**: `snmpwalk -Os -c public -v 1 [IP]`

**SMB Enumeration Scripts**
- **Share Enumeration**: `nmap --script smb-enum-shares.nse --script-args=unsafe=1 -p445 [IP]`
- **User Enumeration**: `nmap --script smb-enum-users.nse --script-args=unsafe=1 -p445 [IP]`
- **OS Discovery**: `nmap --script smb-os-discovery.nse --script-args=unsafe=1 -p 445 [host]`

🧠 SNMP is the forgotten goldmine of network penetration testing. Most administrators secure web services and SSH but completely forget about SNMP running with default communities. The MIB database contains everything - running processes, network connections, installed software, even sometimes passwords in clear text.

---

## **SMTP, LDAP, and Other Service Enumeration**

**SMTP Enumeration Commands**
- **VRFY**: Validates users
- **EXPN**: Shows actual delivery addresses of aliases
- **RCPT TO**: Defines message recipients

**LDAP Enumeration**
- **Nmap Script**: `nmap -sS -sU -p389 -v [IP] -oA ldap-script-results --open --script ldap-brute,ldap-rootdse`
- **Tools**: Softerra LDAP Administrator, LDAP Admin Tool

**VoIP Enumeration**
- **Metasploit**: `use auxiliary/scanner/sip/enumerator`
- **Svmap**: `svmap 192.168.0.1/24`
- **Target Info**: VoIP gateways, IP-PBX systems, user extensions

---

## **Metasploit Database Management**

**Database Setup**
1. **Start PostgreSQL**: `systemctl start postgresql`
2. **Initialize**: `msfdb init`
3. **Verify**: `msfdb status`

**Workspace Management**
- **Add Workspace**: `workspace -a [name]`
- **Delete**: `workspace -d [name]`
- **List Workspaces**: `workspace`

**Data Collection & Management**
- **Nmap Integration**: `db_nmap [options] [targets]`
- **View Hosts**: `hosts`
- **Export Data**: `db_export`
- **Import Results**: `db_import [file]`

🧠 Metasploit's database integration is what separates professional penetration testers from script kiddies. The ability to organize campaigns by workspace, automatically populate target data, and maintain persistence across sessions is invaluable for complex engagements.

---

## **Vulnerability Assessment Tools & Processes**

**Nessus Configuration**
- **80,000+ Plugins** organized by families
- **Built-in Policies**: Basic Network Scan, Web Application Tests
- **Custom Scans**: Granular plugin selection for specific testing
- **Update Mechanism**: Online (24-hour intervals) or offline challenge/response

**OpenVAS Features**
- **Free Alternative** to Nessus
- **53,398 NVTs** (Network Vulnerability Tests)
- **Scan Configurations**: Discovery, Full and Fast, Full and Deep
- **Port Lists**: All IANA assigned, privileged ports, Nmap top ports

**Vulnerability Analysis Process**
1. **Identify Attack Surface**
2. **Determine Risk Level**  
3. **Assess Severity**
4. **Draft Findings Report**
5. **Develop Remediation Plan**

**Critical Vulnerability Example - MS17-010**
- **Impact**: Multiple RCE vulnerabilities in SMBv1
- **Exploits**: ETERNALBLUE, WannaCry, Petya
- **Solution**: Disable SMBv1, block TCP 445, apply patches

🧠 The MS17-010 vulnerability family represents one of the most devastating network vulnerabilities in recent history. Understanding that WannaCry, NotPetya, and other major ransomware campaigns all leveraged these SMB vulnerabilities shows why internal network segmentation and patch management are critical defensive measures.

---

## **Nmap Scripting Engine (NSE)**

**Script Categories**
- **Discovery**: Deep target information gathering
- **Auth**: Authentication-related scripts
- **Vuln**: Vulnerability detection
- **Safe**: Non-intrusive scripts
- **Intrusive**: Potentially disruptive scripts

**Vulnerability Scanning Commands**
- **All Vulnerability Scripts**: `nmap -sV --version-all -p- --script vuln [IP]`
- **SMB Vulnerabilities**: `nmap -p 445 --script=smb-vuln-ms17-010.nse [IP]`
- **Heartbleed**: `nmap -p 443 --script ssl-heartbleed -sV [IP]`

**Advanced Discovery**
- **IPv6 Discovery**: `nmap --script discovery [IP]`
- **SMB Scripts**: `ls *smb*.nse` to view available SMB scripts

---

## **Network Traffic Analysis**

**Tcpdump Essential Commands**
- **Basic Capture**: `tcpdump -c 5 -s 0 -i eth0`
- **HEX/ASCII Display**: `tcpdump -XX -c 20 -50 -i eth0`
- **Write to File**: `tcpdump -w packetcapture.pcap -c 5 -s0 -i eth0`
- **Read File**: `tcpdump -tttt -r packetcapture.pcap`
- **Protocol Filter**: `tcpdump -i eth0 tcp`
- **Port Filter**: `tcpdump -i eth0 port 22`
- **Source IP**: `tcpdump -i eth0 src 192.168.0.2`

**Information Obtained from Traffic Analysis**
- DNS traffic patterns
- Email communications  
- Web browsing activity
- Chat sessions
- Clear-text passwords (POP3/FTP/Telnet)
- Router configurations
- Syslog data

🧠 Network traffic analysis is where the real intelligence gathering happens. Modern networks may have encrypted application traffic, but metadata, DNS queries, and connection patterns reveal enormous amounts about network topology, user behavior, and potential attack vectors. The promiscuous mode capability is what makes this level of analysis possible.