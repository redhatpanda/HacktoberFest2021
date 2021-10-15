def sumcube(no):
    if no == 1:
        return 1
    else:
        return no * no * no + sumcube(no - 1)


while 1:
    n = int(input("enter the number : "))
    if n == -1:
        break
    print(sumcube(n))
