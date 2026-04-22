"""
Date 22-4-2026
Desc: Learning various if stmt formats
"""
#Big2
'''
num1 = int(input("Enter first num:"))
num2 = int(input("Enter second num:"))
if num1 == num2:
    print("Both are Equal")
elif num1 > num2 :
    print(num1, "is big.")
else:
    print(num2, "is big.")
'''

#Big3
'''
num1 = int(input("Enter first num:"))
num2 = int(input("Enter second num:"))
num3 = int(input("Enter third num:"))

if num1 == num2 and num2 == num3:
    print("All are Equal")
elif num1 == num2 or num2 == num3 or num1 == num3:
    print("2 are Equal")
    
if num1 > num2 and num1 > num3:
    print(num1, "num1 is big.")
elif num2 > num1 and num2 > num3:
    print(num2, "num2 is big.")
elif num2 > num1 and num2 > num3:
    print(num3, "num3 is big.")
'''

#week_Day
'''
ch = int(input("Enter a num bet 1-7:"))

match ch:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thu")
    case 5:
        print("Fri")
    case 6:
        print("Sat")
    case 7:
        print("Sun")
    case _:
        print("Invalid choice")
'''


