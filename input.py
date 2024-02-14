# ask user for name
name = input("what's your name?")
print ("hello, world")
print("name")
print(name)
# say hello to user
print("hello, " + name)
print("hello, ", name) # it give two spaces
print("hello,", name) # it give one space
print("hello,", name,name) # , add spaces between variables
# print moving the cursor automatically for me to the next line
"""
print(*objects, sep=' ', end='\n', file=None, flush=False)¶
when you pass multiple arguments to print, by default
they're going to be separated by a single space.
By default, when you pass arguments to print,
it's the whole thing is going to be ended with a new line.
"""
print("hello, ")
print(name)
# how to stop using new line? by adding end
print("##################################")
print("hello, ",end="")
print(name)
print("hello, ",end="???")
print(name)
# how to overwrite the default space with comma
print("##################################")
print("hello,", name)
print("hello,", name, sep="???")
# how to print double quotes around a string
print("##################################")
print('hello, "friend"')
# or use escape character(back slash)
print("hello, \"friend\"")
# What if I put curly braces or curly brackets around the variable's name?
print("##################################")
print("hello, {name}")
# If you put an F at the beginning of the string,
# right before the first quote mark, that's a clue to Python that, ooh,
# this is a special string.
# Let me format this in a special way for you.
print(f"hello, {name}")
print("##################################")
# Remove white space from string.
name= name.strip()
print(f"hello, {name}")
print("##################################")
# Well I could capitalize the user's input.
name = name.capitalize()
print(f"hello, {name}")
# OK, so ironically, "capitalize" is not really capitalizing everything we want.
# It's clearly capitalizing what?
# Just the very first letter.

print("##################################")
# There's yet another function that comes with strings called Title that do title-based capitalization, 
# just like a book or a person's name, capitalizing the first letter of each word.
name = name.title()
print(f"hello, {name}")
print("##################################")
# Do I really need this much?
# Well, not necessarily.
# Watch what I can also do in Python.
# Let me not bother capitalizing the user's name separately.
# remove all name = variable assignment and use only a below
name = name.strip().title()
print(f"hello, {name}")
print("##################################")
# we can use stripe and title directly at input funtion
name = input("What's your name?").strip().title()
print(f"hello, {name}")