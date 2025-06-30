def sumOfDigits(num):
    answer = list(map(int,str(num)))
    return sum(answer)

print(sumOfDigits(47253))