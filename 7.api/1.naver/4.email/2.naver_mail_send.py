import smtplib
from email.mime.text import MIMEText #메일 컨텐츠 인코딩
from dotenv import load_dotenv
import os

load_dotenv()

SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = os.getenv('SMTP_PORT')
NAVER_EMAIL = os.getenv('NAVER_EMAIL')
NAVER_PASSWORD = os.getenv('NAVER_PASSWORD')

RECIPIENT = os.getenv('RECIPIENT')

#메일 컨텐츠
subject = '네이버 이메일 테스트'
body = '이 메일은 파이썬을 통해 발송되엇습니당'

message = MIMEText(body, _charset='utf-8')
message['subject'] = subject
message['from'] = NAVER_EMAIL
message['to'] = NAVER_EMAIL

# try:
#     smtp = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
#     smtp.starttls()
#     smtp.login(NAVER_EMAIL, NAVER_PASSWORD)
#     smtp.send_message(NAVER_EMAIL, RECIPIENT, message.as_string())
#     print('발송 성공')
# except Exception as e:
#     print(e)
# finally:
#     smtp.quit()

smtp = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
smtp.starttls()
smtp.login(NAVER_EMAIL, NAVER_PASSWORD)
smtp.send_message(message)
print('발송 성공')
smtp.quit()