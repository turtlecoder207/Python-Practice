"""
def sum (a,b):
    return a+b
a=3
b=4
c = sum(a,b)
print(c)


#여러 개의 입력값을 받는 함수 만들기
def sum_many(*test):
    sum=0
    for i in test:
        sum = sum+i
    return sum
result = sum_many(1,2,3,4)
print(result)

def say_myself(name, old, man=True):
    print("my name is %s" % name)
    print("I'm %d years old" % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다")
say_myself("hj",25,False)
say_myself("john",25)

#vartest.py
a=1
def vartest(a):
    a=a+1
    print(a)

vartest(a)


#vartest2.py
a=1
def vartest(a):
    a=a+1
    return a
a= vartest(a)
print(a)
"""
#input.py
a = input()
