#marks2.py
"""
marks = [90,25,67,45,80]
number=0
for mark in marks:
    number = number+1
    if mark < 60: continue
    print("%d번 학생 축하합니다!" %number)
    """

#구구단
for i in range(2,10):
    for j in range(1,10):
        print (i*j, end =" ")
    print('')