import re

f = open('text.txt')
o = open('out.txt','w')

filestr = ''

for line in f:
    filestr += line[:len(line)-1]

miter = re.finditer('(?<![A-Z])[A-Z]{3}([a-z])[A-Z]{3}(?![A-Z])',filestr)

outstr = ''

for m in miter:
    outstr += m.group(1)

print outstr
