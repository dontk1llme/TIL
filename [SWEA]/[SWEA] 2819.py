# 2819격자판의 숫자 이어 붙이기 (제출용) D4
# 거쳤던 격자칸을 다시 거쳐도 됨 -> visited 필요없음
# 인자로 tmp 넣어줘..... 그리고 이중for해서 받아저ㅜㅆ으면 혼자도 햇겟다

dx,dy = [-1,1,0,0], [0,0,-1,1]

def dfs(x,y,idx,tmp):
    # global tmp, tmplst
    tmp+=lst[x][y]

    if idx==6:
        if tmp not in tmplst:
            tmplst.append(tmp)
        return

    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if 0<=nx<4 and 0<=ny<4:
            dfs(nx,ny,idx+1,tmp)

T = int(input())
for tc in range(1, T+1):
    lst = [list(map(str, input().split())) for _ in range(4)]
    tmplst = []
    for x in range(4):
        for y in range(4):
            dfs(x,y,0,'')
    # print(tmplst)
    ans = len(tmplst)
    print(f'#{tc} {ans}')