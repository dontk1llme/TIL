def bfs(s, e):
    # [1] 생성
    q = []
    v = [0] * (V + 1)

    # [2] 단위작업
    q.append(s)
    v[s] = 1  # 시작이 1이므로 정답은 -1 후 리턴

    while q:
        c = q.pop(0)
        if c == e:
            return v[e] - 1

        for n in adj[c]:  # 연결된..
            if v[n] == 0:  # 미방문 노드이면
                q.append(n)
                v[n] = v[c] + 1  # 거리를 구하는경우 +1

    # 모든 위치를 탐색했는데도 return 못한경우.. 도달불가능
    return 0


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V + 1)]
    for _ in range(E):
        s, e = map(int, input().split())
        adj[s].append(e)
        adj[e].append(s)
    S, G = map(int, input().split())
    ans = bfs(S, G)
    print(f'#{tc} {ans}')