import zipfile,re



z = zipfile.ZipFile('channel.zip')
n = '90052' ;

solution = False
comments = ''

while not solution:
    f = z.open(n+'.txt')
    comments += z.getinfo(n+'.txt').comment
    
    fstr = f.read()
    match = re.search('Next nothing is (\d+)',fstr)
    if match:
        #print n
        n = match.group(1)
    else:
        solution = fstr
        print fstr

print comments
