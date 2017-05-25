'''
"숫자 야구"

◆Rule
- A가 1~9까지 서로 다른 숫자 세개로 구성된 세자리 수를 생각합니다. (ex. 369)
- B는 1~9까지 서로 다른 숫자 세개로 구성된 세자리 수를 A에게 묻습니다. (ex. 123)
- 자리와 숫자가 모두 일치하면 'Strike', 숫자는 일치하지만 자리가 맞지 않으면 'Ball', 아무것도 일치하는게 없으면 'Out'
(ex. A가 369 생각중에 B가 123을 물으면 0S 1B, 316을 물으면 1S 1B, 124를 물으면 Out)
- B가 세자리 수를 정확하게 맞추면 'Strike out'으로 게임 종료

입력 : 숫자 세자리 (ex. 369)
출력 : 입력한 숫자와 생각하고 있는 숫자를 비교해서 'Strike', 'Ball', 'Out', 'Strike out'을 출력합니다. (ex. 1S 1B)

PS. 위에 까지만 구현하시면 되고 여유 있으시면 입력했던 내용을 기억해서 출력마다 정답으로 유추가능한 경우의 수를 표시해주는 것도 해보시면 좋겠네요.
'''
import random

#세 자리 숫자를 random함수를 이용해 설정하고 스트링으로 변환시켜 thinker 변수에 할당한다.
thinker = str(random.randrange(100,1000))


strike = 0
ball = 0
def checkout(throw):

   for i in range(0,3):
        if thinker[i] == throw[i]:
            strike = strike +1
        elif thinker[i] == throw[i+1]:
            ball = ball+1
        elif thinker[i] == throw[i+2]:
            ball = ball+1


    if __name__ == "__main__":

        ask = input("숫자 세자리를 입력해주세요")
        str(ask)
        checkout(ask)

