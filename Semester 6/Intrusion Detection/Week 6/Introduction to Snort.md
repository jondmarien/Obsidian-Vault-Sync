# Lecture 6 - Snort
![](Pasted%20image%2020240223120903.png)
alert tcp !10.10.0.010.10.0.0/24 any (flags: SF; msg: "SYN-FIN scan"; sid:1001/24 any ->)

**Rule Header**
alert tcp !10.10.0.0/24 any -> 10.10.0.0/24 any

**Rule Options**
(flags: SF; msg: "SYN-FIN scan"; sid:1001)

## Action Field
- Alert
- Log
- Pass
	- If it matches a certain rule, stop evaluating and pass it.

## Protocol Field
- IP
- TCP
- UDP
- ICMP
- ARP
- etc…

## Source + Destination IPs
- 192.168.1.0/24
- 192.168.1.25/32
- Source/Destination: `any`
- Negation: `!`
- Save IP in Variable: `$HOME_NET` ($HOME_NET can equal ip address)
- Range of IPs: `[1.2.3.4,10.0.0.0/8]` <- no spaces between comma

## Source + Destination Ports
- Static port: `111`
- All ports: `any` (can be a range, like the range of IPs)
- Range: `33000:34000`
- Negation: `!80`
- Less than or equal: `:1023`
- Greater than or equal: `1024:`

## Direction Indicator
- Source to Destination: `->` 
- From either direction: `<>`

