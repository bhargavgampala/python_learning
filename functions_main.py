# def main():
#     name = input("What's your name? ")
#     hello(name)

# def hello(to="world"):
#     print("hello," , to)

# main()


# Scope refers to a variable only existing in the context in which you defined it.
def main():
    name = input("What's your name? ")
    hello()

def hello():
    print("hello," , name)

main()