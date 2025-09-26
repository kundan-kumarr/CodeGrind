
# Control Flow

* Conditional Statements
* Boolean Expressions
* For and While Loops
* Break and Continue
* Zip and Enumerate
* List Comprehensions


Python has two kinds of loops - `for` loops and `while` loops

# For Loops

A `for` loop is used to "iterate", or do something repeatedly, over an  **iterable** .

An **iterable** is an object that can return one of its elements at a time. This can include sequence types, such as strings, lists, and tuples, as well as non-sequence types, such as dictionaries and files.


```
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for city in cities:
    print(city)
print("Done!")
```


### Using the `range()` Function with `for` Loops

`range()` is a built-in function used to create an iterable sequence of numbers. You will frequently use `range()` with a `for`  loop to repeat an action a certain number of times. Any variable can be used to iterate through the numbers, but Python programmers conventionally use `i`, as in this example:

```
for i in range(3):
    print("Hello!")
```


#### `range(start=0, stop, step=1)`

The `range()` function takes three integer arguments, the first and third of which are optional:

* The 'start' argument is the first number of the sequence. If unspecified, 'start' defaults to 0.
* The 'stop' argument is 1 more than the last number of the sequence. This argument must be specified.
* The 'step' argument is the difference between each number in the sequence. If unspecified, 'step' defaults to 1.

### Creating and Modifying Lists

In addition to extracting information from lists, as we did in the
first example above, you can also create and modify lists with `for` loops. You can **create** a list by appending to a new list at each iteration of the `for` loop like this:

```
# Creating a new list
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())
```

**Modifying** a list is a bit more involved, and requires the use of the `range()` function.

We can use the `range()` function to generate the indices for each value in the `cities` list. This lets us access the elements of the list with `cities[index]` so that we can modify the values in the `cities` list in place.

```
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

for index in range(len(cities)):
    cities[index] = cities[index].title()
```
