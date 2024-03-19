# 코딩테스트 연습 - 월간 코드 챌린지 시즌1 - 두 개 뽑아서 더하기

def solution(numbers):
    answer = []
    tmp = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            tmp = numbers[i] + numbers[j]
            answer.append(tmp)
    answer = list(set(answer))
    answer = sorted(answer)

    return answer