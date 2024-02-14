# def main():
#     name = input("What's your name? ")
#     hello(name)

# def hello(to="world"):
#     print("hello," , to)

# main()


# Scope refers to a variable only existing in the context in which you defined it.
# def main():
#     name = input("What's your name? ")
#     hello()

# def hello():
#     print("hello," , name)

# main()

# NameError: name 'name' is not defined

def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("hello," , to)

main()

# Now that we've implemented Hello, you'll notice that Hello only has a so-called side effect.
# It only prints out something to the screen.
# Well, what if I also want my function to not have a side effect, per se, but actually hand me back a value?
# Recall that the input function returns a value, the string that the user typed in.
# Recall that the INT function returns a value.
# The float function returns a value that was passed into it.
# Well you can use one final keyword here, literally
# Return to return a value explicitly yourself.

# calculator.py