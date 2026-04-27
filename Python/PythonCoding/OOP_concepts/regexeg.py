
import re

#beginning & ending
'''
txt = input('Enter a text: ')  # India is my country
bpat = input('Enter beginning pattern: ')  # India
epat = input('Enter ending pattern: ')  # country
bpat = '^' + bpat # ^India
epat = epat + '$'  # try$
if re.search(pattern=bpat, string = txt):
    print('Beginning pattern available')
else:
    print('Beginning pattern not available')

if re.search(pattern= epat, string = txt):
    print('ending pattern available')
else:
    print('ending pattern not available')

'''

#digit
'''mbno = input('Enter a mbno:')
pat = r"[0-9]"

if re.fullmatch(pattern = pat, string=mbno):
    print("Only digits")
else:
    print("Other chars available")
'''

#user_name

'''un = input('Enter UN:')
pat = r"^[a-z_]{8,}$"


if re.match(pattern=pat, string=un):
    print('Valid')
else:
    print('Invalid')
'''

#email
'''
email = input('Enter email:')
pat = r"^[a-zA-Z0-9_]+@[a-z]+\.[a-z]+$"

if re.match(pattern=pat, string=email):
    print('Valid')
else:
    print('Invalid')
'''

#password
'''
pwd = input('Password:')
pat = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@_-]).{8,}$"
if re.match(pattern=pat, string=pwd):
    print('Valid')
else:
    print('Invalid')
'''


txt = input('text:')
pat = r"\s+"

#print(re.sub(pattern=pat,string=txt,repl='*'))

print(re.split(pattern=pat,string=txt))




















