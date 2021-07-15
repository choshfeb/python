#19.1.2
print('한글'.encode('utf-8'))


import sys
import codecs

w = codecs.getwriter('utf-8')(sys.stdout.buffer)
print('한글', file = w)



import cgitb; cgitb.enable(display= 0, logdir = '/tmp') #디버깅, 파일로저장
#4-1
w = codecs.getwriter('utf-8')(sys.stdout.buffer)
print('한글', file=w)

#4-2
writer = codecs.getwriter('utf-8')(sys.stdout.buffer)

print('Content-Type: text/html;charset=utf-8\n', file=writer)
print('''
<HTML>
<HEAD></HEAD>
<BODY>
<H2>한글</H2>
Hello again,
</BODY>
<HTML>
''', file=writer)

#
import cgi 

print(cgi.test())


# handle form

print('Context-Type: text/html;charset=utf-8\n\n')

print('''
<form name='form' method='post' action='/cgi-bin/index.py>
<p>
email:<input type='text' name='email'>
name:<input type='text' name='name'>
</p>
</form>
''')

#
import cgi
form = cgi.FieldStorage()
print(form.keys)
print(form.values)


email = form['email']
email = form.getvalue('email')

email = form.getvalue('email', 'default@email.address')

#
import cgi
import codecs
import sys
import cgitb; cgitb.enable()

w = codecs.getwriter('utf-8')(sys.stdout.buffer)

print('Content-Type:text/html;charset=utf-8\n\n', file=w)
form = cgi.FieldStorage()
for name in form.keys():
    print('Input: {} value : {} <br/>'.format(name, form.getvalue(name)),file=w)

print('Finished!', file=w)

#
import cgi
import codecs
import sys
import cgitb; cgitb.enable()

<input type='checkbox' name='composer' value='Bach'>
<input type='checkbox' name='composer' value='Hnadel'>
<input type='checkbox' name='composer' value='Mozart'>
<input type='checkbox' name='composer' value='BEethoven'>
<input type='checkbox' name='composer' value='Debussy'>

form = cgi.FieldStorage()
form.getfirst('composer', 'nobody')
form.getlist('composer')

#
<form name='form' method='post' action='/cgi-bin/upload.py' enctype='multipart/formd=-data'> 
<input type='file' name ='myfile'>
<input type='submit' value='Upload'>
</form>

form['myfile'].value
form['myfile'].filename
form['myfile'].file

#
s = form['myfile'].value
fname =  form['myfile'].filename
fileobj = form['myfile'].file
line = fileobj.readline()
b1 = fileobj.read(1024)
b2 = fileobj.read()

#
from string import Template
temp = Template(open('welcome.html', encoding='utf-8',).read())
name = 'lee gang sung'
print(temp.substitute(locals()))

#
temp.substitute(name= 'lee gang sung', phone = '5284')
temp.substitute(dict(name= 'lee gang sung', phone = '5284'))
temp.substitute({name= 'lee gang sung', phone = '5284'})

#
from http.cookies import Morsel
m = Morsel()
m.keys()
m['expires'] = 60 * 60
m['path'] = '/cgi-bin'
m['comment'] = 'last user\'s visit data'
m['domain'] = '.python.kw.ac.kr'
m['max-age'] = 30 * 24 * 60 * 60
m['secure'] = ''
m.output()

#
from http.cookies import SimpleCookie
import time

c = SimpleCookie()
c.keys()
c['session'] = str(time.time())
c['user'] = 'gslee'
c['session']['path'] = '/cgi-bin'
c['session']['domain'] = '.python.kw.ac.kr'
c['session']['expires'] = 30 * 24 * 60 * 60

#
c = SimpleCookie(os.environ['HTTP_COOKIE'])
session = c['session'].value
path = c['session']['path']

#
import cgi
import html

def hello_world(environ, start_response):
    form = cgi.FieldStorage(environ['wsgi'.input], environ=environ)
    name = html.escape(form.getvalue('name','World'))
    start_response('200 ok', [('Content-Type', 'text/html;charset=utf-8')])
    response=[' hello {0}'.format(name)]
    return (line.encode('utf-8') for line in response)

path_info = environ['PATH_INFO']
path_info = environ.get('PATH_INFO', '')

form = cgi.FieldStorage(environ['wsgi.input'], environ = environ)

email = form.getvalue(‘email’) #폼 필드를 읽는 예
name = cgi.escape(form.getvalue(‘name’, ‘World’), quote=True)

#start_response(status, headers) #start_response()함수의 형식

start_response(‘200 OK’, [(‘Content-Type’, ‘text/html’)])
start_response(‘200 OK’, [(‘Content-Type’, ‘text/html’), (‘Content-Length’, ’15’)])
start_response(‘404 NOT FOUND, [(‘Content-Type’, ‘text/plain’)])
start_response(‘500 INTERNAL SERVER ERROR’, [(‘Content-Type’, ‘text/plain’)])

Response = [‘안녕하세요 {0}’.format(name)]
Return (line.encode(‘uff-8’) for line in response)
