# Lab: Login Verification Script

--------

Now it is time to put these skills together. You will be writing a tool that will look at the credentials someone uses on a login attempt and will decide whether it is a human or is an automated bot. In the end, the script will store bot login attempts in one file and human attempts in another file.

--------

## Setting up:

- Go to your projects folder and create a new Python file.
- Copy in the provided code below to get started.

---------

## Tasks:

We have a login system that only allows a subset of normally allowed characters for login credentials as an extra measure against bots creating accounts and automated login attempts. We tell our human users what the disallowed characters are but we do not make the list available anywhere that a bot could read it. So if someone tries credentials using one or more of those characters, there is a higher likelihood that it is a bot or a script attack. We can then flag those attempts for followup and investigation.

We need you to write the tool that looks at the credentials being used, determines if they contain the restricted characters, and writes them to one file if it is likely a human attempt and another file if it is likely a bot attempt. Though this could be easily implemented in a single function, we would like it contained in a class so that we can easily extend and modularize the tool for use in other systems. A class allows for this better than simply adding a function to our existing class.

Here is the class we use to ask for username and password:

```python
import re

# This is the class that reads in the user's credentials
class InputReader():
  def __init__(self):
    self.username = ""
    self.password = ""
    self.credentials = ""

  def readInput(self):
    self.username = raw_input("Username: ")
    self.password = raw_input("Password: ")
    self.credentials = self.username + ", " + self.password

  def getCredentials(self):
    return self.credentials

# Create a new InputReader named ir
ir = InputReader()

# Run the readInput function to get the user's credentials
ir.readInput()

# Print out the username and password separated by a comma
print ir.getCredentials()
```

Here we see the class InputReader. The `__init__` method initializes three instance variables. The `readInput` method asks for the username and password and then stores them in a comma separated format in the `credentials` instance variable. The `getCredentials` method is available for you to use to get the value of the credentials out of `ir` so you can read it into your class.

Steps:

* Run this code and understand how it works.
* Under the InputReader class and above the `ir = InputReader()` line, add your class.
* Name it `CredentialWriter`.
* Decide how it will receive the credentials string from the InputReader (maybe the `__init__` method is a good idea...)
* TEST FOR THE FOLLOWING DISALLOWED CHARACTERS USING REGEX:
  * The characters `% ^ &` are disallowed.
  * The characters 0 - 9 (digits) are disallowed.
* If none of the disallowed characters appear anywhere in the credentials...
  * Write the attempt to a file named `human_login.csv`
* If any of the disallowed characters appear in the string...
  * Write the attempt to a different file named `bot_login.csv`

-------

### Hints:

* Remember the flags that determine what mode you open a file in. `r` is for read mode, `w` is for write mode. Keep in mind that write mode will erase all contents of the file each time it is called and write new contents. What we really want is each new login to be **appended** to the file with a new-line character `\n` after it. Can you think of a flag that might put us in **append** mode?

* How many variables will you need for the file handles?

* Remember, your regex tests will return **lists**. What is an easy way to see if a list contains anything?

* Break it down into steps:
  * First, write the class name line.
  * Then add a way to be able to get the credential string and print it.
  * Then remove the printing and add regex tests for the disallowed characters.
  * Let the outcome of the regex tests determine which file you write to.

--------

## Solution

Solution code is provided in the `solution_src` folder for this lesson.
