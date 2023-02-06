T = int(input())
for tc in range(1, T+1):
    arr=list(map(int, input().split()))
    cnt = 0

    #부분집합
    for i in range(1, 1<<len(arr)): #부분집합의 개수
        sum = 0
        for j in range(10): # 원소의 수만큼 비트를 비교
            if i&(1<<j): # i의 j번 비트가 1인 경우
                sum+=arr[j] #j번 원소 더하기

        if sum==0:
            cnt+=1 #여기에서 break 해줘도 됨
    if cnt > 0: print(f'#{tc} 1')
    else: print(f'#{tc} 0')
    
    
    # 10개의 정수를 입력 받아 부분집합의 합이 0이 되는 것이 존재하는지를 계산하는 함수를 작성해보자.
    # cnt 개수가 아니라... True False 반환이엇음.......ㄷ.ㄷ.
