# Simple way of printing Hello 
name = input("What's your name?").strip().title()
print(f"hello, {name}")

# a function that looks like it's called Hello, because why is it a function?
# It has a parenthesis and a closed parenthesis immediately after it.
# And that's what every function we've used has looked like.

#Firstname = input("What's your name?")
#hello()
#print(Firstname)

# code failed with     
# hello()
# NameError: name 'hello' is not defined


#  I'm going to first take a moment to define a function called Hello
# using DEF Hello, open parenthesis, close parenthesis, colon.
def hello():
    # What this means now is that Python is going to treat every line of code
    #that I indent underneath this one as the meaning of this new function, Hello.
    print("hello")

name = input("What's your name?")
hello()
print(name)

# I think we can probably do better than this by improving things further.
# Why don't we consider, though, how we might say parameterize this same function?
# That is to say, can we customize Hello to maybe take the user's name as input
# so that we can say, not only Hello, but the person's name all on one line, all in one breath?

# Passing arguments to function
def hello1(to):
    print("hello,", to)

name1 = input("What's your name1?")
hello1(name1)

# What am I doing on line 37? Same as always, I'm just getting the user's name.
# Line 38, I'm not only calling Hello, I'm passing as input the name variable as an argument
# so that that's what gets passed into Hello.

# And what's happening here is essentially this--
# even though the variable is called Name here, when the function itself is called, the computer assumes that same value is now called To.
# So Name is essentially copied to another variable called
# To so that in the context of Hello, I can say Hello to that variable instead.



# What if you wanted your Hello function to say Hello to someone specific,
# but, you know what, if you don't know who you want to say Hello to,
# you want to say Hello to the whole world,

# you can give parameters default values.
# Then on line 60, I'm going to get the name.
# Line 62, I'm going to call Hello with an argument.
# So you'll see Hello now being used in two ways.
def hello2(to="world"):
    print("hello,", to)
hello2()
name2 = input("What's your name2?")
hello2(name2)

#  if you use a function, it must already exist by the time you are calling it.
