# boj 2580 스도쿠
# DFS, 백트래킹
# https://hongcoding.tistory.com/118


def checkRow(x,a):
    for i in range(9):
        if a==lst[x][i]:
            return False
    return True
def checkCol(y,a):
    for i in range(9):
        if a==lst[i][y]:
            return False
    return True
def checkRect(x,y,a):
    nx = x//3*3
    ny = y//3*3
    for i in range(3):
        for j in range(3):
            if a==lst[nx+i][ny+j]:
                return False
    return True

def dfs(idx):
    if idx==len(blank):
        for i in range(9):
            print(*lst[i])
        return

    for i in range(1,10):
        x = blank[idx][0]
        y = blank[idx][1]
        if checkRow(x,i) and checkCol(y,i) and checkRect(x,y,i):
            lst[x][y]=i
            dfs(idx+1)
            lst[x][y]=0

nums = list(range(1,10))
lst = [list(map(int, input().split())) for _ in range(9)]

blank = []
for i in range(9):
    for j in range(9):
        if lst[i][j]==0:
            blank.append((i,j))

dfs(0)
