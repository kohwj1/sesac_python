# numbers = [1,3,5,7,9,11,13,15,17,19]
numbers = list(range(1,1000001))

def linear_search(numbers, target):
    count = 0
    for i in range(len(numbers)):
        count += 1
        if numbers[i] == target:
            print(f'비교 횟수: {count}')
            return i
    return -1

def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1
    count = 0
    while left <= right:
        count += 1
        mid = (left + right) // 2
        if numbers[mid] == target:
            print(f'비교 횟수: {count}')
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

target = 1000000
print(linear_search(numbers,target))
print(binary_search(numbers,target))