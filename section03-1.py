# section03-1
# 기본 스크래핑 실습
# Get 방식 데이터 통신(1)

import urllib.request as req
from urllib.parse import urlparse, urlencode

# 기본 요청 1(encar)
url = "http://www.encar.com"

mem = req.urlopen(url)

# 여러 정보 출력
print("type : {}".format(type(mem)))
print("geturl : {}".format(mem.geturl()))
print("status : {}".format(mem.status))
print("header : {}".format(mem.getheaders()))
print("getcode : {}".format(mem.getcode()))
print("read : {}".format(mem.read(100).decode("utf-8")))
print("parse : {}".format(urlparse("https://www.encar.com?test=test").query))

# 기본 요청2(ipify)
API = "https://api.ipify.org"

# Get 방식 파라미터
values = {"format": "json"}

print("before param : {}".format(values))
params = urlencode(values)
print("after param : {}".format(params))

# 요청 URL 생성
URL = API + "?" + params
print("요청 URL = {}".format(URL))

# 수신 데이터 읽기
data = req.urlopen(URL).read()

# 수신 데이터 디코딩
text = data.decode("utf-8")
print("response : {}".format(text))
