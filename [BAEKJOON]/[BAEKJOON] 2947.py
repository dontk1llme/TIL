# [BAEKJOON] 2947 나무조각
# 뭐시기 정렬 순서 그거 아닌가?

lst = list(map(int, input().split()))

while True:
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
            lst[i],lst[i+1] = lst[i+1], lst[i]
            print(*lst)
    if lst == [1,2,3,4,5]: break