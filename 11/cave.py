from PIL import Image
import re


im   = Image.open('cave.jpg')
w,h = im.size

odd  = Image.new( 'RGB' , (w/2,h/2) , (255,255,255) )
even = Image.new( 'RGB' , (w/2,h/2) , (255,255,255) )

counter = 0

for y in range(0,h-1):
    # checkerboard - one that ended needs also to start
    counter += 1
    for x in range(0,w-1):
        counter += 1
        p = im.getpixel((x,y))
        if 0 == counter % 2:
            even.putpixel((x/2,y/2),p)
        else:
            odd.putpixel((x/2,y/2),p)
        
odd.save('odd.png')
even.save('even.png')
