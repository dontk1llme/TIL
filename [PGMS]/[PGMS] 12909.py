# 코딩테스트 연습
# 스택/큐
# 올바른 괄호

def solution(s):
    lst = []
    for i in s:
        if i=='(':
            lst.append(i)
        else:
            if len(lst)==0 or lst.pop()!='(': #pop을 밑에서 따로 하려고 햇는데 그냥 바로 뽑아도
                return False
    if len(lst)==0:
        return True
    return False