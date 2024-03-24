#  코딩테스트 연습 연습문제 JadenCase 문자열 만들기
def solution(s):
    answer = ''
    lst = list(s.split(" "))  # 왠진 모르겠으나 그냥 () 했다가 (" ")으로 하니까 됨... 머지

    for i in lst:
        for j in range(len(i)):
            if j == 0 and not i[j].isdigit():
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += ' '

    return answer[:-1]  # 마지막공백제거