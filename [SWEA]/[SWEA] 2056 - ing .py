#swea 2056. 연월일 달력 D1
#얘가 D1 중에 젤 까다로운 듯
# 이 문제 풀어서 D1 클리어!!
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QLkdKAz4DFAUq&categoryId=AV5QLkdKAz4DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=1
# https://haerang94.tistory.com/167

num = int(input())
daylist=[0,31,28,31,30,31,30,31,31,30,31,30,31]

for j in range(0,num+1):
    print(f'#{j+1}', end=' ' )
    #연월일 나누기
    #year,month,day = ('','','')
    # for i in range(0,len(date)):
    #     if i<4:
    #         year = int(year+date[i])
    #     elif i<6:
    #         month = int(month+date[i])
    #     else: day = int(day+date[i])
    date=input()
    year=int(date[:4])
    month=int(date[4:6])
    day=int(date[6:])

    #여기서부터 문제임...
    #달: 0 초과 12 이하
    #일: 0 초과 해당일 이하

    if (month <1 or month >12):
        print('-1')
        continue
    if day != daylist[month]:
        print('-1')
        continue
    else: 
        print(f'{year}/{month}/{day}')

d아오개빢ㅊ치내ㅔ