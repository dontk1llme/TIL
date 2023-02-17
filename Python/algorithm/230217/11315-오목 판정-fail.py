# 1315. 오목 판정 D3
# 가로, 세로, 대각선
# 5x5의 판만 있는 게 아님. 10x10 이런 식이면 대각선 5개인 곳이 꼭짓점 말고도 여러군데가 됨. #92/100
# cnt 5개가 아니라 연속으로 5개여야함. 반례: .o.o.o.o.o #73/100
# 대각선일 경우 다른 루프면 cnt 초기화를 해 주어야 함. (tc4번)
# 노가다.........



T = int(input())
for tc in range(1, T+1):
    N = int(input()) #NxN 크기의 판
    omok = [list(map(str, input())) for _ in range(N)]
    ans = "NO"

    # 가로
    for i in range(N):
        cnt = 1
        for j in range(N-1):
            if omok[i][j]=='o' and omok[i][j+1]=='o':
                cnt+=1
            if cnt>=5:
                ans="YES"
                break

    # 세로
    for i in range(N):
        cnt = 1
        for j in range(N-1):
            if omok[j][i]=='o'and omok[j+1][i]=='o':
                cnt+=1
            if cnt>=5:
                ans = "YES"
                break

    # 대각선: o 위치 생각해 두고 거기서부터 좌상, 우상 다 탐색하기.


    #5x5 만 생각하면 얘가 됨
    # 좌상 대각
    cnt1 = 1
    for i in range(N-1):
        if omok[i][i]=='o' and omok[i+1][i+1]=='o':
            cnt1+=1
            continue
    if cnt1 >= 5:
        ans = "YES"


    #우상 대각
    cnt2= 1
    for i in range(N-1):
        if omok[i][N-1-i]=='o' and omok[i+1][N-2-i] =='o':
            cnt2+=1
            continue
    if cnt2>=5:
        ans="YES"


    print(f'#{tc} {ans}')

# //////////////////////////////////////////
# 델타 쓰면 쉽네요...............
# '.' : 돌이 없는 칸, 'o' : 돌이 있는 칸
# 오른쪽, 오른쪽아래대각선, 아래쪽, 왼쪽아래대각선으로 연속 5개나와야함

# arr에 오목이 존재하면 'YES', 존재하지 않으면 'NO' return
# def A(arr):
#     # 우,하,우하대,좌하대
#     dr = [0,1,1,1]
#     dc = [1,0,1,-1]
#     for start_r in range(N):
#         for start_c in range(N):
#             if arr[start_r][start_c] == 'o':
#                 for d in range(4):
#                     r = start_r
#                     c = start_c
#                     # 각 방향으로 연속적으로 오목이 존재하는가?
#                     cnt = 0
#                     # 파이썬만 0 <= r <= N-1 허용
#                     # 다른 언어는 r >= 0 and r <= N-1
#                     while 0 <= r <= N-1 and 0 <= c <= N-1 and arr[r][c] == 'o':
#                         cnt += 1
#                         r += dr[d]
#                         c += dc[d]
#                     # 각 방향으로 오목이 존재?하는가
#                     if cnt >= 5:
#                         return 'YES'
#     return 'NO'
#
# # 테스트 케이스의 개수
# T = int(input())
# for tc in range(1,T+1):
#     # N*N 크기의 판
#     N = int(input())
#     arr = [input() for _ in range(N)]
#
#     print(f'#{tc} {A(arr)}')



#////////////////////
#fail

    # 5x5 만 생각하면 얘가 됨
    # # 좌상 대각
    # cnt1 = 1
    # for i in range(N-1):
    #     if omok[i][i]=='o' and omok[i+1][i+1]=='o':
    #         cnt1+=1
    #     if cnt1 >= 5:
    #         ans = "YES"
    #         break
    #
    # #우상 대각
    # cnt2= 1
    # for i in range(N-1):
    #     if omok[i][N-1-i]=='o' and omok[i+1][N-2-i] =='o':
    #         cnt2+=1
    #     if cnt2>=5:
    #         ans="YES"
    #         break
