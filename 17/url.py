import urllib2,re,cookielib


next_nothing = '92512'
solution = ''
i = 0

numbers = [12345,92512]
cookie_collection = []

cookie_jar = cookielib.CookieJar()
cookie_processor = urllib2.HTTPCookieProcessor(cookie_jar)
opener = urllib2.build_opener(cookie_processor)

while i < 40 and not solution :
    i += 1
    u = opener.open('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='+next_nothing)

    # extract cookies
    for cookie in cookie_jar:
        cookie_collection.append(cookie.value)

    # get next number
    page = u.read()
    match = re.search('and the next busynothing is (\d+)',page)
    if match:
        next_nothing = match.group(1)
        numbers.append(next_nothing)
    else:
        solution = page


print cookie_collection
print urllib2.unquote(''.join(cookie_collection))
print 'Sequence Length: ',len(numbers)
print 'Final item: '+page

numbers = [ int(n) for n in numbers ]
