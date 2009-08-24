
numfiles = 5

f = open('evil2.gfx','rb')
thebytes = f.read()

files = [ open('file'+str(i),'wb') for i in range(0,numfiles) ]

i = 0

for b in thebytes :
    cf = files[ i%numfiles ]
    cf.write(b)
    i += 1
