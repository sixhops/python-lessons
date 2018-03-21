# Intro to Regular Expressions

## Learning Objectives
* Explain the purpose of Regular Expressions
* Explain the common regex tokens for pattern matching
* Use regex to interact with strings

## Purpose of Regular Expressions

Regular Expressions, often abbreviated to "regex", are sequences of tokens that make pattern matching
extremely easy. String manipulation is a very common task in any programming language and many modern
languages implement some version of regular expressions to help this. They can be very cryptic or ugly
looking. Many programmers refer to regex tokens as "warts" because they appear as an ugly, complicated
jumble of characters. For example, here is a regular expression:

> /^\(*\d{3}\)*( |-)*\d{3}( |-)*\d{4}$/

This ugly mess is for validating a telephone number. But with knowledge of only a few tokens, we can get
some very powerful results. Let's take a look at some common tokens.

## Codealong RegEx101.com: Learn Tokens For Matching Characters, Digits, and Whitespace

A fantastic site that I like for testing regex is http://regex101.com. Let's go there now so we can
easily see the results of our efforts. In the center section, we have a narrow box for entering our
regular expressions and we have a larger box below it which will hold the string we are testing. Go
ahead and enter the following string into the larger box:

> This is my test string! There are many like it but this string's mine. 99 test strings on the wall.

In the regex box at the top, type `many`. You will see the word 'many' become highlighted. This is the easiest
regular expression. It simply tests the string to see if the letters 'many' appear in the string in that
order. Try taking out the letter 'n' so we are testing for the string `may`. Notice that nothing is highlighted
for the regex because nowhere in our string do the letters 'may' occur in that exact order. Regular expressions
are very specific.

Now, even though we only typed the word 'many' the full regular expression is everything you see in that
top box:

`/many/g`

It's common for regular expressions to start and end with a forward slash. The 'g' flag signifies that we
are testing the whole string for the pattern. It stands for 'global'. In rarer cases, you may want to only
test a portion of the string but most of what we write will be global so get used to that 'g'.

There are some special types of characters we can search the string for to see if they occur. The first of these
is the token for any whitespace. Clear the regex box and enter:

`\s`

Notice how all the spaces became highlighted. This is very handy when we want to isolate actual printed
characters from spaces. We can reverse the regex (make it search for non-whitespace) by capitalizing the
letter S:

`\S`

Now all the letters, numbers, and punctuation are highlighted. Most tokens of this type work like that: the
lowercase tests for existence and the uppercase tests for non-existence. There is also a token for number
characters. Clear the regex box and type in:

`\d`

This highlights the '99' in the third sentence. Only digits are selected. Try the uppercase version:

`\D`

Everything except the '99' is selected. You can see that RegEx provides many convenient tokens for selecting
or not selecting very specific things. Lastly, we have the token for word and non-word characters:

`\w` for word, or `\W` for non-word

What is a word character? It's any character that is part of a word, excluding punctuation. Notice how the '99'
is also selected? This token makes no distinction between letters and digits. It finds anything that makes up
a word, i.e. a group of characters separated by spaces.

## Codealong: Write a Python Script Using Those Tokens

Alright, let's see how this works in a Python script. Enter this code in a new Python file:

```python
import re

line = "Count to 99"
result = re.findall(r"\d+", line)
print result     # Prints out 99
```

What is this code doing? First, to use regex in Python we need to import the `re` module. Then we set up
a line of text to check for matches. Then there is the line which sets up the regex pattern. Let's look
closely at this. We call `re.findall` to apply the pattern to the string. The first parameter is the regex.
It is preceded with a 'r' so that backslashes are not handled in any special way. Then, in quotes, is the
regular expression for digits we saw above. We added a plus symbol to allow the pattern to match one or
more characters. The second parameter is the string we want to search and then we store the result in the
variable named `result`. Finally, we print the result. The result from `findall()` comes out as a list
since more than one match may be found

Now, you change the regex in the quotes. Replace the `\d` with a `\w`. Be sure to leave the plus symbol
where it is. Now what is being printed? Each of the **word** matches from your regex in a list. Let's
look at some other regex tokens.

## Codealong RegEx101.com: Learn Tokens For Ranges and Repeats

Okay, let's see how we can put some of these together to make more useful patterns. Some of the more common
things you'll see used in regex are brackets. `[ ]` These are used to group a collection of characters we want
to test for. Anything listed in brackets will be tested to see if it occurs in the string. Recall that when
we simply listed characters, like the string 'many', it was testing that exact order of characters. With the
brackets, we test each included token separately.

Let's go back to http://regex101.com and enter a new bit of text to play with. Clear the big box and copy and paste this string:

> I have a protocol droid named D-4PO, no relation. I have an astromech droid named R6\C6[Q6]. His name
sometimes causes problems. I also rigged a communications droid named IEEE 802-11.

If we wanted to see all the matches for any vowel letter, we could use a regex like so:

`[aeiou]`

That looks like it's mostly matching all the vowels. Do you see any problems? It is not matching the capital
vowels. RegEx is very specific. Let's add the capital vowels to our regex:

`[aeiouAEIOU]`

Now, we're matching all vowels, upper and lower case. But notice how they don't need to be in any order or adjacent to each other. Each token in the brackets is tested separately. Let's try it with some of the type
tokens we learned above:

`[\s\d]`

Do you recall what this is matching? All whitespace and all digits. By now, you may have thought of a
potential problem. What if we want to select the dash characters specifically? Seems like we could just
add it to our list of tokens in the brackets:

`[\s\d-]`

Yes, that worked. Now how about the backslash in the R6 unit's name - can we grab it in the same way?

`[\s\d\]`

No! This gives us a pattern error. This is because the backslash is a special character in regex. It is
called an escape character. It is used to mark those special type flags we used above so when the regex
parser reads a backslash it expects a flag character to follow. In order to test for a backslash, we
need to "escape" it by adding another backslash:

`[\s\d\\]`

A few characters that are used by regex need to be "escaped" in order to be used as test tokens, most
notably the backslash and the brackets:

`[\\\[\]]`

Anytime you're looking for a backslash or a square bracket, just remember to add a preceding backslash.

You can also put ranges of alphanumeric characters into the brackets. Want to find any capital letters
without typing the entire alphabet into the brackets? Try this:

`[A-Z]`

Numbers `ex. [1-6]` and lowercase letters `ex. [n-z]` work as you would expect. The ranges you choose are up to
you and what makes sense in your scripts. You can also use a special __not__ character to make logical
exclusions:

`[^a-n]`

This selects all characters that are **not** the letters 'a' through 'n'. You can see how powerful this can
grow to be - and we are only scratching the surface of RegEx. Let's cover one more type of token - repeats.
When testing for simple repeats, you can use the plus symbol:

`g+`

The plus symbol will match one or more occurrences of a character. It even works on bracketed sets:

`[gm]+`

That regex will match one or more 'g' characters and one or more 'm' characters. We can also be more
specific about the number of repeats. By following a letter with curly braces containing a range of
numbers, we can test for a certain amount of repeats or a range:

```python
E{3}   # matches exactly 3 occurrences of E
E{2,}  # matches 2 or more E's (leave off the end number)
E{2,5} # matches between 2 and 5 E's
```

It's worth mentioning that matching a set of 3 repeated capital E's is different than matching each
individual E once for a total of 3 matches. These repeat tests in the curly braces are testing for the
existence of a substring where E occurs a specific number of times. Testing for any capital E will highlight the same letters but it produces multiple matches in the string whereas testing for a repeat E only matches once if it finds the character repeated that many times.

## Exercise: Write a Python Script Using All Tokens We’ve Learned

Okay, time to code again. Create a new Python file with the following code:

```python
import re

line = "I have a protocol droid named D-4PO, no relation. I have an astromech droid \
named R6\C6[Q6]. His name sometimes causes problems. I also rigged a communications \
droid named IEEE 802-11."
result = re.findall(r"E{3}", line)
print result
```

Looks like this code is finding any triple-Es in our string. Now try replacing the regex with some
of the other ones we learned. Try adding some characters inside brackets.

## Review exercise

Now it's your turn to write a script from scratch. Remember to import the `re` module. Use a string
that contains different kinds of characters.

## Review LOs and wrap up

* Regular Expressions are powerful, yet complicated, tools for pattern matching in strings.
* They let you search individual characters, types of characters, ranges and groups of characters.
* Learning the common tokens can save you a lot of time with complicated strings.
