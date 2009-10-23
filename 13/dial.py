from xmlrpclib import ServerProxy

url = 'http://www.pythonchallenge.com/pc/phonebook.php'

sp = ServerProxy(url)

# print 'ServerProxy: ', sp
# print 'Server methods: ', sp.system.listMethods()
# print '"Phone" method: ', sp.system.methodSignature('phone')
# print sp.system.methodHelp('phone')

print sp.phone('Bert')
