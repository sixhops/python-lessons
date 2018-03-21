# Project: Part 2

In the last challenge, you worked on creating some code that could make a decision. This code
would take a given string, called `message`, and check to see if the length of that string was
greater than 40 characters; if it was, your code would print out a message.

Here's a working solution for that challenge:

```python
message = "some message"
if len(message) > 40:
  print "More than 40 characters!"
```

Open a [new repl.it](https://repl.it/languages/python), and type that code into it.

In this next set of challenges, you're going to take those same concepts one step further by adding in lists and loops.

## Challenge 2: Checking a List of Messages

Now, rather than a single string, `message`, your code will have a list of strings; this list
will be stored in the variable `messages`.

```python
messages = ["This is a message.", "So is this.",
"The quick brown fox jumped over the lazy dog. Then the fox did it again."]

# Replace this comment with your code.
```

The code will need to print the same message (`"More than 40 characters!"`) but this time do it for _each string_ in the list that has a length that's greater than 40. Remember, if a string has a length of 40 characters or fewer, your code should not print anything.

Can you do it? Challenge 3, below, builds off of this, so do your best here.

<!--
### Solution code:
```python
messages = ["This is a message.", "So is this.", "The quick brown fox jumped over the lazy dog. Then the fox did it again."]
for message in messages:
# Go through every string in the `messages` list one by one (using `message` as a placeholder for the current string).
# For each string (`message`), do the following:
  if len(message) > 40:                 # If the given string is longer than 40 characters...
    print "More than 40 characters!"    # ... print some text.
```
-->

## Challenge 3: Building a New List

Once you have that working, let's kick things up a notch by making some changes to the code we've just written.
This time, instead of printing a message every time we find a string that's longer than 40 characters, let's
instead add it to a new list, which we'll call `moreThanFortyChars`. What will we need to change in order
to make this work?

_Hint: `moreThanFortyChars` should start out empty._

Try your best to do this. The solution will be at the beginning of the next project challenge.

<!--
### Solution code:
```python
messages = ["This is a message.", "So is this.", "The quick brown fox jumped over the lazy dog. Then the fox did it again."]
moreThanFortyChars = []                 # Create a new empty list.
for message in messages:
# For each string (`message`) in the `messages` list, do the following:
  if len(message) > 40:                 # If the given string is longer than 40 characters...
    moreThanFortyChars.append(message)  # ... add that string to the new list, `moreThanFortyChars`.
```
-->
