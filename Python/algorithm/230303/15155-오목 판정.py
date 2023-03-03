# 11315. 오목 판정 D3
# ㅋㅋ 아래 코드대로 제출하면 제출용은 pass되는데 찐 오목판정은 짤림...

T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # NxN 크기의 판
    omok = [list(map(str, input())) for _ in range(N)]
    ans = "NO"

    # 가로
    for i in range(N):
        cnt = 1
        for j in range(N - 1):
            if omok[i][j] == 'o' and omok[i][j + 1] == 'o':
                cnt += 1
            if cnt >= 5:
                ans = "YES"
                break

    # 세로
    for i in range(N):
        cnt = 1
        for j in range(N - 1):
            if omok[j][i] == 'o' and omok[j + 1][i] == 'o':
                cnt += 1
            if cnt >= 5:
                ans = "YES"
                break

    # 5x5 만 생각하면 얘가 됨
    # 좌상 대각
    cnt1 = 1
    for i in range(N - 1):
        if omok[i][i] == 'o' and omok[i + 1][i + 1] == 'o':
            cnt1 += 1
            continue
    if cnt1 >= 5:
        ans = "YES"

    # 우상 대각
    cnt2 = 1
    for i in range(N - 1):
        if omok[i][N - 1 - i] == 'o' and omok[i + 1][N - 2 - i] == 'o':
            cnt2 += 1
            continue
    if cnt2 >= 5:
        ans = "YES"

    print(f'#{tc} {ans}')