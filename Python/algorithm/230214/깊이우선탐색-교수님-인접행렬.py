#DFS
# 재귀로도 구현 가능하지만 여기에서는 Stack으로
# 방법 두 가지. 1: 인접리스트, 2: 인접행렬
# 인접리스트가 편하지만 지금처럼 조건 있을 때는 sort 해서 풀어야 함
# 이번에는 무가중치 그래프 -> 양방향이라고 생각.

#인접행렬

def dfs_stk(start):
    visited = [0]*(V+1)
    stk = []

    #방문작업
    s = start # 기준점
    visited[s]=1
    ans.append(s)

    while True:
        # s에서 연결된, 미방문인 노드 발견 시 이동 (번호순)
        for e in range(1, V+1):
            if visited[e]==0 and adj[s][e]==1: #==1 (True), ==0:(False or not)
                stk.append(s) #되돌아올 위치(지금 기준점-> s)
                s = e
                visited[s]=1
                ans.append(s)
                break #찾았으면 즉시 그곳을 기준으로 탐색해야하니 for문탈출
        else: #더이상 연결된 방문노드가 없는 경우 (막다른길)
            if stk: #비어있지 않으면
                s = stk.pop() #스택에서 꺼낸 최근 기준점이 바로 내 현재가 됨
            else: 
                break #더이상 탐색할 위치가 없음...


T = int(input())
for tc in range(1, T+1):
    #입력
    V,E = map(int, input().split()) #노드, 링크
    adj = [[0] * (V+1) for _ in range(V+1)] #인접행렬매트릭스. 1부터 수 받으니까 V+1
    #연결된 행렬에 1로 연결 표시
    for i in range(E):
        a,b=map(int, input().split())
        adj[a][b] = adj[b][a] = 1 #지금은 연결돼있으면 1이지만 나중에는 가중치로 쓰기 가능

    ans = []
    dfs_stk(1)
    print(f'#{tc}', *ans)