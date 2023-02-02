# 1859. 백만 장자 프로젝트 D2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))

    gain = 0
    for i in range(len(price)):
        if 