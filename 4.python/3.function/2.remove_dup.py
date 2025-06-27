def remove_duplicate(numbers):
    unique_numbers = []

    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers

def remove_duplicate2(numbers):
    return list(set(numbers))

def remove_duplicate3(numbers):
    temp_dict = dict(zip(numbers,[i for i in range(len(numbers))]))
    unique_numbers = list(temp_dict.keys())
    return unique_numbers
    

numbers = [1,2,3,4,3,2,1,5,6,7,6,5]
# print(remove_duplicate(numbers))
print(remove_duplicate2(numbers))
print(remove_duplicate3(numbers))

