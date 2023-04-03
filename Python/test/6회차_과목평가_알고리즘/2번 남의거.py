# 준혁쓰
def backtracking(depth, i, value):
    global ans
    if visit[a] == 0 and visit[b] == 1: #b를 먼저 지나쳣다면
        return #없던걸로
    if sum(visit) == N: #전부 다 방문했다면
        value += total_map[i][0] #마지막에 0으로 다시 돌아가는 것 더해주고
        ans = min(ans, value) #이전 정답과 지금 정답중 더 적은 에너지가 드는 것을 선택
        return
    if depth == N: #깊이가 바닥까지 내려갔다면 return
        return
    for j in range(N): #백트래킹(갈지말지 고민)
        if visit[j] == 0:
            visit[j] = 1
            backtracking(depth + 1, j, value + total_map[i][j])
            visit[j] = 0
            backtracking(depth + 1, i, value)

testcase = int(input())
for t in range(1, testcase+1):
    N = int(input())
    total_map = []
    visit = [0] * (N)
    ans = 1000 #N이 10 이하, 한칸 에너지 100 이하니까 정답 1000으로 두고 더 작은 값 나올때마다 바꿔주기
    visit[0] = 1 #시작점 방문한 것으로 표기
    for _ in range(N):
        total_map.append(list(map(int,input().split())))
    a, b = map(int,input().split())
    backtracking(0, 0, 0)
    print(f'#{t} {ans}')

#///////////////////////////////////////////////////
# 수형
def SSAFY_Robot(lst, depth):
    if depth == n - 1:
        if lst.index(a) < lst.index(b):
            global ans
            tmp = 0
            lst = [0] + lst + [0]
            for i in range(n):
                tmp += arr[lst[i]][lst[i + 1]]
            ans = min(ans, tmp)
        return

    for i in range(depth, n - 1):
        lst[depth], lst[i] = lst[i], lst[depth]
        SSAFY_Robot(lst, depth + 1)
        lst[depth], lst[i] = lst[i], lst[depth]


T = int(input())
for t in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    a, b = map(int, input().split())
    ans = 10 * 100
    SSAFY_Robot(lst=list(range(1, n)), depth=0)
    print(f"#{t} {ans}")