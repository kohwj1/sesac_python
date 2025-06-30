# 빌트인이 아닌 외부(pypi.org) 모듈 / 라이브러리
# 설치 위치: python 가상 환경 > Lib > site_package 폴더 안에 설치
# 즉, 가상환경을 바꾸면 내가 설치한 그 모듈이 없음 (환경 및 버전 분리)

import requests

response = requests.get('http://makemyproject.net')
print(response)
print(response.status_code)
print(response.text)