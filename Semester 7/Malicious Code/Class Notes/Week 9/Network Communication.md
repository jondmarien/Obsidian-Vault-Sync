---
title: Network Communication
author:
  - Jon Marien
created: 2025-03-12
published: 2025-03-12
tags:
  - classes
  - INFO43921
---

| Title                 | Author                       | Created        | Published      | Tags                                               |
| --------------------- | ---------------------------- | -------------- | -------------- | -------------------------------------------------- |
| Network Communication | <ul><li>Jon Marien</li></ul> | March 12, 2025 | March 12, 2025 | [[#classes\|#classes]], [[#INFO43921\|#INFO43921]] |

# **Chpt. 9 -- Network Communication**

Victims can be infected with malware by other mediums also, including USB disks, but the use of network communications is probably the most widely used mechanism since most devices use the network for some form of communication.

These days pretty much every device is connected with the advent of the Internet of Things (IoT) .This availability of network-connected devices makes the attack surface even bigger and better for attackers to target.

But infecting a victim with malware is only one-half of the work for most attackers. Once the victim is infected, the malware typically uses the same network for further communication.

In this session, we cover the second half of this infection phase, where malware uses the network for various communication-related activities.

## **Why Communicate?**
The following are some examples:

- A bot that is part of a bot network can receive commands from the attacker.
- A password stealer or a banking malware needs to send the victim’s credentials to the attacker.
- Ransomware may need to send the encryption key used in the file encryption process back to the attacker.
- The attacker might want to control the victim’s system remotely using RATs.
- The malware might want to infect other systems on the network.
- The malware might be part of an APT (advanced persistent threat) attack where the actual target of the cyberattack/infection might be another machine on the network, which the malware tries to locate and infect.

### **Types of communication**

#### **1- Command-and-Control (C2C)**
CnC (also known as C2) refers to command and control, which is a means for the malware to be commanded and controlled by its owner/attacker to carry out various malicious activities. The commands are nothing but actions received by the malware on the victim’s device. The commands can range from asking the malware to upload credentials and other victim data, all the way to launching a DOS attack on another victim/server on the Internet.

#### **2- Data Exfiltration**
Most malware includes some functionality that includes capturing some form of data on the victim’s device and sending it to the attacker. Exfiltrated data may include stolen user credentials, wallet IDs, sensitive documents, banking credentials, and so forth. Data exfiltration methods these days have become more complex to evade detection by IDS and firewalls, employing various strategies like encryption, hiding/layering under other protocols.

#### **3- Remote Control**
Although a form of command-and-control, remote control deserves a category of its own. A remote control is no different than the functionality employed by various remote desktop types of software used by most IT teams to manage the devices of their workplaces. This remote-control malware is called RATs, which stands for remote access trojans .

#### **4- Droppers** 
Most malware infections happen through downloader/dropper, which is the first payload in a malware infection. The droppers are basic programs whose task is to connect to the attacker’s server and download the main malware payload. Droppers allow malicious actors to sell such components as a service, providing criminals with the ability to leverage this existing dropper bot network infrastructure to drop their malware into the victim’s machine.

#### **5- Updates** 
Like other software, malware needs to be constantly updated with new versions/variants, often to fix bugs, add new features, and so forth.

#### **6- Lateral Movement**

Lateral movement involves the movement of the malware inside the network of the victim it has infected to infect other devices, laptops, servers on the network. Such lateral movement might come with only a generic worm capability as a part of the malware to infect as many devices as possible. In some other cases, the lateral movement might be intentional and targeted, especially if the malware is part of an advanced persistent threat (APT), where the actual target victim’s machine might be located elsewhere on the network.

![](images/M8-1-Network%20Communication_0.png)

### **CnC Servers, Relays, Proxies, and Malware Networks**

There are multiple ways to receive these commands from its attacker (CnC servers, peer-to-peer (P2P)), but the most popular is the use of stand-alone CnC servers as a way to communicate with the malware and control/command them.

Malware analysts can easily identify the domain/IP address of the CnC server and take it down with the help of law enforcement and other authorities.

To counter this, malware authors use a malware network (the same as a bot network) that comprises multiple servers and machines around the Internet that have been compromised and are now under the control of the attacker. These compromised devices operate as relays/proxies for the malware, where the malware instead establishes a communication channel with the relays/proxies, which then forwards this communication stream to the real CnC server.

Taking these proxies down wouldn’t take down the real CnC server, since its IP address is still hidden as the attacker now switches to using other relays/proxies as an intermediate communication step in the CnC communication channel.

![](images/M8-1-Network%20Communication_1.png)

### **Resolving CnC Server IPs**

After infecting its victim, malware tries to establish a communication channel with its attacker for CnC and data exfiltration and other purposes. Any communication finally requires an IP address to establish a communication channel. In this section, we cover the three predominant methods used by malware to resolve the IP address of the CnC server.

#### **1- Fixed IP Addresses** 
- But embedding such a fixed IP address into the malware binary has various drawbacks, as described next.
- Analysts can easily analyze/reverse the malware payload and extract the IP address of the CnC server and take it down with the help of law enforcement. They can also block all access to this IP using firewalls/IPS rules.
- If the malware attacker decides to move this CnC server, which might result in a change of IP address, the malware that has already infected machines around the world has no way to know the new IP address of the CnC server.

#### **2- Fixed Domain Names**
Malware authors embed the domain names they have registered for their CnC server inside the malware. Using domain names solves the problem where the attacker can now switch the CnC server to use another IP, by just having the domain names they have registered to point to the new IP address of the CnC server. But this still has the drawback that a malware analyst or a reverse engineer can extract these fixed CnC server domain names from inside the malware sample and then block all access to them in the firewall/IPS, basically cutting off all communication with the CnC server.

#### **3- Domain Flux and DGA**  
Attackers have come up with a new method called domain flux, where the domain name that is associated with the CnC server isn’t fixed, nor is it embedded inside the malware. To implement this, malware uses an algorithm called DGA (domain generation algorithm) that dynamically generates domain names for the CnC server that the malware can connect to.

The DGA sample generates multiple domain names that are pseudo-random. It starts with a fixed seed value and generates 15 such domain names.

On the other end, the malware attacker also has the same algorithm on his side and can run this same algorithm with the same seed value to obtain the same list of domain names . But for every domain name generated by this algorithm, the attacker won’t register the domain name and have it point to the IP address of his CnC server. Instead, he randomly picks one domain name from this generated list, registers it, and has it point to this CnC server IP address.

From the malware side, when it runs, it sequentially tries resolving each domain name it generates using the DGA algorithm until it finally hits/resolves a domain name that is registered by the attacker.

![](images/M8-1-Network%20Communication_2.png)

![](images/M8-1-Network%20Communication_3.png)

DGA algorithms generate and try to resolve thousands of such dynamically generated domain names. It is not possible to add such thousands of domain names into our IDS/IPS/FIrewalls to block, since the security product would be overwhelmed with the huge number of domain signatures that it needs to identify.

Plus, attackers might release multiple variants of their malware with multiple seeds, which again leads to such multiple trails of domain names generated by that single family of malware.

On top of that, a lot of malware from other families use DGA for CnC domain name generation.

The list of domain names if you want to cover is practically exhaustive. Instead, we can use other techniques to identify and block the use of DGA, which we cover in the next section.

Malware attackers also combine DGA with other techniques, like Fast Flux, where multiple nodes in their malware network register their IP address against these domain names in a round-robin or any other random fashion, but with a very small time-to-live value. So if server1 from the malware network registers its IP address against a domain name, after 5 minutes another server2 from the malware network might register its IP address against the domain name, cycling through multiple IP addresses against the domain name, making it hard for SoC and IT staff to block a single IP address to contain the CnC communication involved in a network infection.

Most DGA algorithms used by malware generate random domain names, which have a non-human-readable-random look.  **Such malware and their domain names can be caught by testing it for randomness, high entropy, and the absence of human, non-dictionary-based words.**

Once the DGA algorithm generates domain names, malware tries to resolve the domain names for the IPs, at frequent periodic intervals. If you are a malware analyst or SoC analyst, using a tool like an IDS/IPS/firewall or other Network Security Monitoring(NSM) tools to protect your environment, you see that from machines infected with malware that use DGA, a constant periodic DNS resolution for multiple domain names. Such constant  **periodic domain name resolution**  requests can be easily caught by using  **threshold**  related features like the ones available in Suricata and Snort IDS/IPS.

DGA algorithms generate multiple domain names, but the attacker registered only a few of those to point at their CnC server IP Address. DNS resolution for the other domain names generated by the malware’s DGA algorithm  **doesn’t resolve and comes back with no IP address** . We can use this as an indicator in our network security tools if we see too many DNS responses come back from the DNS server, which doesn’t resolve to any IP address. Combine this with the previous point, where you see ** periodic DNS requests** , and you have a strong indicator that the device making these DNS requests is infected with malware that uses DGA.

## **Test: Sample-9-2 with FakeNet**
After running FakeNet, you can run `Sample-9-2.exe`. As can you see in the FakeNet output in Figure 9-4, you can see multiple DNS requests being generated by the sample process on the system and then HTTP requests heading out to this returned IP from FakeNet. If you observe the random format of the domain names resolved and the periodic way in which these DNS requests are heading out from the sample, it all points to DGA by our malware Sample-9-2.exe.

![](images/M8-1-Network%20Communication_4.png)

## **CnC/Data Exfiltration Methods**
Malware uses multiple protocols for establishing a communication channel with the CnC server, to both receive commands and to exfiltrate data.

* HTTP is probably the most common protocol for CnC used by most malware.
  * The availability of this huge number of web servers also means hackers can try to compromise these servers to convert them as their CnC servers, update servers, or relays to build their malware network.
  * Also, since HTTP is a frequently used protocol used by most users and applications at enterprises and users in general, IT admins at corporations pretty much always allow outbound access to the well-known HTTP port 80.
  * the native support for using HTTP via various Win32 APIs and other third-party libraries
* The HTTP protocol not only receives commands issued by attackers but also exfiltrates data and files from the victim’s infected machine to the CnC server.
* The data that needs to be exfiltrated can be done through embedding the data into the URL itself, or it can be part of the HTTP body.

## **Test: Sample-9-3.exe**
**Works on windows XP VM**
Most of the HTTP-based CnC strings use the % and = characters, thereby giving us an easy way to search and identify such CnC-related HTTP strings while you are carrying out string analysis.

![](images/M8-1-Network%20Communication_5.png)

run FakeNet, and then execute Sample-9-3.exe. As seen in Figure 9-6,FakeNet catches HTTP requests heading out with the same format string that you saw in Figure 9-5.

The CnC string get&news_slist&comp=POONA-668123ED0-000C296420A8 matches the CnC string format %s?get&news_slist&comp=%s that we discovered earlier. The second %s has been replaced with the name of the computer, POONA, and the Mac address of the system, 00:0C:29:64:20:A8, indicating that the malware is sending this information to the attacker to fingerprint its victim.

![](images/M8-1-Network%20Communication_6.png)

### **2- A Love Affair with HTTPS**
Malware authors have started moving to use HTTPS, the encrypted variant of HTTP, which rides on top of an outer TLS protocol layer, thereby rendering products like IDS/IPS useless, as they no longer have visibility to the HTTP CnC traffic anymore, since it is now encrypted.

Initially, HTTPS was considered an expensive option in terms of the CPU power needed for the CPU-intensive encryption operations. But these days with devices getting more powerful such concerns no longer exist. Also, the cost of acquiring SSL certificates needed for HTTPS has all but disappeared, with the arrival of Let’s Encrypt and other nonprofit service providers who issue SSL certificates for free. Even web server hosting providers provide encryption/certificates for your servers/domains at no additional cost. All of these have made it very attractive for malware authors to use HTTPS for any communication with their CnC servers.

Probably the only way for a network security product to have visibility into this real CnC traffic is to intercept and MITMing all outbound SSL connections to decrypt them, and this is what firewalls are set up to do these days.

An alternative approach to detect such malware CnC traffic based on the SSL traffic itself has also seen approaches where researchers have used **TLS fingerprints to identify traffic from malware** . For example, various client applications use SSL libraries for the functionality of encrypting traffic, including the browsers we use and our mobile apps. But different applications might use different variants of these SSL libraries that might have subtle variations in how they are built or set up, which can help us uniquely identify these individual applications.

One such TLS fingerprint feature comes from the cipher suites TLS protocol field, which basically lists items like the encryption algorithm and other such vectors supported by the client’s encryption library. The client (library) can also advertise other TLS extensions supported by it. All these features added and more can serve as a  **unique fingerprint for the client librar** y and the sample process using this client library.

These features/fingerprints can be extended to uniquely identifying malware based on such fingerprints as research shows that malware uses SSL libraries that have their specific fingerprints derived from the specific encryption libraries they use and the specific cipher suites and extensions they support. Such features can also be combined with other network-based traffic patterns and behaviors to effectively identify encrypted traffic streams carrying malware CnC traffic.

IRC is a popular  **chat**  protocol used prominently around the world for implementing chat rooms/channels. Malware is known to use IRC for CnC. It is popularly used among botnets, where the bot logs into the IRC channel for the malware network run by the attacker and receives various commands by the attacker via IRC messages.

An easy way to identify CnC that relies on IRC is by using  **string analysis** .

Test: Sample-9-4.exe. Run the sample and carry out dynamic string analysis on the sample.

If you analyze the strings, you find various patterns in its memory, which indicate that it uses IRC protocol, as seen in Figure 9-7. Some of the IRC strings seen are these IRC protocol commands: PRIVMSG, USER, NICK, ACTION.

![](images/M8-1-Network%20Communication_7.png)

![](images/M8-1-Network%20Communication_8.png)

Before you run the sample, start FakeNet. After running the sample, the FakeNet output in Figure 9-8.

Malware has been known to use  **FTP**  protocols for CnC by monitoring text files in FTP CnC servers, which are updated with commands by the attacker. The malware then downloads and executes. Similarly, they use FTP servers to upload extracted data about the victim.

Another well-known protocol used for data exfiltration is  **DNS** . DNS is a well known and established protocol that is pretty much a malware favorite like HTTP, especially because firewalls are configured to allow free-flowing movement of DNS requests and responses across the corporate boundary, making it an attractive use-case for attackers. DNS tunnels are used by malware for data exfiltration by  **inserting victim’s data within DNS queries**  directed at DNS CnC servers managed by the attacker, thereby creating covert communication channels from the malware to the CnC server.

There have even been cases where attackers have even  **exploited the workflow of anti-malware products**  to exfiltrate data. Most anti-malware products involve some cloud server components to which they frequently upload malware they detect on the customer’s boxes for further dissection and analysis. Attackers can hitch a ride on an anti-malware product’s connection to its cloud by inserting their victim’s data to be exfiltrated into malware payloads. Unbeknown to the anti-malware product, it uploads to the cloud, thereby leaking the victim’s data outside the corporate boundary. Attackers then figure out other mechanisms to extract this exfiltrated data from the cloud server of the anti-malware product.

With the arrival and the indiscriminate use of the  **cloud storage platforms like Dropbox** , malware has also explored using such platforms not only to upload victims’ data to these cloud storage platforms but also to disseminate malware. Threat actors have been known to share URLs to their public sharing Dropbox accounts containing malware files, and lure unassuming victims into downloading this malware and running it on their systems.

## **Lateral Movement**

Lateral movement is a technique where after an attacker infects a device inside a network, then scans, searches, and moves into other devices inside your internal network in search of other assets to infect and data to exfiltrate. Lateral movement is a key tactic used in targeted attacks and APTs. The traffic from the lateral movement of an infection is often called  **east-west traffic**  , as opposed to the  **north-south traffic**  that travels between the internal and the external networks.

Lateral movement can be split into the following three stages.

1. Reconnaissance
2. Credential stealing/exploit preparation
3. Gaining access

Once the attacker has gained access to a network by infecting a machine, he starts to scan and map the network for various other assets to identify potential targets that he can infiltrate/infect. Some of the information gathered during this stage are listed as follows.

Other devices on the network, including categorizing them into desktops, servers, IoT, admin devices, devices by various departments like finance, engineering, management, and so forth. For example:
- Operating systems running on the devices and their patch level.
- Software running their version and patch status.
- Various users, their account information, and their privilege levels in the enterprise.
- Important servers on the network.
- Available open ports on various devices and the services listening on them.

Figuring out other assets on the network can be done by various means. For example, the malware might start by fingerprinting the existing device and its user it has infected,  **understanding the importance and priority of the device and the user** . For example, if the current infected machine belongs to an IT admin, then it is likely that this user (IT admin) is going to connect to various other important severs and machines across the network. The current device becomes a high-value asset from which it can pivot around to other devices on the network. This device also becomes important in the sense that the malware can list the other important servers/devices that the machine connects to, by identifying the peers in its network communications. To this end, the malware can use tools like Netstat to list all the connections made by the current device to other devices on the network to figure out the other important assets on the system.

While this mechanism is more passive in the sense that it involves looking within the infected system to figure out other assets on the network, malware also uses active mechanisms, such as  **scanners** like NMAP and Masscan, to map the network and identify open ports. But a lot of times these off the shelf network mapping/scanning tools might be noisy and are easily caught by network security tools and SoC analysts. To avoid easy detection, malware might have custom network scanning tools that covertly scan the network over a long time to avoid any suspicions. These might involve simple TCP SYN–based scans or deeper scans that identify more information about software services running on other systems on the network.

## **Credential Stealing/Exploit Preparation**
* The malware/attacker needs to  **figure out ways to get into the target machines ** on the network. There are multiple ways to go about this process; the following describes two of them.
  * The malware/attacker steals important credentials, including those of IT admins, which they move around various systems on the network.
  * In the reconnaissance stage, the attacker identified various vulnerable software and devices on the network. With this information in hand, the attacker readies an  **exploit payload**  to exploit vulnerable systems on the network to gain access to these systems and infect them with the malware.
* A lot of times, getting access to other systems does not require exploiting any credentials because IT staff configures their systems with no authentication or makes it publicly accessible, allowing malware/attackers to easily infect.

## **Stealing Credentials and Weak Passwords**
Stealing credentials is a commonly employed mechanism by most malware, where it uses tools like  **Mimikatz**  that can scan the memory of the various processes running on the system for passwords and other authentication certificates. Various other such tools can be used by the attacker to ** scan the memory for cleartext passwords. **

Malware may not even get the real password, instead only managing to  **capture password hashes** , using which they can also use to authenticate into other systems on the network.

Malware is also known to ** scan network traffic in search of nonencrypted traffic carrying cleartext passwords** . A lot of server software deployed in the internal network doesn’t use HTTPS (encryption), allowing such traffic to be scanned by network sniffing malware for credentials.

Malware with  **keyloggers**  components can log the keystrokes of its users to obtain the passwords keyed in by the system’s users. Some of them inject themselves into web browsers and other software to intercept the web page/UI loaded by the application to steal user credentials and intercept and steal real-time, OTP-based, two-factor authentication passwords that are commonly used today.

There are various other techniques by which the malware can use other authentication tokens, such as  **the Kerberos golden ticket to get unrestricted access to all the systems in the domain.**

**Weak and default credentials**  are another vulnerable area in security; it is where users don’t change the passwords that come as the default in software installation. In other cases, users are known to use weak commonly known passwords like password and 12345 allow malware to brute-force its way into the target systems.

## **Exploiting Vulnerable Systems**
Vulnerabilities in software are a part of life and most malicious actors use zero-day and other known vulnerabilities in  **unpatched**  systems to gain access into them. Vulnerable applications are especially true for legacy applications and firmware that are never updated with security patches for various reasons, which makes gaining access into these other systems super easy.

Having mapped the various assets, the software they run, and their versions, the attacker maps the various vulnerabilities these software and their specific versions have, readying  **exploits**  which they can then use in the next stage to gain access to the system and further infect it with the malware. But the important part in this stage comes from ** correctly identifying the software/asset that is vulnerable** , and this requires careful fingerprinting of the assets from the previous stage. For example, the WannaCry ransomware used the Eternal Blue exploit that targeted a vulnerability in the version1 of SMB protocol service implementation on Windows systems. If the Windows system supported only SMBv2 and didn’t run a service that used the SMBv1 protocol, then it couldn’t be infected. Correctly identifying the version of SMB to launch the Eternal Blue exploit was important for WannaCry ransomware to exploit and infect other systems.

## **Misconfiguration**
Software is often  **released with default authentication**  settings in their configuration files, which is a bad mistake. These default settings are put in place with the expectation that the IT staff/admin override these default auth settings, but often they don’t override this, either because they forget or they are too lazy to check for any such default settings. Some of these default settings might involve keeping ports open in the application, which can be accessed by using a default set of credentials. In some cases, it may not even need any kind of authentication. In other cases, the admins unintentionally configure specific settings that turn an otherwise secure application into an insecure one by opening it up for abuse by malicious actors.

A lot of malware is known to abuse such  **misconfigurations**  in software to gain access to systems. A recent known example that we blogged about was misconfigured docker services deployed in the cloud docker deployments that allowed anyone to connect to it and start a container of their choice, which was abused by malware to run cryptominer malware. You can read about in our blog post “Container Malware: Miners Go Docker Hunting in the Cloud.” Another good example is the open Redis server, which was abused by attackers and infected with malware.

With the target mapped by the malware for lateral infection, and the access method figured out using either stolen credentials, exploit, or some misconfiguration, the malware now gains access to the target system. Sometimes the malware can also  **brute force authentication credentials to gain access to target systems** . Once on the target system, the malware can repeat the same steps of reconnaissance and stealing credentials and gaining access to other systems on the network until it can reach its final intended target victim and extract the data it needs to exfiltrate out of the system.

## **SMB, PsExec, and Others**
SMB is one of the most popular protocols that have been exploited in recent times by malware to gain access to a target victim’s computer. For example, in the previous section, we spoke about how the WannaCry ransomware used the Eternal Blue exploit to infect vulnerable machines running SMBv1 on Windows. But abusing SMB to infect such machines doesn’t have to always involve using exploits.

Users are known a lot of times to again misconfigure their SMB setup,  **leaving shared folders wide open to public**  access not only to read contents of these folders, but also write into them. In other cases, malware is known to use stolen credentials to gain access to SMB shared folders. With access to these shared folders figured out, malware may copy malicious executables and documents into these shared folders, with socially attractive names, hoping that a user with access to the shared folder will access and execute the malicious payload on their system. Malware is known to also use tools like PsExec using which they can remotely execute malware programs that they copy into shared folders of other machines, basically avoiding the need to wait for the victim to execute them.

## **Detecting Network Communication**
* methods that analysts and detection engineers can use to identify malicious network traffic:
  * 1-Networking APIs and API Logs with APIMiner
  * 2-String Analysis
  * 3-IP and Domain Reputation
  * 4-Static Signatures: IDS and Firewalls

### **1-Networking APIs and API Logs with APIMiner**
Any kind of network connection requires the use of networking APIs by the malware and can be a good and easy way to identify if it uses network connections.

![](images/M8-1-Network%20Communication_9.png)

![](images/M8-1-Network%20Communication_10.png)

To identify the networking APIs used by the sample, you can peek into its import directory using CFF Explorer tool or any other such PE analysis tool. As an exercise, open Sample-9-3.exe using CFF Explorer and click Import Directory, as seen in Figure 9-9.

In this case, the sample is unpacked, so you could see all the networking APIs used by the sample. But most malware is packed in which case all the APIs imported by the actual malware won’t pop up until the malware unpacks itself in memory. In such cases, you can use dynamic string analysis or analyze the PE header’s import directory after it unpacks in memory, to view the list of APIs the sample imports.

![](images/M8-1-Network%20Communication_11.png)

You can also use APIMiner, the API logger tool we developed, that dynamically analyzes the sample by executing it and logging to the disk the APIs used by the sample when it runs. Run Sample-9-3.exe using APIMiner and the command prompt and command line, as seen in Figure 9-10.

Running this command should generate multiple API log files in the same directory that follow the format apiminer_traces.* format. Open both the generated log files and scroll through the various APIs used by the samples to find the use of networking APIs we observed in Figure 9-3 before. In Figure 9-11, you can see the invocation of HttpOpenRequestA networking API which confirms that our sample uses HTTP for CnC

![](images/M8-1-Network%20Communication_12.png)

![](images/M8-1-Network%20Communication_13.png)

### **2-String Analysis**
We already explored string analysis earlier in the chapters in Figure 9-5 and Figure 9-7, where we used string analysis to identify that the samples used HTTP and FTP protocol for its CnC communication.

You can also use string analysis to obtain the list of various networking APIs used by the sample, as discussed in the previous section. If static strings don’t reveal enough strings, it probably indicates that the malware is packed, and you must resort to using dynamic string analysis by running the sample to obtain the strings in the unpacked sample’s memory content.

Using string analysis, you can also obtain other important artifacts about the malware and its attackers and other CnC server related details. For example, a lot of malware embeds the IP addresses or the domain names of its CnC server, which you can easily extract using simple regular expressions. For example using a regex like `[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}` you can match and extract all the IP addresses in the strings you have dumped from string analysis.

The obtained list of IP addresses and domain names from the malware strings can then be cross-referenced against other such analysis reports on the Web by using Google to see if anyone else has identified them as malicious and to identify the threat actor behind the malware infection. Alternatively, you can run these artifacts against IP reputation, and domain reputation feeds to obtain a threat score on them, as you learn in the next section.

### **3-IP and Domain Reputation**
Threat intelligence is a very important part of the anti-malware industry, and this includes various community and commercial endeavors to obtain various kinds of intelligence about ongoing threats in the wild. Two such important threat intelligence information comes in the form of IP reputation feed and domain reputation feed. A reputation feed tracks the latest ongoing threats and malicious IP addresses and domain names used by the attackers in the cyberattack.

Using such feeds as a part of our analysis workflow is very useful, by allowing us to use the obtained IP and domain addresses from our malware infection analysis and quickly querying them against these feeds for a threat score. Intelligence feeds are also useful if you are developing anti-malware products that extract IP addresses and domains from the network packets and cross-verify them against feeds for maliciousness.

Various vendors provide these intelligence feeds. But do be careful in the sense that a lot of these feeds might have False Positives, wrongly scoring benign IP addresses and domains as malicious. Also, some of the feed data might be stale. For example, a compromised web server by an attacker who uses it for a cyberattack might be rightly given a high threat score by a feed. But often it happens that once the compromised web server is cleaned off an infection, these intelligence feeds fail to remove them off their feeds, still identifying them as dangerous/malicious.

It is important to not confine yourself to only one feed, but instead combine multiple such intelligence feeds to arrive at a cumulative threat score to weed out such false positives and even false negatives. Also, combine such intelligence scores with other analysis and behavior aspects of the malware and its network communication to arrive at a cumulative threat score that provides a more accurate threat score for the infection.

Threat intelligence is a very important part of the anti-malware industry, and this includes various community and commercial endeavors to obtain various kinds of intelligence about ongoing threats in the wild. Two such important threat intelligence information comes in the form of IP reputation feed and domain reputation feed. A reputation feed tracks the latest ongoing threats and malicious IP addresses and domain names used by the attackers in the cyberattack.

Using such feeds as a part of our analysis workflow is very useful, by allowing us to use the obtained IP and domain addresses from our malware infection analysis and quickly querying them against these feeds for a threat score. Intelligence feeds are also useful if you are developing anti-malware products that extract IP addresses and domains from the network packets and cross-verify them against feeds for maliciousness.

Various vendors provide these intelligence feeds. But do be careful in the sense that a lot of these feeds might have False Positives, wrongly scoring benign IP addresses and domains as malicious. Also, some of the feed data might be stale. For example, a compromised web server by an attacker who uses it for a cyberattack might be rightly given a high threat score by a feed. But often it happens that once the compromised web server is cleaned off an infection, these intelligence feeds fail to remove them off their feeds, still identifying them as dangerous/malicious.

It is important to not confine yourself to only one feed, but instead combine multiple such intelligence feeds to arrive at a cumulative threat score to weed out such false positives and even false negatives. Also, combine such intelligence scores with other analysis and behavior aspects of the malware and its network communication to arrive at a cumulative threat score that provides a more accurate threat score for the infection.

### **4-Static Signatures: IDS and Firewalls**
Various network security tools like IDS/IPS and firewalls allow us to write static signatures that match the network packets after DPI (deep packet inspection) that allow us to identify malicious network traffic. Suricata and Snort are two such IDS/IPS that use a similar rule language, that allows us to write such signatures to identify malicious network traffic.

The rule language supported by Suricata and Snort provides support to match on raw packet contents and various specific individual application layer fields of various protocols like HTTP, FTP, SMB, and others. There are also other commercial ruleset vendors like Emerging Threats Pro and Cisco Talos that provide daily updated rulesets to identify network traffic from currently trending malware infections in the wild, which we can use with our own instances of Suricata/Snort that we deploy in our network. These tools also provide features that allow you to use IP and domain reputation feeds, which we discussed in the previous section, using which we can query and alert for the IP addresses and domains extracted from the packets.

### **Anomaly baseline**
The problem with most static signatures like the ones we discussed in the previous sections is that most traffic these days are encrypted, making the IDS/IPS blind to the malware CnC traffic. To top it all, it is also very easy for attackers to evade the static signatures used by IDS/IPS by making small string modifications to their CnC patterns.

For example, in Figure 9-5 we see that the malware uses this pattern in its CnC URL` %s?comp=%s, %s?get&news_slist&comp=%s`. But we can catch these CnC URLs by writing a Suricata signature that matches the string pattern get&news_slist. But now all the attacker must do is update his malware to use a slightly modified CnC URL format `%s?comp=%s, %s?get&news_sslist&comp=%s `to avoid getting his CnC identified by the rule. As you see, adding an extra letter `s` to the `news_slist` that converts it into `news_sslist`, renders the signature useless in catching the infection.

To counter this, the network security industry is slowly moving to identify malicious network traffic using anomaly-based detection. With anomaly-based detection, you start by building a baseline of what the clean network traffic looks like for the various devices in the network. With the baseline built over time, you now know what clean traffic and its features look like. With this baseline in place, if you see any new traffic whose features and parameters are widely different from this earlier network baseline you built, it should be considered suspicious traffic that warrants further inspection.

For example, consider a device that has various apps installed that use HTTP for accessing various web-related services on the Internet. One of the important header fields used in the HTTP protocol is user-agent, which identifies the name of the software initiating the HTTP request. If we have a browser like Mozilla Firefox, it’s user-agent starts with "Mozilla/5.0 ...". Similarly, other services on our system which accesses the web and uses HTTP, also have their own user-agent which they insert into an HTTP request they generate. We can build a baseline model for all the user-agent strings seen on the network for this device over time. Once we deploy this baseline model, if our model sees a new user-agent that it doesn’t hold or seen before for that device, it can generate an alert for this new user-agent seen for this device, which might be from malware infection.

Building models like this are not foolproof, since malware can spoof network behavior and field like user-agents to fool network security products into thinking they are from clean software. Hence it is important to combine these alerts with other kinds of alerts and network behavior, including host-based security events from antiviruses, to arrive at a more accurate threat score for malware infection.

Threat actors find new ways to communicate with their CnC servers, using new protocols, implementing covert channels, encrypting their payload to make identifying and analyzing their network traffic hard. As analysts and detection engineers, it is important to keep track of new protocols and strategies used by malware for CnC. Whenever we see a new protocol used by malware, it is important to understand the various aspects of the protocol so that we can understand how the protocol can hold various bits of information in CnC. It is also important for us to combine various analysis methods like string analysis, API logs, network interception tools, Network capture tools like Wireshark to better assess the network traffic for maliciousness.

As detection engineers, we also need to make peace with the reality that identifying malware infections based on network traffic is going to lead to a ton of false positives and some false negatives. A pure network-based security model is never going to work. But using a multilayered defense model that combines the observations/alerts from the network traffic, with the behaviors observed from the various processes and services on the system using antivirus and other such endpoint agent tools, should help fine-tune the alerts and improve alert accuracy.