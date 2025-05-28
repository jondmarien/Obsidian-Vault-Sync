# ClickJacking
## What is It?
- Also known as UI Redress Attack
- A vulnerability in a web application's Presentation Layer
- Similar to XSS but with a different goal and in a different scenario

- Allows an attacker to trick a user into using a malicious control while the user thinks they are using an innocent control
- Occurs when a malicious site or malicious unrestricted 3rd party include is able to create HTML/CSS/JS elements on an otherwise legitimate page
- The attacker can conceal a button or link, for example, overtop of another button or link with the careful use of CSS positioning and styling
- The unsuspecting user will think they are clicking on the "lower" button but are in fact clicking on the attacker's button
- Commonly used to try and steal credentials or execute CSRF attacks

![](Pasted%20image%2020240318144641.png)

## ClickJacking - Root Causes
> A malicious website run by the cybercriminal is the trivial example of the cause of ClickJacking
- Malicious website has content that a user would search for and load (free TV show streaming)
- ClickJacking "code" will be hovering above a desired element or control on the page
> Another example occurs on a non-malicious site when the developer includes untrusted 3rd party content on the page
- The developer includes a rotating advertisement on the page where the ad content is linked externally
- The attacker will load a malicious advertisement into the advertises database
- Eventually the ads will cycle to the malicious ad and the ClickJacking code will show up on the page

## Typical Exploitation Scenario
- The exploit code (the hovering invisible element) is rendered along with the rest of the page. The malicious content is usually contained in an `<iframe>` and uses the z-index css property: 
```css
button {
background: transparent;  
border: none;
outline: none;  
display: block;
cursor: pointer or default;  
Height, width, z-index, etc.
}
```
The user interacts with the malicious content, believing they are interacting with a different element.

## Example
```HTML
<!DOCTYPE html>
<html lang="en">
	<head>
		<title></title>
		<meta charset="utf-8">
		<link rel="stylesheet" type="text/css" href="">
			<script>
				function goodButton() {  window.alert("Good Button"); }
				function evilButton() {  window.alert("Bad Button"); }
			</script>
	</head>
	<body>
		<p>I'm an innocent website</p>
		<input type="button" value="clickme" onclick="goodButton()" id="goodButton">
		<input type="button" value="clickme" onclick="evilButton()" id="evilButton">
	</body>
</html>
```
```css
<style>
body {
	position: relative;
}
#goodButton {
	position: absolute;  left: 100px;
	top: 100px;  z-index: 1;
}
#evilButton {
	position: absolute;  
	left: 102px;
	top: 102px; 
	z-index: 2;
	background: transparent;  
	border: none;
	outline: none; 
	display: block;  
	cursor: default;
}
</style>
```

## ClickJacking Defense
- For the sake of completeness, to prevent the first style of ClickJacking, the only option is to rely on end-user training and browser defense techniques like malicious site blacklists
- Typical defense is to employ functionality which prevents other (external content) from creating frames on your page.
	- Sandboxing can be employed to secure 3rd party content included in a frame:
```html
<iframe src=“http://www.thirdparty.com” sandbox></iframe>
```
- Modern browsers support X-Frame-Option headers (called frame breaking)
	- **DENY**
		- Prevents any an all content frames
	- **SAMEORIGIN**
		- Only allows content frames on the current site
	- **ALLOW-FROM**
		- Allows content frames from a whitelisted URI
- For now the only way to implement this protection is on a per-page basis as the headers must be sent with each HTTP request
- Frame breaking can be implemented in JavaScript