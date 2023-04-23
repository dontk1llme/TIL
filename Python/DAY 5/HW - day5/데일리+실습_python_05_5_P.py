# 1444. 데일리실습 5-5. 패턴매칭을 이용한 반의어 출력 예제

words_dict = {'proper' : '적절한',
'possible' : '가능한',
'moral' : '도덕적인',
'patient' : '참을성 있는',
'balance' : '균형',
'perfect' : '완벽한',
'logical' : '논리적인',
'legal' : '합법적인',
'relevant' : '관련 있는',
'responsible' : '책임감 있는',
'regular' : '규칙적인'}

ls = list(words_dict.keys())
newls=[]
for i in ls:
    if i[0]=='b' or i[0]=='m' or i[0]=='p':
        newls.append('im'+i)
    elif i[0]=='l':
        newls.append('il'+i)
    elif i[0]=='r':
        newls.append('ir'+i)
newls.sort
print(newls)
