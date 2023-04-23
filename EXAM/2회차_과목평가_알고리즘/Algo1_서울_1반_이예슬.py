# 도장 찍기

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N: 도화지 크기, M: 도장 찍은 횟수
    lst = [[0] * N for _ in range(N)]  # 도장 찍을 도화지

    for m in range(M):  # 도장 찍기
        h, y, garo, sero = map(int, input().split())
        if h + sero <= N and y + garo <= N:  # 도장이 찍히는 곳은 도화지의 경계를 벗어나지 않음
            for i in range(h, h + sero):
                for j in range(y, y + garo):
                    lst[i][j] += 1

    cnt = 0  # 도장 찍힌 칸의 개수 세기
    for k in range(len(lst)):
        for l in range(len(lst)):
            if lst[k][l] > 0:
                cnt += 1

    print(f'#{tc} {cnt}')