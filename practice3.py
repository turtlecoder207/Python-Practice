#question1

def fib(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    return fib(n-2)+fib(n-1)

#c = fib(3)
#print(c)

for i in range(10):
    print(fib(i))


#question2

#f=open("sample.txt")
#lines = f.readlines()
#f.close()

#total=0
#for line in lines:
#    score = int(line)
#    total += score

#average = str(total /len(lines)) #len함수!

#f=open("result.txt",'w')
#f.write(average) #write이라는 함수에는 문자열 형태만 사용 가능함!
#f.close()
