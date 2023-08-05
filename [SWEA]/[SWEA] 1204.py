#swea 1204. [S/W 문제해결 기본] 1일차 - 최빈수 구하기 D2

num = int(input())

for i in range(1, num+1):
    case = int(input())
    ls = list(map(int, input().split()))
    max_idx=0
    max_num=0

    count=[0]*101 #0점 이상 100점 이하
    for j in range(1000):
        count[ls[j]] +=1    #순서대로 나온 개수 세기

    for j in range(101):
        if count[j] >= max_num:
            max_num=count[j] #최빈값이 나온 횟수
            max_idx=j        #최빈값
    print(f'#{case} {max_idx}')
 