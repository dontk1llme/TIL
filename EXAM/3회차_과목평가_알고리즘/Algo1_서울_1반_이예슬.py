#봉우리의 수

T = int(input())
d = [(0,1),(-1,0),(-1,1),(-1,-1),(0,-1),(1,-1),(1,1),(1,0)]#8방향

for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int,input().split())) for _ in range(N)]
    high = []

    for i in range(1,N-1): #가장자리는 판단하지 않음
        for j in range(1,N-1):
            findhigh = [lst[i][j]] #중간도 포함해서 봉우리 찾기
            for k in d: #8방향 판단하기
                dx,dy = j,i
                nx,ny = dx+k[0], dy+k[1] #탐색할 방향
                findhigh.append(lst[nx][ny]) #8방향+본인 총 9개 전부
            findhigh.sort() #정렬
            if findhigh[-1] != findhigh[-2]: #젤 큰 애랑 두번째 애가 다르면 높이가 다른 거니까
                high.append(findhigh[-1]) #봉우리 목록에 추가
    high.sort()

    ans = -1
    if len(high)>=2: #봉우리가 2개 이상이면
        ans = high[-1] - high[0] #높이차를 정답으로

    print(f'#{tc} {ans}')




