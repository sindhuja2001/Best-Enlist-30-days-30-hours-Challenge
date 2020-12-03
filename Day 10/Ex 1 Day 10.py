#1) To check a string that contains only a certain set of characters

import re
def check(string):
    A= re.compile(r'[^a-zA-Z0-9.]')
    string= A.search(string)
    return not bool(string)
print(check("Apple1234"))

#2) Check it matches a word 'ab'

import  re
def A(text):
    pattern= '\w*ab\w*'
    if re.search(pattern, text):
        return 'found!'
    else:
        return 'Not Found!'
print(A("Abundant"))

#5) To match a string that contains uppercase letter

import re
def A(text):
    pattern= '^[a-zA-Z0-9_]*$'
    if re.search(pattern, text):
        return 'Found!'
    else:
        return 'Not found!'
print(A("Abc"))

#3) To check a number at the end of the sentence

import re
def number(string):
        text= re.compile(r".*[0-9]$")
        if text.match(string):
            return True
        else:
            return False
print(number("Abc99"))

#4) To search the numbers(0-9) of length between 1 to 3 in a given string

import re
res= re.finditer(r"([0-9]{1, 3})", "Exercise number 1, 12, 123 are important")
for n in res:
    print(n.group(0))

