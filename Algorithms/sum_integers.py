def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)


while 1:

    n = int(input("Enter number :"))
    if n == -1:
        break
    print(sum(n))
