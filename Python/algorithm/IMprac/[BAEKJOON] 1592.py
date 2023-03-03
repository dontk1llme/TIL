#[BAEKJOON] 1592 영식이와 친구들
#인덱스별로 하려고 했는데 그냥 원래번호-1이라고 생각하면 지장없음.

N,M,L = map(int, input().split())
lst = [0]*(N)

now = 0
while max(lst)<M:
    lst[now]+=1
    if lst[now]%2==1: #홀
        now = (now+L)%N
    else: #짝
        now = (now-L)%N

print(sum(lst)-1)