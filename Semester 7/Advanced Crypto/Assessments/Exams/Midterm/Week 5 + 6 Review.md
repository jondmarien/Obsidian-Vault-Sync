---
title: Week 5 + 6 Review
author:
  - Jon Marien
created: 2025-02-18
published: 2025-02-18
tags:
  - classes
---

| Title             | Author                       | Created           | Published         | Tags                   |
| ----------------- | ---------------------------- | ----------------- | ----------------- | ---------------------- |
| Week 5 + 6 Review | <ul><li>Jon Marien</li></ul> | February 18, 2025 | February 18, 2025 | [[#classes\|#classes]] |

---

## **Week 5: Time Complexity & Big-O Notation**

### **Example Question 1**  
**Question**: Show that $3n + 1$ is $O(n)$.

#### **Step-by-Step Solution**  
1. **Set up the inequality**:  
   Find constants $c$ and $k$ such that:  
   $$
   3n + 1 \leq c \cdot n \quad \text{for all } n \geq k
   $$

2. **Choose** $k = 1$:  
   For $n \geq 1$, calculate the left-hand side at$n = 1$:  
   $$
   3(1) + 1 = 4
   $$

3. **Solve for $c$**:  
   Rearrange the inequality:  
   $$
   4 \leq c \cdot 1 \implies c \geq 4.
   $$

4. **Verify**:  
   For $c = 4$ and $k = 1$:  
   $$
   3n + 1 \leq 4n
   $$
  
   This simplifies to:  
   $$
   1 \leq n
   $$
  
   which holds true for all $$n \geq 1$$

#### **Final Answer**:  
$3n + 1$ is $O(n)$ with $c = 4, k = 1$

---

### **Example Question 2**  
**Question**: Estimate the time complexity of the following "pairs" algorithm.  

```python
def pairs(w):
    x = []
    for bit1 in w:
        for bit2 in w:
            x.append(f'{bit1}{bit2}')
    print(x)
```

#### **Step-by-Step Solution**  
5. **Analyze the loops**:  
   - The outer loop runs $$n$$
 times, where $$n$$
 is the length of the input $$w$$
.  
   - The inner loop also runs $$n$$
 times for each iteration of the outer loop.  

6. **Calculate total steps**:  
   The algorithm performs $$n \times n = n^2$$
 iterations.  

#### **Final Answer**:  
The time complexity is $$O(n^2)$$
.

---

## **Week 6: P, NP, & NP-Complete Languages**

### **Example Question 3**  
**Question**: Show that $$FACTOR \in \mathbf{NP}$$
.  

#### **Step-by-Step Solution**  
7. **Define the problem ($$FACTOR$$
)**:  
   The language consists of composite numbers $$N = p \cdot q$$
, where $$p, q > 1$$
.  

8. **Construct a verifier**:  
   - A *certificate* (or "hint") is a factor $$p$$
 of $$N$$
.  
   - Verification involves two steps:
     - Check if $$p > 1$$
.
     - Check if $$N \mod p = 0$$
.

9. **Check runtime**:  
   Division can be performed in polynomial time relative to the size of the input ($$N$$
).  

#### **Final Answer**:  
Since a polynomial-time verifier exists, we conclude that $$FACTOR \in \mathbf{NP}$$
.

---

### **Example Question 4**  
**Question**: Is the instance $$\langle G, s, t \rangle = \{\{\{1,2,3\},\{(1,2),(3,2),(3,1)\}\}, 2, 3\}$$
 in PATH?  

#### **Step-by-Step Solution**  
10. **Interpret the graph ($$G$$
)**:  
   - Nodes are {1,2,3}.  
   - Edges are {(1,2), (3,2), (3,1)}.  

11. **Check for a path from node $$s = 2$$
 to node $$t = 3$$
**:  
   - From node 2:
     - Directly connects to node 3 via edge (2 → 3).  

#### **Final Answer**:  
Yes, there exists a path from node 2 to node 3.

---

## **Word-Based Instructions (No Math)**

### Big-O Proofs
- Identify the dominant term in your function (ignore constants and smaller terms).  
- Set up an inequality comparing your function to a simpler one (e.g., linear or quadratic).  
- Choose a starting point ($$k = 1$$
) and solve for a constant ($$c$$
). Verify your solution by testing it.  

### Time Complexity Analysis
- Count how many times each loop runs. Multiply nested loops together to find total iterations. Use this number to determine complexity (e.g., linear for one loop, quadratic for two nested loops).  

### NP Verification
- Define what makes a solution valid (e.g., a factor of a number). Use this as your "certificate." Ensure there’s an efficient way to check if this certificate works (e.g., division). If verification is polynomial-time, it’s in NP.

### Path Problems
- Break down the graph into nodes and edges. Start at the source node and trace possible paths to see if you can reach the target node.

---

This formatting should now be clear and easy to follow! Let me know if you'd like further adjustments or additional examples!

Citations:
[1] https://pplx-res.cloudinary.com/image/upload/v1739909891/user_uploads/TPVxhQhoEFRlmhU/image.jpg
[2] https://pplx-res.cloudinary.com/image/upload/v1739909895/user_uploads/dNSbykCHuxApQFD/image.jpg
[3] https://pplx-res.cloudinary.com/image/upload/v1739909902/user_uploads/xDxXhlnpZSEckJV/image.jpg