# 1684. 데일리실습 3-5.
# 문자열 메서드와 슬라이싱 활용 예제

#소금물의 퍼센트 농도와 소금물의 양을 입력
salt = []
i=5
while i>0:
    a = input('퍼센트 농도: ') # 농도 (%)
    if a=='Done': #Done을 입력하면 중지
        break
    b = input('소금물 양: ') # 소금물 양(ml)
    t = (float(a),float(b))
    salt.append(t)
    i-=1

#농도와 ml 합계 구하기
totalml=0
findsalt=0
for i in range(len(salt)):
    totalml += salt[i][1]
    findsalt += salt[i][0]*salt[i][1]/100

totalpercent = round(findsalt/totalml*100,2) #두 번째 인자: 표시할 자릿수로 암기
print(f'농도: {totalpercent}%, 양: {totalml}ml')
    