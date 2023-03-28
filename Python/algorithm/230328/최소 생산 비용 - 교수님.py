# 경우 3개................... 시간 긴 순서대로

#1 하던 대로 visited 배열 사용이긴함 -> 모든 경우를 복사붙여넣기하다보니까 시간이 오래걸림
# v[]
def dfs_1(n, sm, v):
    global ans
    if ans <= sm:
        return

    if n == N:
        ans = min(ans, sm)
        return

    for j in range(N):
        if j not in v:  # 미방문인 경우
            dfs_1(n + 1, sm + arr[n][j], v + [j])


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = N * 99

    # [1] v[] 전달
    dfs_1(0, 0, [])

    print(f'#{test_case} {ans}')
#//////////////////////////////////////////////////////////
#2 전역배열 사용 -> visited를 queue로 씀 -> 더 ms가 짧아짐
# v append, pop

def dfs_2(n, sm):
    global ans
    if ans <= sm:
        return

    if n == N:
        ans = min(ans, sm)
        return

    for j in range(N):
        if j not in v:  # 미방문인 경우
            v.append(j)
            dfs_2(n + 1, sm + arr[n][j])
            v.pop()


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = N * 99

    # [1] v[] 전달 => 1000mS
    # dfs_1(0, 0, [])

    # [2] append/pop => 700mS
    v = []
    dfs_2(0, 0)

    print(f'#{test_case} {ans}')

#////////////////////////////////////////////////////////
# 3. visited에 0,1 사용해서 바꿔주면서! -> 473으로 얘가 젤 짧네요

def dfs_3(n, sm):
    global ans
    if ans <= sm:
        return

    if n == N:
        ans = min(ans, sm)
        return

    for j in range(N):
        if v[j] == 0:  # 미방문인 경우
            v[j] = 1
            dfs_3(n + 1, sm + arr[n][j])
            v[j] = 0


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = N * 99

    # [1] v[] 전달 => 1000mS
    # dfs_1(0, 0, [])

    # [2] append/pop => 750mS
    # v = []
    # dfs_2(0, 0)

    # [3] v[] 표시
    v = [0] * N
    dfs_3(0, 0)
    print(f'#{test_case} {ans}')
