# Extra Snort Configuration (Preprocessors)
## What is It?
- Preprocessors are plug-ins which work with packets before detection begins
- Two types of plug-ins:
	- Plug-ins which **examine packets for evidence** of suspicious activity
	- Plug-ins which **modify packets prior to processing** by the detection engine

## Types of Preprocessors
- For reassembling packets
	- [Stream](http://manual-snort-org.s3-website-us-east-1.amazonaws.com/node17.html#SECTION00323000000000000000) (see generator ID section)
	- [frag3](http://manual-snort-org.s3-website-us-east-1.amazonaws.com/node17.html#SECTION00321000000000000000) (see generator ID section)
- For decoding and normalizing protocols
	- Telnet negotiation
	- HTTP normalization
	- rpc_decode
- For non-rule or anomaly-based detection
	- [sfPortscan](http://manual-snort-org.s3-website-us-east-1.amazonaws.com/node17.html#SECTION00324000000000000000)
	- [arpspoof](http://manual-snort-org.s3-website-us-east-1.amazonaws.com/node17.html#SECTION003215000000000000000)
	- [Performance Monitor](http://manual-snort-org.s3-website-us-east-1.amazonaws.com/node17.html#SECTION00326000000000000000)

## Frag3
- `frag3` works to defragment IP packets
- IP fragmentation is used to evade IDS
- `Fragroute` is a popular tool to create fragmented packets
- `frag3` defaults to a 4MB RAM buffer, and keeps fragments up to 60s
- It will generate alerts for illegal overlapping fragments (anomalous traffic)
## Stream
- TCP sessions can be broken into segments to evade IDS
- Stream reassembles TCP streams, with stateful inspection and summary stats 
- Detects 
	- TCP overlap
	- Bad RST packets
	- Data in the SYN packet
	- Sequence no. abuse

- Default ports are 21, 23, 25, 53(dns), 80(http), 110, 111, 143, 513 
## sfPortscan
- Detects port scans from single or multiple hosts

**Portsweep** checks for many computers (i.e., the whole network) using that port
**Portscan** checks for one computer using that port

## Arpspoof
- Detects ARP spoofing attempts
- Requires a list of hosts in the local LAN, with their IP and MAC addresses (won't work on Sheridan's network)
- Anomalies also will be detected, like a unicast ARP request 
	- ARP requests are usually broadcasts
- Man in the middle attack
- **ONLY WORKS** in the same broadcast domain
## HTTP Inspect
- HTTP Protocol allows encoding of data using Unicode, MS `%u` codes, base36, and backslashes
- This has been exploited to disguise certain types of HTTP attacks from NIDS
- Snort decodes all HTTP before matching rules, thereby overcoming encoding
- Note that it does NOT decode SSL encryption
- **Can detect HTTP traffic even if server is not running on port 80**

[HTTP Inspect](http://manual-snort-org.s3-website-us-east-1.amazonaws.com/node17.html#SECTION00327000000000000000)
- HTTP Inspect is a generic HTTP decoder for user applications. Given a data buffer, HTTP Inspect will decode the buffer, find HTTP fields, and normalize the fields. HTTP Inspect works on both client requests and server responses.

## Generator ID

| Generator Id | Module                               |
| :----------- | :----------------------------------- |
| 105          | Back Orifice preprocessor            |
| 106          | RPC Decode preprocessor              |
| 112          | Arpspoof preprocessor                |
| 116          | Snort Decoder                        |
| 119          | HTTP Inspect preprocessor ( Client ) |
| 120          | HTTP Inspect preprocessor ( Server ) |
| 122          | Portscan preprocessor                |
| 123          | Frag3 preprocessor                   |
| 124          | SMTP preprocessor                    |
| 125          | FTP (FTP) preprocessor               |
| 126          | FTP (Telnet) preprocessor            |
| 127          | ISAKMP preprocessor                  |
| 128          | SSH preprocessor                     |
| 129          | Stream preprocessor                  |
| 131          | DNS preprocessor                     |
| 132          | Skype preprocessor                   |
| 133          | DceRpc2 preprocessor                 |
| 134          | PPM preprocessor                     |
| 136          | Reputation preprocessor              |
| 137          | SSL preprocessor                     |
| 139          | SDF preprocessor                     |
| 140          | SIP preprocessor                     |
| 141          | IMAP preprocessor                    |
| 142          | POP preprocessor                     |
| 143          | GTP preprocessor                     |

## Policy ID
| Policy Name | Operating Systems                                                  |
| ----------- | ------------------------------------------------------------------ |
| first       | Favor first overlapped segment                                     |
| last        | Favor last overlapped segment                                      |
| bsd         | FresBSD 4.x and newer, NetBSD 2.x and newer, OpenBSD 3.x and newer |
| linux       | Linux 2.4 and newer                                                |
| old-linux   | Linux 2.2 and earlier                                              |
| windows     | Windows 2000, Windows XP, Windows 95/98/ME                         |
| win2003     | Windows 2003 Server                                                |
| vista       | Windows Vista                                                      |
| solaris     | Solaris 9.x and newer                                              |
| hpux        | HPUX 11 and newer                                                  |
| hpux10      | HPUX 10                                                            |
| irix        | IRIX 6 and newer                                                   |
| macos       | MacOS 10.3 and newer                                               |

## Many Others
- Sensitive Data Preprocessor
	- CC no., SSN, etc…
- Reputation Preprocessor
	- Looks at the reputation of IP address (address known to send malicious traffic)
- DNS
- SSH
- SSL/TLS
- IMAP
- [Dshield](https://dshield.org/block.txt)
- …

[Snort Manual](http://manual-snort-org.s3-website-us-east-1.amazonaws.com/node17.html)
