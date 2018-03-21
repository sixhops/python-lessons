# Python Recap So Far

Before we go further into a little more complex Python, let's recap what we've seen.

### Printing
- `print` means "Display on the screen"
- `print "Hello"` will display `Hello` on the screen.
- ***New Info:*** Sometimes, when people explain code, they write `=>` after a `print` statement to show what will be printed. This code won't run in Python, but it's useful in tutorials.
  - This is normal code, that will print "Hello" to the screen:
  `print "Hello"`
  - This code will not run if you put it in repl.it:
  `print "Hello"   => Hello`
  - The `=>` is here in a tutorial to tell you that if you run the code above the `=>` (here, `print "Hello"`), what will be printed is "Hello"

### Variable Basics
- Variables are used to store data into the memory of the computer so that it can be referenced later.
- Use camelCase: `myNumber`, `thisVariableIsAwesome`.
- Strings should be surrounded by quotes: `greeting = "Hello"`.
- Numbers should *not* be surrounded by quotes: `number = 7`.

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
print favoriteMovie # Will print Moana.
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
- `+` : Addition
- `-` : Subtraction
- `*` : Multiplication
- `/` : Division
- `%` : Modulus (the remainder after division; `6 % 2` equals `0` and `7 % 2` equals `1`)

### Concatenation
- Using the + operator with two strings literally puts them next to each other instead of evaluating their total.
- This is called "string concatenation."
```python
name = "Doc"
lastName = "Brown"
name = name + " " + lastName
print name # This will be "Doc Brown"
```
