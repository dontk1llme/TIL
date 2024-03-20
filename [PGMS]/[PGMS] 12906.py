# 코딩테스트 연습
# 스택/큐
# 같은 숫자는 싫어

def solution(arr):
    answer = ['']
    for i in arr:
        if i != answer[-1]:
            answer.append(i)
    answer.pop(0)
    return answer