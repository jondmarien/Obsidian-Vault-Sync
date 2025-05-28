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


*Activity 3 Answers*
tcpdump -nvr BA "src port 53 and dest port 53 and tcp[13]= 3 and tcp[4:4] = 239012370"
