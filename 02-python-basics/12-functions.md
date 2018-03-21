# Functions

### Learning Objectives
*After this lesson, you will be able to:*
- Create and call a function.
- Identify when to use a function.
- Use parameters and arguments.
- Return a value from a function.

## Introduction: What Are Functions?

The definition of a function is simple — it's a reusable piece of code.

What if you want to reuse a piece of code over and over again? Instead of writing out all of this code out many times, it's much cleaner to write a _function_, which can then be used repeatedly.

In this lesson, we'll be taking a look at how we can use functions to group together statements that perform a specific task and reduce repetition in our programs.

### Function Example

Consider a program that prints the $5 shipping charge for products on a website:

```Python
print "You've purchased a Hanging Planter."
print "Thank you for your order.
  There will be a $5.00 shipping charge for this order."

print "You've purchased a Shell Mirror."
print "Thank you for your order.
  There will be a $5.00 shipping charge for this order."

print "You've purchased a Modern Shag Rug."
print "Thank you for your order.
  There will be a $5.00 shipping charge for this order."
```

- Run this in [repl.it here](https://repl.it/@SuperTernary/cybersec-functions-1).

This is all easy enough to write out, but considering that this website has thousands of products, we'd have to rewrite this `print` statement a lot! Let's try to keep our code from getting out of hand by putting that `print` statement in a function.

Change your repl.it to look like this:

```Python
def printOrder():
  print "Thank you for your order.
    There will be a $5.00 shipping charge for this order."

print "You've purchased a Hanging Planter."
printOrder()

print "You've purchased a Shell Mirror."
printOrder()

print "You've purchased a Modern Shag Rug."
printOrder()
```

If you hit "Run", it does the same thing. Notice how much cleaner and simpler this function looks compared to our repeated lines of code?


#### Breaking This Down

How did we create a function? In Python, functions are defined using the `def` syntax shown below. `def` stands for "define." Here, we're defining a function named `printOrder`.

```Python
def printOrder():
    # What the function should do.
```

This is the name we can then use to call the function. Now, Python knows that whenever it sees `printOrder`, it should do what's defined in the function.

You can name a function anything you'd like, as long as the name used when it's called matches the function name that's defined.

- In repl.it, change the function name `printOrder` to `finishedOrder`. As long as you also change the function calls, it will still work.

- Change it back to `printOrder` — it's a more descriptive name, so it'll help us remember what the function does.

Now Python knows we want to make a shortcut. Whenever we say `printOrder` in the future, we want it to perform the same action. Next, of course, we have to tell Python what to do when we call `printOrder`.

Following `def` and the function's name, `printOrder`, we have a set of parentheses and a colon. This is telling Python, "Hey! What to do when we call the function starts here." We will also need to include some code to indicate what the function will accomplish. This is just normal Python code, but it's indented so that Python knows it's part of the function.

```Python
def printOrder():
  print "Thank you for your order.
  There will be a $5.00 shipping charge for this order."
```

We now have a function named `printOrder`, and, whenever we call it, Python will run the code `print "Thank you for your order. There will be a $5.00 shipping charge for this order."`

You call the function simply by pairing its name with the parentheses: `printOrder()`. The code in a function will not run when the function is defined ("This is what you do when it's called"); it will only run when the function is called ("Do what's in the definition now").

- Take the line `printOrder()` out of repl.it and hit `Run` — nothing will print to the screen.

Every single function will have the `def`, `()`, `:` syntax...

```Python
def functionName():
  # Code here.
```

... and be called with its name when you want to use it.

```Python
functionName()
```

-----------

## You Do: A `welcome` Function

- In a [blank repl.it](repl.it/languages/python), write a function named `welcome` that prints "Hello!" to the screen.
- Make sure your code actually prints "Hello!" when you hit `Run`.

Does your code look like this?

```Python
def welcome():
  print "Hello!"

welcome()
```

### Multi-Line Functions

Functions can contain as many lines of code as you like, as long as each line is indented.
- Add another `print` statement to your code in repl.it that reads "Bonjour!"

Does your code look like this?

```Python
def welcome():
  print "Hello!"
  print "Bonjour!"

welcome()
```

-----------

## Parameters

Now that we know how to call functions, let's add more details. This is your current order program:

```Python
def printOrder():
  print "Thank you for your order.
  There will be a $5.00 shipping charge for this order."

print "You've purchased a Hanging Planter."
printOrder()

print "You've purchased a Shell Mirror."
printOrder()

print "You've purchased a Modern Shag Rug."
printOrder()
```

There's still some repetition there — it always prints, "You've purchased a ..." What if there are hundreds of products in our shop? We'd need to write out variations of this same sentence hundreds of times.

What if you could use the function to dynamically print what the user buys? This is where **parameters** come in.

Let's take a look:

```Python
def printOrder(product):
  print "Thank you for ordering the ", product, "."
  print "There will be a $5.00 shipping charge for this order."

printOrder("Hanging Planter")
printOrder("Shell Mirror")
printOrder("Modern Shag Rug")
```

- Run this in [repl.it here](https://repl.it/@SuperTernary/cybersec-functions-parameters)

Now, we don't need to know the product name in advance. Instead, when we call the function, we can tell Python, "Run the `printOrder` function. Here is the name of the product to use." Then, when Python gets to the line `print "Thank you for ordering the ", product, "."`, it will say "OK, what was I told the product is?" and print that.

Let's break down this process:

1. Notice that the parentheses after `def printOrder` are no longer empty. Instead, we have the word `product`. This is a parameter; it's in the parentheses to tell the function that we are going to provide it with a `product`.
  - There's nothing special about the word "product." We are simply using descriptive names in order to remember what information we're providing our function.
  - Below, we've replaced `product` with `pineapple.` Change the parameter name in your repl.it and hit run. Does it still work?


  ```Python
  def printOrder(pineapple):
    print "Thank you for ordering the ", pineapple, "."
    print "There will be a $5.00 shipping charge for this order."

  printOrder("Hanging Planter")
  printOrder("Shell Mirror")
  printOrder("Modern Shag Rug")
  ```

  - However, `pineapple` isn't very informative when we look at the function definition, so we use `product`.

2. When you call a function that has a parameter, you wrap the variable you want to pass the function in the parentheses: `printOrder("Shell Mirror")`. This is called an **argument**. The argument corresponds to the parameter in the function definition.
  - When we call the function with an input of `"Shell Mirror"`, the string is assigned as `product` (or `pineapple`) inside the function. Then, the function's internal code runs, printing the correct sentence.

3. What if you don't do this correctly?

  - In your repl.it, remove `"Hanging Planter"` from the code so `printOrder` is just called with empty parentheses, then hit `Run`.

  ```Python
  def printOrder(product):
    print "Thank you for ordering the ", product, "."
    print "There will be a $5.00 shipping charge for this order."

  printOrder()
  printOrder("Shell Mirror")
  printOrder("Modern Shag Rug")
  ```

You get an error. Python is expecting to be told what the product is; if you don't specify the product, it won't be able to print anything.

### To Recap:

- **Parameter**: The variable that's defined in a function's declaration.
  - For example:

```Python
def doSomething(parameter):
  # Does something.
```
- **Argument**: The actual value passed into the function when the function is called.
  - For example:

  ```Python
  doSomething(argument)
  ```

-----------

## You Do: Parameters


Imagine that you are tasked with creating a program to calculate the total amount, including sales tax, for each item at a coffee shop.

Take a look at the function below, which will calculate the total amount for a latte:

```Python
def latteTotal():
  price = 4.50
  salesTaxRate = .10
  totalAmount = price + (price * salesTaxRate)
  print 'The total is $', totalAmount

latteTotal()
```

What would we do if we also wanted to find the the total amount for Americanos? We could create another function:

```Python
def americanoTotal():
  price = 5.00
  salesTaxRate = .10
  totalAmount = price + (price * salesTaxRate)
  print 'The total is $', totalAmount

americanoTotal()
```

However, what if we wanted to find the total for every item in the coffee shop, including drinks and baked goods? We don't want to have to create a separate function for each item — that's a lot of work on our end. It will also burden our program with repeated code, which we want to avoid (remember, keep it DRY — Don't Repeat Yourself).


- In repl.it, change what's there and instead a function that prints the total of any drink if you pass it the price. Work from [this starter code in repl.it](https://repl.it/@SuperTernary/cybersec-functions-latte)


```Python

# Your function here.

calculateTotal(5.5) # This will print 6.05.
calculateTotal(4.75) # This will print 5.225.
```

How did it go?

[Here's the solution](https://repl.it/@SuperTernary/cybersec-functions-latte-solution). Is that close to yours?

-----------

### Multiple Parameters

Our shop is getting successful, and we have locations opening all across the country. However, each state has a different sales tax rate. If we want to keep using our function to calculate an item's price, we will now also need provide it with the sales tax rate each time. We can add more parameters and arguments by simply separating them with commas.

- Change your code in repl.it to have a second parameter:

```Python
def calculateTotal(price, taxes):
  totalAmount = price + (price * taxes)
  print 'The total is $', totalAmount

calculateTotal(5.5, .10) # This will print 6.05.
calculateTotal(4.75, .12) # This will print 5.32.
```

- Would you rather buy a drink in the first state or the second? This is a useful function to help you decide.

Order is important here.
- The first argument that's provided, `5.5`, will correspond with the first parameter we provided for the function, `price`.
- The second argument, `.10`, will correspond with the second parameter, `salesTaxRate`.

In the second example, what does `4.75` correspond to? `.12`?

To write functions with more than one parameter, use a comma-separated list — e.g., (parameter1, parameter2, parameter3, parameter4, etc.).

Here's an example of a function with four parameters:

```Python
def greetUser(firstName, lastName, year, city):
  print "Hello ", firstName, " ", lastName, " born in ", year, " from ", city, "!"
```
What would happen if we called the function with the following arguments?

```Python
greetUser("Bruce", "Wayne", 1939, "Gotham")
```

We would get this result:

`Hello Bruce Wayne born in 1939 from Gotham!`

What would happen if we called the function with the same arguments in a different order?

`greetUser("Bruce", 1939, "Gotham", "Wayne")`

We would get this result:

`Hello Bruce 1939 born in Gotham from Wayne!`

Try all of this by running [this repl.it](https://repl.it/@SuperTernary/cybersec-functions-batman).

Unlike a human, Python doesn't use the variables' names to figure out what they're for. If you tell it that Bruce's last name is 1939, it will believe you! This is why it's important for parameters to have descriptive names, such as "firstName" and "year" — so that we as the humans running the program can pass the right arguments.


-----------

## You Do: Functions With Logic

Let's return to our shipping example. If the order amount is greater than $30, the customer will receive free shipping. If the total order amount is less than $30, there will be a $5 shipping charge. This is the current code:

```Python
product = "Hanging Planter"
orderAmount = 35
print "Thank you for ordering the ", product, "."
if orderAmount >= 30:
    print "It's your lucky day!
    There is no shipping charge for orders over $30.00.",
else:
    print "There will be a $5.00 shipping charge for this order."


product = "Shell Mirror"
orderAmount = 15
print "Thank you for ordering the ", product, "."
if orderAmount >= 30:
    print "It's your lucky day!
    There is no shipping charge for orders over $30.00.",
else:
    print "There will be a $5.00 shipping charge for this order."

product = "Modern Shag Rug"
orderAmount = 75
print "Thank you for ordering the ", product, "."
if orderAmount >= 30:
    print "It's your lucky day!
    There is no shipping charge for orders over $30.00.",
else:
    print "There will be a $5.00 shipping charge for this order."
```

[Here is the code in repl.it](https://repl.it/@SuperTernary/cybersec-functions-exercises). You're going change the code, but make sure it has the same functionality.

[Here is a starting repl.it](https://repl.it/@SuperTernary/cybersec-functions-exercise2). Write a function called `printOrder` that takes two arguments: `product` and `orderAmount`. Fill in your function so that you can call it with the test in the repl.it.

* **Hint**: You can put anything inside a function. Copy and paste are your friends.
* **Hint 2**: Don't forget about indenting!

What do you think? Could you do it?

[Here](https://repl.it/@SuperTernary/cybersec-functions-solution) is the answer, but give it your best shot before looking!

Notice that we can define the function once and then call it multiple times. This is a huge advantage of functions. Functions are especially useful because they enable a developer to segment large, unwieldy applications into smaller, more manageable, and (most importantly) reusable pieces.

-----------

## Return Statements

We now know how to communicate with functions in one direction, by passing values using parameters and arguments.

However, functions can also communicate back to you and return values. Sometimes we don't necessarily want to show or log something immediately to the console or update something on a page. When we **return** something, it ends the function's execution and "spits out" whatever we are returning.

We can then store this returned value in another variable.

What if your user orders a bunch of drinks and you want to save their prices to add them together?

For example, let's say your customer orders a drink that costs $5.50 at a 10-percent tax rate and a drink that costs $4.75 at a 12-percent tax rate. You want to know the total amount of money they've spent.

So far, you have a function that prints the individual price:

```Python
def calculateTotal(price, taxes):
  totalAmount = price + (price * taxes)
  print 'The total is $', totalAmount

calculateTotal(5.5, .10) # This will print 6.05.
calculateTotal(4.75, .12) # This will print 5.32.
```

How would you add those together? It'd be easiest if you could save the amount that's returned, like this:

```Python
def calculateTotal(price, taxes):
  totalAmount = price + (price * taxes)
  print 'The total is $', totalAmount
  # Somehow, send the totalAmount for the drink back to the main program.

calculateTotal(5.5, .10) # Somehow, save the amount of this drink
# into a variable like "latteTotal."
calculateTotal(4.75, .12) # Somehow, save the amount of this drink
#into a variable like "americanoTotal."

totalOfOrder = latteTotal + americanoTotal

print 'Your order total is', totalOfOrder

```


To do this, we need to use a **return** statement. With this function, we are sending the `totalAmount` back to the main program using the `return` keyword. Then, we're saving the value that's returned into a variable like `latteTotal` or `americanoTotal`.

```Python
def calculateTotal(price, taxes):
  totalAmount = price + (price * taxes)
  print 'The total is $', totalAmount
  # Somehow, send the totalAmount for the drink back to the main program.
  return totalAmount

latteTotal = calculateTotal(5.5, .10)
# Somehow, save the amount of this drink
# into a variable like "latteTotal."
americanoTotal = calculateTotal(4.75, .12)
# Somehow, save the amount of this drink
# into a variable like "americanoTotal."

totalOfOrder = latteTotal + americanoTotal

print 'Your order total is', totalOfOrder

```

- Copy this to a [repl.it](repl.it/languages/python) and run it.


Let's look at a shorter example. Here, we're creating a new variable, `total`, which is simply `number` plus `2`. We use the `return` keyword to specify that the function will output `total`.

```Python
def addTwo(number):
 total = number + 2
 return total

finalVar = addTwo(3)
print finalVar
```

- Type this (it's short - practice!) into a [blank repl.it](repl.it/languages/python) and run it.

When we call the function with an input of `3`, the integer is assigned as `number` inside the function. Then, the function's internal code runs, creating the `total` variable and returning it as the output. In this case, the function's output is the integer `5`, which we assign to `finalVar`.

### Return Statements With Logic

The `return` statement *stops the execution of a function* and returns a value from that function. What do you think the following will print?

```Python
def mystery():
   return 6
   return 5

myNumber = mystery()
print myNumber
```

- Run this in a [repl.it](repl.it/languages/python) to see if it's what you expected.

When Python hits a `return` statement, it knows that it's done its job and it won't run any more code.

- What do you think the program below will print out?


```Python
def addBonusPoints(score):
    if score > 50:
        return score + 10
    return score

totalPoints = addBonusPoints(55)
print totalPoints
```

- Run it in [repl.it](repl.it/languages/python) to see if the output is what you expected.

- Because the score in this case is greater than 50, we will hit the `return` statement `return score + 10`, and the function will stop running.
  - This means the code that's below the `return` statement will never be executed and will be ignored completely. The function stopped executing at the first `return` statement it hit.

Change the argument `55` to something less than 50, like `35`. Run the function again. It should now print `35` — the function didn't enter the `if` statement and therefore simply hit a `return`.

### Exiting a Function

We can also use `return` by itself as a way to exit the function and prevent any code that follows from running.

Take a look at this example:

```Python
def rockAndRoll(muted):
   song = "It's only Rock 'N' Roll"
   artist = "Rolling Stones"

   if (muted == True):
       return
       # Here, we use return as a way to exit a function
       # We don't actually return any value.
   print "Now playing: ", song, " by ", artist

rockAndRoll(True)
```

Here, we use `return` as a way to exit the function instead of returning any value. When we call the function and pass in `True` as an argument for `muted`, this statement will never run: `print "Now playing: ", song, " by ", artist`.

Put this in [repl.it](repl.it/languages/python) and run it.

Then, change `True` to `False` and run it again. The statement should print.

-----------

## You Do: Function Practice Exercises

1. In a [new repl.it](repl.it/languages/python), define a function named `areBothEven`.
  - It should accept two parameters: `num1` and `num2`.
  - Inside the function, return `True` if `num1` and `num2` are both even but `False` if they are not.
  - Test this with `print areBothEven(1, 4)`, `print areBothEven(2, 4)`, and `print areBothEven(2, 3)`.

  **Hint**: You can use the modulus operator (`%`) to see if both numbers are even. If you use `num % 2`, it will return `1` if the number is odd and `0` if the number is even.*

2. Underneath that, in your repl.it, define a function named `lightOrDark` that takes the parameter `hour`. The function should return "It's dark outside!" if `hour` is less than 7 or greater than 17. Otherwise, it should return "It's light outside!"


## Quick Knowledge Check

Let's test your knowledge of what we've learned this lesson.

1. Look at the following code. Where will the function stop if `x` is `10`?

```Python
def categorize(x):
  if (x < 8):
      return 8
  x += 3
  if (x < 15):
      return x
  return 100
```

> Answer: `'return 100'`. Because `x` is greater than `8`, the first `if` condition is false. After adding `3` to `x` with `x += 3`, `x` will be `12`, which is less than `15`. This means that the second `if` statement condition is true, and Python will run the line `return x` and then stop running.


2. Look at the `adder` function:

```Python
def adder(number1, number2):
 return number1 + number2
```

Which of the following statements will result in an error?

A. `adder(10, 100.)` <br>
B. `adder(10, '10')` <br>
C. `adder(100)` <br>
D. `adder('abc', 'def')` <br>
E. `adder(10, 20, 30)` <br>

>  Answers: B, C, and E. `adder(10, '10')` is incorrect because it tries to combine a string and an integer. Meanwhile, `adder(100)` will result in an error because it only provides one value, while `adder(10, 20, 30)` provides too many.
