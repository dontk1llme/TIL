# swea 1210. [S/W 문제해결 기본] 2일차 - Ladder1
T = 10
for tc in range(1,T+1):
    num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    #사다리:1, 도착점:2, 맨윗줄에서 x좌표 구하기.
    #X 구하기
    xx, xy = len(arr)-1,0 #x의 x좌표, y좌표
    for j in range(len(arr)):
        if arr[xx][j]==2:
            xy = j

    while True:
        now = arr[xx][xy]
        if xy<99 and arr[xx][xy+1]==1: #우가 1이면
            while xy <99 and arr[xx][xy+1]==1:
                # if arr[xx][xy + 1] != 0:# 만약 우로 이동햇으면 좌로는 다시 가면 안되고 좌로 이동햇으면 우로는 다시가면안됨
                xy += 1           #그래서 한쪽으로 쭉 가다가
            else: xx -=1

        elif xy>0 and arr[xx][xy-1]==1: #좌가 1이면
            while xy>0 and arr[xx][xy-1]==1:  # 만약 우로 이동햇으면 좌로는 다시 가면 안되고 좌로 이동햇으면 우로는 다시가면안됨
                xy -= 1           #그래서 한쪽으로 쭉 가다가
            else: xx -=1
        else: xx-=1 #좌우 다 못가면

        if xx==0: break #도착

    print(f'#{num} {xy}')

# https://sbox.tistory.com/8
# 인덱스에러..............................
#  xy<99 and arr[xx][xy+1]==1 < 이걸 못만들어서. ㅠ 멍청아
