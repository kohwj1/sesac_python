numbers = [3, 7, 2, 9, 1, 4, 5, 8, 6]

def find_max(numbers):
    max_num = 0  #잘못된 초기값 설정 시 오동작할 수 있음 (만약 리스트에 0보다 작은 수밖에 없다면?)
    max_num =  numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

print(find_max(numbers))
print(max(numbers)) #내장함수

numbers.sort(reverse=True) #굳아이디어!
print(numbers[0])