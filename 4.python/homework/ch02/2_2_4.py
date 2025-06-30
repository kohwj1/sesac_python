input_sum = 0
while True:
    number = int(input())
    if number < 0:
        break

    input_sum += number

print(input_sum)