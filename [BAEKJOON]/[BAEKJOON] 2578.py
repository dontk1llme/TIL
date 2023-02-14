#[BOJ] 2578 빙고
#우선 수를 찾아서 0으로 만들고 cnt+=1
#만든 다음... 줄이 0인 경우인지 검사하고 맞으면 bng+1
#bng==3: 빙고, cnt출력

def bingo(lst):
    bng = 0

    #가로
    for i in player:
        if i.count(0) == 5:
            bng+=1

    #세로
    #배열 새로 만들어서 볼려고 했는데 그냥 세서 해도 됨
    for i in range(5):
        y=0
        for j in range(5):
            if player[j][i]==0: #세로니까
                y+=1
        if y==5:
            bng+=1

    #왼쪽시작대각선
    d1 = 0
    for i in range(5):
        if player[i][i]==0:
            d1+=1
    if d1==5:
        bng+=1

    #오른쪽시작대각선
    d2 = 0
    for i in range(5):
        if player[i][4-i]==0:
            d2+=1
    if d2==5:
        bng+=1

    return bng


player = [list(map(int, input().split())) for _ in range(5)]
owner = [] #2차원 배열일 필요가 없어서... 아래처럼 일차원으로입력
for _ in range(5):
    owner+=list(map(int, input().split()))

cnt = 0 #부른 개수
for i in range(len(owner)):
    for k in range(len(player)):
        for l in range(len(player)):
            if player[k][l]== owner[i]: #해당 위치 0으로 바꿔줌
                player[k][l]=0
                cnt+=1

    if cnt >= 12:#어느 for문 안에 넣을지 위치 주의...
        bbing = bingo(player)

        if bbing >= 3:
            print(i+1) #인덱스보다 1큼
            break
