# SWEA 3143. 가장 빠른 문자열 타이핑 D4
T = int(input())
for tc in range(1, T+1):
    A,B = map(str, input().split())

    cnt = 0
    i=0
    while i<len(A):
        if A[i:i+len(B)] == B:
            cnt+=1
            i+=len(B)
        else:
            cnt+=1
            i+=1
    print(f'#{tc} {cnt}')


    # for i in range(len(A)-len(B)+1):
    #     print(i)
    #     print(A[i:i + len(B)])
    #     if A[i:i+len(B)] == B:
    #         print('웅 겹쳐')
    #         cnt+=1
    #         i+=i+len(B)
    #         print(i)
    #     else: cnt+=1
