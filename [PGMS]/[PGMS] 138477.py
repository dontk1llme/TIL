# pgms 명예의 전당 1 - 138477
def solution(k, score):
    answer = []
    lst = []
    for i in range(len(score)):
        lst.append(score[i])
        if len(lst)>k:
            lst.remove(min(lst))
        answer.append(min(lst))
        
    return answer