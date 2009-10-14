import urllib,urllib2,re,cookielib,pickle,zlib,bz2


next_nothing = '12345'
solution = ''
i = 0

numbers = [12345]
cookie_collection = []

cookie_jar = cookielib.CookieJar()
cookie_processor = urllib2.HTTPCookieProcessor(cookie_jar)
opener = urllib2.build_opener(cookie_processor)
page = ''

while not solution :
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

numbers = [ int(n) for n in numbers ]
cookie_string = ''.join(cookie_collection)

print 'Sequence Length: ',len(numbers)
print 'Final item: '+page


# shortcut
#cookie_string = 'BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90'
unquoted = urllib.unquote_plus(cookie_string)

print 'raw: (',len(cookie_string),')',cookie_string
print 'unquoted: (',len(unquoted),')',unquoted

print bz2.decompress(unquoted)

