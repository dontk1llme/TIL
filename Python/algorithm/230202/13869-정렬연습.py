# 13869-정렬연습
# 어제 버블정렬로 풀어봤는데 오늘은 카운팅정렬로 풀어보겠슴도
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = [0]*(max(arr)+1) #정수 항목들로 직접 인덱스 되게
    for num in arr: #항목들 개수 세기
        cnt[num]+=1
    for i in range(1, len(cnt)): #정렬된 위치로 바로 삽입하기 위해서 갱신
        cnt[i]=cnt[i]+cnt[i-1]

    result = [0]*len(arr) #정렬된
    for num in arr:
        idx = cnt[num]
        result[idx-1] = num #idx-1 말고 idx하면 인덱스에러남. #인덱스 0부터 시작이라 이렇게 하라는데 음...
                            # 만약 num = 4면 cnt[num]==5면 카운트가 무조건 숫자보다 +1 크니까 해당 자리에 넣어줄수있음
        cnt[num] -=1


    print(f'#{tc}', end=' ')
    for k in range(N):
        print(result[k], end=' ')
    print()