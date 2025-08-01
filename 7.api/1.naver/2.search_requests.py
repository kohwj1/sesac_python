from dotenv import load_dotenv
import requests, os, json
from tabulate import tabulate

#환경 설정파일을 읽어와 메모리에 올리는 함수
load_dotenv()

text = 'python 개발'
enc_text = requests.utils.quote(text)

url = f'https://openapi.naver.com/v1/search/blog?query={enc_text}'
headers = {
    "X-Naver-Client-Id": os.getenv('NAVER_CLIENT_ID'),
    "X-Naver-Client-Secret": os.getenv('NAVER_CLIENT_SECRET')
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    response_body = response.text
    data = json.loads(response_body)

    selected_columns = [['title', 'link', 'description']]

    for item in data['items']:
        selected_columns.append([item['title'], item['link'], item['description']])
    
    print(tabulate(selected_columns, headers='firstrow', tablefmt='list'))