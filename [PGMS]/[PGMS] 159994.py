# 159994 카드 뭉치
# 문제 이해 및 경우의 수 생각
def solution(cards1, cards2, goal):
    stack_1 = []
    stack_2 = []

    cnt = 0
    for i in cards1:
        if i not in goal:
            cnt += 1

    for _ in range(cnt):
        cards1.pop()

    cnt = 0
    for i in cards2:
        if i not in goal:
            cnt += 1

    for _ in range(cnt):
        cards2.pop()

    for i in goal:
        if i in cards1:
            stack_1.append(i)
        else:
            stack_2.append(i)

    if stack_1 == cards1 and stack_2 == cards2:
        return "Yes"
    else:
        return "No"