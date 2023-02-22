# [파이썬 S/W 문제해결 기본] 8일차 - 이진탐색 (제출용) D2
# https://independenceday.tistory.com/entry/SWEA-5176-%EC%9D%B4%EC%A7%84%ED%83%90%EC%83%89-python?category=939239
# https://mungto.tistory.com/209
# 왼쪽 자식 노드는 현재 노드의 *2 위치에 잇음. 오른쪽 자식 노드는 *2+1 위치에 잇음.

def make_tree(n):
    global number
    if n<=N: #배열 크기 내에서
        make_tree(n*2) #왼쪽노드는 헌재 인덱스의 2배
        tree[n] =number #더 못 가면 값 넣기
        number+=1
        make_tree(n*2+1)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    tree = [0 for i in range(N+1)]
    number = 1
    make_tree(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}') #루트, N/2번노드(홀수면 소수점 버림)