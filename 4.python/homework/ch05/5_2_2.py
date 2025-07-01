# 파이썬 shell에 아래 내용 입력
a = 3
b = 4
c = (a ** 2 + b ** 2) ** 0.5

# >>> a = 3
# >>> b = 4
# >>> c = (a ** 2 + b ** 2) ** 0.5
# >>> print(c)
# 5.0

def hypotenuse(a, b):
    return round((a ** 2 + b ** 2) ** 0.5, 2)