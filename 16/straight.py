from PIL import Image

im = Image.open('mozart.gif')
#im = im.convert('RGB')
w,h = im.size
out = Image.new('RGB',(w,h))
outpix = out.load()

imd = list(im.getdata())

marker = [195,195,195,195,195]
marker_len = len(marker)

for y in range(0,h):
    for x in range(0,w):
        i = y*w + x
        slyce = imd[i:i+marker_len]
        if marker == slyce:
            before = imd[ y*w : i ]
            after  = imd[ i : i + w-x ]
            line = after + before
            for xo in range(0,w):
                outpix[xo,y] = line[xo]
            break

out.save('out.gif')
