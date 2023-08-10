# 176963 추억 점수
# 진짜 매일 한 문제씩 풀어야겠다

def solution(name, yearning, photo):
    answer = [0]*len(photo)
    for i in range(len(name)):
        for j in range(len(photo)):
            for k in range(len(photo[j])):
                if name[i]==photo[j][k]:
                    answer[j]+=yearning[i]
    
    return answer