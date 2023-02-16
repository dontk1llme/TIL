def quickSort(lst,L,R): #퀵소트 나누기라고 생각
    if L<R:
        p = partition(lst,L,R)
        quickSort(lst,L,p-1)
        quickSort(lst,p+1,R)

def partition(lst,L,R): #1회 정렬하는거
    pivot = (L+R)//2
    while L<R:
        while(L<R and lst[L]<lst[pivot]): L+=1
        while(L<R and lst[R]>=lst[pivot]): R-=1
        if L<R:
            if L==pivot: pivot=R
            lst[L], lst[R] = lst[R], lst[L]
    lst[pivot], lst[R] = lst[R], lst[pivot]
    return R

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    L = 0
    R = len(lst) - 1  # 인덱스

    quickSort(lst,L,R)
    print(f'#{tc} {lst[N//2]}')