# 1452. 데일리과제 6-2. 데이터 구조 복습 및 심화 예제1
# # 입력 예시
# # mass percent.py 실행 시
# 1.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 1% 400g
# 2.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 8% 300g
# Done

# 출력 예시
# 4.0% 700.0g
n=1
pctls=[]
gramls=[]
sogeum=[]
while(n<=5):
    #입력받기
    print(f'{n}. 소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: ', end='')
    try:
        pct, gram = map(str, input().split())
        n+=1
    except ValueError: 
        break

    #계산
    pctls.append(int(pct.rstrip('%')))
    gramls.append(int(gram.rstrip('g')))
for i in range(len(pctls)):
    sg = pctls[i]*gramls[i]/100
    sogeum.append(sg)

sumgram = sum(gramls)
nd = round(sum(sogeum)/sumgram*100,2)
print(f'{nd}% {sumgram}g')