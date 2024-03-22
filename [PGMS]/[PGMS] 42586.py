import math


def solution(progresses, speeds):
    answer = []

    l = []
    n = len(progresses)
    for i in range(n):
        l.append(math.ceil((100 - progresses[i]) / speeds[i]))

    c, t = 1, l[0]
    for i in range(1, n):
        if l[i] > t:
            answer.append(c)
            t = l[i]
            c = 1
        else:
            c += 1
    answer.append(c)

    return answer