def bfs(s):
    # [1] q, v[], 필요 flag 생성
    q = []
    v = [0] * (V + 1)

    # [2] 단위작업
    q.append(s)
    v[s] = 1
    alst.append(s)

    while q:
        # [3] 데이터 한개 꺼냄
        c = q.pop(0)

        # [4] 4/8방향, 연결된 노드 등 반복처리
        for n in adj[c]:
            # 범위내, 미방문, 조건맞으면(길이면, 같은 값이면, 일정범위 이내면)
            if v[n] == 0:
                q.append(n)
                v[n] = 1  # 이전 v[c]+1 인 경우도 있음
                alst.append(n)


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V + 1)]
    for _ in range(E):
        s, e = map(int, input().split())
        adj[s].append(e)
        adj[e].append(s)  # 양방향 연결!

    # 인접리스트=>번호순 조건: 반드시 정렬후 사용
    for lst in adj:
        lst.sort()

    alst = []
    bfs(1)
    print(f'#{tc}', *alst)