R, C, M = map(int,input().split())
sharks = dict()

for _ in range(M):
    r, c, s, d, z = map(int,input().split())
    #위치 / 속력 / 방향 / 크기
    # 키  / [0      1      2]

    sharks[(r-1,c-1)] = [s, d, z]

    # 방향
    # 1   2     3     4
    # 위 아래 오른쪽 왼쪽
fisherman = -1
res = 0

while fisherman < C:
    # 1. 낚시왕이 이동
    fisherman += 1
    # 2. 가장 가까운 상어를 잡습니다.
    for i in range(R):
        if (i, fisherman) in sharks:
            shark = sharks[(i,fisherman)]
            res += shark[2]
    # 2.a 상어가 사라집니다.
            del shark

    
    # 3. 상어가 이동을 합니다.
    next_sharks = dict() 
    # 여기다가 이동을 시킬 예정이에요
    for key, value in sharks.items():
        x, y = key # 나, 샤크, (r, c)
        s, d, z = value #  속력 / 방향 / 크기

        if d == 1 or d == 2:
            s = s % (R * 2 - 2)
        else:
            s = s % (C * 2 - 2)
        while s :
            if d == 4:
                if y > s:
                    y = y - s
                    s = 0 # 나는 이제 이동 안해
                else:
                    y = 0
                    s = s - y
                    d = 3
            elif d == 3:
                if C - y- 1 > s:
                    y += y + s
                    s = 0
                else:
                    s = s - (C - y - 1)
                    y = C - 1
                    d = 4
            # 나머진 해보세요


        



    # 4. 큰 상어가 나머지 상어를 먹습니다.
    if (x, y) in next_sharks:
        if z > next_sharks:
            next_sharks[(x,y)] = [s, d, z]
    else:
        next_sharks[(x,y)] = [s, d, z]


    sharks = next_sharks
# res . 낚시왕이 잡은 상어