def sumOfDigits(num):
    num_str = str(num)
    answer = []
    for i in range(len(num_str)):
        answer.append(int(num_str[i]))
    
    print(sum(answer))

sumOfDigits(123)