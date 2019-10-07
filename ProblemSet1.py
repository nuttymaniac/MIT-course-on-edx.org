# -*- coding: utf-8 -*-

count = 0
for letter in s:
    if letter == 'a' or  letter == 'i' or  letter == 'e' or  letter == 'o' or  letter == 'u':
        count += 1
print(count)

------------------------------------------------------------------------------------------

count = 0
for i in range(len(s)):
    if s[i:i+3] == 'bob':
        count += 1
print(count)

------------------------------------------------------------------------------------------

result = ''

while len(s) != 0:
    new = s[0]
    for i in range(len(s)-1):
        if s[i+1] >=  s[i]:
            new += s[i+1]
        elif s[i+1] <  s[i]:
            break
    if len(new) > len(result):
        result = new    
    s = s[1:]
    
print("Longest substring in alphabetical order is:" + result)



