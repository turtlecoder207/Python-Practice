
def f(n):
    global sum
    sum = 0
    for i in range(1,n+1): #1부터 n까지인 리스트 생성
        a= [int(j) for j in str(i)] #각 리스트의 리스트 생성 (10도 1,0으로 분해)
        for parts in a: #a 리스트에 있는 동안,
            if parts == 1: #리스트 요소랑 1과 같으면,
                sum = sum+1

    return sum




i=1
j=0
while j<3:
    k = f(i)
   # print(k)
    if i == k:
      print(k)
      j = j+1
      i = i+1
    else:
        i = i+1
