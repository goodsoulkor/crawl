# section02-2
# 파이썬 크롤링 기초
# urlopen 함수 기초

import urllib.request as req
from urllib.error import URLError, HTTPError

# 다운로드 경로 및 파일명
path_list = ["./data/test1.jpg", "./data/index.html"]

# 다운로드 리소스 url
target_list = [
    "http://imgnews.naver.net/image/5120/2020/01/17/0000141371_001_20200117203403732.jpg",
    "http://google.com",
]

for i, url in enumerate(target_list):
    # 예외처리
    try:
        # 웹 수신 정보 읽기
        response = req.urlopen(url)

        # 수신 내용
        contents = response.read()

        # 상태 정보 중간 출력
        print("-----------------------------------")
        print("Header Info-{} : {}".format(i, response.info()))
        print("HTTP Status Code : {}".format(response.getcode()))
        print()
        print("-----------------------------------")

        # 파일 생성
        with open(path_list[i], "wb") as f:
            f.write(contents)

    except HTTPError as e:
        print("Download Failed")
        print("HTTPError Code :", e.code)
    except URLError as e:
        print("Download Failed")
        print("URLError Reason :", e.reason)
    else:
        print()
        print("Download Complete")
