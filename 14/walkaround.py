from PIL import Image

im = Image.open('wire.png')
out1 = Image.new('RGB',(100,100))

imdata = im.getdata()

z = 0

for y in range(0,100):
    for x in range(0,100):
        pixel = imdata[z]
        out1.putpixel((x,y),pixel)
        z += 1
out1.save('out1.png')



coord = (-1,0)
length = 100
z = 0
out2 = Image.new('RGB',(100,100))

while length > 0 :
    orders = [ ((1,0),length) , ((0,1),length-1) , ((-1,0),length-1) , ((0,-1),length-2) ]

    for order in orders :
        direction,distance = order
        for i in range(0,distance):
            coord = ( coord[0]+direction[0] , coord[1]+direction[1] )
            pixel = imdata[z]
            out2.putpixel(coord,pixel)
            z += 1
            
    length -= 2
out2.save('out2.png')
