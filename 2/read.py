f = open('text.txt','r')
o = open('out.txt','w')

freq = {}

for line in f:
    for char in line:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
f.close()
f = open('text.txt','r')

rare = []
for char,count in freq.items():
    if count < 10:
        rare.append(char)

for line in f:
    for char in line:
        if char in rare:
            print char

#items = [(v,k) for k,v in freq.items()]
#items.sort()
#items.reverse()
#outstr = ''
#for pair in items:
#    outstr += pair[1] + '\t' + str(pair[0]) + '\n'
#o.write(outstr)
#o.close()
