#  [파이썬 S/W 문제해결 구현] 4일차 - 병합 정렬 (제출용) D3

def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    nleft = merge_sort(left)
    nright = merge_sort(right)
    return merge(nleft, nright)


def merge(nleft, nright):
    global cnt
    i, j = 0, 0
    nlst = []

    if nleft[-1] > nright[-1]: #정답 찾기
        cnt += 1

    while i < len(nleft) and j < len(nright):
        if nleft[i] < nright[j]:
            nlst.append(nleft[i])
            i += 1
        else:
            nlst.append(nright[j])
            j += 1
    while i < len(nleft):
        nlst.append(nleft[i])
        i += 1
    while j < len(nright):
        nlst.append(nright[j])
        j += 1
    return nlst


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0

    ans = (merge_sort(lst))[N // 2]

    print(f'#{tc} {ans} {cnt}')

