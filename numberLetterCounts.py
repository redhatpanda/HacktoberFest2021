from num2words import num2words

# Project Euler Problem 17

letterCount = 0

for i in range(1, 1001):
    letterCount += len((num2words(i).replace(" ", "")).replace("-", ""))

print(letterCount)
