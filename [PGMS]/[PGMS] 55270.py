# [PCCP 모의고사 #1] 외톨이 알파벳

# solution 1
def solution(input_string):
    input_string += "0"
    answer = ''
    number = [0] * 26

    for i in range(len(input_string) - 1):
        if input_string[i] != input_string[i + 1]:
            number[ord(input_string[i]) - 97] += 1

    for i in range(26):
        if 2 <= number[i]:
            answer += chr(i + 97)

    return answer if answer else "N"

# solution 2
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