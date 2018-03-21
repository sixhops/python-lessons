# Project: Part 1

Throughout the pre-work, there will be a series of small projects for you to do. By the last piece of the project, you'll have used your new Python skills to write a simple piece of cybersecurity software. Specifically, you will write a program to analyze traffic records and develop a "blacklist" of users who are putting an unusually high amount of traffic through the network.

Why would this be a problem? Well, consider another scenario: online gaming. Suppose you're playing a popular online Xbox game with a large number of players who might be logged in at any time. When there are more players logging in and out, the game is more likely to lag for all players, as resources are limited.

Now, suppose that there's a player who, for whatever reason, sets up multiple Xboxes and repeatedly logs in and out on each machine. Eventually, this player could cause a lot of lag for others, even if the total number of players is relatively small. Game admins would probably want to ban that user from joining the game server in the future!

Sounds tough, right? Well, to help you ramp up to that task, you'll first face a set of smaller challenges; ones that will build off of what you've learned and push you to go beyond it.

Ready to begin your first challenge?

Good luck!

## Challenge 1: Decision-Making Logic

Write some code to accomplish the following behavior:
1) Create a variable called `message` and assign a string of your choosing as its value.
2) Write instructions that check to see if `message` has a length that's greater than 40 characters. If the string is longer than 40 characters, the code should `print` the message `"More than 40 characters!"`.

You can start off in [this repl.it](https://repl.it/@SuperTernary/cybersecurity-project-1).

_Hint: The way to check the length of a string in Python is to use `len()`. For example, `len("abcde")` will equal `5`. Don't use quotes if you're passing a variable!_

Once you've written your code, test it out by changing the value of the string `message`. If it's working correctly, your code should print `"More than 40 characters!"` if `message` has a length that's greater than 40. Otherwise, it should not print anything.

Is your code working correctly? Try your best! We'll go over it in the next part of the project.

<!--
### Solution code:
```python
message = "this is a message"
if len(message) > 40:               # Check if the length of `message` is greater than 40 characters.
  print "More than 40 characters!"  # If it is, print some text.
```
-->
