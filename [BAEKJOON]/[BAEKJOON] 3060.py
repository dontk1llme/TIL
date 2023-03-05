# [BAEKJOON] 3060 욕심쟁이 돼지

d = {0:3, 1:4, 2:5, 3:0, 4:1, 5:2} #맞은편

T = int(input())
for tc in range(1, T+1):
    N = int(input()) #사료의 양
    lst = list(map(int, input().split()))#돼지가 먹엇던 양
    cnt=0
    while N>=0:
        N -= sum(lst)
        cnt+=1
        for i in range(len(lst)):
            next = i%5+1
            before = i%5-1
            lst[i] = lst[next] + lst[before] + lst[d[i]]
        # print(N, lst)

    print(cnt)


#////////////////////////////
# 더 쉬운 규칙이 잇엇네. 쩝
# 하루마다 4배의 양이 는대여.
for _ in range(int(input())):
    N = int(input())
    slst = sum(list(map(int, input().split())))
    day = 1
    while N>=slst:
        day+=1
        slst*=4
    print(day)