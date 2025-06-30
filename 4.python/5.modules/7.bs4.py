# 모듈 내의 특정 객체만 가져오기
from bs4 import BeautifulSoup as bs
import requests

response = requests.get('http://makemyproject.net')
# print(response)
# print(response.status_code)
# print(response.text)

#bs4로 응답 문서를 파싱해서 DOM(자료구조) 형태로 만들어 제어 가능
soup = bs(response.text, "html.parser")
body = soup.find('body')
body_text = body.text.rstrip()
print(body_text)