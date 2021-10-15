"""This would be a python program to reverse a given number. 
    The number is given as input by the user. Also add a function here to check if number is palindrome. 
    If it is it prints "Palindrome" else prints "Not a palindrome".
    Ex: 4321 --> 1234 Not a palindrome
    Ex: 12321 --> 12321 Palindrome
    """

num = int(input("Enter a number : "))
n = num  # Creating another variable to store num value as its value changes during the program.
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print(f"Reversed Number is : {reversed_num} ", end="")  # Printed using format string.


if (
    n == reversed_num
):  # Here n is compared with reversed_num as num value changes during program.
    print("Palindrome !")
else:
    print("Not a Palindrome !")
