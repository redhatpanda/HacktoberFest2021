# This code will ask the number you want to find of
# after then it will show the multiplication table of that following number
# IF YOU WANT TO UPDATE THIS CODE FEEL FREE TO DO IT
# Thnkyou


# Multiplication table (from 1 to 10) in Python

num = 12

# To take input from the user
num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
