# [BAEKJOON] 10709 기상캐스터

H,W = map(int,input().split())
lst = [list(map(str, input())) for _ in range(H)]
newlst =[[-1]*W for _ in range(H)]

for i in range(H):
    cin = False #줄에 c 나왓는지 안나왓는지
    for j in range(W):
        if lst[i][j]=='c':
            newlst[i][j]=0
            cin = True
        else: #c가 나왔어야만 증가해야대는디
            if cin:
                newlst[i][j] = newlst[i][j-1] +1

for i in range(H):
    print(*newlst[i])