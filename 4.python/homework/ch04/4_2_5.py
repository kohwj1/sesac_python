score = [0, 0, 2, 4, 7, 7, 9, 11, 11, 13, 18, 20]
stem_leaf = [[], [], []]

for point in score:
    if point < 10:
        stem_leaf[0].append(point)
    elif point <20:
        stem_leaf[1].append(point % 10)
    else:
        stem_leaf[2].append(point % 20)


for i in range(len(stem_leaf)):
    print(f'{i}: {stem_leaf[i]}')