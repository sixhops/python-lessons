# Control Flow

### Learning Objectives
*After this section of lessons, you will be able to:*
* Use if/elif/else conditionals to control program flow based on boolean conditions
* Use comparison operators to evaluate and compare statements

## What is Control Flow?

Programming is the practice of writing a set of instructions for our computer to execute. These are interpreted by our computer one at a time, in order. Sounds kind of like a recipe, right? Suppose, however, that we are trying to cook something complicated. For example, consider the following excerpt from "French Toast":

*1) Whisk eggs, milk, honey, and kosher salt until eggs are no longer visible.*

*2) Dip your bread slices in the custard. If you're using a pre-sliced loaf and the slices are thin, a short dip (just enough to coat both sides) should be enough. However, if your slices are thick, dip the bread for a minute or two to soak up the egg mix.*

*3) Transfer the slices to your frying pan and cook on a medium-low heat until brown on the bottom.*


Instructions like these require the cook to make decisions based on available data. For example, **if** the cook is using thin slices of bread, they should follow one set of instructions, **but if** the cook is using thick slices, they should follow a separate set of instructions. In the context of programming, this is called control flow, because it specifies the flow of the computer's actions through the program.

### The `if` Statement

We've been writing scripts that start at the top and sequentially execute each line until they reach the bottom. Let's say we want execution to branch - that is, we want it to do one thing **if** some condition is true and do a different thing **if** the condition is false. We would then use the `if` statement:

```python
floor = "sticky"
walls = "clean"
if floor == "sticky":
  print "Clean the floor! It's sticky!"
if walls == "sticky":
  print "Clean the walls! They're sticky!"
```

You can see this code run [here](https://repl.it/@SuperTernary/cybersec-if-sticky).

This script sets up two variables and then compares them to certain values to decide if the next lines should be executed. We check to see if `floor` is equal to "sticky". If it is equal, we print a message saying to clean up. Because the floor was sticky, the condition evaluated to True and the next line ran. Then we see if the walls are sticky. The walls were not sticky, they were clean, so the condition evaluated to False and the next line **was skipped over**.

Here's how you write an `if` statement:

```python
if condition:
  # Run these lines if condition is True
```

We use the word `if` and then put in the logical comparison we want to make. The `if` line ends in a colon and the indented lines that follow are the lines that will only be run if the condition results in True. Let's write one:

#### Codealong: It's Too Hot In Here

Let's make a temperature script that lets us know when it is too hot. Open a new [Python repl.it](https://repl.it/languages/python) and set up a temperature variable:

```python
temperature = 55
print "It's too hot!"
```

Okay, we have a script that sets the temperature to 55 degrees (F) and then immediately prints that it is too hot. But 55 degrees isn't really hot so our app is kind of useless. Let's give it the ability to make a decision about whether it is too hot or not.

Change your code to the following:

```python
temperature = 55
if temperature > 80:
  print "It's too hot!"
```

Now our script will only complain about the heat if it is over 80 degrees. At present it prints nothing.

Crank the heat to see what it does:

```python
temperature = 95
if temperature > 80:
  print "It's too hot!"
```

It's getting hot in here now and the script appropriately prints its message.

### The `else` Statement

Using the `if` statement like above gives us a situation where the script will do something if the condition is true but it will do nothing if the condition is false. What if we want it to do one thing if it's true and a completely different thing if it is false? Python gives us the `else` statement. It has this basic structure:

```python
if condition:
  # do something
else:
  # do something else
```

This works exactly the same as a simple `if` statement except that it adds `else` and another line that will be executed only if the condition evaluates to False. Let's use this to add some more messages to our temperature script so that it will say something for any temperature.

Add the `else` statement to your repl.it:

```python
temperature = 95
if temperature > 80:
  print "It's too hot!"
else:
  print "It's just right!"
```

Now for any value over 80, the script will print a complaint. **Else**, if the temperature is not over 80, the script will express its satisfaction. Change the temperature to 65 and run it again. Python chooses the other path now and executes the line saying that it is just right.

### The `elif` Statement

This is great! Now we can have our scripts actually look at some data and make a different decision based on its value. It reads the `temperature` variable and compares the value to `80`. Since the temperature we coded in was lower than `80`, it evaluated to False and printed the "just right" comment. But as we all know, the world is not all black and white and frequently we will need to have more than just two branches for our script to choose from. That's where the `elif` statement works its magic. `Elif` is a portmanteau of "else if". It is used when you need to have multiple branches of execution but each one needs to use a different comparison. Let's use this to really beef up our temperature script to give some really nice feedback.

Change your `else` and add these `elif` statements to your repl.it:

```python
temperature = 95
if temperature > 80:
  print "It's too hot!"
elif temperature <= 80 and temperature > 60:
  print "It's just right!"
elif temperature <= 60 and temperature > 40:
  print "It's pretty cold!"
else:
  print "It's freezing!"
```

Let's look at this line by line. We make our `temperature` variable and set it to 95. Then we check to see if it is greater than 80. If it is, we print the "hot" message. If that condition is false, we then move to the next one which checks to see if the temperature is between 60 and 80. Note the use of the `and` operator to make sure that both of those comparisons must be true for the whole conditional to be true. If the temperature is less than or equal to 80 **and** greater than 60, then we print the "just right" message. If that one is false we proceed to the next `elif` which checks for cold temperatures. Finally, we end with `else`. You will use `else` as the last statement in any block that uses `elif` statements.

## Exercises:

1. What do you think the following code will print:

```python
foo = 5
bar = 1
if foo > 13:
  print "Flip"
elif bar:
  print "Flop"
else:
  print "Fly"
```

2. Write a script ([here](https://repl.it/languages/python) is a blank repl.it) that prints whether a number is even or odd. Do you remember how to determine that? We can use the modulus operator (`%`) to check the remainder. If a number has a non-zero remainder when we divide it by 2 then it is odd, else it is even. Here is some code to get you started:

```python
number = 10
remainder = number % 2
```

## Conclusion

Just like using the words "if" and "else" in real life, these let us make decisions in our programs.

* `if` statements let us control the flow of execution in our scripts.
* We use conditional operators in our `if` statements to perform the comparisons.
* The `else` statement lets us define what to do when our primary conditional test is false.
* The `elif` statement lets us add multiple comparisons to our `if` blocks.
