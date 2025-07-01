import random

color = ['검은','하얀','붉은','파란','그린','옐로우']
word = ['콰삭칩','소보로','쭈꾸미','커피','세탁소','옹심이','풀스택']

color_range = random.randint(0, len(color)-1)
word_range = random.randint(0, len(word)-1)

print(color[color_range],word[word_range])