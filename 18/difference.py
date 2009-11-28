from PIL import Image,ImageChops

im = Image.open('balloons.jpg')

im1 = im.crop((0,0,375,335))
im2 = im.crop((375,0,750,335))

#im1.save('lighter.jpg')
#im2.save('darker.jpg')

limit = 2
for i in range(0,limit):
    diff = ImageChops.difference(im1,im2)
    diff.save(str(i)+'.jpg')
    diff.show()
    im1 = im2
    im2 = diff
