import random
print('::::Welcome to Dice number Generator::::')
c = input('Type start to continue: ')
if c== 'start' or c == 'START':
    x = 'y','yes','YES','Y'
    while x == x:
        ch = random.randint(1,6)
        print('The value on the dice is:',ch)
        if ch == 1:
            print(" _____ ")
            print("|     |")
            print("|  0  |")
            print("|_____|")
        elif ch == 2:
            print(" _____ ")
            print("| 0   |")
            print("|     |")
            print("|___0_|")
        elif ch == 3:
            print(" _____")
            print("|     |")
            print("|0 0 0|")
            print("|_____|")
        elif ch == 4:
            print(" _____")
            print("|0   0|")
            print("|     |")
            print("|0___0|")
        elif ch == 5:
            print(" _____")
            print("|0   0|")
            print("|  0  |")
            print("|0___0|")
        elif ch == 6:
            print(" _____")
            print("|0 0 0|")
            print("|     |")
            print("|0_0_0|")     
        else:
            ('Invalid value!')     
        x=input("\nReroll the dice? (yes/no):")
        if x=='no' or x=='n':
            break
        else:
            pass
