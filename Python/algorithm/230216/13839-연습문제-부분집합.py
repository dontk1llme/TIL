# Stack2_연습문제_2: 부분집합 (제출용) D3
# 수업 중 풀어 준 코드.

# #비트 사용
# def f(i,k,key): #i부터 k까지 합이 5
#     global cnt
#     if i==k:
#         s=0
#         for j in range(k):
#             if bit[j]:
#                 s+=lst[j]
#         if s==key:
#             cnt+=1
#         return cnt
#     else:
#         bit[i]=1
#         f(i+1, k, key)
#         bit[i]=0
#         f(i+1, k, key)
#
#
# T = int(input())
# for tc in range(1,T+1):
#     N,key=map(int, input().split())
#     lst = list(map(int, input().split()))
#     bit=[0]*N
#     cnt=0
#
#     f(0,N,key)
#     print(f'{tc} {cnt}')


#//////////////////////////////////
#다른풀이
def f(i, N, s, K):
    global cnt
    if s == K:
        cnt += 1
        return
    elif s > K:
        return
    elif i == N:
        return
    else:
        f(i + 1, N, s + lst[i], K)
        f(i + 1, N, s, K)


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = 0
    f(0, N, 0, K)
    print(f'#{tc}', cnt)