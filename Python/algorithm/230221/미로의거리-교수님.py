def bfs(si, sj, ei, ej):
    # [0] 생성
    q = []
    v = [[0] * (N + 2) for _ in range(N + 2)]

    # [1] 단위작업
    q.append((si, sj))
    v[si][sj] = 1

    while q:
        # [2] 한 개 꺼냄 & 정답처리
        ci, cj = q.pop(0)
        if (ci, cj) == (ei, ej):
            return v[ei][ej] - 2

        # [3] 4/8방향 반복처리: 범위내, 미방문, 조건!
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            # 둘레를 벽 == '1' 으로 둘러쌓기 때문에 범위체크 안해도 됨! (간단, 속도 빨라짐)
            if v[ni][nj] == 0 and arr[ni][nj] != '1':
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
    return 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = ['1' * (N + 2)] + ['1' + input() + '1' for _ in range(N)] + ['1' * (N + 2)]
    # [1] 시작, 종료좌표 저장
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if arr[i][j] == '2':
                si, sj = i, j
            elif arr[i][j] == '3':
                ei, ej = i, j

    ans = bfs(si, sj, ei, ej)
    print(f'#{tc} {ans}')