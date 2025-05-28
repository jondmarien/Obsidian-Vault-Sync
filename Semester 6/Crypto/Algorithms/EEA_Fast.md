# EEA_Fast
```python
#Extended Euclidian Algorithm
#Returns r,s,t where N(s) + a(t) = r

def EEA_fast(N,a):
    
    #initialize 2 rows, 3 columns (R,S,T)
    R=[N,a]
    S=[1,0]
    T=[0,1]
    
    #add rows until remainder = 1 or 0
    while R[-1]>1:
        S+=[ S[-2] - R[-2]//R[-1]*S[-1] ]
        T+=[ T[-2] - R[-2]//R[-1]*T[-1] ]
        R+=[ R[-2]%R[-1] ]
    
    #print all rows
    for r,s,t in zip(R,S,T):
        print (r,s,t)
```

Then, run it:
```python
EEA_fast(26,15)
```

| R   | S   | T   |
| --- | --- | --- |
| 26  | 1   | 0   |
| 15  | 0   | 1   |
| 11  | 1   | -1  |
| 4   | -1  | 2   |
| 3   | 3   | -5  |
| 1   | -4  | 7   |

And again:
```python
EEA_fast(481,71)
```

| R   | S   | T    |
| --- | --- | ---- |
| 481 | 1   | 0    |
| 71  | 0   | 1    |
| 55  | 1   | -6   |
| 16  | -1  | 7    |
| 7   | 4   | -27  |
| 2   | -9  | 61   |
| 1   | 31  | -210 |
