
#Count how many times "a" appears in a string using enumerate.

txt = 'enumerate'
count = 0

for index, char in enumerate(txt):
    if char == 'a':
        count += 1
print('Count of "a": ',count)