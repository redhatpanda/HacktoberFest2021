no = int(input("Enter a number: "))
no = str(no)
rev = no[::-1]
if no == rev:
    print(f"{no}--->{rev} Input is a palindrome")
else:
    print(f"{no}--->{rev} Input is not a palindrome")
