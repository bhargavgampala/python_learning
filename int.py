x = 1
y = 2
z = x + y
print(z)

# Let's bring back that input function.
x = input("What's x? ")
y = input("What's y? ")
z = x + y
print(z)
# But the interesting thing here is that, when you get user input, because they're using a keyboard on their Mac
# or PC or their phone, it is always going to be text.

# we don't want to treat those inputs as strings,
# we want to treat them as actual numbers?
# Well we need another function and it turns out in Python
# that you can convert sometimes from one type of data to another type of data,
# for instance, from string to INT by doing something like this.
z = int(x) + int(y)
print(z)
# And let me now improve this, right?

"""
Do I really need the z variable?
It's worth noting that I'm creating a variable called z,
and then I'm immediately using it on the next line of code.
Now that's not that compelling, because if you're creating a variable
and then immediately using it, but never again using it,
did you really need to take the time to introduce another symbol
and another variable just to use it once and only once?
Well, maybe not.
"""

x = int(input("What's x? "))
y = int(input("What's y? "))
# Just like in math, if you have parentheses, parentheses, parentheses,your teacher probably taught you to focus
# on what's inside the innermost parentheses first and then work your way out.
print(x + y)
