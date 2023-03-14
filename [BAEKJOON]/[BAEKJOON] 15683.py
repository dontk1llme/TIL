# BOJ 15683 감시
# 사각지대의 최소 크기
# 감시까지는 하겠는데 회전을 어케할건지? -> d 만들어서 인덱스 써야겟당
# https://developer-ellen.tistory.com/53

import copy #깊은복사 사용하려고...

d = [(-1,0), (0,1) , (1,0), (0,-1)] #상 우 하 좌 (시계방향)
mode = [ # cctv 번호 == 인덱스 번호. 경우 정해주기
    [],
    [[0],[1],[2],[3]],
    [[0,2],[1,3]],
    [[0,1],[1,2],[2,3],[3,0]],
    [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
    [[0,1,2,3]]
]

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
cctv = [] #cctv 위치 담아줄. . .
ans = int(1e9) #최소값 구해야 돼서 10억 넣어줌
for i in range(N):
    for j in range(M):
        if 1<=lst[i][j]<=5:#cctv라면
            cctv.append([lst[i][j], i, j]) #값, 좌표 저장

def watch(tmp, mm, x, y): #cctv 돌리기
    for i in mm:
        nx, ny = x,y
        while True:
            nx, ny = nx+d[i][0], ny+d[i][1]
            if 0<=nx<N and 0<=ny<M:
                if tmp[nx][ny] ==6: #벽 만나면
                    break
                elif tmp[nx][ny]==0: #감시 가능하면
                    tmp[nx][ny]=7
            else: break #이거 안 써 줘서 무한반복.. ;;

def dfs(depth, arr):
    global ans
    if depth == len(cctv): #tv 다 돌았으면 최소값 찾고 종료
        cnt = 0
        for i in range(N):
            cnt+=arr[i].count(0) #사각지대 카운트
        ans = min(ans, cnt)
        return
    tmp = copy.deepcopy(arr)
    tvnum, x, y = cctv[depth] #번호, 좌표
    for i in mode[tvnum]:
        watch(tmp, i, x, y)
        dfs(depth+1, tmp)
        tmp = copy.deepcopy(arr) #원상태로 돌려서 다시 dfs 해줘야함

dfs(0, lst)
print(ans)