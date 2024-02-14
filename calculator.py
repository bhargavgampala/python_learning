# def main():
#     x = int(input("What's x? "))
#     print("x squared is", square(x))

# def square(n):
#     return n * n
# main()

# I've defined a function called Main and I've implemented two lines.
# The first of these lines prompts the user for a value x and converts it to an INT and stores it in a variable called x.
# On line 3, I then say x squared is and then
# I pass a second argument to the print function, whatever the return value is of a square function. 



# If the user enters something that cannot be converted into an integer using int(), the program will raise a ValueError. 
# To handle this gracefully, you might want to catch this exception and prompt the user to enter a valid integer.

def main():
    try:
        x = int(input("What's x? "))
        print("x squared is", square(x))
    except ValueError:
        print("Please enter a valid integer.")

def square(n):
    # return n ** 2
    # return n * n
    return pow(n, 2)

main()

# And here too there's going to be so many ways to solve this same problem.
# I can actually raise n to the power of 2.
# We've not seen this syntax before, but if you use two asterisks like this, two stars, 
# that raises the thing on the left to the power on the right.

# Or it turns out there is in Python a function called
# POW for raising something to the power that takes two arguments, the first of which is the number, the second of which is the exponent.
# So there too, there's just so many ways to actually solve that same problem
