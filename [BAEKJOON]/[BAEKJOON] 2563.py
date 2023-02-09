#[BOJ] 2563.색종이
#오 한방에됏다 ㅋㅋ
#가로세로 각 100인 배열
#가로 시작점, 세로 시작점 기준으로 배열 채우기
#0이 아닌 인덱스만 카운트해서 출력

T = int(input())
paper = []
for t in range(T):
    paper.append(list(map(int, input().split())))

white = list([0]*100 for _ in range(100))

for i in paper:
    x = i[0]
    y = i[1]
    for j in range(10):
        for k in range(10): #세로를 아래에서 주든 말든... 위에서 하는 거랑 똑같음...
            white[x+j][y+k] = 1
    
cnt = 0
for i in white:
    cnt+=i.count(1)
print(cnt)
    
    

