# SWEA 1859. 백만 장자 프로젝트 D2


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))

    gain = 0
    num = 0
    for i in range(N - 1, -1, -1):  # 뒤에서부터... 가장 큰 거에서만 더하면 되니까.
        # 인덱스 주의
        if price[i] > num:
            num = price[i]
        else:
            gain += num - price[i]

    print(f'#{tc} {gain}')