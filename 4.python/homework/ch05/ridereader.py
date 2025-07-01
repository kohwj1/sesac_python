def read(text):
    ridename = text.split(':')[0]
    condition = text.split(':')[1].lstrip().replace('cm','')

    cmmin = None
    cmmax = None

    if '~' in condition:
        cmmin = int(condition.split('~')[0])
        cmmax = int(condition.split('~')[1])
    elif '이상' in condition:
        cmmin = int(condition.split()[0])
    elif '이하' in condition:
        cmmax = int(condition.split()[0])
    else:
        pass

    return ridename, cmmin, cmmax


if __name__ == "__main__":
    ridename, cmmin, cmmax = read(input())
    print("이름:", ridename)
    print("하한:", cmmin)
    print("상한:", cmmax)

