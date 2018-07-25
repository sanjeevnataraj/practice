import random
print("\n ----------------------------------------")
print("| Welcome to the Dice Rolling Simulator  |")
print(" ----------------------------------------")
a=int(input("\nEnter the minimum range: "))
b=int(input("\nEnter the maximum range: "))
def Random(a,b):
        c=random.randint(a,b)
        print("\nThe Randomly Generated Number is :",c)
while True:
    print("\n ----------------------------------------")
    print("| Welcome to the Dice Rolling Simulator  |")
    print(" ----------------------------------------")
    print("Press Any of these option")
    print("1.play\n2.Help\n3.exit")
    n=int(input())
    if n==1:
        Random(a,b)
    if n==2:
        print("\n The simulator Randomly generate between Min_Range and Max_Range")
        print("\n The normall dice will have range between 1 to 6")
        print("\n Minimum number is 1")
        print("\n Maximum number is 6")
    if n==3:
        print("Thank you for playing dice stimulator")
        break
