#코딩테스트 연습 - 연습문제 - 정수 제곱근 판별


def solution(n):
    answer = 0
    # 제곱인지 아는 법: 루트 씌우면 됨
    tmp = n ** (0.5)
    if tmp % 1 == 0: # 루트n이 정수라면
        answer = (tmp+1)**2
    else: answer = -1
    return answer