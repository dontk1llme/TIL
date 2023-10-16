# PGMS 135808 과일장수
def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    
    for i in range(len(score)//m):
        box = score[m*i:m*(i+1)]
        # 상자에 담긴 사과들은 내림차순 정렬되어있기 때문에 인덱스 -1이 가장 작은 점수
        # 상자에 있는 가장 낮은 사과 점수와 m(한 상자에 들어갈 사과 수)을 곱하여 가격 계산
        answer += box[-1] * m
    
    return answer