# section04-3
# Requests
# requests 사용 스크래핑(3) - Rest API

# Rest API : GET, POST, DELETE, PUT : UPDATE, REPLACE(FETCH : UPDATE, MODIFY)
# URL을 활용해서 자원의 상태 정보를 주고 받는 모든 것을 의미

import requests

# 세션 활성화
s = requests.Session()

# ex1
r = s.get("https://api.github.com/events")

# 수신상태 체크
r.raise_for_status()

# 출력
print(r.text)

# ex2
# 쿠키설정
jar = requests.cookies.RequestsCookieJar()

# 쿠키 삽입
jar.set("name", "goodsoul", domain="httpbin.org", path="/cookies")

# 요청
r = s.get("http://httpbin.org/cookies", cookies=jar)

# 출력
print(r.text)

# ex3
r = s.get("https://github.com", timeout=5)

# 출력
print(r.text)

# ex4
r = s.post("http://httpbin.org/post", data={"id": "test", "pw": "111"}, cookies=jar)

# 출력
print(r.text)
print(r.headers)

# ex5
# 요청(POST)
payload1 = {"id": "test", "pw": "111"}
payload2 = (("id", "test"), ("pw", "1111"))

r = s.post("http://httpbin.org/post", data=payload2)

# 출력
print(r.text)

# ex6(PUT)
r = s.put("http://httpbin.org/put", data=payload1)

print(r.text)

# ex7(DELETE)
r = s.delete("http://httpbin.org/delete")

print(r.text)

r = s.delete("https://jsonplaceholder.typicode.com/posts/1")

print(r.text)

s.close()
