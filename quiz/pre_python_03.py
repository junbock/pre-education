"""3.Enter key를 눌러 주사위를 던지게 한 후, 주사위의 눈이 높은 사람이 승리하는
간단한 주사위 게임을 만드세요


예시
<입력>
첫번째 참가자 엔터키를 눌러 주사위를 던져 주세요 : 1~6 랜덤숫자 출력
두번째 참가자 엔터키를 눌러 주사위를 던져 주세요 : 1~6 랜덤숫자 출력

<출력>
첫 번째(두 번째) 참가자의 승리입니다. or 비겼습니다.

"""
import random
print('첫번째 참가자 엔터키를 눌러 주사위를 던져 주세요: ')
input()
x = random.choice(range(1,7))
print(x)
print('두번째 참가자 엔터키를 눌러 주사위를 던져 주세요 : ')
input()
y = random.choice(range(1,7))
print(y)
if x == y:
    print('비겼습니다.')
elif x > y:
    print('첫번째 참가자의 승리입니다.')
elif x < y:
    print('두번째 참가자의 승리입니다.')
