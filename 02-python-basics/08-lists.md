# Lists

### Learning Objectives
*After this lesson, you will be able to:*
- Create variables that hold lists.
- Print out a specific element in a list.
- Determine the length of a list.
- Add an element to a list.
- Remove an element from a list.

## Introducing Lists

A *list* is a collection of elements; for example, a collection of *strings* or *numbers*.
- A list is contained within square brackets `[]` like this:
```python
colors = ["red", "yellow", "green"]
```
- An *index* describes the location of an element. The first element in a list is at *index* `0`, and it counts from there. We can access an element inside of a list at index `1` (the second element) like this:
```python
print colors[1]
	=> yellow
```

Because a variable is just a box that can hold information, it can also hold lists. Python knows that your variable will hold a list if it begins and ends with square brackets. For example, let's say we are working for a company with three locations, and we want to store all three city *strings*: `"New York"`, `"London"`, and `"Tokyo"`.

We could do that like this:

```python
cities = ["New York", "London", "Tokyo"]

print cities[0]
	=> New York
```

## You Do: List Practice

Perform the following exercises in [repl.it](https://repl.it/languages/python):

1) Create a **list** with the names `"Holly"`, `"Juan"`, and `"Ming"`.

2) Print the third name.

3) Create a **list** with the numbers `2`,`4`, `6`, and `8`.

4) Print the first number.

### Determining List Length

Just as with *strings*, we can determine how long a *list* is (i.e., how many elements it has) using the `len()` method like so:

```python
colors = ["red", "yellow", "green"]

print len(colors)
	=> 3
```

## Mutability and Lists

Earlier, we mentioned *mutability*. Mutability refers to a variable's ability to be changed. Lists are *mutable*, so we can change the data inside of them. Specifically, we can add an element to a list or remove one from it.

### Adding an Element to a List

Forgot to add something to that list of colors? No problem; you can use the `.append()` method like so:

```python
colors = ["red", "yellow", "green"]

colors.append("blue")

print colors
	=> ["red", "yellow", "green", "blue"]
```

The `.append()` method will add an element to the end of the list. However, what happens if we want to add something somewhere else? We can use the `.insert()` method, which specifies where (i.e., to which index) we want to add the element:

```python
colors = ["red", "yellow", "green"]

colors.insert(1, "blue")

print colors
	=> ["red", "blue", "yellow", "green"]
```

### Removing an Element from a List

What if we have too many colors? We can easily remove an element from a list using the `.pop()` command like so:

```python
colors = ["red", "yellow", "green"]

colors.pop()

print colors
	=> ["red", "yellow"]
```

By default, the `.pop()` method will remove an element from the end of the list. However, what happens if we want to remove something from somewhere else? We just need to specify where (i.e., from which index) we want to remove the element inside the parentheses after `pop`:

```python
colors = ["red", "yellow", "green"]

colors.pop(0)

print colors
	=> ["yellow", "green"]
```

### A Quick Warning about Adding/Removing Elements

All of the methods above *mutate*, i.e., change the array in place; they don't give you the *mutated*, or changed, array back.

When adding or removing elements from an array, _don't do_ the following:

```python
colors = ["red", "yellow", "green"]

print colors.append("blue")
	=>None
```

When adding or removing elements from an array, do the following:

```python
colors = ["red", "yellow", "green"]

colors.append("blue")

print colors
	=> ["red", "yellow", "green", "blue"]
```

## You Do: Mutating Lists Practice

Try the following exercises in [repl.it](https://repl.it/languages/python). After each step, run your code to print the list, so you know you did the step correctly.

1) Save a **list** with the names `"Holly"`, `"Juan"`, and `"Ming"` into a variable called `names`.

2) `append` `"Steve"` to the end of your `names` **list**.

3) `print` the *mutated* `names` **list**.

4) `print` the length of the `names` **list**.

5) Save a **list** with the numbers `2`, `4`, `6`, and `8` into a variable called `numbers`.

6) `insert` the number `5` at *index* 2 in your `numbers` **list**.

7) `print` the *mutated* `numbers` **list**.

8) `print` the length of the `numbers` **list**.

9) `pop` the last name in the `names` **list** off.

10) `print` the *mutated* `names` **list**.

11) `print` the length of the `names` **list**.

12) `pop` the second number in the `numbers` **list** off.

13) `print` the *mutated* `numbers` **list**.

14) `print` the length of the `numbers` **list**.

## Conclusion
- In this lesson we covered how to create variables that hold lists, how to print out a specific element in a list, how to determine the length of a list and lastly, how to add and remove elements from a list. Feel free to review the materials in this lesson as needed. Also — to deepen your understanding — considering exploring some of the resources in the Additional Readings section that follows.
### Additional Readings
- [Python Lists - Khan Academy Video](https://www.youtube.com/watch?v=zEyEC34MY1A)
- [Google For Education: Python Lists](https://developers.google.com/edu/python/lists)
- [Python-Lists](https://www.tutorialspoint.com/python/python_lists.htm)
