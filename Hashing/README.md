# Hash Tables

## Introduction

**Hash tables** are the data structures which are key-value pairs(dictionary). It provides quick key-to-value lookup.

```
Python:
  hash = {}
  for i in hash:
    print i
```

One use of a hash table would be to implement a phone book. In this scenario, the key is a name and the value is a phone number.

 The implementation may use some hashing functions, which
 can lead into collisions upon which some sort of resolution must happen
 -- either a collision is handled by simply allowing multiple items in a
 bucket (using a linked list, for instance) or by creating secondary
hashing functions, or even creating internal binary search trees. The
implementation is often language-dependent.

Sometimes, interviewers will just ask you about this though to see if
 they can trip you up. Another common "trick" question is the time-space
 complexity of a hashmap. Given a perfect hashing function with no
collisions, you can expect O(1) / constant time on lookup, insertion,
and deletion. But it can be as bad as O(n) / linear time if you have
100% collisions using a linked list implementation for
collision-handling.

```
address_book = {}
address_book["Bob"] = "111-222-3333"
address_book["Alice"] = "444-555-6666"
address_book.get("Bob")
'111-222-3333'
```

Hash tables are very efficient – their insertion, deletion, and get operations take, on average, constant time.

## How it works

### Hash Codes

Internally, a hash table stores its values in an array. A special **hash function**
 is utilized to convert each key into a code, which is then converted
into an index into the underlying array. This hash function has a hard
requirement to return the same hash code for equal keys.

Hash function generate a code, known as the  **hash code** .
 Each data type will have its own hash function that generates its hash
code differently. It is important to remember that a hash code is not
equivalent to the index in the underlying array storage structure--there
 are often more hash codes than indices in the underlying array.

 **Figure below** : Internals of a hash table
![](https://i.imgur.com/bEIWPaQ.png)

**Note:** When utilizing a hash table with a class
you've created, be sure that the hash function for that object type
operates as you would expect. If two objects are equivalent, you should
ensure that their hash codes are the same.

### Collisions

If the hash function is implemented well, inputted objects will be
distributed evenly across the array indices. However, the number of hash
 codes is often greater than the size of the underlying array, so some
keys will be assigned the same index. When two keys are matched to the
same index, this is called a  **collision** . There are several different ways of addressing collisions.

There are multiple approaches to dealing with collisions. The most
common one is simply to store all the objects that get assigned to the
same index in a linked list. In this scenario, instead of simply storing
 the value at that index, the linked list must contain both the entire
key and the value in pairs instead of just the value, so that the values
 can be uniquely tied to a key.

 **Figure below** : Hash Collision
![](https://i.imgur.com/ZqF2crs.png)

For more information about other ways to address hash collisions, see the [hash tables Wikipedia page](https://en.wikipedia.org/wiki/Hash_table#Open_addressing)
 for descriptions of several different approaches. If you have time, I'd
 encourage you to learn about open addressing, the other common hash
collision method.

 **Note on updating keys in the hash table** : Be wary of
updating a key object that's present in the hash table. Once it's
updated, lookup will no longer work for that key. Instead, if a key
needs to be updated, remove it, update the key, then re-insert the key
into the table.

## Runtimes

For interviews, it is generally assumed that the hash table is a well
 formed one, with few collisions. However, in the worst case scenario,
all operations can take linear time. When a hash table distributes the
objects poorly, all the objects may hash to the same index in the
underlying array and any operation would require going through all of
the previous entries.

|            | Lookup | Insert | Delete |
| ---------- | ------ | ------ | ------ |
| Best Case  | O(1)   | O(1)   | O(1)   |
| Worst Case | O(n)   | O(n)   | O(n)   |

## Key takeaways

* Hash tables are an extremely useful data structure-- keep them in mind as a tool for most interview questions
* Hash tables have the best performance for lookups, inserts, and deletions. All three operations on average take O(1) time.

## Resources

To get a more thorough understanding on the internals of hash tables, here are a few links to helpful resources.

* Hash table guide with helpful diagrams: [https://medium.com/basecs/hashing-out-hash-functions-ea5dd8beb4dd](https://medium.com/basecs/hashing-out-hash-functions-ea5dd8beb4dd)
* Princeton Coursera video lecture series: [https://www.coursera.org/learn/algorithms-part1/lecture/CMLqa/hash-tables](https://www.coursera.org/learn/algorithms-part1/lecture/CMLqa/hash-tables)
* HackerRank video (short summary): [https://youtu.be/shs0KM3wKv8](https://youtu.be/shs0KM3wKv8)

## Introduction

`Hash Table` is a data structure which organizes data using `hash functions` in order to support quick insertion and search.

There are two different kinds of hash tables: hash set and hash map.

* The `hash set` is one of the implementations of a `set` data structure to store `no repeated values`.
* The `hash map` is one of the implementations of a `map` data structure to store `(key, value)` pairs.

 It is `easy to use` a hash table with the help of `standard template libraries`. Most common languages such as Java, C++ and Python support both hash set and hash map.

By choosing a proper hash function, the hash table can achieve `wonderful performance` in both insertion and search.

In this card, we will answer the following questions:

1. What is the `principle` of a hash table?
2. How to `design` a hash table?
3. How to use `hash set` to solve duplicates related problems?
4. How to use `hash map` to aggregate information by key?
5. How to `design a proper key` when using a hash table?

 And we also provide exercises for you to be familiar with hash table.

## Design a Hash Table

In this chapter, we will discuss the underlying principle of the hash table.

After completing this chapter, you should be able to answer the following questions:

1. What is the `principle` of hash table?
2. Which factors will influence the choice of `hash function` and `collision resolution strategy`?
3. Understand the difference between a `hash set` and a `hash map`.
4. How to design a simple version of `hash set` and a `hash map` as in a typical `standard template library`.
5. What is the `complexity` of insertion and lookup operations?

 **Keys to Design a Hash Table**[Report Issue](https://github.com/LeetCode-Feedback/LeetCode-Feedback/issues)

---

There are two essential factors that you should pay attention to when you are going to design a hash table.

### 1. Hash Function

---

The hash function is the most important component of a hash table
which is used to map the key to a specific bucket. In the example in the
 previous article, we use y = x % 5 as a hash function, where x is the key value and y is the index of the assigned bucket.

The hash function will depend on `the range of key values` and `the number of buckets`.

Here are some examples of hash functions:

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/05/04/screen-shot-2018-05-04-at-145454.png)

It is an open problem to design a hash function. The idea is to try to assign the key to the bucket as `uniformly as you can`. Ideally,
 a perfect hash function will be a one-one mapping between the key and
the bucket. However, in most cases, a hash function is not perfect and
it is a tradeoff between `the amount of buckets` and `the capacity of a bucket`.

### 2. Collision Resolution

---

Ideally, if our hash function is a perfect `one-one mapping`, we will not need to handle collisions. Unfortunately, in most cases, collisions are almost `inevitable`. For instance, in our previous hash function (y = x % 5), both 1987 and 2 are assigned to bucket 2. That is a `collision`.

A collision resolution algorithm should solve the following questions:

1. How to organize the values in the same bucket?
2. What if too many values are assigned to the same bucket?
3. How to search for a target value in a specific bucket?

These questions are related to `the capacity of the bucket` and `the number of keys` which might be mapped into `the same bucket` according to our hash function.

Let's assume that the bucket, which holds the maximum number of keys, has `N` keys.

Typically, if N is constant and small, we can simply use an `array` to store keys in the same bucket. If N is variable or large, we might need to use `height-balanced binary search tree` instead.

### Exercise

---

By now, you should be able to implement a basic hash table. We
provide the exercise for you to implement a hash set and a hash map. `Read the requirement, determine your hash function and solve the collision if needed.`

> *If you are not familiar with the concepts of hash set and hash
> map, you can go back to the introduction part to find out the answer.*

`Insertion` and `search` are two basic operations in a hash table.

Besides, there are operations that are based on these two operations. For example, when we `remove an element`, we will first search the element and then remove the element from the corresponding position if the element exists.


**The Principle of Hash Table**

---

As we mentioned in the introduction,  `Hash Table` is a data structure which organizes data using `hash functions` in order to support `quick insertion and search`. In this article, we will take a look at the principle of the hash table.

### The Principle of Hash Table

---

The key idea of Hash Table is to use a hash function to `map keys to buckets`. To be more specific,

1. When we insert a new key, the hash function will decide which
   bucket the key should be assigned and the key will be stored in the
   corresponding bucket;
2. When we want to search for a key, the hash table will use the `same` hash function to find the corresponding bucket and search only in the specific bucket.

### An Example

---

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/20/screen-shot-2018-02-19-at-183537.png)

In the example, we use `y = x % 5` as our hash function. Let's go through the insertion and search strategies using this example:

1. Insertion: we parse the keys through the hash function to map them into the corresponding bucket.
   * e.g. 1987 is assigned to bucket 2 while 24 is assigned to bucket 4.
2. Search: we parse the keys through the same hash function and search only in the specific bucket.
   * e.g. if we search for 1987, we will use the same hash function to
     map 1987 to 2. So we search in bucket 2 and we successfully find out
     1987 in that bucket.
   * e.g. if we search for 23, will map 23 to 3 and search in bucket 3.
     And We find out that 23 is not in bucket 3 which means 23 is not in the
     hash table.

**Design Hash Table - Solution**

---

Here are C++ and Java solutions for your reference. In our solution, we use an `array` to represent the hash set. Each element in the array is a bucket. And in each bucket, we use the `array list` (or `vector` in C++) to store all the values.

### More

---

Let's take a look at the operation `"remove"`. After we find out the position of the element, we need to `remove the element from the array list`.

Let's assume that we are going to remove the `ith` element and the size of the array list is `n`.

The strategy used in the built-in function is to move all the
elements after ith element one position forward. That is to say, you
have to move `n - ``i` times. So the time complexity to remove an element from an array list will be `O(n)`.

> Consider different value of i. In average, we will move ((n - 1) + (n - 2) + ... + 1 + 0) / n = (n - 1) / 2 times.

Hopefully, there are two solutions to reduce the time complexity from `O(n)` to `O(1)`.

**1. Swap**

There is a tricky strategy we can use. First, `swap the element`
 which we want to remove with the last element in the bucket. Then
remove the last element. By this way, we successfully remove the element
 in `O(1)` time complexity.

**2. Linked List**

Another way to achieve this goal is to use a `linked list` instead of an array list. By this way, we can remove the element in O(1) time complexity `without modifying the order` in the list.

**Hash Set**

---

The `hash set` is one of the implementations of a `set` which is a data structure to store `no repeated values`.

We provide an example of using the hash set in Java, C++ and Python.
If you are not familiar with the usage of the hash set, it will be
helpful to go through the example.

# 1. initialize the hash set

hashset = set()

# 2. add a new key

hashset.add(3)
hashset.add(2)
hashset.add(1)

# 3. remove a key

hashset.remove(2)

# 4. check if the key is in the hash set

if (2 not in hashset):
    print("Key 2 is not in the hash set.")

# 5. get the size of the hash set

print("Size of hashset is:", len(hashset))

# 6. iterate the hash set

for x in hashset:
    print(x, end=" ")
print("are in the hash set.")

# 7. clear the hash set

hashset.clear()
print("Size of hashset:", len(hashset))

**Find Duplicates By Hash Set**

---

As we know, it is easy and effective to insert a new value and check if a value is in a hash set or not.

Therefore, typically, a hash set is used to `check if a value has ever appeared or not`.

**Hash Map - Usage**

---

The `hash map` is one of the implementations of a `map` which is used to store `(key, value)` pairs.

We provide an example of using the hash map in Java, C++ and Python.
If you are not familiar with the usage of the hash map, it will be
helpful to go through the example.

# 1. initialize a hash map

hashmap = {0 : 0, 2 : 3}

# 2. insert a new (key, value) pair or update the value of existed key

hashmap[1] = 1
hashmap[1] = 2

# 3. get the value of a key

print("The value of key 1 is: " + str(hashmap[1]))

# 4. delete a key

del hashmap[2]

# 5. check if a key is in the hash map

if 2 not in hashmap:
    print("Key 2 is not in the hash map.")

# 6. both key and value can have different type in a hash map

hashmap["pi"] = 3.1415

# 7. get the size of the hash map

print("The size of hash map is: " + str(len(hashmap)))

# 8. iterate the hash map

for key in hashmap:
    print("(" + str(key) + "," + str(hashmap[key]) + ")", end=" ")
print("are in the hash map.")

# 9. get all keys in hash map

print(hashmap.keys())

# 10. clear the hash map

hashmap.clear();
print("The size of hash map is: " + str(len(hashmap)))

**Scenario I - Provide More Information**[Report Issue](https://github.com/LeetCode-Feedback/LeetCode-Feedback/issues)

---

The first scenario to use a hash map is that we `need more information` rather than only the key. Then we can `build a mapping relationship between key and information` by hash map.

### An Example

---

Let's look at an example:

> Given an array of integers, return **indices** of the two numbers such that they add up to a specific target.

In this example, if we only want to return true if there is a
solution, we can use a hash set to store all the values when we iterate
the array and check if `target - current_value` is in the hash set or not.

However, we are asked to `return more information` which
means we not only care about the value but also care about the index. We
 need to store not only the number as the key but also the index as the
value. Therefore, we should use a hash map rather than a hash set.

### What's More

---

In some cases, we need more information not just to return more information but also to `help us with our decisions`.

In the previous examples, when we meet a duplicated key, we will
return the corresponding information immediately. But sometimes, we
might want to check if the value of the key is acceptable first.

**Scenario II - Aggregate by Key**[Report Issue](https://github.com/LeetCode-Feedback/LeetCode-Feedback/issues)

---

Another frequent scenario is to `aggregate all the information by key`. We can also use a hash map to achieve this goal.

### An Example

---

Here is an example:

> Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

A simple way to solve this problem is to `count the occurrence` of each character first. And then go through the results to find out the first unique character.

Therefore, we can maintain a hashmap whose key is the character while
 the value is a counter for the corresponding character. Each time when
we iterate a character, we just add the corresponding value by 1.

### What's more

---

The key to solving this kind of problem is to `decide your strategy when you encounter an existing key`.

In the example above, our strategy is to count the occurrence.
Sometimes, we might sum all the values up. And sometimes, we might
replace the original value with the newest one. The strategy depends on
the problem and practice will help you make a right decision.

**Design the Key**

---

In
 the previous problems, the choice of key is comparatively
straightforward. Unfortunately, sometimes you have to think it over to `design a suitable key` when using a hash table.

### An Example

---

Let's look at an example:

> Given an array of strings, group anagrams together.

As we know, a hash map can perform really well in grouping
information by key. But we cannot use the original string as
key directly. We have to design a proper key to present the type of
anagrams. For instance, there are two strings "eat" and "ate" which
should be in the same group. While "eat" and "act" should not be grouped
 together.

### Solution

---

Actually, `designing a key` is to `build a mapping relationship by yourself` between the original information and the actual key used by hash map. When you design a key, you need to guarantee that:

> 1. All values belong to the same group will be mapped in the same group.
> 2. Values which needed to be separated into different groups will not be mapped into the same group.

This process is similar to design a hash function, but here is an essential difference. `A hash function satisfies the first rule but might not satisfy the second one.` But your mapping function should satisfy both of them.

In the example above, our mapping strategy can be: sort the string
and use the sorted string as the key. That is to say, both "eat" and
"ate" will be mapped to "aet".

The mapping strategy can be really `tricky` sometimes. We provide some exercise for you in this chapter and will give a summary after that.

**Design the Key - Summary**

---

Here are some takeaways about how to design the key for you.

1. When the order of each element in the string/array doesn't matter, you can use the `sorted string/array` as the key.![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/28/screen-shot-2018-02-28-at-144518.png)
2. If you only care about the offset of each value, usually the offset from the first value, you can use the `offset` as the key.![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/28/screen-shot-2018-02-28-at-144738.png)
3. In a tree, you might want to directly use the `TreeNode` as key sometimes. But in most cases, the `serialization of the subtree` might be a better idea.![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/28/screen-shot-2018-02-28-at-143858.png)
4. In a matrix, you might want to use `the row index` or `the column index` as key.
5. In a Sudoku, you can combine the row index and the column index to identify which `block` this element belongs to.![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/28/screen-shot-2018-02-28-at-145454.png)
6. Sometimes, in a matrix, you might want to aggregate the values in the same `diagonal line`.  ![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/28/screen-shot-2018-02-28-at-140029.png)

# Maps and Hashing

When we're talking about hash tables, we can define a "load factor":

```
Load Factor = Number of Entries / Number of Buckets
```

The purpose of a load factor is to give us a sense of
how "full" a hash table is. For example, if we're trying to store 10
values in a hash table with 1000 buckets, the load factor would be 0.01,
 and the majority of buckets in the table will be empty. We end up
wasting memory by having so many empty buckets, so we may want to
rehash, or come up with a new hash function with less buckets. We can
use our load factor as an indicator for when to rehash—as the load
factor approaches 0, the more empty, or sparse, our hash table is.

On the flip side, the closer our load factor is to 1 (meaning the
number of values equals the number of buckets), the better it would be
for us to rehash and add more buckets. Any table with a load value
greater than 1 is guaranteed to have collisions.


#### References

a. Hash Functions: https://youtu.be/kCPFfHx_LgQ

b. Collisions: https://youtu.be/BUaWIjZ_ToY

c. Hash Maps: https://youtu.be/A-ahUVi8pYQ

https://www.w3schools.com/python/python_dictionaries.asp

https://docs.python.org/3/library/collections.html

https://www.geeksforgeeks.org/python-dictionary/

https://realpython.com/python-dicts/
