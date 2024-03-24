# 코딩테스트 연습
# 연습문제
# 최댓값과 최솟값

def solution(s):
    lst = list(s.split())
    min, max = 0, 0

    # 숫자로 해서 비교
    for i in range(len(lst)):
        if i == 0:
            min, max = int(lst[i]), int(lst[i])
        else:
            if int(lst[i]) < min:
                min = int(lst[i])
            if int(lst[i]) > max:
                max = int(lst[i])
    answer = f'{min} {max}'

    return answer