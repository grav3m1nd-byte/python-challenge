from PIL import Image
import re

def isgrey(pixel):
    if pixel[0]==pixel[1] and pixel[1]==pixel[2]:
        return True
    else:
        return False

im = Image.open('oxygen.png')


w,h = im.size
print (w,h)

count = 0
greycount = 0
c = {}
for y in range(0,h-1):
    c[y] = 0
    for x in range(0,w-1):

        p = im.getpixel((x,y))
        count += 1
        if isgrey(p):
            greycount += 1
            c[y] += 1
print "count: "+str(count)
print "greycount: "+str(greycount)

avggrey = greycount / h
print 'average grey:'+str(avggrey)

for line,qty in c.items():
    if qty > avggrey:
        linetoscan = line
        break

print linetoscan

colors = []
currentcount = 0
lastcolor = False

countlimit = 7

for x in range(0,w-1):
    p = im.getpixel((x,linetoscan))
    if not isgrey(p):
        break
    color = p[0]
    if color == lastcolor and currentcount < 7:
        currentcount +=1
    else:
        colors.append((lastcolor,currentcount))
        currentcount = 1
    lastcolor = color

colors.append((lastcolor,currentcount))
finalstr = ''

for color,count in colors:
    #print str(color)+':'+('#'*count)
    finalstr += chr(color)
print finalstr

m = re.search('\[([^\]]+)',finalstr)
numbers = m.group(1)
print numbers
l = numbers.split(', ')
print l
print ''.join([chr(int(n)) for n in l])
