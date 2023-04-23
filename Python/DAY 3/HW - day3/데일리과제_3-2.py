# 2215. 데일리과제 3-2. 윤년 판별하기 예제

year = int(input())

if ((year%4==0) and (year%100!=0)) or (year%400==0):
    print("윤년")
else: print("윤년아님")