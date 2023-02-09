for _ in range(10):
    tc = int(input())
    row, col = 100, 100
    ladder = [list(map(int, input().split())) for l in range(row)]

    #시작지점 리스트 만들기Z
    startidx=[]
    for i in range(col):
        if ladder[0][i]==1:
            startidx.append(i)

    #도착점까지의 거리 모음 리스트 만들기
    #아래로 내려가는 건 다들 99일 테니 제외. 좌우만 세기
    dist=[]
    for idx in startidx:
        r, c = 0, idx #시작위치
        dtmp = 0
        while r<row: #row는 최대 99(인덱스)
            if 0<=c-1<col and ladder[r][c-1]==1:# 좌측이동
                while c>0 and ladder[r][c-1]==1: #쭉
                    c-=1
                    dtmp+=1
            elif 0<=c+1<col and ladder[r][c+1]==1: #우측이동
                while c<99 and ladder[r][c+1]==1: #쭉
                    c+=1
                    dtmp+=1
            r+=1 #아래로 이동
        dist.append(dtmp)

    #복수 개인 경우 가장 큰 X좌표.
    minidx = 0
    mindt = row*col
    for idx,dt in enumerate(dist): #enumerate 하면 for문 한번 덜쓰기 가능
        if mindt >= dt:
            minidx=idx
            mindt=dt

    print(f'#{tc} {startidx[minidx]}')




