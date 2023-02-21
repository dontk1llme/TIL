# 1238. [S/W 문제해결 기본] 10일차 - Contact D4
# 방향 존재함, 한번 연락받은 사람에게 다시 연락할 일 없음
# 1차원 해야하는지 2차원 해야하는지 헷갈리지 말기...


T = 10
for tc in range(1, T+1):
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))
    graph = [[] for _ in range(101)] #최대 100명
    for i in range(0,N,2):
        s,e = lst[i], lst[i+1]
        graph[s].append(e)

    visited=[0]*101
    visited[S]=1
    q = [S]
    while q:
        t = q.pop(0)
        for i in graph[t]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[t]+1 #마지막에 연락받은 사람 찾아야되니까 누적

    max_=0
    ans = 0
    for i in range(101):
        if visited[i]>=max_:
            ans = i
            max_ = visited[i] #마지막 사람 중 숫자 가장 큰 사람
    print(f'#{tc} {ans}')