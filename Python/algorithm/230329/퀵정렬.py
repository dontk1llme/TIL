#  [파이썬 S/W 문제해결 구현] 4일차 - 퀵 정렬 (제출용) D2

def hoare(A,l,r):
    pivot=A[l] #맨 왼쪽원소 기준
    i,j = l,r #피봇보다 큰값은 오른쪽, 작은값은 왼쪽으로 이동
    while i<=j:
        while i<=j and A[i]<=pivot: #교차되거나 큰애 만나면 멈추기
            i+=1
        while i<=j and A[j]>=pivot: #교차되거나 작은애 만나면 멈추기
            j-=1
        if i<j: #교차하지 않은 경우
            A[i],A[j]=A[j],A[i]
    A[j],A[l] = A[l],A[j]
    return j

def qsort(A,l,r):
    global cnt
    cnt+=1
    if l<r:
        s = hoare(A,l,r)
        qsort(A,l,s-1)
        qsort(A,s+1,r)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0 #qsort 호출된 횟수
    qsort(lst, 0, N-1)
    print(f'#{tc} {lst[N//2]}')
