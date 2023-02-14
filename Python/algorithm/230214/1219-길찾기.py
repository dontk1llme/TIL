# 1219. [S/W 문제해결 기본] 4일차 - 길찾기 D4
# 그래프경로랑 똑같은 거 아냐?
# 인접리스트로 풀어보기
# 인접리스트, 행렬 다 잇는 곳: https://jennnn.tistory.com/16

T = 10
for _ in range(T):
    #입력
    tc, N = map(int, input().split())
    lst=list(map(int, input().split())) #순서쌍. 0: 시작점, 99: 도착점
    adjl = [[] for _ in range(100)] #인접리스트
    for i in range(N):
        v1, v2 = lst[i*2], lst[i*2+1]
        adjl[v1].append(v2)

    #여기에서 DFS 해보기
    visited = [0]*100
    stk = [0] #첫번째노드
    while stk:
        now = stk.pop()

        if visited[now]==0:
            visited[now]=1

            for v in adjl[now]:
                if visited[v]==0:
                    stk.append(v)

    if visited[99] ==1: ans=1
    else: ans=0

    print(f'#{tc} {ans}')