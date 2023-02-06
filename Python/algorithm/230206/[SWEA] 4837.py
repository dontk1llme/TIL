#swea 4837 부분집합의 합

T = int(input())
for tc in range(1, T+1):
    N,K = map(int, input().split())
    arr = list(range(1,13))
    cnt = 0

    for i in range(1, 1<<len(arr)): #부분집합의 개수
        subset = []
        sum = 0
        for j in range(len(arr)): # 원소의 수만큼 비트를 비교
            if i&(1<<j): # i의 j번 비트가 1인 경우
                subset.append(arr[j]) # 부분집합 개수 찾기 위해서 새 list에 더해주기
                sum+=arr[j] #j번 원소 더하기

        if len(subset)==N and sum==K:
            cnt+=1
    print(f'#{tc} {cnt}')
