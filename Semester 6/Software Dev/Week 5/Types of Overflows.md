## Heap Overflows

**Heap Concepts**
- Dynamically allocated data "lives" on the heap
- The heap is one of the components of the virtual address space allocated by the kernel when a process starts
- The heap *grows toward the stack*, so the "bottom" of the heap is at lower addresses and it grows towards higher addresses
- Heaps are typically constructed using linked lists of allocated and unallocated blocks of 
- Local variables are stored in the heap

**Glibc Struct**
```c
struct malloc_chunk{
	INTERNAL SIZE prev size;
	INTERNAL SIZE size;
	struct malloc chunk* fd;
	struct malloc chunk* bk;
}
```

**Heap Overflow**
![](Pasted%20image%2020240205145413.png)
- An attacker's goal in a heap overflow is to fill one allocated “chunk” of memory past its capacity
- The hope is that the overflowed data will leak into an adjacent variable’s chunk of memory
	- Can lead to code execution or just plain variable corruption

## Integer Overflows

**Signed and Unsigned Data**
![](Pasted%20image%2020240205140652.png)
- When a program tries to store a value that exceeds a variable's limits, an overflow occurs.
- Unlike a buffer overflow, extra data will <u>not</u> "spill over" into adjacent memory addresses.
	- The only issue is that the most significant bits are <u>lost</u> and execution continues as normal
	![](Pasted%20image%2020240205140840.png)	

**Integer Overflow Exploitation**

```C
int save vals (long* array, unsigned int num val s)
{
	long* arr;
	arr = malloc (num vals * sizeof (long));
	for (int i 0; i < num val s; i++) {
		arr[i] = array[i];
	}
	output_array(arr);
	return 0;
}
```
- In the example above, the calculation used for malloc(int * 4) may result in an integer overflow. If the overflow occurs, malloc will only allocate a few bytes to the array. These bytes are then overridden inside the for loop, creating a heap overflow vulnerability.

**Protection Checks**
- Range checking data validation
- Pre-calculation validation
- Post-calculation validation
- Type strictness (are you adding a signed var to an unsigned var?)
- Should the results of the calculation be stored in a different datatype? possibly, long?

[Overflow Diagram](Overflow%20Diagram.canvas)



**Spot the Bug!!**
![](Pasted%20image%2020240205145215.png)
- Handle negative values from `network_get_int`
- Allocate `buf` dynamically
- Change the check to be `length - MAX_PACKET > 1` 
	- The maximum safe value for `length` is `MAX_PACKET - 1` because arrays are zero-indexed in C
