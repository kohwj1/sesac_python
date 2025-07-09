from flask import Flask, render_template, request
import re
import ipaddress

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
    return render_template('cidr.html', ipaddress=ip, blocklength=suffix)

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