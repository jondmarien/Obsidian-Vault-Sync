---
title: Appendix H - Ruby Environment Scripting
author:
  - Jon Marien
created: 2025-04-30
published: 2025-04-30
tags:
  - skillsontario
  - competitions
  - certifications
  - classes
---

| Title                                   | Author                       | Created        | Published      | Tags                                                                                                                               |
| --------------------------------------- | ---------------------------- | -------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Appendix H - Ruby Environment Scripting | <ul><li>Jon Marien</li></ul> | April 30, 2025 | April 30, 2025 | [[#skillsontario\|#skillsontario]], [[#competitions\|#competitions]], [[#certifications\|#certifications]], [[#classes\|#classes]] |

# Ruby Environment Scripting

---

# Exercise 1: Basic Ruby Programming

## Objective

- Create basic Ruby scripts and extract data and explore the features and components of Ruby.

---

First, we boot into the interactive ruby terminal with `irb`, and create a basic ruby script:
![[image-404.png]]
Cool! What's next?
The shell can also do math:
![[image-405.png]]

Here we can try executing more expressions:
![[image-406.png]]

Then, we write this `arpscanner.rb` script out, in ruby, of course:
![[image-407.png]]

We can run it with `ruby filename.rb`:
![[image-408.png]]

The above code can be explained as so:
- The code starts with standard calls to create a socket. Then, use the send capability to send data into port User Diagram Protocol (UDP) 53, since you need to retrieve ARP responses, which are stored in the s type of socket.
- If the host is up, the ARP entry will be added to the OS's ARP cache and will have an Internet provider (IP) address assigned with it. Browsing this ARP cache shows which hosts are up.
- To enumerate the IP space, use the times operator of the Fixnum class-the class for numbers that have not been assigned to a variable. The times operator iterates from 0 to 254, and assigns the current value to our i variable. If i is equal to 0, skip it, as you only want the usable IP addresses in the subnet. For the subsequent iterations, append it to the subnet `192.168.177`.
- Once the UDP packets are sent, make use of the proc file system to directly access the system's ARP table. For this step, you need to run a Linux or UNIX system.
- Because you have already split the output on newline characters, you will have an array, with each value being an ARP entry. Create a new empty array called `up_hosts` using the array syntax of `[]`. Iterate through each line, each time assigning the line from the ARP cache to the line variable.
- Finally, if you have a good ARP entry, create a hash using the {} syntax and use the `:ip` and `:mac` symbols as the keys for the parsed values. Assign each key the value with the => operator. The two fields you want are the IP address, which is the first element in the field, and the MAC address, which is the fourth element. Because arrays start with an index of 0, count up from 0, yielding the array fields of 0 and 3. Now that you have the hash, append it to the end of the `up_hosts` array using the `<<` append syntax, resulting in the hash appearing as the last element of that array.
- You now have an array of hashes containing the hosts that were found via the ARP resolution. Print them in an easy-to-view format. Start by printing the header using the print format string. Use `%s` to indicate a string, and `%-12s` to indicate a 12-character string that is left-aligned.

Using Control Statements to print when the user last logged in:
![[image-410.png]]

Web Banner:
![[image-409.png]]

File Manipulation:
![[image-411.png]]
![[image-412.png]]
![[image-413.png]]

All done!

---
# Exercise 2: Basic Ruby Socket Programming

## Objective

- Create network connection Ruby scripts and extract data and explore the features and components of Ruby sockets.

---
