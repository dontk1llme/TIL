# 1691. 데일리실습 4-5. 패턴매칭을 이용한 반의어 출력 예제 lv5
test_status = {
    '김싸피': 'solving',
   	'이코딩': 'solving',
   	'최이썬': 'cheating',
   	'오디비': 'sleeping',
   	'임온실': 'cheating',
   	'조실습': 'solving',
   	'박장고': 'sleeping',
   	'염자바': 'cheating'
}

# v == cheating: ts에서 제거, key 오름차순 출력
new_status=[]
cheatname=[]

for i in test_status.items():
	if i[1] == 'cheating':
		cheatname.append(i[0])
	else: new_status.append(i)
cheatname.sort(reverse=False) #오름차. False가 디폴트 맞는데 안 돼서 지정해줌
print(cheatname)


# v == sleeping: solving으로 바꾸기
st = []
for i in new_status:
	mylist = list(i)
	if mylist[1] == 'sleeping':
		mylist[1]='solving'
	st.append(tuple(mylist))#얘는 바뀌었는데.왜.newstatus에 안들어가.왜

test_status = dict(st)
print(test_status)


