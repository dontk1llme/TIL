R,C,M = map(int,input().split())
sharks = dict()
for _ in range(M):
    r,c,s,d,z = map(int,input().split()) #위치, 속력, 방향, 크기
    # 방향 1 위 2 아래 3 오른쪽 4 왼쪽
    sharks[(r-1,c-1)] = [s,d,z] #인덱스 우리한테 익숙하게 하려고 1,1 아닌 0,0부터 시작

ans = 0
man = -1
while man<C:
    man+=1
    # 상어잡기
    for i in range(R):
        if (i, man) in sharks:
            shark = sharks[(i,man)]
            ans += shark[2]
            del shark
    # 상어이동 (새 dict 만들어서 다 이동 후 원dict=새dict 할거임)
    nsharks = dict()
    for key, value in sharks.items():
        x, y = key #나, 샤크, (r,c)
        s,d,z = value #속력, 방향, 크기
        for _ in range(s): #이동하기. *2-2 하면 됨...! 이걸 좀 생각해라
            if d == 1 or d==2: #세로
                s = s %(R*2-2)
            else: #가로
                s = s%(C*2-2)

            while s: #모든 경우를 싹 아우를 수 있음! 이거 이해 못햇엉~
                if d==4:
                    if y>s:
                        y=y-s
                        s = 0 #나 이제 이동 안함
                    else:
                        y=0
                        s = s-y
                        d=3
                elif d==3:
                    if C-y-1>s:
                        y = y+s
                    else:
                        s = s-(C-y-1)
                        y = C-1
                        d = 4

    # 상어냠냠
    if (x,y) in nsharks:
        # z #나
        # nsharks[(x,y)][2] #원래 잇던 녀석
        if z > nsharks:
            nsharks[(x,y)] = [s,d,z]
    else:
        nsharks[(x,y)] = [s,d,z]




    sharks = nsharks

print(ans)