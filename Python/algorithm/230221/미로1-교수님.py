def bfs(si, sj, ei, ej):
    q = []  # [0] q, v 등 생성
    v = [[0] * N for _ in range(N)]

    q.append((si, sj))  # [1] 초기데이터 삽입, v표시: 단위작업
    v[si][sj] = 1

    while q:
        ci, cj = q.pop(0)  # 필요시 정답처리
        if (ci, cj) == (ei, ej):
            return 1

        # 4/8..방향 등 반복처리
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            # 범위내, 미방문, 조건: !='1'
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and arr[ni][nj] != '1':
                q.append((ni, nj))
                v[ni][nj] = 1

    return 0  # 모두 탐색했으나 못찾은 경우


T = 10
for tc in range(1, T + 1):
    _ = input()
    N = 16
    arr = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                si, sj = i, j
            elif arr[i][j] == '3':
                ei, ej = i, j

    ans = bfs(si, sj, ei, ej)
    print(f'#{tc} {ans}')