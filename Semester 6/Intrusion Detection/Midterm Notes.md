# Week 1

## Tcpdump
- "tcpdump -enx | tcpshow -nolink"
- e: mac address + show frame header
- n: no resolution
- x: show hex
- -nolink: doesn't show layer 2
- "tcpdump -x" || "tcpdump -X" || "tcpdump -xX"
	- hex || ascii || hex and ascii

## IHL Header Length
- 4 bits long
- 2^4=16  max value
- always IHL * 4 for the real value

## IP Datagram
- Expressed in bytes

## Dissecting the Whole Packet
- embedded protocol lays in the 9th byte offset of the IP header
- ip protocols
	- 1: icmp
	- 6: tcp
	- 17: udp
- if the ip header length is longer than 5, there are optional fields (if IHL * 4 > 20)

# Week 2

## Evasion Attack
- SYN segments usually do not contain data
- NIDS ignores data, while the host accepts data within SYN segments
- Usual Traffic ![[Pasted image 20240215230906.png]]The attacker can put an "R" in the SYN packet and then send "EWT" in a separate packet and the host will just receive "EWT" -- because there is data in the syn which is abnormal so it is dropped ![[Pasted image 20240215230936.png]]

## IP Header Fields: IP Version
- version will be 4 or 6
- packets containing version not 4 or 6 will be discarded
- could be used in an insertion attack if the attacker is on the same network as the  target and if the NIDS accepts packets with the invalid version

## IP Protocol Number
- nmap -sO: scans for listening protocols
	- inverse scan, as it says which protocols are NOT supported
		- similar to how udp port functions, if it is closed you get an unreachable message
	- If the site has "no ip unreachable" statement on outbound interfaces, this will not work


## DF Flag (Don't Fragment)
- fragmentation comes with overhead, avoid
- can be used in insertion attack if the nids is on a network with a higher MTU than the target host
- ![[Pasted image 20240215231422.png]]

## MF Flag (More Fragments)
- Can be used as a scanning technique by eliciting a "reassembly time exceeded" message from hosts on scanned network
- host must be listening on tcp or udp port
- host must recieve the first fragment so the timer is set for reassembly
- timer is recommended to be 1-2mins
- timers are not always set to proper values

## IP Addresses
- Local addresses (127.0.01), Private addresses (10.x.x.x, 172.16.x.x, 172.31.x.x, 192.168.x.x) should be discarded
- disallow outgoing traffic that has a strange src address
	- this prevents hosts from starting DDoS attacks
		- If sheridan's addresses all start with 142.55.x.x, then all outgoing traffic should start with this. 
		- If there is a packet leaving the network that doesn't start with 142.55 then the address must be spoofed 


## IP ID Number
- Needed if packet is fragmented
- Some hosts increase this value by 1 for each packet, some by 256
	- you don't see ip d 0
- if you see traffic from different src ips with similar incrementing ip ids, they might be spoofed ips

## TTL
- Can be used in an insertion attack if the ttl is low enough to be expired before it reaches the target host
Look at this address to discover IP source spoofing![[Pasted image 20240215233416.png]]
- TTL is same for all 3
- ip ids are similar (small increments)
- could be coming from one pc that is spoofing the ips

## IP Checksums
- validated by every router along the way
- only covers the ip header
- recalculated because of the TTL value changed at each hop

## Exercises
1) 
	![[Pasted image 20240215233649.png]]
	- the highlighted `0000` represents the checksum because there are the 10th and 11th bytes on the ip header
	- `0000` as a checksum is strange.
 2) 
	![[Pasted image 20240215233753.png]]
	- all the packets are tcp segments except for the highlighted line, which is udp
3) 
	![[Pasted image 20240215233823.png]]

4) low ttl
	![[Pasted image 20240215234457.png]]
5) tcp sequence number overlap
	first packet is 602-614 so next packet should be 615 but it starts at 603 so there is overlap ![[Pasted image 20240215234508.png]]
6) data on syn
	the other two packets that have the syn flag on do not have a range of seq numbers but the highlighted line has a range which tell us there is syn data (shown below)![[Pasted image 20240215234524.png]]
		![[Pasted image 20240215234751.png]]
7) don't fragment
	df flag turned on but length of 1265. ids will see the packet but the router will discard it and it wont reach the host![[Pasted image 20240215234608.png]]

# Week 3

## TCP
- connection-oriented protocol
- tcp header has more fields than udp header
- Acks, seq numbers, flow control ![[Pasted image 20240215235059.png]]
### Ports
- 16-bit fields
- Range 1-65535
- Port 0 never used
- well known ports 1-1023
- Ephemeral (temporary) ports >1023
**STATIC SOURCE PORT INDICATES A SYN SCAN**


## TCP Checksums
- Tcp and udp are end-to-end checksums
	- different than ip checksums which are changed at every router due to the ttl being different
- udp does not require the checksum to be computed
	- can have a checksum of 0
- includes a pseudo-header
	- ![[Pasted image 20240216004516.png]]
- ![[Pasted image 20240216004538.png]]

## Tcp Sequence Numbers
- 2^32 possible seq numbers
- First byte of data will have **I**nitial **S**eq **N**umber (ISN+1)
- ISNs should be random


## Acknowledgement Numbers
- ack 0 is rare
- unsolicited ack can be sent in host scan attempt
- nmap ack scan is obvious bc the ack flag is set but ack number is 0

## Tcp flags
- syn, ack, rst, fin, psh, urg
- some combinations are not valid (like syn/fin)
- corruption can also result in mutant flag settings

## Tcp corruption
- not all odd traffic is malicious, it could be corrupted

## ECN flag bits
![[Pasted image 20240216004856.png]]
- the 2 high order bits in the tcp byte are to be reserved
	- they can be used for congestion notification
	- they are used in os fingerprinting
	- many nids still alarm if these bits are set

## OS fingerprinting
- nmap sends mutant flag combinations when it finds an open port
- ![[Pasted image 20240216005014.png]]
- 3 scenarios where a syn/fin was sent
	- win98 responded with syn/ack
	- linux did not respond

## Retransmissions
- Destinations might not be up, or does not exist
- Destinations may have replied, but reply got lost
- How can you distinguish retransmissions from new tcp connection?
	- ![[Pasted image 20240216005328.png]]
	- here the seq numbers are all the same
	- ports are all the same
		- if these were separate tcp connections, the port numbers would be different
	- time stamps are very close together

## LaBrea Tarpit Version 1
- used against code red worm that scans for web servers
- installed on local host, listens for arp requests for unassigned ips
- if no reply is generated, labrea fakes a host response
- if a syn follows, labrea fakes a syn/ack
- labrea then ignores further packets, which causes sender to resubmit, thus slowing it down
## LaBrea Tarpit Version 2
- sends a window size of 0 to attacker
- attacker will send a window probe after a while
- labrea hosts respons with a window size of 0 again
	- loops forever

## TCP Window Size
- used for flow control
- tells the other side of the connection what window size to use
- initial window sizes are used by nmap in os fingerprinting

## UDP
- Close ports respond with ICMP port unreachable
- not very accurate
- udp length field
	- usually 8192 bytes
- dns payload limited to 512 bytes

## ICMP
- ID and seq numbers are used in pings


![[Pasted image 20240216005953.png]]Highlighted: destination Mac, source mac, type (this is ARP request, we know this because the
destination is the broadcast address)

![[Pasted image 20240216010002.png]]Again, highlighted the ethernet header

![[Pasted image 20240216010013.png]]The ip header starts at the highlighted 45 and continues for 20 bytes because of the length of 5 which is multiplied by 4

![[Pasted image 20240216010036.png]]
- src port is 0050 in hex which is 80 in decimal (http port)
- dest port is 0d 2c
- tcp flags are 12 which is 0001 0010 in binary which means the syn and ack flags are turned on
- this is the second step of the 3-way handshake

![[Pasted image 20240216010141.png]]Source and destination addresses

# Week 4

## Netbus
![[Pasted image 20240216010714.png]]
- a tool that allows remote access and control of a windows host
- one of many backdoor trojans that can be run to provide stealthy access. 
- usually on port 12345
![[Pasted image 20240216010827.png]]

![[Pasted image 20240216010835.png]]
- Network scanned for port 12345
- Entire class B network was scanned — very unstealthy
- `tcpdump —r file 'net 192.168 and port 12345 and tcp[13] = 0x12'`
- One host responded
- Found the host, then used 'fuser' and 'PS' to find the process that opened port 12345

##### How to find open processes that opened ports
- unix: `lsof -i tcp:12345`
- windows: `fport`
- windows: `nirsooft.com currports`

## RingZero Worm

# Week 5

**TCPdump Filter Format**
- `<protocol header>[offset:length] <relation> <value>`
	- Example
		- `tcpdump 'ip[9]=1'`
			- What does this filter do?

**Bit Masking**
- Using a logical `AND` operation to mask out bits
	- `ip[0] & 0x0f > 5`
		- This masks the bits of the version, and keeps the IHL (Looking for IP packets where the headers have optional fields, more than 20 bytes)
	- `ip[0] & 0xf0 > 0x40`
		- This masks the bits of the IHL, and keeps the version of IP

**Bit Shifting**
- `ip[0] >> 4`
	- This shifts the version 4 bits over, knocking (shifting) the bits off of the IHL
- bit shift to the right -> divide (can use divide symbol)
- bit shift to the left -> multiply

**Tcpdump IP Filters**
- `src host`
- `tcp or udp`
- `tcp and port 80`
- `icmp`
- `icmp[0]=3`

	*Detecting Traffic to Broadcast Address*
	- `ip[19] = 0xff`
	- `ip[19] = 0x00`
	- `ip[19] = 0xff or ip[19] = 0x00`
	- `ip[19] = 255 or ip[19] = 0`
	- `not src net 192.168 and (ip[19] = 0xff or ip[19] = 0x00)`
		- looks for external traffic and the destination address ends with 255 or 0

	*Detecting Fragmentation*
	- `ip[6] & 0x20 != 0`
		- this only works if it is <u>one</u> bit you are masking
	- `ip[6] & 0x20 = 0x20`
		- `ip[6] & 0x20 = 32`
			- This is masking out the rest of the 7 bits and leaving the single MF (More Fragments) flag

*TCP where <u>ONLY</u> SF are set*
- `tcp[13] & 0x03=0x03`
*TCP where SF are set*
- `tcp[13] != 0`


**TCPdump UDP Filters**
- `udp and dst port 31337`
- `dst port >= 33000 and dst port < 34000`
- `udp[2:2] >= 33000 and udp[2:2] < 34000`
- `udp[2:2] >= 33000 and udp[2:2] < 34000 and ip[8] = 1`

**TCP Payload Length**
- What is the tcpdump filter you would use to calculate this:
	- IP Length - IP Header Len - TCP Header Len
	- IP Packet Length = `ip[2:2]`
	- IP Header Length = `(ip[0] & 0x0f) * 4`
	- TCP Header Length
		- `= (tcp[12] & 0xf0) * 4 / 16 )`  = `(tcp[12] >> 4) * 4`
		- `= (tcp[12] & 0xf0) / 4 )`


```
tcp[13] = 2

and

(  ip[2:2] –

  ( (ip[0] & 0x0f) * 4) –

  ( (tcp[12] & 0xf0) / 4 )

) != 0
```

<u>SAME THING (formatted differently)</u>

```
tcp[13] = 2 and (ip[2:2] – ((ip[0] & 0x0f) * 4) – ((tcp[12] & 0xf0) / 4 )) != 0
```

- This filter is finding where tcp[13] = 2 and the segment is not empty (!= 0, there is data), and the SYN bit is turned on
	- "Data on SYN (segment)"
