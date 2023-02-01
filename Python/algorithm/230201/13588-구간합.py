T = int(input())
for tc in range(1, T+1):
    N,M=map(int, input().split())
    arr = list(map(int, input().split()))
    max = 0
    min = 10000*N
    for i in range(0, N-M+1):
        sum = 0
        for j in range(i, M+i):
            sum += arr[j]
        if sum > max: max = sum
        if sum < min: min = sum
    print(f'#{tc} {max-min}')


