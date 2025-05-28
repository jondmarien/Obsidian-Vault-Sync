Week 6-1 Lecture

Slide 1 - Monitoring Logged - On Users

Slide 2 - Monitoring Logged - On Users

Slide 3 - Monitoring Logged - On Users

Slide 4 - Case Study

Slide 5 - ii. Monitoring Users in Linux

Slide 6 - Case Study

Slide 7 - e. Monitoring of a Network
e. Monitoring of a Network
• Network monitoring involves tracking the performance and reliability of network resources and
services. It's vital for ensuring the integrity and performance of a network's infrastructure.
• i . Using Network Monitoring Utilities
• Network monitoring utilities can range from simple command - line tools to complex software platforms that provide real -
time analytics and alerts on network performance, traffic, and threats.

Slide 8 - Common Tools
Common Tools
1. Wireshark: A network protocol analyzer that can capture and interactively browse the traffic running
on a computer network.
2. Nagios: An open - source software that monitors systems, networks, and infrastructure. Nagios offers
monitoring and alerting services for servers, switches, applications, and services.
3. Zabbix : Another open - source monitoring tool for networks and applications. It provides a
comprehensive set of features, including real - time monitoring, visualization, and alerting.

Slide 9 - Case Study
Case Study
• A regional internet service provider (ISP) faced challenges in maintaining network stability and
performance. They implemented Zabbix to monitor their network infrastructure. Zabbix helped in
identifying bottlenecks and predicting potential issues by analyzing trends and real - time data. The ISP
could proactively address problems before they affected customers, significantly reducing downtime
and improving customer satisfaction.
Example Use
• The ISP set up Zabbix to monitor various metrics such as bandwidth usage, latency, packet loss, and
error rates across their network. Custom alerts were configured to notify the network operations center
(NOC) team of any anomalies or performance issues, enabling quick response to incidents and
maintenance needs.
Conclusion
• The practice of monitoring logged - on users and network activities is essential for the security,
efficiency, and reliability of IT environments. Through exploring methods for user monitoring in
Windows and Linux, alongside network monitoring utilities like Wireshark, Nagios, and Zabbix, we've
highlighted how these strategies enable IT professionals to preemptively identify and address security
threats, manage resources effectively, and maintain operational continuity. The case studies further
illustrate the tangible benefits of such monitoring, including enhanced security posture and improved
service quality. As the digital landscape evolves with more sophisticated cyber threats, mastering these
monitoring techniques equips students with crucial skills for safeguarding and optimizing technological
assets in any organization, underscoring the critical role of proactive IT management in today’s tech -
driven world.

Slide 1 - Overall Network Topology Diagrams

Slide 2 - Purpose
Purpose
• The overall network topology diagram provides a comprehensive view of the organization's network
architecture. It's a visual representation that shows how different network devices (like routers,
switches, firewalls) and network segments are interconnected.

Slide 3 - Key Components
Key Components
• Routers: Devices that connect different networks together, facilitating data packets' movement between
networks. In a diagram, routers are crucial for illustrating how the company's network is connected to
the internet and other external networks.
• Switches: Operate within a network to connect devices like computers, printers, and servers, enabling
them to communicate within the same network segment. They're essential for showing the internal
connectivity within each office's LAN.
• Firewalls: Act as a security barrier between the internal network and external networks (such as the
internet), controlling incoming and outgoing network traffic based on security rules. In diagrams,
firewalls are depicted at the network's edge, protecting LANs from unauthorized access.
• Connections: Physical (wired) or wireless links between devices and network components. These are
represented by lines in the diagram, showing how data flows from one component to another.

Slide 4 - Design Tips

Slide 5 - LAN (Local Area Network)
LAN (Local Area Network)
• Setup: Details the configuration within each office, showing how devices are connected to switches and
how those switches connect to the office's main router.
• Components: Includes computers, printers, local servers, Wi - Fi access points, and any intra - office
networking equipment.
• Representation: Often depicted with a clear layout of different departments or work areas within an
office, highlighting the network infrastructure supporting them.

Slide 6 - WAN (Wide Area Network)
Design Tips
• Start by placing the core components (like the main router and firewall) that connect the network to
external services.
• Add switches that represent the core of each office's LAN, connecting endpoints like workstations,
servers, and printers.
• Use different shapes or colors to differentiate types of devices for clarity.
• Include external connections to the internet, VPNs (Virtual Private Networks), and other remote
services.
WAN (Wide Area Network)
• Connectivity: Shows how different office locations are connected to each other across geographical
distances. This can involve dedicated leased lines, broadband connections, or secure VPN tunnels over
the internet.
• WAN Devices : Includes routers or WAN switches that facilitate long - distance connectivity. Also, it may
involve cloud - based services or data centers that the company uses.
• Design Considerations : WAN diagrams should emphasize the resilience and redundancy of
connections, such as backup links and failover systems, to ensure continuous operations.

Slide 7 - Design tips
Design tips
1. Highlight the method of connectivity between sites (e.g., MPLS, VPN) and the expected
performance or bandwidth.
2. For LAN setups, detail the network segmentation or VLAN configuration to illustrate logical
separations within the network, such as separating the guest Wi - Fi network from the internal
corporate network.
3. Use labels to specify the types of connections and their speeds or protocols (e.g., 1 Gbps Ethernet,
802.11ac Wi - Fi).

Slide 8 - Conclusion

Slide 9 - Source : What is a DMZ (Demilitarized Zone)...
Conclusion
• Creating these diagrams requires a careful balance between detail and readability, ensuring that the
network's layout is both accurate and understandable. They serve as crucial documentation that aids in
network management, troubleshooting, and planning for future expansions or upgrades.
Source : What is a DMZ (Demilitarized Zone) Network? - zenarmor.com
TALKING ABOUT MIDTERM HERE

Slide 1 - INFO 30004

Slide 2 - Overview

Slide 3 - What is monitoring?

Slide 4 - Why monitor?
Why monitor?
4
• Reasons to monitor
• Audit requirement
• Ease auditing with continuous auditing
• Other general compliance requirement
• Legal / governmental / industry specific requirement
• Observe overall performance & stability
• Look for system bottlenecks, areas of improvement
• Security events and incidents
• Incident response effectiveness, forensics
• Monitoring is how we can collect metrics that show how well
the security controls are functioning
• In the absence of a control, it allows us to observe the
consequences of the missing control
• Remember trying to justify an IT security budget in first year?
INFO 30004
Information System Security Auditing
Monitoring
1
Overview
2
• What is monitoring?
• Why monitor?
• Monitoring process
• Monitoring from the bottom up
• Monitoring technologies
What is monitoring?
3
• “Observe and check the progress or quality of something
over a period of time; keep under systematic review” –
Google dictionary
• Systematic implies that there is a specific process in
place which informs the overall monitoring activity
• Checking for progress vs. checking for quality
• Monitoring for IT Audit vs. monitoring for IT Security
Audit
• Monitoring for day - to - day IT vs. monitoring for IT
security

Slide 5 - A general process for monitoring
A general process for monitoring
5
1. Generate event data
• User requests a page from our web server
2. Store event data in standardized format
www.mysite.com 123.123.123.123 - - [05/Feb/2014:06:36:49 - 0500] "GET
/index.html HTTP/1.1" 200 14334
3. Transmit standardized data to a logging/monitoring
server
• stunnel , rsync , rsynccrypto , ssh , etc.
4. Centralize all incoming data in a RDBMS
• events(timestamp, src , dst , description, etc )
5. Data analysis / analytics on collected data
• SELECT * FROM web_events WHERE
status_code =200
6. Reporting
• html/ js charts, pdf , email, gnuplot ?, etc.

Slide 6 - Centralizing Log Monitoring Data
Centralizing Log Monitoring Data
6
• Large organizations have many devices / systems capable
of generating monitoring data and log files
• It would be infeasible to inspect each device or system’s logs
by either being physically present at the system or via
remote connects
• Centralized log/monitoring data allows all events to be
examined from a central location
• A centralized approach also allows for more detailed
analysis by incorporating multiple data sources

Slide 7 - A general process for monitoring
A general process for monitoring
7
Process (from SANS critical security controls)
Step 1: Production systems generate logs and send them to a centrally managed log
database system
Step 2: Production systems and log database system pulls synchronize time with
central time management systems
Step 3: Logs analyzed by a log analysis system
Step 4: Log analysts examine data generated by log analysis system.

Slide 8 - Monitoring from the bottom up
Monitoring from the bottom up
8
• Assuming we’re dealing with a Linux machine (similar
steps, different log file names for Windows)
• Hardware devices: dmesg , messages
• System: boot, messages, kern, secure
• Services: daemon, cron , mdadm , syslogd
• Users: auth , user, secure
• Applications: antivirus, maillog , cups, httpd , database, ...
• Internal Network: proxy server logs, internal IDS
• Perimeter Security: firewall, network hardware, DMZ IDS
• External Network: ISP? Other service providers?
• Physical security log data: CCTV, access cards, etc.
Standard activity from all of the above services will, over
time, establish a baseline against which future events are
compared

Slide 9 - Monitoring technologies
Monitoring technologies
9
• SEM: Security event manager
• SIM: Security information management
• SIEM: Security information and event management
• SOC: Security operations centre
• IDS: Intrusion detection system
• IPS: Intrusion prevention system
Some specific analysis tools (a very small list)
• Syslog - ng / syslogd : “ oldschool ” log centralization using the
actual system logging daemons
• Nagios : monitoring devices and overall infrastructure
• Tripwire: monitoring changes to a baseline
• Splunk : log centralization and front - end reporting
• http://www.elasticsearch.org/
• Logstash – Log centralization
• Elasticsearch – Indexing and searching
• Kibana – Front - end reporting
ELK
LOGSTASH
ELASTICSEARCH
KIBANA

Slide 10 - Monitoring Notes
Monitoring Notes
10
• The use of baselines is key to removing false positives
• Anomaly detection
• Looking for things outside of the norm ( ie . Not baseline)
• File hashes
• Packet contents
• User activity
• Can use data mining, machine learning, statistical models
• Use community information (ex. Snort community rules)
• Weaknesses: errors in baseline, only catches “normal” abnormal
activity
• Misuse Detection
• Rule - based approach to examine activity
• Look for common attack patterns or sequences of events
• State - Transition Analysis: Detection of misuse through analyzing state
changes
• State before breach
• State after breach
• Weaknesses: Novel / Unknown attacks, rules/patterns need to be
understood to be described

Slide 11 - DefCon 18 Video
DefCon 18 Video
11
• Building a security operations centre for little or no money
• http://www.youtube.com/watch?v=x1tCJfy_iZ4
• http://www.defcon.org/images/defcon - 18/dc - 18 -
presentations/Pyorre/DEFCON - 18 - Pyorre - Building - Security -
Operations - Center.pdf

Slide 12 - Activity

Slide 13 - References
Activity
12
• Use any of the technologies from the previous slides to
attempt to transfer and analyze some log data from one of
your virtual machine servers
• Naigos , splunk , tripwire, logstash , elasticsearch , kibana and
syslogd are all either free and open source or have free
versions available with reduced capabilities
• Try following the steps from the video and setting up a simple
single - machine SOC
• http://supervisord.org/
• A handy service for monitoring and controlling processes
• Useful for starting/monitoring/logging your monitoring
services
• Will automatically restart a crashed service
• Other candidates for process control are systemd and
runit .
References
13
• http://www.elasticsearch.org/
• tripwire.com
• splunk.com
• nagios.org
• http://en.wikipedia.org/wiki/Security_event_manager
• http://en.wikipedia.org/wiki/Security_information_and_event_
management
• http://www.sans.org/critical - security -
controls/control.php?id=14
• http://en.wikipedia.org/wiki/Continuous_auditing
ALL DONE !!!
Made with Glean