dice1 = (1, 2, 3, 4, 5, 6)
dice2 = (2, 3, 5, 7, 11, 13)
result_set = []

for d1 in dice1:
    for d2 in dice2:
        result_set.append(d1 + d2)

print(set(result_set))
