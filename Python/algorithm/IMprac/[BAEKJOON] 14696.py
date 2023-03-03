# [BAEKJOON] 14696 딱지놀이

N = int(input()) #라운드
for _ in range(N):
    # 4 3 2 1: 별 동그라미 네모 세모
    # 첫 인덱스는 그 줄의 개수임
    a = list(map(int, input().split()))
    a = a[1:]
    b = list(map(int, input().split()))
    b = b[1:]

    # 두 딱지의 별의 개수가 다르다면, 별이 많은 쪽의 딱지가 이긴다.
    # 별 동그라미 네모 세모 순으로 반복됨
    num = 4
    while num>=0:
        if num==0: #비김
            print('D')
            break
        if a.count(num) != b.count(num):
            if a.count(num)>b.count(num): print('A')
            else: print('B')
            break
        else: num-=1


