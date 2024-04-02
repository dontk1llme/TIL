# 코딩테스트 연습
# 코딩 기초 트레이닝
# 특별한 이차원 배열 2

def solution(arr):
    answer = 1
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != arr[j][i]:
                answer = 0
                break
        if answer == 0:
            break

    return answer