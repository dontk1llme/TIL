# 2217. 데일리과제 4-2. 끝말잇기 탈락 확인 예제 Lv2

words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]

for i in range(1,len(words)):
    if (words[i-1][-1]!=words[i][0]):
        print(f'{i}번째 사람 탈락')
        break
    elif words[i] in words[:i]: #이거 앞에거 하나가 아니라 앞에 전체랑 비교해서 햇어야함. 주의
        print(f'{i}번째 사람 탈락')
        break
else: print('끝말잇기 완벽함')