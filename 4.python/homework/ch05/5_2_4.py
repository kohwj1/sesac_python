import sys
sys.path.append("../ch03")
from ridereader import read


rides = ['와일드 윙: 110cm 이상','드림보트: 120cm 이상', '자이안트 루프: 120cm 이상', '툼 오브 호러: -',
         '플라이벤처: 140cm~195cm' ,'회전목마: 100cm 이상', '매직 붕붕카: 110cm~140cm']


def allowedrides(height):
    assert type(height) == int

    result = []

    for ride in rides:
        name = read(ride)[0]
        cmmin = read(ride)[1]
        cmmax = read(ride)[2]

        if cmmin == None:
            cmmin = 0
        if cmmax == None:
            cmmax = 999

        if (height >= cmmin) and (height <= cmmax):
            result.append(name)

    return result


if __name__ == "__main__":
    height = int(input())
    print(allowedrides(height))

