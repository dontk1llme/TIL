# 1445. 데일리과제 5-2. 날짜 분석 프로그램 Lv2

'''
연도, 월, 일을 순서대로 입력받는다.
윤년으로 가면 타임머신에 에러가 생긴다. 윤년을 입력했을 경우 연도를 다시 입력받아야 한다.
윤년이 아닌 연도를 입력받을 경우, 날짜를 편하게 정할 수 있도록 해당 연도의 달력을 출력하라.
김코딩은 월요일을 싫어한다. 입력한 날짜가 월요일인 경우 경고 메시지를 출력하라.
입력이 완료되면 연, 월, 날짜, 그리고 요일을 dictionary에 정리하여 출력하라.
HINT: calendar 모듈을 활용하라.	
윤년, 달력, 월요일, 딕
'''
# 입력 예시
# 2015
# 8
# 31

# 출력 예시 
# (2016) 윤년입니다. 연도를 다시 입력해주세요.
#경고 월요일입니다.
#{'년': 2015, '월': 8, '일': 31, '요일': '월요일'}

import calendar

while True:
    year = int(input())
    if ((year%4==0) and (year%100!=0)) or (year%400==0): #윤년
        print(f"({year}) 윤년입니다. 연도를 다시 입력해주세요")     
    else: break

year = int(input())
month = int(input())
date = int(input())

#달력
text_cal = calendar.TextCalendar(firstweekday=0)
print(text_cal.formatyear(year,3))

#월요일
days = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
yoday = days[calendar.weekday(year,month,date)]
if yoday=='월요일':
    print("경고 월요일입니다.")

#딕
new_dict={'년': year, '월': month, '일': date, '요일': yoday}
print(new_dict)