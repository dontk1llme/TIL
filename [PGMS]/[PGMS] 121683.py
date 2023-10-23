# pccp 모의고사 1-1
# 121683

def solution(input_string):
    answer = ''
    solo = []
    dic = {}
    now = ''

    for s in input_string:
        if dic.get(s) is None :
            dic[s] = 1
        else:
            if s != now:
                solo.append(s)
        now = s

    if len(solo) == 0:
        answer = 'N'
    else:
        answer = "".join(sorted(set(solo)))

    return answer