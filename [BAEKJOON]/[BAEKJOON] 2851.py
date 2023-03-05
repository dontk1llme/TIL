# [BAEKJOON] 2851 슈퍼 마리오

lst = []
for _ in range(10):
    lst.append(int(input()))

score = 0
for i in lst:
    score+=i
    if score>=100:
        if score-100 > 100-(score-i):
            score-=i
        break
print(score)