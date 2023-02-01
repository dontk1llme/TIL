T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    min = 1000000
    max = 0
    for i in range(N):
        if min > arr[i]: min = arr[i]
        if max < arr[i]: max = arr[i]
    print(f'#{tc} {max-min}')



