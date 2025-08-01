import urllib.request
import json
from dotenv import load_dotenv
import os

#환경 설정파일을 읽어와 메모리에 올리는 함수
load_dotenv()

text = 'python 개발'
enc_text = urllib.parse.quote(text)


url = f'https://openapi.naver.com/v1/search/blog?query={enc_text}'

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", os.getenv('NAVER_CLIENT_ID'))
request.add_header("X-Naver-Client-Secret", os.getenv('NAVER_CLIENT_SECRET'))

res = urllib.request.urlopen(request)

res_code = res.getcode()

if res_code == 200:
    res_body = res.read()
    print(res_body.decode('utf-8'))