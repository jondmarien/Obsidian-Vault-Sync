# Mitnick Attack

## Exploiting TCP
- The attack took place on December 1994, OS' of that time were more susceptible to attack
- The attack used 2 techniques
	- SYN flooding
	- TCP hijacking

## IP Weaknesses
- ICMP broadcasts for network mapping and DoS with Smurf
- Fragmentation weaknesses (gaps, illegal offsets) used for perimeter penetration, IDS evasion, DoS
### Example
- In this example, PROTOS tests an SNMP server. This packet crashed an unpatched RH 7.0 server, and an earlier version of Ethereal. Why? 
	- ASN.1 length is 4.2 billion, which is too much memory to allocate.
- Exhausting memory resources is a good way to disable a system. ![](Pasted%20image%2020240322121608.png)
#### Connection Info
![](Pasted%20image%2020240322121625.png)
## SYN Flooding
- An unpatched Solaris 2.5 with 1 GB of RAM will still be DoSed after 32 SYNs
- A SYN flood is performed by not completing the 3-way handshake, thus reaching the limit of the queue for waiting connections (5-10 for older systems, 100-1000 for modern systems)
	- After the queue is filled, the system will not be able to accept any new connections -- therefore the system is now silenced
		- Each waiting connection has a timer, about 1 minute, after which the memory that holds the state for the connection is released, and the queue count is decremented by one
	- To keep the system silent, we must keep the queue full by sending about 10 new SYNs per minute
	- You must cover your tracks by using a spoofed source IP address
	- This address should be routable but not active.
		- If the address is NOT routable, when the target sends the spoofed address, somewhere along the way, there will be a router that doesn't know where to send it, which will result in ICMP network unreachable, which would terminate the session with a RST.

## Trust Relationships
- Mitnick had to find a computer trusted by the target to silence
- He did this by doing some recon
```
finger -l @target
finger -l @server
finger -l root@server
finger -l @x-terminal
showmount -e x-terminal
rpcinfo -p x-terminal
finger -l root@x-terminal
```

## Finger Utility (UNIX)
- `finger` tells you who is logged on to the system, when they logged on, when they last logged on, where they are logging on from, how long they have been idle, whether they have mail
- The analogous command for Microsoft Windows systems is NBTSTAT
### Finger Example
![](Pasted%20image%2020240322124650.png)
![](Pasted%20image%2020240322131246.png)
## Showmount
- `showmount -e` provides information about the file systems mounted with NFS (Network File System)
- It is of particular interest to attackers for file systems that are **mounted world readable or writeable** -- that is, available to everyone (no authentication)
### Showmount Example
![](Pasted%20image%2020240322130352.png)

## Rpcinfo
- `rpcinfo` provides information about the remote procedure call services available on a system
- `rpcinfo -p` gives the ports where these services reside
- `sudo apt install rpcbind`
### Rpcinfo Example
![](Pasted%20image%2020240322130520.png)
![](Pasted%20image%2020240322130626.png)
![](Pasted%20image%2020240322130649.png)

## Ports

| Name               | Proto/Port  |
| ------------------ | ----------- |
| finger             | tcp/79      |
| rcpinfo/portmapper | tcp/udp/111 |
## TCP Sequence Numbers
![](Pasted%20image%2020240322131501.png)
![](Pasted%20image%2020240322131505.png)

## The Actual Attack
![](Pasted%20image%2020240322131436.png)
## How Does This Work?
- **IP address** is _spoofed_
- **TTL value** is _unusual_
- **Route taken is different**, but nobody uses IP options like _IP Record Route_
- If the sequence number is wrong, **a RESET will be sent**, that is why we needed a _predictable sequence number_

## The Actual Attack Explained
- We now see a forged SYN (connection request), allegedly from `server.login` to `x-terminal.shell`.
- The assumption is that `x-terminal` probably trusts `server`, so `x-terminal` will do whatever `server` (or anything masquerading as `server`) asks.
- `x-terminal` then replies to `server` with a **SYN-ACK**, which must be **ACK'd** in order for the connection to be opened.
- As `server` is ignoring packets sent to `server.login`, the ACK must be forged as well.
- The sequence number of the **ACK** will be predicted
- The target will send **SYN/ACK** back to the spoofed address. 
	- Since the spoofed address never sent the initial **SYN**, it will respond with a **RESET** -- that is why we must silence it first with a **SYN flood**.
- With the real server disabled by the SYN flood, the trusted connection is used to execute the following UNIX command with `rshell`: 
	- ` rsh x-terminal "echo + + >> /.rhosts"`
- The result of this causes `x-terminal` **to trust, _as root_, all computers and all users** on these computers (as already discussed).


## Attack Completed
- At this point, the connection is terminated by sending a FIN to close the connection
- Mr. Mitnick logs on to `x-terminal` from the computer of his choice and can execute any command. The target system, `x-terminal`, is compromised.
- We should not leave the silenced server silenced, as not to attract any attention. We empty its connection queue with a series of **RESETs**. ![](Pasted%20image%2020240322132350.png)

## Detecting the Mitnick Attack
- TCP spoofing is harder now because modern operating systems randomize their ISNs (textbook says Microsoft is a notable exception).
- TCP hijacking is impossible to detect still in the field (too many false positives).

## Detecting Using NIDS
- A single finger request may be ignored, but a pattern like the finger traffic should be noticed

## Trust Relationship
- The scan is targeted to exploit a trust relationship. The whole point of the Mitnick probe was to determine the trust relationship between systems.
- There must have been some form of earlier intelligence gathering to determine which systems to target.
- If Mitnick could do this from a network, the site should be able to do the same thing, perhaps even better.
- Trained analysts who know their networks can often look at an attack to determine whether it is a targeted attack, but intrusion-detection systems don't currently have this capability.

## Port Scan
- You saw toad.com fire three probes to `x-terminal`. However, two of them (`showmount` and `rpcinfo`) will probably be directed at the same port (`portmapper`), which is at TCP/UDP 111.
- It is possible to set the alarm thresholds to report connection attempts to two different ports on a host computer in under a minute.
- This would create a large number of false alarms. It wouldn't take long for the analyst to give up and set the threshold higher.
- Therefore, a **network-based intrusion-detection** system probably **would not** detect this probe as a port scan.
## Host Scan
- Host scans happen when multiple systems are accessed by a single system in a short period of time.
- In the example, `toad.com` connects to three different systems in as many minutes.
- Host scan detects are extremely powerful tools that force attackers to coordinate their probes from multiple addresses to avoid detection.
- Simple rules like "flag any host that connects to more than five hosts in an hour" will work with an acceptable false positive rate.
- "3 hosts in 5 minutes" will also work.
	- Therefore, a NIDS should be able to detect this host scan

## Connections to Dangerous Ports
- Port 111 should be monitored
- Attacker can go low and slow
	- Or, can hide in a "sea of useless packets"

## Host-based IDS (HIDS)
- TCP Wrappers
- Tripwire

## TCP Wrappers
- You can wrap the services that can be probed (like finger or portmapper)
- You can add access control lists to specify who is permitted to access this service
![](Pasted%20image%2020240322132707.png)
## Tripwire
- Creates and stores a high-quality checksum of critical files
- Tripwire could detect the actual system compromise, aka the point at which the `/.rhosts` file was overwritten
	- That would be too late.