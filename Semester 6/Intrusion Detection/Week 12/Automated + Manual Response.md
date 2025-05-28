# Automated Response

## Overview
- Automated response
	- Architectural Issues
		- Response at the Internet Connection
		- Internet Firewalls
		- Host-Based Defenses
	- Response options
		- Throttling 
		- Drop Connection
		- Shun
		- Islanding
		- SYN/ACK
		- Reset
	- Honeypot
		- Proxy system
		- DTK
		- Empty System

- Manual response
	- Preparation
	- Identification
	- Containment
		- Freeze the Scene
		- On-site Containment
			- Site Survey
			- System Containment
			- Hot Search
	- Eradication
	- Recovery
	- Lessons Learned


## Are These Successful Attacks?
- Ping sweep
	- no
- Usb-based survey
	- no
- TCP port 53 connections
	- Yes, it can be a zone transfer

## Automate Response
- False positives
- Spoofed addresses
- Attacker using auto response against you

## Architectural Issues
- IDS is usually passive
- Some can connect to firewall

## Internet Firewalls
- Much safer, lot less space to evaluate because traffic is already filtered
- You know your policy better; you know which hosts need to connect to a few critical hosts
- NAT is very effective at preventing attacks

## Host-Based Defenses
- Minimum bang for buck
- Risk of spoofing much lower
- Universities protect their UNIX hosts using PortSentry, which blocks an offending host from making any further connections
- Used mainly by security-conscious admins at sites with no filtering from the Internet, like:
	- Cable modems and DSL
	- Commercial organizations that don't care
	- Universities (academic freedom)
	- Connecting while traveling (hotel)

## Response Options
- Throttling 
- Drop Connection
- Shun
- Islanding
- SYN/ACK
- Reset

### Throttling
- Adds a delay as a scan or SYN flood is detected, if the activity continues, increase delay
- UDP can send source quench
- TCP can send a small window size

### Drop Connection
- IDS asks firewall to drop offending connection after an attack string is detected
- In the case of buffer overflow, the host will execute the command sent in the offending packet
- If attacker left a listening telnet server, they can just reconnect

### Shun
- One of the most important responses
- Block attacker's IP address, or attacker's subnet
- A "never shun" file should contain addresses of customers and suppliers to protect against DoS
- This will not help if attacker is using 2 address families

#### Proactive Shunning
- Shun entire ISPs or countries if they do not manage their hosts properly
- Eventually, they may not be able to reach large parts of Internet
- That may encourage them to better manage their hosts

### Islanding
- Auto response of last resort
- If sufficient number of attacks occur over a period of time, the IDS sends a command to a logic relay to drop power to the router
- Usually done over a holiday for high-security sites
- Serious potential for DoS attack

### SYN/ACK
- IDS replies with a forged SYN/ACK to SYNs sent to blocked ports
- Attacker gets a lot of false positives
- Attacker may put data in the last ACK, so we can see what they're up to

### Reset
- AKA Reset kill, aka session sniping
- Attackers are learning to ignore Resets

### HoneyPot
- If you notice lots of interest and probes directed towards a host, you can change its name and IP address and install a honeypot in its place
	- There are several ways to do this

### Proxy System
- Configure a certain OS to look like another OS
- You can see what kind of attacks are being attempted and make sure your real systems are protected against these attacks

### DTK
- [Deception Tool Kit ](http://all.net/dtk)
- Written in Perl and C
- Emulates lots of services
- _**Appears**_ to be a system with lots of vulnerabilities (but is not)

### Empty System
- Nothing looks more like UNIX than UNIX, or Windows than Windows
- The perfect honeypot is just a system that is older, slower, and has a smaller disk (as small as possible)
- [HoneyNet Project](https://www.incidents.org)
- You can also use VMWare
## Links
[ZoneTransfer.me](https://digi.ninja/projects/zonetransferme.php)
[Webhook.site](https://webhook.site/)
[Hacker Target Zone Transfer Test](https://hackertarget.com/zone-transfer)
[Cowrie](https://github.com/cowrie/cowrie)
