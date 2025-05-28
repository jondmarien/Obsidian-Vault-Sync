# Lecture 8
## Format of Snort Options
```C
alert tcp !HOMET_NET any -> $HOME_NET any \
(msg: "SYN-FIN scan"; flags: SF;)
```

- Snort is forgiving about the lack or abundance of whitespace between delimiters such as `;` and `:`
- These are both valid: 
```C
(msg:"SYN-FIN scan";flags:SF;)
(msg               :           "SYN-FIN scan"; flags:           SF           ;)
```
- Backslash `\` is a rule continuation character
- The pound sign `#` is used as the comment character 

test
## Rule Options
https://snort.org
- General
	- These options provide information about the rule but do not have any affect during detection
- Payload
	- These options all look for data inside the packet payload and can be inter-related
- Non-Payload
	- These options look for non-payload data
- Post-Detection
	- These options are rule specific triggers that happen after a rule has "fired"

How a packet looks:

| ETH | IP  | TCP/UDP | **APP** |
| --- | --- | ------- | ------- |
|     |     |         |         |
Payload sits in "APP(location)"
## Msg Option (General Rule)
Format: `msg: "<message text>";`
Sample rule: 
```C
alert udp any any -> 192.168.5.0/24 31337 \ 
(msg: "Back Orifice";)
```
Sample output: ![](Back%20Orifice.png)

## Logto Option (Post-Detection Rule)
Sample rule: 
```C
alert udp any any -> 192.168.5.0/24 31335 \
(msg: "trinoo port"; logto: "DDoS";)
```
Sample output: 
	If the rule is triggered, the output on this UNIX host will be found in `/var/log/snort/DDoS` ![](Pasted%20image%2020240308122245.png)

## TTL Option (Non-Payload Detection)
Sample rule: 
```C
alert udp any any -> 192.168.5.0/24 33000:34000 \ 
(msg: "Unix traceroute"; ttl: 1;)
```
Sample output: ![](Pasted%20image%2020240308122418.png)

## ID Option (Non-Payload Detection)
Sample rule: 
```C
alert icmp any any -> 192.168.5.0/24 any \ 
(msg: "Suspect IP Identification #"; ID:0;)
```
Sample output: ![](Pasted%20image%2020240308122617.png)

## Dsize Option (Non-Payload Detection)
Sample rule: 
```C
alert icmp any any -> 192.168.5.0/24 any \ 
(msg: "Large ICMP payload"; dsize: >1024;)
```
Sample output: ![](Pasted%20image%2020240308122743.png)

Header of the packet that was discarded 
default ping payload size is 46 bytes 
## Sequence (seq) Option (Non-Payload Detection)
Sample rule: 
```C
alert tcp any any -> any any \ 
(msg: "Possible Shaft DDoS"; seq: 0x28374839;)
```
Sample output: ![](Pasted%20image%2020240308122849.png)

## Acknowledgement (ack) Option (Non-Payload Detection)
Sample rule: 
```C
alert tcp any any -> any any \ 
(msg: "nmap TCP ping"; flags: A; ack: 0;)
```
Sample output: ![](Pasted%20image%2020240308123012.png)

## Itype and Icode Option (Non-Payload Detection)
Sample rule: 
```C
alert icmp 1.1.1.0/24 any -> 192.168.5.0/24 any \ 
(msg: "port unreachable"; itype: 3; icode: 3;)
```

Sample output: ![](Pasted%20image%2020240308123819.png)

## Flags Option (Non-Payload Detection)

| Flags | Description                                                 |
| ----- | ----------------------------------------------------------- |
| F:    | Finish flag set                                             |
| S:    | Synchronize flag set                                        |
| R:    | Reset flag set                                              |
| P:    | Push flag set                                               |
| A:    | Acknowledgement flag set                                    |
| U:    | Urgent flag set                                             |
| 2:    | ECN echo flag set (formerly a reserved bit)                 |
| 1:    | ECN congestion window reduced set (formerly a reserved bit) |
| 0:    | No flag bits set                                            |
![](Pasted%20image%2020240308124055.png)

Sample rule: 
```C
alert tcp any any -> any any (msg:"Null Scan"; flags:0;)
```
Sample output: ![](Pasted%20image%2020240308124146.png)

## Content Option (Payload Detection)
**CASE SENSITIVE** (if you want lower case, use _nocase_ option)

Sample rule: 
```c
alert udp $EXTERNAL_NET any -> $HOME_NET 53 \
(msg: "EXPLOIT BIND tsig Overflow Attempt"; \
content: "|00 FA 00 FF|"; content: "/bin/sh";)
```
Sample output:
![](Pasted%20image%2020240308130222.png)
![](Pasted%20image%2020240308130236.png)

## Offset Option (Payload Detection)
Can **only** use this option in use with the content option. Order matters, must **follow** the content option

Sample rule:
```C
alert tcp any any -> 192.168.5.0/24 21 \
(msg: "Attempted anonymous ftp acess"; \
content: "anonymous"; offset: 5;)
```
Sample output:  ![](Pasted%20image%2020240308130447.png)

## Depth Option (Payload Detection)
Can **only** use this option in use with the content option. Order matters, must **follow** the content option

Can use this option in use with the _content_ and _offset_ option. Order matters, must **follow** the _offset_ option

Sample rule:
```C
alert udp !$HOME_NET -> $HOME_NET 5632 \
(msg: "PCAnywhere Startup"; content: "ST"; depth: 2;)
```
Sample output: 
![](Pasted%20image%2020240308130616.png)

## Nocase Option (Payload Detection)
Sample rule:
```C
alert tcp any any -> any 21 \
(msg: "FTP warez snooping"; content: "warez"; nocase;)
```
Sample output: ![](Pasted%20image%2020240308130829.png)

## Pcre Option (Payload Detection)
pcre = perl compatible regular expressions

Sample rule: 
```C
log tcp any any -> 192.168.5.0/24 515/
(msg: "Attempted shell on lpd"; content: "/bin/*sh"; regex;)
```
Sample output: ![](Pasted%20image%2020240308131305.png)

## Session Option (Post-Detection)
Sample rule:
```C
log tcp any any <> 192.168.5.0/24 21 (session: printable;)
```
Sample output:
	Assuming the source host for the session is 1.2.3.4 on port 1025, the following output will be in the log directory in subdirectory 1.2.3.4 file SESSION: 1025-21:
	![](Pasted%20image%2020240308131725.png)

The session option can degrade the performance of Snort, so it is best used retrospectively (don't do it with live traffic):
	Capture the data in binary format (TCPdump files), and then run it through Snort. When you use this option (_session_), you should use the direction operator `<>`. Finally, it is best practice to use the `-d` CLI option to dump at the application level (otherwise, why are we specifying the session option)

## Resp Option (Post-Detection)
Format: `resp <resp_option[, resp_option…]>;`

| Available choices for response | Description                                                  |
| ------------------------------ | ------------------------------------------------------------ |
| rst_snd                        | Send TCP RESET packets to sending socket                     |
| rst_rcv                        | Send TCP RESET packets to receiving sockrt                   |
| rst_all                        | Send TCP RESET packets to both sending and receiving sockets |
| icmp_net                       | Send an ICMP_NET_UNREACH to sender                           |
| icmp_host                      | Send an ICMP_HOST_UNREACH to sender                          |
| icmp_port                      | Send an ICMP_PORT_UNREACH to sender                          |
| icmp_all                       | Send all of the above ICMP_UNREACH packets to sender         |
Might not be enabled by default, must be enabled at compilation (`n./configure --enable-flexresp`). Enabled in kali by default.

Sample rule:
```C
alert tcp any any -> $HOME_NET 21 \
(msg: "FTP password file retrieval"; \
flags: A+; resp: rst_all; content: "passwd";)
```
Sample Session: 
![](Pasted%20image%2020240308132346.png)

## Tag Option
- type: What traffic to record
	- session: Record the packets from both sides of the connection
	- host: Record the packets from the host that caused the rule to trigger (must use direction modifier `<>`)
- count: Number of units specified by metric
- metric: Number of packets/second to record
	- packets: Record host/session for `<count>` packets
	- seconds: Record host/session for `<count>` seconds
- direction: Used only with "host" type to indicate host to tag
	- src: Tag all traffic of source IP in triggered rule
	- dst: Tag all traffic of destination IP in triggered rule

Sample rule:
```C
alert tcp any any -> any 21 \
(msg: "FTP passwd access"; flags: A+; \
content: "passwd"; tag: session, 10, packets;)
```
Sample output:
	The alert file shows the abbreviated data from the miscreant connection to destination port 21: ![](Pasted%20image%2020240308133158.png)
