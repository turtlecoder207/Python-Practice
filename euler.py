#euler 1
"""
sum = 0

for i in range (1,1000):
    if (i%3 ==0) or (i%5==0) :
        sum = sum + i

print(sum)

"""
#euler2
def fib(n):
    if(n==1):
        return 1
    if(n==2):
        return 2
    return fib(n-2)+fib(n-1)


res = fib(10)
print(res)