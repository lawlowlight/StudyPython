# 네이버 웹페이스 긁어오기
from urllib import request
from urllib.request import Request, urlopen

req = Request('https://www.naver.com/')
res = urlopen(req)
print(res.status)


