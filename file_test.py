#file practice
#f= open("새파일.txt", 'w')
#f.close()

#writedata.py
f= open("C:/Users/Linny/PycharmProjects/새파일.txt", 'a')
for i in range(11,21):
    data = "%d번째 줄입니다. \n" %i
    #print(data)
    f.write(data)
f.close()

#readline.py
#f=open("C:/Users/Linny/PycharmProjects/새파일.txt", 'r')
#line = f.readline()
#print(line)
#f.close()

#readline_all.py
#f= open("C:/Users/Linny/PycharmProjects/새파일.txt", 'r')
#while True:
#    line = f.readline()
#    if not line: break
#    print(line)
#f.close()