# Intro to Variable Scope

## Learning Objectives
* Describe what is meant by variable scope
* Understand the difference between global and local scope
* Use the global keyword for accessing global variables
* Explain the order of scope precedence Python follows when resolving variable names

## What is scope in programming?

We've learned about Python's built-in data types and how to manipulate those. We've also learned about how to make our own complex data types using Classes and how objects that are instantiated from those classes contain their own copies of variables. Each dog object that we created from the Dog class had a `name` variable and each name was distinct. How does Python keep track of which variable we are accessing at different parts of our code? The answer is something called __Scope__.

You can think of scope as the neighborhood in which a variable lives. Think about your address. If someone wanted to send me a letter, they would first put my name on it. But there are huge amounts of people in the world with my name so we need to know more info about where to find me. If they provide my street address, city, and state then the mail carrier will have a better chance of getting the item to me. I am the only person with my name within the __scope__ of my street, city, and state.

Python is not organized by street address, however, so how does it keep track of which variable we are referring to? Python has three main scopes:

1. **Global scope**: Any variable declared/assigned outside of any function or class is considered global.
Global variables are accessible from anywhere in the script. This is not necessarily a good thing
because those variables can be accessed, changed, or reassigned by anything and this can lead to troublesome
bugs.
2. **Local scope in a class**: Any variable declared/assigned inside of a class but not inside any
methods in the class is **local to the class**. It is only accessible by attaching it to the class name
because it only exists in the class. If you have code outside the class and do not have access to the
class then the variable will not be accessible. We say it is "out of scope".
3. **Local scope in a function**: Any variable declared/assigned inside of a function is **local to that function**. This is the most specific level of scope and is, ideally, where most of your variables should be declared. Nothing has access to this scope except the function that the variable was declared in. The variable
is out of scope for everything but that function.

Scopes that are more exclusive are generally better. If a variable is harder to accidentally access then it is safer from an entire class of bugs. You will hear programmers say things like, "Keep the global scope clean" or "Don't pollute the global scope." This is because every variable that is declared/assigned in the global scope is in danger of mutating or being mutated by another global variable. This leads to bugs that are time-consuming to solve so, over the years, modern programmers have come to adhere to the practice of only using the global scope if absolutely necessary. Sometimes it is unavoidable so we will teach you how it works but do your best to keep variables in the narrowest scope possible.

## Codealong: Accessing variables in and out of scope, 'global' keyword

Lucky for us, Python makes it a little trickier than other languages to fiddle around with global
variables if we're not already in that scope. Start up a blank script. The following line will assign
a global variable named `foo` the value of 5:

```python
foo = 5
```

Now, we can easily reassign and access that variable with the following lines:

```python
foo = 5
print foo
foo = 7
print foo
```

That's the global scope: No restriction on accessing or mutating a variable. Let's make a variable
in local function scope and try to access it from the global scope:

```python
foo = 5
def coolFunc():
  bar = 8

coolFunc()
print foo
print bar
```

If you run this code you will get an error: `NameError: name 'bar' is not defined`. This is because the
variable `bar` is only accessible from inside the `coolFunc` function. We called the `coolFunc` function
but as soon as it finished running, the variable `bar` ceased to exist. Even while the function was running,
it was only accessible to itself. But `foo` in the global scope was still accessible.

What if we actually want to modify a global variable from within our function. We need to explicitly tell
Python that this is our intent. Let's modify that code a bit:

```python
foo = 5
def incrementFoo():
  global foo
  foo += 1

print foo
incrementFoo()
print foo
```

Here we can see that we got a reference to the global variable and incremented its value. We did this by
using the `global` keyword. This tells our function that we mean the global `foo` when we say `foo` inside this
function. What would happen if we didn't use the `global` keyword and just tried to access `foo`? Let's see:

```python
foo = 5
def incrementFoo():
  foo = 6
  print "Inside the function, foo is", foo

print "Outside the function, before we call it, foo is", foo
incrementFoo()
print "Outside the function, after we call it, foo is", foo
```

Hey! The variable `foo` went back to its old value after the function finished. Not quite. What happened
was because we didn't use the `global` keyword, the line in the function where foo is assigned the value
of 6 causes a new local variable to be created. We then set this variable's value to 6, the function prints
the value, and then the function finishes. However, the global variable `foo` was never touched by the function. The `global` keyword is always required when we want to write a function that accesses global variables.

## Order of Scope Precedence

Lastly, we should discuss how Python will try to find a variable name when you use it. It begins in the
most local scope and tries to find the variable there. If it fails to find a variable declared in the local
scope, it will then go up one level to whatever the containing scope is. For example, the global scope
contains all other scopes. The narrowest scope may be inside a function. If Python doesn't find a variable in
the current function, it will go out to the next larger scope, perhaps to a containing class. If the variable
doesn't exist there, it will move to the next containing scope until it finally reaches the global scope.

So in the last part of the codealong above, where we removed the `global` keyword, we told the function to print
the value of foo. Python looked in the current function and found a variable foo to which we assigned the value
of 6. It stopped looking for the variable at that point which is why we never got to access the global `foo` -
Python already found the variable in a narrower scope.

The order Python follows is this:
1. **Local**: Any variable in a local function or class scope will take precedence over a variable with
the same name in a broader scope.
2. **Enclosing**: If Python does not find a local variable, it will move to the next enclosing scope
(perhaps a class or another function).
3. **Global**: If no enclosing scope contains the variable, Python will eventually search the global scope.
4. **Built-in**: Finally, if the variable is not declared in any narrower scope or in the global scope, it
will look for the name among the built-in Python classes and objects.

Let's practice some of this.

## Write functions using the `global` keyword

1. Write two functions. In the first, assign the variables x and y some integer values. In the second function,
assign the variables a and b some integer values. Try to modify the values x and y from within the second function.
Why doesn't this work?

2. Now take the second function and put it inside the first function. Are you able to modify x and y now?

3. Add a variable `z` in the global scope and try to modify it from within your functions. What do we need to
do to make this work?

## Review Learning Objectives and Wrap Up

* Scope is how Python keeps track of the location of variables with the same names.
* Global scope, accessible by everything, is the space outside of any function or class.
* Local scope, inside a function or class, is more protected from accidental accesses and mutations.
* The `global` keyword when used in a local scope tells Python that we want to use a globally scoped variable instead.
* Python first looks in the local scope, then in enclosing scopes, the the global scope and finally the built-in
Python modules when trying to find a variable.
