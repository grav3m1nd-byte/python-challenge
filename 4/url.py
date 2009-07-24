import urllib,re


next_nothing = '46059'
solution = ''
i = 0

while i < 400 and not solution:
    i += 1
    u = urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+next_nothing)
    page = u.read()
    match = re.search('and the next nothing is (\d+)',page)
    if match:
        next_nothing = match.group(1)
        print next_nothing
    else:
        solution = page

print 'Solution: '+page
