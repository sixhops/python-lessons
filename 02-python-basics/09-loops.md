# Loops

### Learning Objectives
*After this lesson, you will be able to:*

- Understand the use of loops in programming.
- Explain a `for` loop and its best use cases.
- Explain a `while` loop and its best use cases.
- Use loops to solve repetitive tasks in Python.

## Introducing Loops

One of the most powerful things that programming can do for you is automatically perform repetitive tasks.
In the tiny scripts we've been writing, printing out every variable has not been much of an issue. But with lists in the game now, things can get a bit more challenging.

This situation isn't so bad:

```python
visibleColors = ["red", "orange", "yellow", "green", "blue", "violet"]
print visibleColors[0]
print visibleColors[1]
print visibleColors[2]
print visibleColors[3]
print visibleColors[4]
print visibleColors[5]
```

But, what if we had a list with 283,000 items in it? We can't write one line for each element. We
need a way to write the `print` statement once and have it run for every element in the list. Python
enables us to do this with loops.

Probably the most common use of loops is iterating through collections of data, such as lists. You just learned
how to create lists, store data in them, and access that data. Now, we will show you how to use loops to
easily process and manipulate the items in collections.

Loops are at the heart of most user interfaces. Most applications are simply running in a loop that
constantly checks to see if the user has done anything new. They loop dutifully away until the user clicks
the mouse or enters some text into a field. Then, the loop pauses, handles the user's input, and
resumes looping, waiting for the next user action.

Python provides two loop types: The `for` loop, which is great for looping over collections,
and the `while` loop, which is great for when your loop could run an indeterminate number of times.

## The `for` Loop

A common and extremely useful type of loop is the `for` loop. `for` loops appear in several computer programming languages and get their name from the fact that they loop (or iterate) **for** a specific number of times: once **for** each item in a list, or once **for** each number in a range.

The `for` loop is perfect for when you have a specific collection of items — each of which must be processed once — or for when you know that you must execute a set of instructions a specific number of times.

Let's take a look at the syntax:

```python
names = ["Tom", "Deborah", "Murray", "Axel"]

for name in names:
  print name
```

You can run that in this repl.it [here](https://repl.it/@SuperTernary/cybersec-for-names).

Line by line, this code does the following:
* Creates a new list containing some name strings.
* Begins the `for` loop. We loop once for each "name" in the list (`names`).
* Prints the current name inside the loop.

The `for` loop always follows this form:

```python
for item in collection:
  # Do something with item
```

That is our template. When we write a `for` loop we do the following:
* We replace `item` with a meaningful name for the items in the collection.
  * We use this name as the name of the item within our loop.
* We replace `collection` with the name of our list (or other collection).
* Indented inside the loop, we write the code to be run for each item.
* Python will start with the first item and automatically stop after it loops with the last item.

### Indentation in Python

Unlike other languages, such as JavaScript, C#, or Java, Python does not use curly braces to
denote the beginning or end of a code block. It uses the colon at the end of a line (`:`) to start the block,
and every line that is indented to the same level after that colon is part of that code block. Once the lines
cease to be indented after the colon, the block has ended. This means that, if you have three lines of code that
you want to execute on each loop iteration, each must be indented one level underneath your `for` line:

```python
for name in ["Tom", "Deborah", "Murray", "Axel"]:
  print "Now appearing in the Refreshment Room..."  # in the loop
  print name                                        # in the loop
  print "THUNDEROUS APPLAUSE!"                      # in the loop
```

Each name is met with `"THUNDEROUS APPLAUSE!"` because that line, and the two above it, are indented to be in
the body of the `for` loop. Next, let's save all of the applause until the very end, taking that
line out of the loop by un-indenting it:

```python
for name in ["Tom", "Deborah", "Murray", "Axel"]:
  print "Now appearing in the Refreshment Room..."  # in the loop
  print name                                        # in the loop
print "THUNDEROUS APPLAUSE!"                      # OUTSIDE the loop
```

Now, if you run that, the loop prints the welcome and the name of each person in the list. Then, the loop ends (stops being indented), and finally `"THUNDEROUS APPLAUSE!"` prints one time.

## Codealong: Write a Loop To Greet People On Your Guest List

Use this [blank repl.it](https://repl.it/languages/python) workspace to follow along with the code below.

You are writing a greeting script that will automatically give a personalized greeting to every guest attending
your event. You are provided a list of names. Let's write a loop that will extend a greeting to each person on
the list:

```python
guestList = ["Fred", "Sally", "Chester", "Franklin", "Merwyn", "Rebecca", "Denise"]
```

That's the list. We can see that it is named `guestList`, so we already know what the second half of our
`for` loop line will look like. Now, we should select a meaningful name to serve as the item variable name
inside our loop. How about `guest`?


```python
guestList = ["Fred", "Sally", "Chester", "Franklin", "Merwyn", "Rebecca", "Denise"]

for guest in guestList:
  # Print out a greeting in here
```

Now, when we write the code inside our loop, we can use `guest` to represent the name being pulled from the
list. Let's add a couple of lines to print a greeting:

```python
guestList = ["Fred", "Sally", "Chester", "Franklin", "Merwyn", "Rebecca", "Denise"]

for guest in guestList:
  # Print out a greeting in here
  print "Hello, " + guest + "."
  print "Welcome to the party!"
```

Fantastic! Now each guest is greeted by their name and welcomed to the party. Those two `print` lines
are executed on every iteration because both are indented to be in the `for` loop's code block.
Think of the indented block as a unit of instructions executed as a group each time the
loop runs.

Can you think of another kind of collection for which we could use a `for` loop? You may not realize it, but
a string is a __collection__ of characters. Just so you can see that a `for` loop has the same syntax for
any collection, let's add the following code below what we've just written:

```python
myString = "Hello, world!"

for character in myString:
  print character
```

When we run this, we see that each character in the string `"Hello, world!"` is printed on its own line.

## Codealong: Write a Loop That Iterates Over a Range

Use this [blank repl.it](https://repl.it/languages/python) workspace to follow along with the code below..

Whenever we have a collection, such as a list or string, and we want to iterate over each item it contains,
we should use a `for` loop. Python has internal logic for determining exactly how many times the loop should
run based on the length of the collection.
- But, what if we want to do something in a loop a specific number of times, but we don't have a collection to start with? Maybe we are initializing a new collection and we need to add a specific number of items to it. In this case, we can have the `for` loop iterate over a range of numbers.

We do this using Python's built-in `range()` function:

```python
for i in range(10):
  print i
```

This line says, "For every number, `i`, in the range from zero to nine, print `i`." In this case, `i` represents the item in the collection on which we are currently iterating. We said `range(10)`, which creates a range for the loop from zero to nine. Then, we print the current value of `i`. Run this, and you'll see each number printed on its own line. Let's use this form of the `for` loop to add some numbers to a list:

```python
squares = []

for i in range(5):
  sqr = i ** 2
  squares.append(sqr)

print squares
```

Here, we create an empty list named `squares`. We then set up a `for` loop to iterate over `range(5)`, which is
the numbers zero through four. Next, we raise each number to the second power and store the result in `sqr`. This
result is appended into the list. Once the loop is done, we print the list and see that it contains each of the
values of `i` squared.

This way of writing the `for` loop is especially useful if you want to **modify** items in the collection instead of just reading them and printing them out. Let's use this to change the values in a list of strings. All of the strings in our list are mixed case, which is annoying. First, let's convert them all to uppercase strings for ease of processing:


```python
names = ["Flint", "John Silver", "Billy Bones", "Israel Hands"]

for i in range(len(names)):
  names[i] = names[i].upper()

print names
```

We create a list of names with mixed uppercase and lowercase letters. Then, we set our `for` loop to start `i` at zero and loop through the range determined by the length of the `len(names)` list. By doing so, we can use `i` as the index for our list. Using this index, we access the location of each name and then set that name to its uppercase equivalent. Lastly, we print the list to see the new values contained therein.

## The `while` Loop

We won't always have the luxury of a collection of discrete data items for controlling our loop. Frequently, we will need to write a loop that will run an unknown number of times. This is what the `while` loop is for. It's
another loop construct that will continue to iterate __while a given condition is true__. These loops are quite
useful for data sets of unknown sizes, or for when we need to loop until some value changes.

`While` loops present a potential "gotcha" in programming: the infinite loop. Because the `while` loop only terminates when a condition turns to false, it's possible to write the loop in such a way that it never terminates. This creates a serious bug in your code where the loop never, ever returns control to the app, and it will freeze indefinitely. The way to avoid this is to __always__ remember to update your conditional variable inside your loop block.

Let's look at the syntax:

```python
a = 0
while a < 10:
  print a
  a += 1
```

You can run that [here](https://repl.it/@SuperTernary/cybersec-while-intro).

Outside of our `while` loop, we create the variable `a`, which we'll use as our conditional. We then start
our loop. We say to loop "while `a` is less than 10." Then, in the loop, we print `a` and add one to its value.
Once the value of `a` reaches 10, the loop condition evaluates to false and the loop finishes.

## Codealong: Filling a Glass of Water, Making a Guessing Game

Use this [blank repl.it](https://repl.it/languages/python) workspace for this challenge.

Can you think of the mental process you follow when pouring water into a glass? You start with an empty
glass and begin adding water to it, right? While you are adding the water, you must constantly check
to see if the glass has reached its maximum capacity. If it has, you then stop pouring.
Otherwise, you continue adding water. Let's see how that would work as a `while` loop:

```python
# Fill our glass
glass = 0
glassCapacity = 12

while glass <= glassCapacity:
  glass += 1  # Here is where we add more water
```

We declare our `glass` variable and set it to `0` water, currently. Then, we declare our glass' capacity and
set it to `12` units. Next, we set up our `while` loop. We want to loop while the glass has a value less than or equal to `glass_capacity`. Inside of our loop, we add `1` unit of water to our glass. Each time the loop runs, it checks the value of `glass` to see if it has reached the same value as `glass_capacity`. The loop stops once `glass` reaches `12`, conveniently before we spill.

`While` loops are also great for guessing games. Let's use a small function called `raw_input()` to get some
user input so that they can take guesses about our secret number. We will discuss `raw_input()` more in later
units. For this guessing game, let's hard-code in an answer, just for simplicity:

```python
answer = 4
guess = raw_input("Guess what number I'm thinking of (1-10): ")
while guess != str(answer):
  guess = raw_input("Nope, try again: ")
print "You got it!"
```

Run this to see what the `raw_input()` function does. You should see the prompt asking you to enter a guess
between 1 and 10. Input a number and hit `enter`. It stores the number you entered into the `guess` variable, but what gets stored is actually a string and not a number. As a result, when we compare the guess to the answer, we need to use the `str()` function to convert the value in `answer` to a string. (Just like apples and oranges, you can't compare integers to strings. Both things being compared must be of the same type.) If they are not the same, the guess was wrong, so we prompt the user to try again. Each time the user enters a new number, the script checks to see if it matches the answer and loops again if it doesn't. When the guess finally matches the answer, the loop condition will be false and the loop will exit. Finally, the notification that the user guessed correctly is displayed.

## You-Do: Practice with Loops
Use this [blank repl.it](https://repl.it/languages/python) workspace for these practice exercises.


1) Choose which type of loop is most appropriate for the following situations:
  * Your script queries a database and is given a collection of records that should be printed to the screen.
  * Your script calls an API that returns a stream of an unknown amount of data to fill a buffer.
  * Your script needs to take two lists of values and add them together to store in a third list of equal size.

2) What does this code print? (Bonus: What is the name of this sequence?):

```python
a = 0
b = 1
while b < 15:
  print(b)
  prev_a = a
  a = b
  b = prev_a + b
```

3) Write a script that declares an empty list for names. Use `raw_input()` to ask the user to enter a name
or to enter `'quit'` in order to quit the script. Store the input in a variable named `input`. While the
input is _not_ equal to the word `'quit'`, perform the following steps in your loop:
  * Add the inputted name to the `names` list.
  * Print the string `"The list so far..."`.
  * Create a loop (yes, inside of your outer loop) to print each name in the `names` list.
  * Once the printing loop completes, use `raw_input()` again to ask for new `input` (otherwise you'll get an infinite loop).
  * After the user enters `'quit'` and your outer loop finishes, print `"Quitting..."` so that the user knows the command has worked.

**Solution:**
```python
names = []
input = raw_input("Enter a name (or type 'quit' to quit):")

while input != 'quit':
  names.append(input)
  print "The list so far..."
  for name in names:
    print name
  input = raw_input("Name (or quit):")
print "Quitting..."
```

## Conclusion
Here's a recap of key takeaways from this lesson:
* Loops are powerful control structures in Python that let us efficiently deal with repetitive tasks.
* `For` loops iterate a specific number of times. They are designed to be used when you have a collection of items or if you know exactly how many times you need to iterate.
* For creating or modifying lists using a loop iterator as a list index, set the `for` loop to use a `range()`.
* `While` loops iterate an indefinite number of times based on whether a condition is true or false. They are designed to be used when you don't know how many times you need to iterate.

Feel free to go back and review this material as necessary. To deepen your understanding, consider exploring some of the resources in the Additional Reading section that follows.

### Additional Reading
- [Learn Python Programming: Loops Video](https://www.youtube.com/watch?v=JkQ0Xeg8LRI)
- [Python: For Loop](https://wiki.python.org/moin/ForLoop)
- [Python: Loops](https://www.tutorialspoint.com/python/python_loops.htm)
