Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=5
b=str(a)
b
'5'
c=float(b)
c
5.0
d=str(c)
c
5.0
d
'5.0'
e=int(b)
e
5
x='hi'
y=int(x)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    y=int(x)
ValueError: invalid literal for int() with base 10: 'hi'
x='i'
y=int(x)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    y=int(x)
ValueError: invalid literal for int() with base 10: 'i'
y=bool(x)
y
True
x='i'
y=x
y=int(y)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    y=int(y)
ValueError: invalid literal for int() with base 10: 'i'
x=''
y=bool(x)
y
False
x='hiiiii'
y=bool(x)
y
True
print("hi")
hi
print(6+2)
8
print('ans:',6)
ans: 6
print('ans:' +6+3)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print('ans:' +6+3)
TypeError: can only concatenate str (not "int") to str
print('ans:' +'6+3')
ans:6+3
print('ans:' ,6+3)
ans: 9
print('my brother's house')
      
SyntaxError: unterminated string literal (detected at line 1)
print('my brother's house)
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("my frother's house")
      
my frother's house
input()
      
hii
'hii'
input()
      
350465
'350465'
p=input()
      
70
3
2
      
2
p=input()
      
7032
p
      
'7032'
p=input('type some thing:")
        
SyntaxError: unterminated string literal (detected at line 1)
p=input("type some thing:")
        
type some thing:7032
p
        
'7032'
>>> p=int(input('type something:'))
...         
type something:35353
>>> p
...         
35353
>>> KeyboardInterrupt
>>> p=float(input('type something:'))
...         
type something:54
>>> p
...         
54.0
>>> p=int(input('type something:'))
...         
type something:hdbsj
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    p=int(input('type something:'))
ValueError: invalid literal for int() with base 10: 'hdbsj'
>>> 
============= RESTART: C:/Wipro Training/Python/firstpgm.py ============
Hello World!!
>>> 
============ RESTART: C:/Wipro Training/Python/secondpgm.py ============
sum:  15
>>> 
=========== RESTART: C:/Wipro Training/Python/calculations.py ==========
give first num:6
give second num:10
sum:  16
