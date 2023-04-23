# 1675. 데일리실습 2-3. 문자열 슬라이싱에 대한 이해 예제
'''
하나의 문장을 입력받아, 그 문장에 끝말잇기 규칙을 적용시켜보려 한다. 
세 단어가 입력으로 주어졌을 때 그 끝말잇기가 옳으면 Pass, 옳지 않으면 Fail을 출력하시오. 
예를 들어 saFe eMotion Nail 인 경우, pass를 출력한다.
'''

str_lst = input('문자열을 입력하세요. : ')
str_lst = str_lst.upper().split()

for i in range(0,len(str_lst)-1):
    if str_lst[i][-1]!=str_lst[i+1][0]: 
        print('Fail')
        break
else: print('Pass')