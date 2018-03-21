# Python Cheat Sheet

Here are some notes on what's been covered in the Python portion of this pre-work. Feel free to copy this information and leverage it to make your own cheat sheet.

- Variables
- Math
- Strings
- Booleans
- Conditionals (`if`/`elif`/`else`)
- Lists
- Loops
- Tuples and Dictionaries
- Functions
- Sets

### Variable Basics
- Variables are used to store data in the memory of the computer so that it can be referenced later.
- Use camelCase: `myNumber`, `thisVariableIsAwesome`.
- Strings should be surrounded by quotes: `greeting = "Hello"`.
- Numbers should not be surrounded by quotes: `number = 7`.

### Variable Assignments

- A variable is assigned a value using the `=` operator. First, the expression to the right of the `=` is evaluated. Then, this value is assigned to the variable to the left of the `=`.

```python
favoriteMovie = "Jaws"
```

- To use the value stored by a variable, simply include that variable in an expression. An expression containing variables will evaluate just like one without variables, except that the variables will themselves be evaluated as part of the expression.

- When a variable is reassigned, it retains no knowledge of any prior values it may have held.

```python
favoriteMovie = "Jaws"
favoriteMovie = "Moana"
print favoriteMovie # This will print Moana.
```

- A variable may be reassigned "in place" using an expression, such as `myVariable = myVariable + 1` (or its shorthand, `myVariable += 1`).

### Assignment Operators in Numerical Variables

- The `=` operator assigns a value to a variable.
  - `x = 4`
- The `+=` operator adds a value to an existing numerical variable.
  - `x += 5 # x is now 9.`
- The `-=` operator subtracts a value from an existing numerical variable.
  - `x -= 2 # x is now 7.`

### Common Arithmetic Operators
- `+` - Addition
- `-` - Subtraction
- `*` - Multiplication
- `/` - Division
- `%` - Modulus

### Strings

A *string* is a complete list of characters, such as a word. "Apple" is a string.

### Concatenation
Using the `+` operator with two strings literally puts them next to each other instead of evaluating their total. This is called "string concatenation."
```python
name = "Doc"
lastName = "Brown"
name = name + " " + lastName
print name # This will print "Doc Brown".
```

### Booleans

Comparisons can be made using `<`, `>`, `<=`, and `>=`, and work for both strings and numbers.

```python
13 >= 13  # result is True because 13 is greater than or equal to 13.
"d" < "a" # result is False because "d" is *not* less than "a".
```

Equality (`==`) determines if two things are the same. It will only evaluate `True` if both sides are completely identical in data type and value (i.e., a string and a number will never be equal because they are different types).

Inequality (`!=`) is essentially the reverse of the equality operator: It will only evaluate `True` if both sides are *not* completely identical in data type and value.  

In Python, there are other values that will evaluate `True` or `False` if they are used in a comparison. These are called "truthy" and "falsey" values because they are not explicitly `True` or `False` but they implicitly behave the same way. For instance, `0` and `""` are both "falsey," but `2` and `"hi"` are "truthy."

`or` checks if **either** comparison is `True`.

```python
False or True # This will be True, because one of the sides is True.
False or False # This will be False, because neither side is True.
```

`and` checks if **both** comparisons are `True`.

```python
True and True # This would be True, because both sides are True.
True and False # This would be False, because both sides are not True.
```

### Conditionals: if/else

* `if` statements let us control the flow of execution in our scripts.
* We use conditional operators in our `if` statements to perform the comparisons.
* The `else` statement lets us define what to do when our primary conditional test is false.
* The `elif` statement lets us add multiple comparisons to our `if` blocks.

For instance:

```python
if temperature > 80:
  print "It's too hot!"
elif temperature <= 80 and temperature > 60:
  print "It's just right!"
elif temperature <= 60 and temperature > 40:
  print "It's pretty cold!"
else:
  print "It's freezing!"
```

### Lists

A *list* is a collection of elements; for example, a collection of *strings* or *numbers*.

- A list is contained within square brackets `[]` like this:
```python
colors = ["red", "yellow", "green"]
```
- An *index* describes the location of an element. The first element in a list is at *index* `0`, and it counts from there. We can access an element inside a list at index `1` (the second element) like this:
```python
print colors[1]  # this will print "yellow"
```

You can check the length of a list like this:

```python
print len(colors) # this will print 3.
```

You can add an element to the end of a list like this:

```python
colors.append("blue")

print colors # this will print ["red", "yellow", "green", "blue"]
```

You can add an element somewhere else like this:

```python
colors.insert(1, "blue")

print colors # this will print ["red", "blue", "yellow", "green"]
```

And you can remove an element like this:

```python
colors.pop(0)

print colors
	=> ["yellow", "green"]
```

### Loops

A common and extremely useful type of loop is the `for` loop. It gets its name from the fact that it loops (or iterates) **for** a specific number of times.

`for` loops look like this in Python:

```python
names = ["Tom", "Deborah", "Murray", "Axel"]

for name in names:
  print name
```

If we want to do something in a loop a specific number of times, we can use `range` like this:

```python
for i in range(10):
  print i
```

And when we need to write a loop that will run an unknown number of times, we can use a `while` loop like this:

```python
a = 0
while a < 10:
  print a
  a += 1
```

### Tuples and Dictionaries

A **tuple** is just a list with elements you cannot change.

This is how you make a tuple:

```python
tup1 = ("red", "orange", "yellow", "green", "blue", "violet")
```

And this is how you select an element:

```python
print tup1[0]    # outputs "red"
```

A **dictionary** is a set of **key:value pairs**. A key, like an index, is a direct reference to that element in the dictionary; the key is used to find the associated value.

This is how you make a dictionary:

```python
friendzips = {98107: "Lauren", 92211: "Markus", 90210: "Brenda"}
```

And this is how you access a *value* by a *key*:

```python
print friendzips[92211] # this will print "Markus"
```

### Functions

A **function** is a reusable piece of code. If we want to run the same set of code over and over again, we can define a function like this:

```python
def printOrder():
  print "Thank you for your order."
```

And then run it like this:

```python
print "You've purchased a Hanging Planter."
printOrder() # This will print "Thank you for your order."

print "You've purchased a Shell Mirror."
printOrder() # So will this.

print "You've purchased a Modern Shag Rug."
printOrder() # And this!
```

You can make this even neater with **parameters**:


```Python
def printOrder(product):
  print "Thank you for ordering the ", product, "."

printOrder("Hanging Planter")
printOrder("Shell Mirror")
printOrder("Modern Shag Rug")
```

Here, the **parameter** called `product` is in the parentheses to tell the function that we are going to provide it with a `product`.

And the items during the **function call** or **execution**, such as "Hanging Planter," are **arguments**.

If you want to use or save the result of a function somewhere else, you need to use **return** like this:

```python
def addTwo(number):
 total = number + 2
 return total

finalVar = addTwo(3)
print finalVar
```

### Sets

A **set** is a **list** where all of the *elements* must be unique. This can be very useful when trying to remove duplicate elements from a **list** like this:

```python
set(["red", "yellow", "green", "red"])
	=> {"green", "yellow", "red"}
```
