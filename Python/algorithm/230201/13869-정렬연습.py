#버블정렬 해보기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(N - 1, 0, -1):  # 각 구간의 끝
        for j in range(i):  # 비교할 왼쪽 원소
            if arr[j] > arr[j + 1]:  # > 말고 < 하면 내림차순으로 가능
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # 큰 원소 오른쪽으로 (오름차)
    print(f'#{tc}', end=' ')
    for k in range(N):
        print(arr[k], end=' ')
    print()