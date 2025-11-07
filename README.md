## Data Structure and Algorithms Preparation Guide

#### #100DaysOfCode
-------------------------------------------

#### General Approach 
- Coding 
    - Code should be clean & structured.
    - Cover the edge and base cases.
    - All variables and functions well-defined
- Data Structures & Algorithms 
    - Solve the problem efficiently with suitable data structure or  algorithm.
    - Analyze that solution in terms of time & space complexity and the trade-offs.
    - Compare brute force solutions versus more optimal solutions.
    - Solve Efficiently 
- Communication 
    - Communicate effectively.

#### UMPIRE 
The UMPIRE model is a structured, iterative framework for systematic problem-solving, research, and project execution, ensuring logical flow and continuous improvement across stages.
- Use UPI (Understand, Plan, Implement) technique which help you to plan and verbalize your thinking before writing code
![](umpire.png)

`Understand the Problem`
- Understand what the interviewer is asking with clarifying questions
- Generate basic sample input and output
- Explore more unusual edge cases
- Explore tradeoffs (memory, performance, code simplicity)


      
##### Key Principles for Effective Preparation
- ✨2 Code Everyday✨
- ✨Update Daily for Tracking✨
- ✨Add Notes for Revision ✨
-  ✨Handwritten Notes or Medium or Substack✨
  
---
#### Topics
##### Data Structure
- Arrays & Strings
- Hashing
    - Design Hash
    - Hash Set & Hash Map
    - Design Key & Hashing
- Stacks and Queues
- Linked Lists
- Binary Trees 
- Heaps
- Graph Algorithms
- Recursion and Divide & Conquer
- Dynamic Programming


---
| Week | Topic |
| ------ | ------ |
| `week 1` | [Arrays] [Strings] |
| `week 2`  | [Dictionaries] [Hashing] |
| `week 3`  | [Stacks] [Queues] [Two Pointer] |
| `week 4`  | [Linked Lists I] [Linked Lists II] |
| `week 5` | [Recursion] [Divide & Conquer Algorithms] |
| `week 6` | [Binary Trees] [Binary Search] |
| `week 7` | [Searching] [Sorting] |
| `week 8`  | [Graphs I] [Graphs II] |
| `week 9`  | [Coding Patterns I] [Coding Patterns II] |
| `week 10`  | [Bit Manipulation] [Maths] |
| `week 11` | [Dynamic Programming I] [Dynamic Programming II] |
| `week 12` | [Dynamic Programming III] [Dynamic Programming IV] |
| `week 13`  | [Coding Practice I] [Coding Practice II] |
| `week 14` | Design Patterns] [Object Oriented Design] |
| `week 15` | [System Design I] [System Design II] |
---
##### Time-Space Complexity Analysis 

- `Big O` notation describes the worst-case time or space complexity of an algorithm relative to the size of the input.
![](https://kajabi-storefronts-production.kajabi-cdn.com/kajabi-storefronts-production/products/306049/images/EDEK0CQaRFm7VyYLjZJ3_bigo.jpg)
---------
### Algorithms Design
#### Arrays
- Two Pointer Techniques
    - Iterates

- Sliding Windows Fixed Size vs Variable Size
    - Fixed Size Approach:
        - Initialize the window by summing the first k elements.
        - Slide the window one element at a time by removing the element on the left and adding the element on the right.
        - Track the maximum sum as you move the window.
  
     - Variable Size Approach:
        - Start with both pointers (left and right) at the beginning of the array.
        - Expand the window by moving the right pointer, adding elements to the window.
        - When the sum of the window meets or exceeds the target, attempt to shrink the window by moving the left pointer to find the smallest possible window that satisfies the condition.
```

def fn(arr):
    left = ans = curr = 0

    for right in range(len(arr)):
        # Add arr[right] to curr (based on the problem's logic)
        curr += arr[right]

        # Check if the window condition is broken (e.g., sum exceeds some value)
        while curr > some_limit:  # Replace 'some_limit' with an actual condition
            # Remove arr[left] from curr to shrink the window
            curr -= arr[left]
            left += 1

        # Update ans based on the window (e.g., maximum sum, minimum length, etc.)
        ans = max(ans, right - left + 1)  # an example for update

    return ans

  ```

#### Time Complexity 

    - `O(n)`, where `n` is the number of elements in the array. Sliding the window across the array involves constant-time operations for each step (add and subtract an element).
    - `O(n)`, where n is the number of elements in the array. The sliding window adjusts dynamically, with each element being added and removed from the window at most once.


- Prefix Sums
- Kadane's Algorithm

#### Linked Lists
- Fast and Slow Pointers
---

##### Advanced Algorithms Design
- Dynamic
----------

### Few Important Notes & Links

| Topics         | URLs |
| :------------- | ---- |
| Data Structure Notes| []   |
| Algorithm  Notes    | []   |
---
### References
- Cormen 




