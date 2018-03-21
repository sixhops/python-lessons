# Strings

### Learning Objectives
*After this lesson, you will be able to:*
- Create variables that hold strings.
- Concatenate strings.
- Print complex structures.

## Introducing Strings

A *string* is a complete list of characters, such as a word. "Apple" is a string.
- A character is anything on your keyboard, such as a letter or a number.
- The "Apple" string is five characters long: a, p, p, l, e.

A space counts as a character, too (it's on the keyboard). For example, "Marty McFly" is a string.

Because a variable is just a box, it can also hold strings. You tell Python that your variable will hold a string using quotation marks. Declare these variables below in [repl.it](https://repl.it/languages/python) and print them. Don't just copy and paste this code! You'll be doing a lot of programming, and if you practice typing variable declarations out, you'll get faster every time.

```python
name = "Doc Brown"
age = 65
location = "Future Town"
```

Python defines anything in quotes as a string. For example:

```python
name = "Doc Brown" # This is a string.
age = 65 # This is a number.
ageAsString = "65" # Because this is in quotes, this is a string.
```

It's important to note that you cannot do math on strings! Even if what's inside the quotations is a number, Python will interpret it as a word. Try this out in [repl.it](https://repl.it/@SuperTernary/cybersec-strings-intro2):

```python
age = "65" # Because of the quotes, this is a string.
newAge = age - 15 # Let's try to do math on it.
print newAge
```

Instead of printing `50`, Python will throw an error. It sees `age` as a string, not a number. Make sure that, when you want a numerical value, you **do not** use quotes.


## String Concatenation

Now, let's see how you can use string values (textual information) in Python.

When given string values, the `+` operator actually behaves differently — it concatenates, or combines, two strings together to make one big string. Using the `+` operator to combine the two strings together literally puts them next to each other instead of evaluating their total.

This is called concatenation (when strings are glued together). Here's an example of concatenation. Try this in [repl.it](https://repl.it/@SuperTernary/cybersec-strings-concatenation).

```python
firstName = "Doc"
lastName = "Brown"
fullName = firstName + lastName
print fullName
```

Python put the two strings together, but do you notice anything wrong? There is no space between the two words! This is because we didn't add the spaces in ourselves. It's just one of many reasons why we have to carefully watch our spacing and grammar. Try it.

To fix this, we'll have to add in the space ourselves:

```python
firstName = "Doc"
lastName = "Brown"
fullName = firstName + " " + lastName
print fullName
```

Now it prints correctly.

You can also `print` directly; you don't necessarily need the last variable. To print strings next to each other, you separate them with a comma. Then, Python will add the space for you. Try it!

```python
firstName = "Doc"
lastName = "Brown"
print firstName, lastName
```

This isn't concatenating variables, but it's useful to know!

Python will always concatenate strings via the `+` sign — remember, anything in quotes is a string. Look at the code below. You can run it in [repl.it](https://repl.it/@SuperTernary/cybersec-strings-concatenation2).

```python
# Using math on numerical variables:
firstNumber = 1
secondNumber = 1
fullNumber = firstNumber + secondNumber
print fullNumber # This will print 2.

# And, printing without the last variable:
firstNumber = 1
secondNumber = 1
print firstNumber + secondNumber # This will print 2
# you use the + symbol here because it's math.

# Using math on string variables:
firstNumber = "1"
secondNumber = "1"
fullNumber = firstNumber + secondNumber
print fullNumber # This will print "11", because it's concatenating a string.

# And, printing without the last variable:
firstNumber = "1"
secondNumber = "1"
print firstNumber, secondNumber # This will print "1 1" because it's
          # concatenating a string.
```

You can concatenate (which is frequently shortened to "concat") any strings together — as many strings as you'd like. For example, add this to your repl.it:

```python
firstName = "Doc"
lastName = "Brown"
fullName = firstName + " " + lastName
print fullName # This will be "Doc Brown"

docAge = "63"
totalDoc = fullName + " " + docAge # We don't need the space,
# but it makes it easier to read.
print totalDoc # This will print "Doc Brown 63."
```

## Reassigning a String to Itself

Reassigning a variable using itself can be done with any variable, not just numerical ones. For example:

```python
name = "Doc"
lastName = "Brown"
name = name + " " + lastName
print name # This will be "Doc Brown"
```

## Conclusion

Variables come in all different types. We've covered strings and numbers so far:

```python
string = "This is a String"
number = 51
```

One last thing: printing. As you saw, you can use a comma to separate strings when printing them out. You can also use a comma to separate any variables or strings. Try this in [repl.it](https://repl.it/@SuperTernary/cybersec-strings-conclusion):

```python
name = "Doc"
lastName = "Brown"
age = 63
print name, age
print name, " ", age
print name, 5, " ", name
```
Feel free to go back and review the material in this lesson as necessary. Also consider exploring some of the resources in the Additional Readings section that follows.
### Additional Reading
- [Python-Strings](https://www.tutorialspoint.com/python/python_strings.htm)
- [String Concatenation and Formatting](http://www.pythonforbeginners.com/concatenation/string-concatenation-and-formatting-in-python)
- [String Concatenation and Formatting - Video](https://www.youtube.com/watch?v=jA5LW3bR0Us)
