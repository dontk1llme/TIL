# 박스끼리의 거리를 구하는 문제
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max = 0

    for i in range(N):
        cnt = 0
        for j in range(i+1, N): #이 범위 설정 제대로 안 해 줘서 Fail될 뻔
            if arr[i] > arr[j]:
                cnt += 1

        if cnt > max:
            max = cnt

    print(f'#{tc} {max}')
