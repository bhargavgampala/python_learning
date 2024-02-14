x = float(input("what's x? "))
y = float(input("What's y? "))
print("##################################")
z= x + y
print(z)
print("##################################")
# I just want to round the result to the nearest possible integer, for instance.
# round(number, ndigits=None)
z = round(x + y)
print(z)
# What if I wanted this to be outputted as 1,000?
print("##################################")
print(f"{z}") # pass inputs as 999 and 1
print("##################################")
# I can put a colon after the z and I can put a comma thereafter.
print(f"{z:,}")
print("##################################")

# Division

a = float(input("what's a? "))
b = float(input("What's b? "))
z = a / b
print(z)
print("##################################")
# So here too we see a way of rounding now, not just to a nearest integer, but to a nearest number of digits.
z = round(a / b, 2)
print(z)
print("##################################")
# other way
# according to the documentation, the way you specify using an F string how many digits you want to print.
print(f"{z:.2f}")

