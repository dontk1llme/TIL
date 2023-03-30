# 1865
# https://epser.tistory.com/13


def backtracking(depth, value):
    global max_value
    if depth == N: #최대 깊이라면 탐색을 종료해라!
        if value >= max_value:
            max_value = value
        return

    if value<=max_value:
        return

    for i in range(N):
        if visit[i] == 0: #방문 안했으면
            visit[i] = 1
            backtracking(depth+1, value * total_map[depth][i])
            visit[i] = 0

testcase = int(input())
for t in range(1, testcase+1):
    N = int(input())
    total_map = []
    max_value = 0 #이게 정답이겟져?
    for n in range(N):
        total_map.append(list(map(int, input().split())))
    visit = [0] * (N)
    backtracking(0, 1)
    max_value *= 100
    max_value /= (100**N)
    print(f'#{t} {format(max_value, ".6f")}')