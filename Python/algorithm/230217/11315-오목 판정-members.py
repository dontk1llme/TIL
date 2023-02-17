#진익근
Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    result = 'NO'

    for i in range(N):
        for j in range(N - 5 + 1):
            if board[i][j:j + 5] == (['o'] * 5):
                result = 'YES'

    cross = []
    rev_cross = []

    for i in range(N):
        cross.append(board[i][i])
        rev_cross.append(board[i][N - 1 - i])

    for i in range(N - 5 + 1):
        if cross[i:i + 5] == (['o'] * 5) or rev_cross[i:i + 5] == (['o'] * 5):
            result = 'YES'

    for i in range(N):
        for j in range(N):
            if i < j:
                board[i][j], board[j][i] = board[j][i], board[i][j]

    for i in range(N):
        for j in range(N - 5 + 1):
            if board[i][j:j + 5] == (['o'] * 5):
                result = 'YES'

    print(f'#{t + 1} {result}')


#최홍준
def cal_straight(arr):
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 'o':
                cnt += 1
                if cnt == 5:
                    return 'yes'
            else:
                cnt = 0
    return 'no'


def cal_d1(arr):  # N이 7일때 9번 6일때 4번 5일때 1번
    for i in range(N - 4):
        for j in range(N - 4):
            cnt = 0
            for k in range(5):
                if arr[i + k][j + k] == 'o':
                    cnt += 1
            if cnt == 5:
                return 'yes'
    return 'no'


def cal_d2(arr):
    for i in range(N - 4):
        for j in range(N - 4):
            cnt = 0
            for k in range(5):
                if arr[i + k][j + 4 - k] == 'o':
                    cnt += 1
            if cnt == 5:
                return 'yes'
    return 'no'


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    # 가로, 세로, 대각선 확인
    # 대각은 끝과 끝 말고도 N이 5이상일때 다른 대각도 있음을 확인해야함
    arr_t = list(zip(*arr))
    a = cal_straight(arr)
    b = cal_straight(arr_t)
    c = cal_d1(arr)
    d = cal_d2(arr)
    ans_lst = [a, b, c, d]
    if 'yes' in ans_lst:
        ans = 'YES'
    else:
        ans = 'NO'
    print(f'#{test_case} {ans}')