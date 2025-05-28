---
title: How to Count O(n) in Code
author:
  - Jon Marien
created: 2025-02-05
published: 2025-02-05
tags:
  - classes
---
Here's how to calculate time complexity for individual lines of code and their cumulative impact:

---

## **Step-by-Step Calculation Method**

### **1. Basic Operations (O(1))**
- **Assignments**, arithmetic operations, comparisons, and simple returns take **constant time**.
  ```python
  x = 5           # O(1)
  y = x + 10      # O(1)
  return x        # O(1)
  ```

---

### **2. Loops**
#### **Single Loop (O(n))**
- A loop iterating `n` times multiplies its body's complexity by `n`:
  ```python
  for i in range(n):      # O(n) iterations
      print(i)            # O(1) per iteration → Total: O(n)
  ```

#### **Nested Loops (O(n²))**
- Nested loops multiply complexities:
  ```python
  for i in range(n):          # O(n) iterations
      for j in range(n):      # O(n) iterations
          print(i, j)         # O(1) → Total: O(n²)
  ```

---

### **3. Conditional Statements**
- Use the **worst-case branch** for Big O:
  ```python
  if condition:           # O(1) for the check
      do_something()      # O(n) (worst case)
  else:
      do_another_thing()  # O(1)
  ```
  **Total**: O(n) (dominated by the `if` branch).

---

### **4. Function Calls**
- Replace the function call with its time complexity:
  ```python
  def helper(arr):        # O(n) time
      for x in arr:
          print(x)

  helper(my_list)         # O(n)
  ```

---

## **Key Rules**
1. **Sequential Statements**: Add complexities:
   ```python
   do_A()  # O(n)
   do_B()  # O(n²)
   ```
   **Total**: O(n + n²) → Simplified to **O(n²)**.

2. **Nested Constructs**: Multiply complexities:
   ```python
   for i in range(n):      # O(n)
       do_C()             # O(log n) per iteration → Total: O(n log n)
   ```

3. **Trim Constants/Lower Orders**:  
   - O(3n² + 2n + 100) → **O(n²)**.

---

## **Examples**

### **Example 1: Linear Time**
```python
for i in range(n):        # O(n)
    x = i * 2             # O(1) → Total: O(n)
```

### **Example 2: Quadratic Time**
```python
for i in range(n):        # O(n)
    for j in range(n):    # O(n)
        sum += i + j      # O(1) → Total: O(n²)
```

### **Example 3: Mixed Complexities**
```python
print("Start")            # O(1)

for i in range(n):        # O(n)
    if i % 2 == 0:        # O(1)
        print(i)          # O(1) → Total for loop: O(n)

for j in range(n):        # O(n)
    for k in range(n):    # O(n)
        compute(j, k)     # O(1) → Total: O(n²)
```
**Total**: O(1) + O(n) + O(n²) → **O(n²)**.

---

## **Common Patterns**
| Code Pattern                     | Time Complexity | Explanation                          |
|----------------------------------|-----------------|--------------------------------------|
| Single loop                      | O(n)            | Iterates `n` times                   |
| Double nested loops              | O(n²)           | `n × n` iterations                   |
| Halving input each iteration     | O(log n)        | Binary search, divide-and-conquer    |
| Recursion with branching factor | O(2ⁿ)           | Fibonacci (naive recursive method)   |

---

By analyzing how often each line executes relative to the input size **n**, you can systematically calculate time complexity. Always focus on the **dominant term** (e.g., ignore constants and lower-order terms).

Citations:
[1] https://adrianmejia.com/how-to-find-time-complexity-of-an-algorithm-code-big-o-notation/
[2] https://www.youtube.com/watch?v=fZc3ijGM0aM
[3] https://www.educative.io/answers/how-to-calculate-the-time-complexity
[4] https://www.reddit.com/r/learnprogramming/comments/v6obt3/how_to_figure_out_the_time_complexity_of_my_code/
[5] https://stackoverflow.com/questions/32634263/calculating-time-complexity-from-code-line-by-line-for-while-and-switch-case-and
[6] https://www.datacamp.com/tutorial/big-o-notation-time-complexity
[7] https://stackoverflow.com/questions/64253070/how-can-i-calculate-the-time-function-tn-of-the-following-code
[8] https://www.w3schools.com/dsa/dsa_timecomplexity_theory.php
[9] https://www.bigocheatsheet.com
[10] https://stackoverflow.com/questions/23935825/best-practices-for-measuring-the-run-time-complexity-of-a-piece-of-code/30019361
[11] https://courses.caslab.queensu.ca/cisc121/wp-content/uploads/sites/11/2015/10/complexity.pdf
[12] https://www.freecodecamp.org/news/big-o-cheat-sheet-time-complexity-chart/
[13] https://www.youtube.com/watch?v=hFQkMw8B5Z4
[14] https://www.hackerearth.com/practice/basic-programming/complexity-analysis/time-and-space-complexity/tutorial/
[15] https://www.crio.do/blog/time-complexity-explained/
[16] https://www.reddit.com/r/learnprogramming/comments/v6obt3/how_to_figure_out_the_time_complexity_of_my_code/
[17] https://www.enjoyalgorithms.com/blog/time-complexity-analysis-in-data-structure-and-algorithms/
[18] https://en.wikipedia.org/wiki/Linear_time
[19] https://www.youtube.com/watch?v=jGrU1UgYQkI
[20] https://www.simplilearn.com/tutorials/data-structure-tutorial/time-and-space-complexity