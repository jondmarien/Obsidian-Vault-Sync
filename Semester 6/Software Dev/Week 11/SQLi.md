# SQL Injection

## What is SQLi?
- A vulnerability in (primarily web based) applications which interact with a data layer
- SQL injection attacks are attempts by attackers to execute arbitrary SQL statements against the application's database
- SQL injection can be used for simple data mischief, denial of service attacks or for more sophisticated long term information gathering schemes

## Causes, Impacts & Considerations for SQLi
- User input data not validated
- Incorrect data validation technique
- Dynamic SQL statement generation
- Incorrect application of the principle of least privilege
- Insufficient restrictions at the data layer
- Easy to locate and exploit

## Variations in Exploitations
- <u>Method 1:</u> Modify the dynamic SQL statement by:
	- Inserting a `Boolean` condition into the existing statement which will always evaluate to true, or
	- Modifying it in some other way, like issuing a `UNION` instruction with another table, forcing the SQL statement to return unexpected records
- The modified expression will now return more records than expected or, depending on the specific SQL statement, disrupt the normal operation of the application in some way

- Method 2: Terminate the dynamic SQL statement by:
	- Ending it and inserting a semicolon
	- Inserting a new SQL expression to be run against the database
	- Forcing the backend process to ignore the rest of the expected SQL statement by inserting a "start of comment" symbol
- The first statement will terminate and the "stacked" second SQL statement will be run against the database


| Exploitation Variations Method: | Modify the dynamic SQL statement                                                                                                                                                                                                                  | Terminate the dynamic SQL statement                                                                                                                                                                                                         |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Instructions:                   | - Insert a `Boolean` condition into the existing statement which will always evaluate to true, or<br>- Modify it in some other way, like issuing a `UNION` instruction with another table, forcing the SQL statement to return unexpected records | - Ending it and inserting a semicolon<br>- Inserting a new SQL expression to be run against the database<br>- Forcing the backend process to ignore the rest of the expected SQL statement by inserting a "start of comment" **symbol, --** |


## Defense & Mitigations for SQLi
- Escape sequences and regular expression pattern matching
	- Good for modification of legacy code
	- Difficult to maintain
	- Difficult to match all possible cases (what **EXACTLY** do you search for?)
- Stored procedures
	- Better than character escaping
	- Stored procedures, if incorrectly written, can be exploited to run system commands
- Parameterized queries (prepared statements)
	- Optimal solution
	- Always performs correct escaping and treats all arguments as simple text strings
	- Also faster and more efficient than dynamic SQL
	- Also forces better application development strategy by defining all possible queries
- Other mitigation strategies
	- Applying least privilege
	- Don't connect as DBA


| Defense + Mitigations: | Escape Sequences                                                                                             | Stored Procedures                                                                                                        | Parameterized Queries                                                                                                                                                                                                                                   | Other Mitigation Strategies                          |
| ---------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| Reasonings:            | - Good for modification of legacy code<br>- Difficult to maintain<br>- Difficult to match all possible cases | - Better than character escaping<br>- Stored procedures, if incorrectly written, can be exploited to run system commands | - Optimal solution<br>- Always performs correct escaping and treats all arguments as simple text strings<br>- Also faster and more efficient than dynamic SQL<br>- Also forces better application development strategy by defining all possible queries | - Applying least privilege<br>- Don't connect as DBA |


## Links
[SQLi Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)