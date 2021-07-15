#쿠키 인증 웹 페이지 가져오기
import urllib.request, urllib.parse, http.cookiejar
cj=http.cookiejar.CookieJar() #책에는 상위클래스인 http가 적혀있지 않아서 오류가 나므로 http. 추가
cookie_handler=urllib.request.HTTPCookieProcessor(cj)
opener=urllib.request.build_opener(cookie_handler)
urllib.request.install_opener(opener)

def my_request(url, postfields):
    headers={'User-agent':'Mozilla/4.0(compatible; MSIE 5.5; Windows NT)'}
    req=urllib.request.Request(url, postfields, headers)
    response=urllib.request.urlopen(req)
    return response

def login(usernaem, password):
    login_url='http://logins.daum.net/accounts/login.do'
    form_values={'id':username,'pw':password,}
    formdata=urllib.parse.urlencode(form_values)

    try:
        response=my_request(login_url,formdata.urlencod()) #formdata 인스턴스의 하위 클래스에는 encode가 아니라 urlencode이므로 url추가 
    except IOError as e:
        print('We failed to open "%s".'%login_url)
        if hasattr(e,'code'):
            print('We failed with error coed - %s.'%e.coed)
        raise SystemExit
    else:
        pass

def getPage(url):
    response=my_request(url, None)
    return response.read()

def run():
    login('my_login_id', 'my_password') #자신의 다음 아이디와 비밀번호
    url='http://duam.net/'
    html=getPage(url)
    print('내정보' in html)
    url='http://mail2.daum.net/hanmailex/simple/Top.daum'
    html=getPage(url).decode()
    print('내게쓴편지함' in html)

if __name__ == '__main__':
    run()
