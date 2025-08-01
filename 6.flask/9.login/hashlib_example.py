import hashlib
import bcrypt

def generate_hash(pw):
    # 소금 안 뿌린 버전
    # result = hashlib.sha256(pw.encode()).hexdigest()
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pw.encode(), salt)

hashed_pw1 = generate_hash('hello123')
hashed_pw2 = generate_hash('hello123')

print(f'hash1: {hashed_pw1}')
print(f'hash2: {hashed_pw2}')

#--> 해시 처리만 하면 (평문 기준) 같은 비번이면 해시된 비번도 똑같다
# hash1: 27cc6994fc1c01ce6659c6bddca9b69c4c6a9418065e612c69d110b3f7b11f8a
# hash2: 27cc6994fc1c01ce6659c6bddca9b69c4c6a9418065e612c69d110b3f7b11f8a

#그래서 salt를 뿌려야 함
# hash1: b'$2b$12$TdbbFpGt4HlhK.GsqtSBeONBtumcqZpuhgsU9Amp4i/jcXPmwnlWy'
# hash2: b'$2b$12$Qt1jTxo7WdMTxecHxUbZYOQWzs80mZxi83uvrXZhOBi1FcKXmMtym'

#같은 평문에 소금 뿌려서 상이해진 값을 어떻게 검증? bcrypt 안의 내부 검증 함수로 확인해야 함

def verify_pw(pw, hashedpw):
    return bcrypt.checkpw(pw.encode(), hashedpw)

print(f"암호 일치 여부 확인: {verify_pw('hello132', hashed_pw1)}")
print(f"암호 일치 여부 확인: {verify_pw('hello123', hashed_pw1)}")
