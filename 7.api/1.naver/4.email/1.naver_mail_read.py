import imaplib
import email
from email.header import decode_header
from dotenv import load_dotenv
import os

load_dotenv()

IMAP_SERVER = os.getenv('IMAP_SERVER')
IMAP_PORT = os.getenv('IMAP_PORT')
NAVER_EMAIL = os.getenv('NAVER_EMAIL')
NAVER_PASSWORD = os.getenv('NAVER_PASSWORD')

mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
mail.login(NAVER_EMAIL, NAVER_PASSWORD)

mail.select('inbox')
status, messages = mail.search(None, 'All')

# print(status, messages)

mail_ids = messages[0].split()
latest_mail_id = mail_ids[-1]

status, msg_data = mail.fetch(latest_mail_id, "(RFC822)")
# print(status, msg_data)

for response_part in msg_data:
    if isinstance(response_part, tuple):
        msg = email.message_from_bytes(response_part[1])

        #제목 디코딩
        subject, encoding = decode_header(msg['subject'])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding if encoding else 'utf-8')
        print(f'메일 제목: {subject}')

        #발신자
        from_ = msg.get('From')
        print(f'보낸 사람: {from_}')

        #본문 (첨부파일 있을 수도 있으므로 멀티파트)
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                body = part.get_payload(decode=True).decode('utf-8')
        else:
            body = msg.get_payload(decode=True).decode('utf-8')
            break
        
print(f'본문: {body}')

mail.logout()
