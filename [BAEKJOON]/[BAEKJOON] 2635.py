# 2635. 수 이어가기
import random

N = int(input())
sec = random.choice(range(N))
lst = [N]
front, next = N, sec
while next>0:
    lst.append(next)
    front, next = next, front-next
    # print(front ,next)
print(len(lst))
print(*lst)


