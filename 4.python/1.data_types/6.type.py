x = 5
y = 'hello'
z = [1,2,3]

print(type(x))
print(type(y))
print(type(z))

# print(x.upper()) --> 각 변수는 클래스로 되어 있고, 클래스 내의 함수를 통해 세부 클래스의 함수들이 동작한다. x는 int이므로 upper 함수 실행 불가
print(isinstance(x, int))
print(isinstance(y, int))
print(isinstance(y, str))
print(isinstance(x, (int, str))) # is x int or str?
print(isinstance(y, (list, str))) # is x int or str?


class A:
    pass

class B(A):  #A를 상속 받은 클래스 B
    pass

class C:
    pass

a = A()
b = B() #B 클래스의 인스턴스 b

print('---'*10)

print(isinstance(b, (A,C))) #A를 상속받은 B의 인스턴스이므로 True가 나온다
print(isinstance(a, (B))) #A는 B를 상속받는 관계가 아니므로 False
print(isinstance(b, (C))) #False
