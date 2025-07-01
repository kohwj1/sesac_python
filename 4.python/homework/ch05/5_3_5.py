def dooem(word):
    return []


com_list = ['게맛살', '구멍', '글라이더', '기차', '대롱', '더치페이', '롱다리', '리본', '멍게', '박쥐', '본네트', '빨대', '살구', '양심',
                   '이빨', '이자', '자율', '주기', '쥐구멍', '차박', '트라이앵글']
history = []
com_dict = {}


for item in com_list:
    com_dict[item[0]] = item


print('<시작>끝말잇기를 하자. 내가 먼저 말할게.\n기차')
computer_word = '기차'
history.append(computer_word)
com_list.remove(computer_word)


while True:
    user_input = input()
    
    if not user_input.startswith(computer_word[-1]):
        print('글자가 안 이어져. 내가 이겼다!<끝>')
        break

    elif user_input in history:
        print('아까 했던 말이야. 내가 이겼어!<끝>')
        break

    else:
        try:
            history.append(user_input)
            com_list.remove(user_input)
            computer_word = com_dict[user_input[-1]]
            history.append(computer_word)
            com_list.remove(computer_word)
            print(computer_word)
        except KeyError:
            print('모르겠다. 내가 졌어.<끝>')
            break