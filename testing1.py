"""
임의의 문장(영문)의 대문자 알파벳만 수집하여 비밀 메세지를 찾아내는 함수를 만드시오

입력: string 타입의 텍스트 (유니코드)
출력: string 또는 빈 string인 비밀 메시지

예시1) find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO"
"""
def find_message(string):
    #문장을 띄어쓰기대로 나눠서 리스트 형식으로 보관한다.
    string_list = string.split()


    i = 0
    j = 0
    result = " "

    #나눈 단어의 한 글자씩 대문자인지 확인한다.
    #리스트(단어) 접근을 위한 for 문
    for i in range(len(string_list)):
        #리스트의 각 글자(단어의 각 글자) 접근을 위한 for 문
        for j in range(len(string_list[i])):
            #해당 리스트의 글자가 대문자이면, result에 추가
            if string_list[i][j].isupper():
                result  = result + string_list[i][j]

    return result

if __name__ == "__main__":

    secret_result1 = find_message("Blue Lemonade Use to bE my favorite drink")
    print (secret_result1)

    secret_result2 = find_message("coldplay")
    print(secret_result2)