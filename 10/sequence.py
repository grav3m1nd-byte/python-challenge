import re

l = (1, 11, 21, 1211, 111221)

number = '1'
a = (number,)

for i in range(0,30):
    solution = ''
    m = re.finditer(r"(\d)\1*",number)
    for x in m:
        s = x.group(0)
        solution += str(len(s))+s[0]
    a += (solution,)
    number = solution

print(len(a))
print len(a[30])
