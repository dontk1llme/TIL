#  [파이썬 S/W 문제해결 구현] 6일차 - 연산 (제출용) D4
#  swea 5247
# 최단거리 -> BFS

from collections import deque #시간초과 방지


def bfs(s, e):
    # [1] q생성, v[] 생성
    # q = []                # 일반큐 시간초과: >2000mS
    q = deque()  # 덱을 만들어서 처리:

    v = [0] * 1000001  # (1 ~ 1000000범위의 숫자만 가능)

    # [2] q에 초기데이터 삽입(단위작업)
    q.append(s)
    v[s] = 1  # 정답리턴시에는 -1 해서 리턴!

    while q:
        # c = q.pop(0)
        c = q.popleft()
        if c == e:
            return v[e] - 1  # 연산회수를 리턴

        # 네 방향, 범위내, 미방문, 조건(1~1000000)맞으면 큐 삽입
        for n in ((c - 1), (c + 1), (c * 2), (c - 10)):
            if 1 <= n <= 1000000 and v[n] == 0:
                q.append(n)
                v[n] = v[c] + 1
    # e를 못찾은 경우: 본 문제에서는 이런 경우는 없지만...
    return -1


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    ans = bfs(N, M)

    print(f'#{test_case} {ans}')
#////////////////////////////////////////////////////////////

def bfs(s, e):
    # [1] q생성, v[] 생성
    # q = []                # 일반큐 시간초과: >2000mS
    # q = deque()             # 덱을 만들어서 처리: 350mS
    q = [0] * 1000000  # 리스트로 큐 구현 : deque와 비슷
    w = r = 0  # w: write idx, r: read idx

    v = [0] * 1000001  # (1 ~ 1000000범위의 숫자만 가능)

    # [2] q에 초기데이터 삽입(단위작업)
    # q.append(s)
    q[w] = s
    w = (w + 1) % 1000000
    v[s] = 1  # 정답리턴시에는 -1 해서 리턴!

    while w != r:  # 큐에 데이터가 있는 동안 반복처리..
        # c = q.pop(0)
        # c = q.popleft()
        c = q[r]
        r = (r + 1) % 1000000
        if c == e:
            return v[e] - 1  # 연산회수를 리턴

        # 네 방향, 범위내, 미방문, 조건(1~1000000)맞으면 큐 삽입
        for n in ((c - 1), (c + 1), (c * 2), (c - 10)):
            if 1 <= n <= 1000000 and v[n] == 0:
                # q.append(n)
                q[w] = n
                w = (w + 1) % 1000000
                v[n] = v[c] + 1
    # e를 못찾은 경우: 본 문제에서는 이런 경우는 없지만...
    return -1


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    ans = bfs(N, M)

    print(f'#{test_case} {ans}')