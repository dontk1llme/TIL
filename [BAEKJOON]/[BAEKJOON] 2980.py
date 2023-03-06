# boj 2980 신호등
# https://kimmeh1.tistory.com/314

N, L = map(int, input().split())
pos = 0
answer = 0

for _ in range(N):
    d, r, g = map(int, input().split())

    answer += (d - pos)
    pos = d
    if answer % (r+g) <= r:
        answer += (r - (answer%(r+g)))

answer += (L-pos)
print(answer)