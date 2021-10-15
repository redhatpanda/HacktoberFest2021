# Taking the sentence Input
S = input("Enter Your Sentence Here: ")


D = {}
# SS = S.split()
for item in S:
    if item in D:
        D[item] = D[item] + 1
    else:
        D[item] = 1

print(D)
