name = input("What's your name?").strip().title()
# split user's name into first name and last name
first, last = name.split(" ")
# say hello to user
print(f"hello, {first}")