# section02-1
# 파이썬 크롤링 기초
# urllib 사용법 및 스크랩핑

from urllib import request as req

# 파일 URL
img_url = "http://imgnews.naver.net/image/5353/2019/05/24/0000538290_001_20190524164450136.jpg"
html_url = "https://www.daum.net/"

# 다운받을 경로
save_path1 = "./data/test1.jpg"
save_path2 = "./data/index.html"

# 예외 처리
try:
    file1, header1 = req.urlretrieve(img_url, save_path1)
    file2, header2 = req.urlretrieve(html_url, save_path2)
except Exception as e:
    print("Download Failed")
    print(e)
else:
    # Header 정보 출력
    print(header1)
    print(header2)

    # 다운로드 파일 정보
    print("Filename1 {}".format(file1))
    print("Filename2 {}".format(file2))
    print()

    # 성공
    print("Download Succeed")
