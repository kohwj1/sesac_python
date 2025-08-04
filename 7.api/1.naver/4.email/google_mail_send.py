import smtplib
from email.mime.text import MIMEText #메일 컨텐츠 인코딩
from dotenv import load_dotenv
import os

load_dotenv()

SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = os.getenv('SMTP_PORT')
GOOGLE_EMAIL = os.getenv('GOOGLE_EMAIL')
NAVER_EMAIL = os.getenv('NAVER_EMAIL')
GOOGLE_PASSWORD = os.getenv('GOOGLE_PASSWORD')
# https://support.google.com/accounts/answer/185833 여기 도움말 통해서 설정 가능

RECIPIENT = os.getenv('RECIPIENT')

#메일 컨텐츠
subject = '구글 이메일 테스트'
body = '이 메일은 파이썬을 통해 발송되엇습니당'

message = MIMEText(body, _charset='utf-8')
message['subject'] = subject
message['from'] = GOOGLE_EMAIL
message['to'] = NAVER_EMAIL

try:
    smtp = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtp.starttls()
    smtp.login(GOOGLE_EMAIL, GOOGLE_PASSWORD)
    smtp.send_message(message)
    print('발송 성공')
except Exception as e:
    print(e)
finally:
    smtp.quit()