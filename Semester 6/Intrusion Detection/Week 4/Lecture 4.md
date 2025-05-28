 **Server Hardening**
- Latest software, patches
- No open ports that aren't required to be open
-


**Is this a break-in?**
![](Pasted%20image%2020240202121946%201.png)
**No, it is not**
- No successful 3-way handshakes
- No data exchange
- No session termination
- Looks like a simple scan of the DNS server
- Responded with a RST because it didn't listen on port 21
- This was an example of miscommunication
- This shows the usefulness of tcpdump records

**Netbus Scan**
![](Pasted%20image%2020240202122054%201.png)
![](Pasted%20image%2020240202122224%201.png)
![](Pasted%20image%2020240202122440%201.png)
https://www.f-secure.com/v-descs/netbus.shtml

*Netbus Scan*
![](Pasted%20image%2020240202122507%201.png)
*Analysis*:
- Network scanned for port 12345
- Entire class B network was scanned — very unstealthy
- `tcpdump —r file 'net 192.168 and port 12345 and tcp[13] = 0x12'`
- One host responded
- Found the host, then used 'fuser' and 'PS' to find the process that opened port 12345
![](Pasted%20image%2020240202122757%201.png)

**Other Commands to Find Processes that Opened Ports*
- Unix: `lsof -i TCP:12345`
- Windows: `fport (foundstone.com)`
- Windows: `nirsoft.net's CurrPorts`

**Slow Site**
*Fragmented Activity for several hours*
![](Pasted%20image%2020240202123304%201.png)
- Response time was very slow
- Type 1 character, takes 30 seconds to see the echo back on the screen
- There is no first fragment
- There are repeated offsets with the same fragment ID
- There is no final fragment
- The destination IP address is a broadcast address
- Discovered that there was a firewall that blocked incoming echo requests — that's why the first fragment was never seen
- The firewall was stateless, it allowed subsequent fragments into the network
- The router had a BSD based TCP/IP stack, it responds to broadcast addresses, so it tried to reassemble the fragments
- Router had limited cache for reassembly
- Successful DoS attack against the router
- The source IP address was blocked, the router regained its stability and started routing normally again.
- Why didn't the router expire the incomplete set of fragments? 
	- Because the first fragment was missing
- This attack succeeded because of the broadcast address, repeated fragment ID, and missing fragments.

**RingZero Worm**
![](Pasted%20image%2020240202125222%201.png)
- Discovered in late 1999
- 3 different source IPs, 3 different internal targets
- Targets were not live hosts

![](Pasted%20image%2020240202125550%201.png)
- First, they tried to see if the source IP's were spoofed. They examined TTL values, IP IDs, TCP options, retry times, traceroute to source IP's.
- They learned that other sites had similar traffic.
- Turned out to be RingZero.