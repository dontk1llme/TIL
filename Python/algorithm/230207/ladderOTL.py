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

    # dc = [1, -1] #좌 우
    # dl = -1 #내려가는 경우는 필요없음. 올라가기만

    while xx>=0:
        now = arr[xx][xy]

        # for i in range(2):
        #     if arr[xx][xy+dc[i]]==1: #좌우가 1이면.
        #         while arr[xx][xy+dc[i]]!=0:  #만약 우로 이동햇으면 좌로는 다시 가면 안되고 좌로 이동햇으면 우로는 다시가면안됨
        #             xy += dc[i]             #그래서 한쪽으로 쭉 가다가
        #         xx += dl                    #0 만나면 위로 한칸 가게 햇음
        if arr[xx][xy+1]==1: #우가 1이면
            xy += 1
            while arr[xx][xy + 1] != 0:  # 만약 우로 이동햇으면 좌로는 다시 가면 안되고 좌로 이동햇으면 우로는 다시가면안됨
                xy += 1           #그래서 한쪽으로 쭉 가다가
            xx -=1
        elif arr[xx][xy-1]==1: #좌가 1이면
            xy -= 1
            while arr[xx][xy - 1] != 0:  # 만약 우로 이동햇으면 좌로는 다시 가면 안되고 좌로 이동햇으면 우로는 다시가면안됨
                xy -= 1           #그래서 한쪽으로 쭉 가다가
            xx -=1
        else: xx-=1


        if xx==0: break

    print(f'#{num} {xy}')
