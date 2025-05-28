# Text_to_Int
```python
#converts text string to integer string
#using 2-digit blocks
def text_Z26(text):
    
    letters='abcdefghijklmnopqrstuvwxyz'
    
    Z26=''
    for i in text:
        Z26+=format(letters.find(i),'02d') 
        
    return(Z26)
```
```python
text_Z26('security')
```
Output: '1804022017081924'

```python
#converts integer string to text string
#using 2-digit blocks
def Z26_text(Z26):
    
    letters='abcdefghijklmnopqrstuvwxyz'
    
    text=''
    for i in range(0,len(Z26),2):
        text+=letters[int(Z26[i:i+2])]
        
    return(text)
```
```python
Z26_text('1804022017081924')
```
Output: 'security'

```python
Z26_text(text_Z26('check'))
```
Output: 'check'