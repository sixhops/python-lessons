# Intro to Python Scripting

## Learning Objectives
* Explain what scripting is used for
* Write scripts that perform file IO
* Write scripts that take user input

## What Is Scripting? What Is It For?

We have actually been scripting this whole time! Technically, anything we write in Python is scripting. But historically, when developers talk about scripting, usually they are referring to writing small programs that do tasks at the system level, such as reading and writing files, accessing system resources, or doing other repetitive things that are easier when run with a script. We are going to learn a bit about file access and a bit about prompting the user for input.

## Codealong: Reading and Writing Files

Open a new file and type in this Python code:

```python
myFile = open("output.txt", "w")
myFile.write("I've just written to a file on disk!")
myFile.close()
```

Let's see what these lines do. The first line uses the `open()` function to open a file for writing. The
file is stored in the variable `myFile`. The first param is the file to be written to and the second param is a flag that says the file is opened for writing. The second line uses the `write()` function to write a string
to that file. The third line is very important. You must always close any file that you have opened. The writing
will not be saved to the file until you close it.

Run this code and you should see a new file called 'output.txt' pop up in your REPL project. This file was created for us because we opened it in write mode. If you look in this file you will see the string you used.

Now let's see how we can read from this file into our scripts. Go ahead and comment out the code above and add this:

```python
myFile = open("output.txt", "r")
print myFile.read()
myFile.close()
```

Line 1 here opens the file again but this time with the 'r' flag which specifies that we're opening it for reading.
Then we print the value returned by the `read()` function and close the file on the last line. If you run this code
in the folder with the output.txt file then it will print out the contents of that file we just created above. So, now that we can interact with the file system, let's get a little more input from our users.

## Codealong: Get a List of Names From a User, Sort Them, and Write Them To a File.

There is a very simple function that lets us get user input: `raw_input()`. All we need to do is place a nice,
friendly prompt into the parentheses so that the user knows they're up. Open up a new file and enter the following:

```python
word = raw_input("Enter a word:")
print "You entered: " + word
```

Run this code. It asks you to enter a word and then it prints the word you entered. Simple, right? Alrighty then,
let's make a script that asks a user for a few names, stores them all in a list, sorts them, then writes them to
a file. Don't worry, we've done all this before. We're just tying it together. Change your code to the following:

```python
names = []
for i in range(3):
  name = raw_input("Enter a name:")
  names.append(name)
```

We've set up a list `names` to hold the inputted names. Then we make a `for` loop that runs three times and asks for a name each time. When each name is entered, we append it to the list. Now, how do we sort a list? Luckily for us, Python lists have a built-in function called sort(). Let's add that code:

```python
names = []
for i in range(3):
  name = raw_input("Enter a name:")
  names.append(name)
names.sort()
print names
```

That will put our names in alphabetical order. We added the print line after the sort so we can see the results before we write them to our file. Save and run this script to make sure it works. You should be able to enter three names and then see them printed in a list in alphabetical order. Now, let's add the file writing:

```python
names = []
for i in range(3):
  name = raw_input("Enter a name:")
  names.append(name)
names.sort()
print names
namesFile = open("sorted_names.txt", "w")
for name in names:
  namesFile.write(name + "\n")
namesFile.close()
```

We use `open()` to create and open a file for writing. Then we loop through the names list and write each
one to the file with a new line character (which makes it more attractive). Finally, we close the file to
finalize everything. Let's run this beast. Once you've entered the names and completed the running of the
script, open up the "sorted_names.txt" and take a look. Your names are in the file in alphabetical order.

## Review Learning Objectives and Wrap Up

* Scripting with Python allows us to use all of Python's power as a language and apply it to performing system
tasks for us.
* Python has built-in file IO functions that we can use to easily read and write files to the disk.
* We can also use Python's built-in user input functions to accept data from our users.
