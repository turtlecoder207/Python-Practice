#돈이 3000원 이상 있으면 택시를 타고 그렇지 않으면 걸어 가라
"""
money =1
if money >= 3000:
    print("택시를 타라")
else:
    print("걸어 가라")

#돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어 가라
money=2000
card=1

if money>=3000 or card:
    print('택시를 타라')
else:
    print('걸어 가라')

#만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어 가라
pocket = ['paper','cellphone','money']
if 'money' in pocket:
    print('택시를 타라')
else:
    print('걸어 가라')

#주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드로 없으면 걸어 가라
pocket = ['paper','cellphone']
card = 1
if 'money' in pocket:
    print("택시를 타라")
else:
    if card:
        print("택시를 타라")
    else:
        print("걸어 가라")

#using elif
pocket = ['paper','cellphone']
card = 1
if 'money' in pocket:
    print("택시를 타라")
elif card:
    print("택시를 타라")
else:
    print("걸어 가라")

#while문 기초
treeHit=0
while treeHit <10:
    treeHit = treeHit+1
    print("나무를 %d번 찍었습니다." %treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")

#continue 문장
a=0
while a<10:
    a= a+1
    if a%2 ==0: continue
    print(a)

#for문 기초
test_list = ['one','two','three']
for i in test_list:
 print(i)

#for문 응용: 총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고 그렇지 않으면 불합격이다.
# 함격인지 불합격인지 결과를 보여주시오

marks = [90,25,67,45,80]
for i in marks:
    if i > 60:
        print("%d점 받은 학생은 합격" %i)
    else:
        print("%d점 받은 학생은 불합격" %i)
"""
#리스트 안에 for문 포함하기
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print(result)





