"""
"로마숫자 출력하기"
설명:
1 부터 10까지의 로마 숫자는 아래와 같습니다.
I, II, III, IV, V, VI, VII, VIII, IX, X.

로마 숫자는 7가지의 심볼의 조합으로 만들어집니다.
I 1
V 5
X 10
L 50
C 100
D 500
M 1,000

문제: 1 부터 3999 사이의 정수를 입력했을 때 로마 숫자를 출력해주는 함수를 만드십시오.

입력 값: 1 부터 3999 사이의 정수
출력 값: 스트링 형식의 로마 숫자

예)
foo(6) == 'VI'
foo(76) == 'LXXVI'
foo(13) == 'XIII'
foo(44) == 'XLIV'
foo(3999) == 'MMMCMXCIX'

"""
def div1000(test1):
    #이 함수가 포인트임. 리스트를 절댓값으로 오름차순으로 정렬한다.
    result = sorted(test1, key=abs, reverse=False)

    return result

if __name__ == "__main__":
    list1 = [-20, -5, 10, 15,-30, 50]
    result = checkio(list1)
    print(result)