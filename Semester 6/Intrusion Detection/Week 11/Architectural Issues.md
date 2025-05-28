# Arch. Issues in Networking

## Events of Interest (EOI)
- Three main issues surrounding the subject of EOI in intrusion detection
	- The balance between false **positives** and false **negatives**
	- Targeting or Focusing the sensor to ensure we detect EOI
	- The effects of the limits of our system on our capability to detect
![](Pasted%20image%2020240406155426.png)

## Limits to Observation
- Events on a different network (modems)
	- HIDS might help (Host-Based Intrusion Detection System)
- Sensor not functioning
	- Crashed
	- Rebooting
	- Full Disk
- Unknown protocols
	- SNA
	- SS7
- Exceeding bandwidth limit

## Low Hanging Fruit Paradigm
- IDS (Intrusion Detection System) depends on signatures
- Commercial products may use Snort ruleset as base
- Signatures are widely available
	- Attacker may tailor his attack code to avoid any known signatures
- A good IDS will have general filters to capture EOI that might be missed by rules (no TCP flags set, all TCP flags set, unknown protocols)

## Human Factors
- Can limit detections by:
	- Failing to report what the IDS detects
	- Having a lack of:
		- Training to investigate new pattern
		- Understanding TCP/IP
		- Trust in IDS itself

## Severities
- Criticality
- Lethality 
- Countermeasures
![](Pasted%20image%2020240406161210.png)
### Criticality

| Points | Device                            |
| ------ | --------------------------------- |
| 5      | Firewall, DNS Server, Core Router |
| 4      | Email relay/Exchange Server       |
| 2      | User UNIX Desktop System          |
| 1      | MS-DOS 3.11                       |
### Lethality
- Lethality drops with time

| Points | Problem/Issue                                |
| ------ | -------------------------------------------- |
| 5      | Attacker can gain root access across network |
| 4      | Total lockout by DoS                         |
| 4      | User access (i.e., via sniffed password)     |
| 1      | Attack very unlikely to succeed              |
### Countermeasures
- Firewalls
- Patches
- Live CDS

**System Countermeasures**

| Points | Systems                                                                        |
| ------ | ------------------------------------------------------------------------------ |
| 5      | Modern OSes, all patches, added security such as TCP Wrappers and Secure Shell |
| 3      | Older OSes, some patches missing                                               |
| 1      | No TCP Wrappers/Allows fixing unencrypted passwords                            |

**Network Countermeasures**

| Points | Network Systems                                                           |
| ------ | ------------------------------------------------------------------------- |
| 5      | Validated restrictive firewall, only one way in or out                    |
| 4      | Restrictive firewall, some external connections (modems, ISDN)            |
| 2      | Permissive firewall (Does the firewall allow the attack through, or not?) |

### How to Calculate Severity
==(Criticality + Lethality) - (System Countermeasures +== 
==Network Countermeasures) = Severity==

## Examples

==Slide 15-23

## Sensor Placements
- Outside
- Inside
- Both
- Other
- Issues
### Sensor Placement: Outside
- Outside firewall in the DMZ (De-militarized Zone)
![](Pasted%20image%2020240406162344.png)


### Sensor Placement: Inside
- Inside the firewall
- Protects sensor from attack
- Less noise, fewer false positives 
- Detect whether firewall is misconfigured

==Attack Detection vs Intrusion Detection

### Sensor Placement: Both Sides
- Best of both worlds
- You don't have to guess whether an attack penetrated the firewall
- May detect insider/internal attacks
- Help system admin with misconfigured systems

### Other Sensor Locations
- Partner Networks
- High-value locations, like research or accounting networks
- Networks with a large number of transient employees, like consultants or temps
- Subnets that appear to be targeted

### Issues with Sensors
- Spanning port on the switch must be configured properly and tested
- Two interface cards
- Consider doing a network tap
- TopLayer has a switch designed to copy data from the network to the IDS
- Cisco Catalyst 6000 switch can support a Policy Feature Card

## Push Vs Pull
- Push
	- The IDS will alert us when something happens, via email, pager or phone.
	- Disadvantages?
		- False positives
		- Can be monitored in high-end attacks
		- Push is most common
- Pull
	- Used in cover sensors
	- Most sniffers used by hackers to collect usernames + passwords are pull-based


## Analyst Console
- What they look for when shopping:
	- Real-time
	- Automated response
	- Detects everything (no false negatives)
	- Runs on whatever OS the org uses
- What they wish for after buying:
	- Faster console
	- Better false positive management
	- Display filters
	- Mark events that have already been analyzed
	- Drill down
	- Correlation
	- Better reporting

## HIDS or NIDS?
![](Pasted%20image%2020240406164019.png)
- As the size and value of the org increases, so does the importance of additional countermeasures
- Insider threats must not be forgotten
- Trojans and info-gathering viruses and worms could be thought of as insider attacks

## Insider Attacks Countermeasures
- Use taps or spanning ports on switches
- Configure:
	- DMZ sensor so as to not ignore internal systems
	- Egress filtering to allow outbound traffic only if source addresses match internal addresses
- Deploy:
	- Sensors at high-value locations
	- Honeypot systems at juicy locations with files that insider attackers might want to steal
	- HIDS on servers and key personnel's systems
- Place additional sensors from time to time on user networks as a random spot check
- Establish a reward system for those who report on employees who misuse or steal from the org
## Netflow
- What does it log (headers, data, part of header)?
	- Source and destination IP addresses
	- Source and destination ports for TCP/UDP traffic
	- IP protocol number
	- Class of service
	- Interface information (ingress and egress interface)
	- Flow timestamps (start and end times)
	- Number of bytes and packets transferred
	- Next-hop IP address
- Is it Cisco only?
	- No. Originally developed by Cisco, it has become an industry standard. 
		- The IETF has standardized it as the IP Flow Information Export Protocol (IPFIX).
- What does the capturing (routers, switches, sensors)?
	- NetFlow data can be captured and exported by routers, switches, firewalls, and dedicated sensors/probes that analyze copied traffic from a switch or tap. 
		- The capturing is done by enabling NetFlow on the device's interfaces where you want to monitor traffic flows. 
	- In summary, NetFlow provides rich flow-level details about IP traffic traversing network devices, enabling visibility into traffic patterns, bandwidth usage, and security monitoring.