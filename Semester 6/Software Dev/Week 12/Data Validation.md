# The First Line of Defense

## What is Data Validation
- "The process of ensuring that a program operates on clean, correct, and useful data"
- "Ensuring that data is strongly typed, with correct syntax, within length boundaries, contains only permitted characters, or that numbers are correctly signed and within range boundaries"

## Why Validate?
- Non-validation of data can lead to 2 serious issues
	- Application vulnerabilities like injection, overflows and  other unexpected behavior
	- Data corruption like incomplete records, incorrectly calculated values and inconsistent data representations
- Validation for prevention is not good enough
	- Should include detection so that an attacker cannot continue to probe for weaknesses until one is found

## When and Where to Validate?
- One obvious question is, where should the  checking be performed? When the data first enters the program, or later by a lower-level routine that actually uses the data? Often, it's best to check in both places; that way, if an attacker manages to slip around one defense, they'll still encounter the other. The most important rule is that all data must be checked before it's used." – David Wheeler, Institute for  defense analysis at IBM

- Every layer should perform it's own validation
- The appropriate tier should validate against attacks which it is susceptible to.

- Data layer should guard against data related attacks like SQL injection but presentation and application layer should not check for SQL injection.
![](Pasted%20image%2020240401140026.png)

## General Validation Strategies
- **Whitelist** Validation Approach
	- Check for expected values, ranges, permitted characters, etc.
		- Ex. `if (option == ‘A’ || option == ‘B’) { permit=true;}`
- **Blacklist** Validation Approach
	- Check specifically for flaws and known exploits
		- Ex. `if (option.contains(“drop table”)) { permit=false;}`

- Which is better?
	- Blacklist? I think, because it is easier to disallow things rather than allowing things. 
	- Both are valid -- blacklist is focused on security whilst whitelist can allow many things

- **Whitelist** Validation Techniques:
	- Check that data is strongly typed and enforcing strongly typed data interaction
	- Checking correct syntax (ex. postal code format)
	- Length boundaries (10 chars, 20 chars, etc.)
	- Permitted characters (ex. only numeric | alpha | alphanumeric)
	- Numbers are correctly signed (ex. No negative ages)
	- Range boundaries (max and min permitted values)
	- Business rules (logical boundaries and expected values like interest rates)

- **Sanitizing**: Changing the user input into an acceptable and "safe" format
	- Ex. if your field should be numeric, strip all non-digit characters from the input
	- Good practice is to always replace non-alphanumeric characters into their HTML/URL encoded representation
		- Ex. single quote `'` is `%27`
	- For binary file data, consider encoding the whole thing in `base64`.

## Other Types of Validation
- Batch totals to check for missing records
- Cardinality and referential integrity checks to enforce relational data connections
- Check digits included as simple integrity and checksum validators (ex. ISBN)
- File existence checks before performing IO
- Presence checks make sure data has not been omitted (ex. Required field in a web form)
- Spelling and grammar checks are very specific contextual validators. They **must** consider language and text context.
- Uniqueness checks


## Coding Exercise
Where and how would you include detection and reporting?
```python
#!/usr/bin/python3

import string

def validateNum(min, max, data):
    if data <= max and data >= min:
        return True
    else:
        return False

def validateString(min, max, permittedChars, data):
    if len(data) >= min and len(data) <= max:
        for char in data:
            if char not in permittedChars:
                return False
        return True

def urlEncode(data):
    return None

def stripWhiteSpace(data):
    return None

def validateEquals(allowedStrings, data):
    return None

def validate(rule, data):
    rules = ["ALPHA1", "NUM1", "URLENCODE", "WHITESPACE", "MATCH"]
    result = None
    if rule in rules:
        if rule == "ALPHA1":
            result = validateString(5, 12, string.ascii_letters, data)
        elif rule == "NUM1":
            result = validateNum(1, 100, data)
        elif rule == "URLENCODE":
            result = urlEncode(data)
        elif rule == "WHITESPACE":
            result = stripWhiteSpace(data)
        elif rule == "MATCH":
            allowedStrings = ["value1", "value2"]
            result = validateEquals(allowedStrings, data)
        return result
    else:
        return False


```

Check [OWASP Input Validation Cheat Sheet](https://owasp.deteact.com/cheat/cheatsheets/Input_Validation_Cheat_Sheet.html) and add two more validations.

Finished, added **type** and **regex** checking:
```python
#!/usr/bin/python3

import string
import urllib.parse
import re

def validateNum(min, max, data):
    if data <= max and data >= min:
        return True
    else:
        return False

def validateString(min, max, permittedChars, data):
    if len(data) >= min and len(data) <= max:
        for char in data:
            if char not in permittedChars:
                return False
        return True

def urlEncode(data):
    if isinstance(data, str):
        # Encode a string directly
        return urllib.parse.quote(data)  
    elif isinstance(data, dict):
        # Encode a dictionary of key-value pairs
        return urllib.parse.urlencode(data)
    else:
        raise TypeError("Unsupported data type: please provide a string or dictionary.")

def stripWhiteSpace(data):
    if isinstance(data, str):
        # Remove leading and trailing whitespace
        return data.strip()
    else:
        raise TypeError("Unsupported data type: please provide a string.")

def validateEquals(allowedStrings, data):
    if isinstance(data, str) and any(data == allowedString for allowedString in allowedStrings):
        return True
    else:
        return False
        
def validateType(data, expected_type):
  return isinstance(data, expected_type)
  
  
def validateRegex(data, pattern):
  if not isinstance(data, str):
    raise TypeError("Input must be a string.")

  regex = re.compile(pattern)
  return bool(regex.fullmatch(data))

def validate(rule, data):
    rules = ["ALPHA1", "NUM1", "URLENCODE", "WHITESPACE", "MATCH", "TYPEVALIDATION", "REGEX"]
    result = None
    if rule in rules:
        if rule == "ALPHA1":
            result = validateString(5, 12, string.ascii_letters, data)
        elif rule == "NUM1":
            result = validateNum(1, 100, data)
        elif rule == "URLENCODE":
            result = urlEncode(data)
        elif rule == "WHITESPACE":
            result = stripWhiteSpace(data)
        elif rule == "MATCH":
            allowedStrings = ["value1", "value2"]
            result = validateEquals(allowedStrings, data)
        elif rule == "TYPEVALIDATION":
            result = validateType(data, int)
        elif rule == "REGEX":
            email_pattern = r"^[^@]+@[^@]+\.[^@]+$"  
            result = validateRegex(data, email_pattern)
        return result
    else:
        return False


```