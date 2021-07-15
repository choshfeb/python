‘이강성’.encode(‘utf-8’)

import urllib.parse
urllib.parse.quote('이강성')

urllib.parse.unquote('%EC%9D%B4')
urllib.parse.unquote('%EA%B0%95')
urllib.parse.unquote('%EC%84%B1')

a = ''.join([chr(b) for b inb'\xec\x9d\xb4\xea\xb0\x95\xec\x84\xb1'])
print(a)

q = ''.join(['%{:X}'.format(ord(c)) for c in a])
q
urllib.parse.unquote(q)

#import urllib.parse

def hello(environ, star_response):
    args = environ['url_args']
    if args:
        q = ''.join(['%{:X}'.format(ord(c)) for c in escape(args[0])])
        name = urllib.parse.unquote(q)
    else:
        name = 'world'
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    response = ['Hello {}'.format(name)]
    return (line.encode('utf-8') for line in response)
