year = int(input('What year were you born?'))

if year > 1996:
    generation = 'Generation Z'
elif year > 1980:
    generation = 'Millennial'
elif year > 1964:
    generation = 'Generation X'
elif year > 1945:
    generation = 'baby boomer'
elif year > 1924:
    generation = 'The Silent Generation'
else:
    generation = 'The Greatest Generation'

print(f"You're {generation}")