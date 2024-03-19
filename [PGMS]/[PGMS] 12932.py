# 코딩테스트 연습
# 연습문제
# 자연수 뒤집어 배열로 만들기

def solution(n):
    answer = []
    while n>0:
        answer.append(n%10)
        n=n//10
    return answer