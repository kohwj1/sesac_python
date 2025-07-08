from flask import Flask, render_template, request
import re
import ipaddress

DESCRIPTION = """
CIDR IP 주소는 비트 그룹이라고 불리는 두 개의 숫자 그룹으로 구성된다.
네트워크 주소와 호스트 식별자로 구성되어 있으며, IP 주소를 세 블록 중 하나로 분류해야 하는 클래스 기반과 달리
CIDR는 IP 주소 블록을 인터넷 서비스 공급자에게 할당할 수 있다.
그런 다음 인터넷 서비스 제공사업자는 할당 받은 블록을 분할하여 고객에게 할당할 수 있다.
지금 우리가 통신사를 통해 할당 받은 IP 주소가 이런 식으로 할당된 것이다.

CIDR 이전에는 A, B, C, D와 같은 클래스 기반을 통해 IP 주소의 범위를 표기하였는데,
이 방법을 더 이상 사용하지 않고 새로운 방법이라는 의미에서 CIDR의 명칭에 Classless로 표기되었으며,
클래스 대신 CIDR 블록과 서브넷 마스크 형태로 IP 주소의 범위를 표기한다.
"""

def is_validip(ip):
    pattern = re.compile(r'^(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d{2}|(0|[1-9]\d?))){3}$')
    return bool(pattern.match(ip))

def cal_cidr(ip, suffix):
    my_ip = list(ipaddress.ip_network(f'{ip}/{suffix}').hosts())
    return (my_ip[0], my_ip[-1])

app = Flask(__name__)

@app.route('/')
def home():
    ip = '192.168.0.0'
    suffix = '24'
    return render_template('cidr.html', ipaddress=ip, blocklength=suffix, description=DESCRIPTION)

@app.route('/calculate',methods=['POST'])
def display_result():
    ip = request.form.get('ipaddress') #body 파라미터 파싱
    suffix = request.form.get('blocklength') #body 파라미터 파싱

    if ip and suffix:
        if is_validip(ip):
            try:
                ip_range = cal_cidr(ip, suffix)
                msg = f'IP 범위: {ip_range[0]} ~ {ip_range[1]}'
            except ValueError:
                msg = '[!] 입력 범위 계산 시 호스트 비트가 포함되어 있습니다. 올바른 CIDR을 입력해주세요!'
            return render_template('cidr.html', msg=msg)
    return render_template('cidr.html', msg='[!] IP주소와 블록 길이를 올바르게 입력해주세요!')

if __name__ == '__main__':
    app.run(debug=True)