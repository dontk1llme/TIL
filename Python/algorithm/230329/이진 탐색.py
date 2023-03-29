#  [파이썬 S/W 문제해결 구현] 4일차 - 이진 탐색 (제출용) D3
# 왼,오 번갈아가는걸 position으로 표현. 난 그거 못해서 혜진언니거 베낌

T = int(input())

def bs(lst, t, s, e, p): #p -1: 왼쪽, p 1: 오른쪽
    global ans

    if s>e:
        return None

    mid = (s+e)//2

    if lst[mid]==t:
        ans+=1
        return
    elif lst[mid]>t:
        if p==-1:
            return
        return bs(lst,t,s,mid-1,-1)
    else:
        if p==1:
            return
        return bs(lst,t,mid+1,e,1)




for tc in range(1, T+1):
    N,M = map(int,input().split())
    Alst = sorted(list(map(int,input().split()))) #이진탐색을 위해 정렬
    Blst = list(map(int, input().split()))


    ans = 0
    for b in Blst:
        bs(Alst, b,0,len(Alst)-1, 0)

    print(f'#{tc} {ans}')


#/////////////////////////////////////////////
# 영진님 코드
def func(l, r, k, drc):
    global ans
    m = (l + r) // 2
    if A[m] == k:
        ans += 1
        return
    if l > r:
        return
    # drc: 1일때 오른쪽탐색, 2일때 왼쪽 탐색, 처음앤 양쪽탐색
    if (drc == 1 and k < A[m]) or (drc == 2 and k > A[m]):
        return
    # 왼쪽 탐색
    if drc != 1:
        func(l, m - 1, k, 1)
    # 오른쪽 탐색
    if drc != 2:
        func(m + 1, r, k, 2)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    ans = 0

    for b in B:
        func(0, N - 1, b, 0)

    print(f'#{tc}', ans)