#//////////////
def qsort(lst):
    # [1] 종료조건
    if len(lst) <= 1:  # 더 이상 정렬불가능: 1개 이하인 경우
        return lst
    # [2] 단위작업: p 기준으로 양쪽 정렬
    p = lst.pop()  # 가장 오른쪽의 값을 기준으로 삼은 경우
    left = []
    right = []
    for n in lst:
        if n < p:  # 기준보다 작은경우 왼쪽에 추가
            left.append(n)
        else:
            right.append(n)

    # [3] 왼쪽정렬 결과 + p + 오른쪽 정렬결과 리턴
    return qsort(left) + [p] + qsort(right)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    lst = qsort(lst)
    print(f'#{test_case} {lst[N // 2]}')


# //////////////////////////
def qsort(lst):
    # [1] 종료조건
    if len(lst) <= 1:  # 더 이상 정렬불가능: 1개 이하인 경우
        return lst
    # [2] 단위작업: p 기준으로 양쪽 정렬
    p = lst.pop()  # 가장 오른쪽의 값을 기준으로 삼은 경우
    left = []
    right = []
    for n in lst:
        if n < p:  # 기준보다 작은경우 왼쪽에 추가
            left.append(n)
        else:
            right.append(n)

    # [3] 왼쪽정렬 결과 + p + 오른쪽 정렬결과 리턴
    return qsort(left) + [p] + qsort(right)


def qsort_idx(s, e):
    # [1] 종료조건: 정렬할 개수가 1개 이하인 경우
    if s >= e:
        return

    # [2] 단위작업: p 기준으로 정렬
    p = e
    t = s
    for i in range(s, e):
        if lst[i] < lst[p]:
            lst[i], lst[t] = lst[t], lst[i]
            t += 1
    lst[t], lst[p] = lst[p], lst[t]

    # [3] t 기준으로 양쪽 정렬
    qsort_idx(s, t - 1)  # 왼쪽
    qsort_idx(t + 1, e)  # 오른쪽


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    # lst = qsort(lst)
    # qsort_idx(0, N-1)
    lst.sort()
    print(f'#{test_case} {lst[N // 2]}')