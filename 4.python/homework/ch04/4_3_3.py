num_list = list(map(int, input().split()))

plus = num_list[0]
minus = num_list[0]
multiple = num_list[0]
divide = num_list[0]

for i in range(1, len(num_list)):
    plus += num_list[i]
    minus -= num_list[i]
    multiple *= num_list[i]
    divide /= num_list[i]

print(plus, end=' ')
print(minus, end=' ')
print(multiple, end=' ')
print(divide)