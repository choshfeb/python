#19.3
#urlparse
from urllib.parse import urlparse
o=urlparse('http://python.kw.ac,kr:8080/hello;parameters?a=b#fragment')
o
o.scheme
o.path
o.netloc
o.hostname
o.port
o.password
o.geturl()

#urlunparse
from urllib.parse import urlunparse
urlunparse(('http', 'python.kw.ac.kr', '/hello', '', '', ''))

#urlsplit
from urllib.parse import urlsplit
o=urlsplit('http://python.kw.ac.kr/hello;params?a=b#frag')
o
o.geturl()
o.scheme

#urlunsplit
from urllib.parse import urlunsplit
urllib.parse.urlunsplit(('http','pyton.kw.ac.kr','/hello;params','a=b','frag'))

#urlencode
from urllib.parse import urlencode
form = {'name': 'gslee', 'phone': '5284'}
urlencode(form)

#parse_qs
from urllib.parse import parse_qs as qs
qs('phone=1234&name=gslee&phone=5284')

#parse_qsl
from urllib.parse import parse_qsl as qsl
qsl('phone=1234&name=gslee&phone=5284')

#quote
from urllib.parse import quote as q
q('Nown !@#$%^')

#unquote
from urllib.parse import unquote as uq
uq('Nown%20%21%40%23%24%25%5E')

#quoto_plus
from urllib.parse import quote_plus as qp
qp('Nown !@#$%^')

#문서와 파일 가져오기
from urllib.request import urlopen
f=urlopen('http://www.python.org/')
print(f.headers)
html=f.read()
print(html)

#파일 내려받기
from urllib.request import urlretrieve as ur
url='http://www.python.org/ftp/python/3.3.0/python-3.3.0.msi'
fname,header = ur(url,'pyton-3.3.0.msi')
print(fname)

#쿠키 이늦ㅇ 웹 페이지 가져오기
#쿠키를 파일로 출력하거나 쿠키 파일을 읽어들일때
cj=cookiejar.LWPCookieJar()
cj.load(cookie_path, ignore_discard=True, ignore_exprice=True)
cj.save(cookie_path, ignore_discard=True, ignore_exprice=True)
