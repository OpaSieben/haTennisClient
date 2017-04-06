import urllib2

from client import Netcat


def gethash(inputhash):
    url = 'http://md5decrypt.net/Api/api.php?hash=' + inputhash + '&hash_type=sha256&email=MAIL&code=KEY'
    response = urllib2.urlopen(url, timeout=5)
    return response.read()


cl = Netcat("80.74.140.117", 8888)

print cl.read()
cl.write('y\n')
while 1:
    res = cl.read()
    print res
    split = str.split(res, '\n')
    for item in split:
        if len(item.strip()) == 64:
            answer = gethash(item.strip())
            print answer
            cl.write(answer+'\n')


