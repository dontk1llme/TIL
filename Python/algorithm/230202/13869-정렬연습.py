# 13869-정렬연습
# 어제 버블정렬로 풀어봤는데 오늘은 카운팅정렬로 풀어보겠슴도

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))



    print(f'#{tc}', end=' ')
    for k in range(N):
        print(arr[k], end=' ')
    print()