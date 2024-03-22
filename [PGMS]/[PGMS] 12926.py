# 코딩테스트 연습
# 연습문제
# 시저 암호

def solution(s, n):
    # 문자열 함수랑 유니코드 26인 거 인지...
    answer = ''
    for i in s:
        if i==' ':
            answer+=i
        elif i.islower():
            answer += chr((ord(i)-ord('a') + n) % 26 + ord('a'))
        elif i.isupper():
            answer += chr((ord(i)-ord('A') + n) % 26 + ord('A'))
    return answer