# Project: Part 3

## Challenge 4: Making a Function

In the last set of challenges, you wrote some code to take a list of strings, `messages`, and create
a new list from it called `moreThanFortyChars`. This new list was filled only with strings from `messages` that were
longer than 40 characters. Here's the solution code for that:

```python
messages = ["This is a message.", "So is this.",
"The quick brown fox jumped over the lazy dog. Then the fox did it again."]
moreThanFortyChars = []
for message in messages:
  if len(message) > 40:
    moreThanFortyChars.append(message)
```

Your mission this time, should you choose to accept it, is to:
1) Take this code and turn it into a function called `getOverFortyChars`. <br>
2) Rather than having `messages` be a hard-coded list of values, make `messages` a parameter of the function so that your code can operate on any list of strings that is passed in as an argument. <br>
3) Have the function return the list `moreThanFortyChars` so that other code can use it. <br>

Once you're done, try testing your code by passing in different lists of strings to see if it still works!

Challenge 5, below, follows up on this, so make sure you try your best here.

<!--
### Solution code:
```python
def getOverFortyChars(messages):  # This is how to define a function so that you can reuse it later.
# This function's name is `getOverFortyChars`, and it takes an argument, which we'll refer to with the placeholder `messages`.
  moreThanFortyChars = []         # Create a new empty list.
  for message in messages:        # For each string (`message`) in the `messages` list...
    if len(message) > 40:               # ... if that string is longer than 40 characters...
      moreThanFortyChars.append(message)      # ... then add it to the end of the list `moreThanFortyChars`.
  return moreThanFortyChars       # Return that list back.
```
-->

## Challenge 5: Checking a List of Messages

Building off of the solution above, because `messages` is a parameter, it can hold whatever value happens to be passed in as an argument. This means that it could potentially contain duplicate messages. Suppose that you wanted your function to only return _one_ of each message that's longer than 40 characters, even if there were more than one present in the initial list (you can rename it `getUniqueOverFortyChars` to reflect this change in how it operates).

How can you modify the code so that it will only return unique (i.e., non-duplicate) values?

_Hint: The keys in a dictionary are guaranteed to be unique, as trying to add a key twice will just overwrite the old value with the new one._

Challenge 6, below, follows up on this, so make sure you try your best here.

<!--
### Solution code:
```python
def getUniqueOverFortyChars(messages):    # Define a function, this time with a different name.
  messageDictionary = {}                  # Create an empty dictionary, which will be used to create a list of unique messages.
  for message in messages:                # For each `message` in `messages`...
    messageDictionary[message] = True         # ... add it to the dictionary as a key.
    # When the code encounters a message that's already been seen, it will try to add that duplicate message to the dictionary.
    # However, because that message is already in the dictionary, it just overwrites the old value instead of creating a new entry.
    # Interestingly, the `True` value actually isn't important at all here; it could just as easily be a number or another string.
  moreThanFortyChars = []                 # Create a new empty list.
  # Because the object's keys are unique, we can go through each of the keys to get a list of unique messages.
  for message in messageDictionary:       # For each key (which, in this case, are all unique messages) in the dictionary...
    if len(messageDictionary[message]) > 40:    # ... if the message is longer than 40 characters...
      moreThanFortyChars.append(message)            # ... add it to the end of `moreThanFortyChars`.
  return moreThanFortyChars               # Return that list back.
```
-->

## Challenge 6: Traffic Analysis?

Continuing from above, [here](https://repl.it/@SuperTernary/cybersecurity-project-5-solution) is the repl.it with the solution code you should have up to this point. Now, it's time to tackle the big challenge: writing a program to analyze traffic.
It's a totally different kind of problem from what you've seen before... or is it?

Your task is to create a function called `analyzeTraffic` that has the following features:
-  It should take two arguments: an array of IP addresses (`addresses`) and a maximum request limit (`limit`).
-  It should return a list of only those IP addresses (`blacklist`) that have submitted more messages
than the limit (`limit`) allows.

Go ahead and give it a shot!

_Hint: You'll need to find a way to count how many times each address appears in the list. Does this remind you of anything you've done before?_

The solution code will be at the beginning of the next project challenge. Good luck!

<!--
### Solution code:
```python
def analyzeTraffic(addresses, limit):
# Define a new function called `analyzeTraffic` that takes two arguments, `addresses` and `limit`
  hist = {}                     # Create a dictionary.
  # You'll use this dictionary to hold the counts of how many times you've seen each unique address.
  for address in addresses:     # For each address in the list of addresses...
    if address not in hist:       # ... if you encounter an address that isn't in the dictionary yet...
      hist[address] = 0              # ... create an entry for that address with a value of 0 (see below).
    hist[address] += 1            # Whether or not the address was new, it should now be in the dictionary, so add 1 to its count.
  blacklist = []                # Create a new empty list called `blacklist`.
  for address in hist:          # For each unique address in the dictionary...
    if hist[address] > limit:     # ... if that address appeared more than the number of times specified by `limit`...
      blacklist.append(address)     # ... add it to the list `blacklist`.
  return blacklist              # Return that list back.
```
-->
