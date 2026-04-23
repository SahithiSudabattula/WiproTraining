'''
#functions
def add(n1, n2):
    print('n1 ', n1)
    print('n2 ', n2)
    return n1 + n2

#driver
num1=int(input("enter first num:"))
num2=int(input("enter second num:"))

result = add(num1, num2) #possitional
print('addition:',result)

result = add(n2=num2, n1=num1) #keyword
print('addition:',result)


#from basic_programs.While_looping import count

def sub(n1,n2):
    return n1 - n2

def multi(n1,n2):
    return n1 * n2

def div():
    pass

result = sub(num1, num2)
print('subtract:',result)

result = multi(num1, num2)
print('multi:',result)


#Arbitary_orguments
#functions
def add(*nums):
    sum = 0
    for n in nums:
        sum += n
    return sum

#driver
# numbers = list()
# count = int(input('How many ? '))
# for _ in range(1, count+1):
#     numbers.append(int(input('No: '))

print(add(*nums:5,6,9))
print(add(*nums:5,6))
print(add(*nums:5,6,9,3,10,8,7,23))



#Optional_arguments

def add(n1,n2,n3=10):
    return n1+n2+n3

num1=int(input("enter number:"))
num2=int(input("enter number2:"))

print(add(num1,num2))
print(add(num1, num2,100))

#Lambds

num1=int(input("enter number:"))
num2=int(input("enter number2:"))

add = lambda n1,n2 : n1+n2 

print(add(num1, num2))
'''


numbers = [1,2,3,4,5,6,7,8,9,10]

sq = lambda nums : [num *num for num in nums if num%2==0]
print((sq(numbers)))

# sq = lambda nums : (num *num for num in nums)
# print(tuple( sq(numbers)))






