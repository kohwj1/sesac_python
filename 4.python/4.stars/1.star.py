# print('*')
# print('**')
# print('***')
# print('****')
# print('*****')

def draw_ltriangle(lines):
    # for i in range(lines):
        # print(i+1)
    for i in range(1, lines+1):
        print(i * '*')

def draw_rtriangle(lines):
    for i in range(1, lines+1):
        print((lines-i) * ' ', end='')
        print(i * '*')

def draw_iltriangle(lines):
    for i in range(lines,0,-1):
        print(i * '*')

def draw_irtriangle(lines):
    for i in range(lines,0,-1):
        print((lines-i) * ' ', end='')
        print(i * '*')



# draw_ltriangle(5)
# draw_iltriangle(5)
draw_irtriangle(5)