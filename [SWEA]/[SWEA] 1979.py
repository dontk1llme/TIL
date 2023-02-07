#swea 1979. 어디에 단어가 들어갈 수 있을까 D2

# 가로로 한번 보고 세로로 한번 보기
# 연속된 1의 길이가 K보다 길면 ㄱㅊ


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split()) # 퍼즐 길이, 단어 길이
    arr = [0]*N
    for n in range(N):
        arr[n] = list(map(int, input().split())) #0은 불가능, 1은 가능

    cnt = 0
    # 1이면 +1, 0이면 다음 배열로 change, 1이면 다시 +1
    avail = [0] * (N*N)
    avnum = 0
    #가로
    for i in arr:
        for j in range(len(i)):
            if i[j] == 1: avail[avnum]+=1
            elif i[j]==0:
                if j+1<len(i):
                    if i[j+1]!=0: avnum+=1
        avnum+=1
    #세로
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[j][i] ==1: avail[avnum]+=1
            elif arr[j][i]==0: #0이 한 칸일 때..... 어떡함
                avnum += 1
                # if i+1<len(arr):
                #     if arr[j][i+1]!=0: avnum-=1 #걍 얘 없어도 됨... 배열 크기 좀만 늘리면
        avnum += 1

    for i in avail:
        if i == K: cnt+=1

    print(f'#{tc} {cnt}')






