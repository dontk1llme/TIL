# 2164. 카드 2 (내 문제)
# 제일 위에 있는 카드 버리기
# 제일 위에 있는 카드를 맨 뒤로
# 그냥 하면 시간초과나서... 어쩔 수 없이 deque 써봤다
# pop(0) 보다 deque의 popleft가 시간복잡도가 낮음.

from collections import deque

N = int(input())
card = deque()

for i in range(1, N+1): #큐 생성
    card.append(i)
while len(card)>1: #조건문 실행
    card.popleft()
    a = card.popleft()
    card.append(a)

print(card[0])


# N = int(input())
# card = list(range(1,N+1))
# while len(card)>1:
#     card.pop(0)
#     tmp = card.pop(0)
#     card.append(tmp)
#
# print(card[0])