#PGMS 150368 kakao - 이모티콘 할인행사

# 1번 목표가 우선, 2번 목표가 그 다음
# 비율을 하나하나 조정해가면서 보는 걸 어케 하는지 모르겟어서...

# 로직설명 https://velog.io/@yannju/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%9D%B4%EB%AA%A8%ED%8B%B0%EC%BD%98-%ED%95%A0%EC%9D%B8%ED%96%89%EC%82%AC
# 파이썬 풀이 좀 더 간결함 https://magentino.tistory.com/59
# 백트래킹이라는데 할 줄 모르겟어서 일단 포기함. 받아적으면서 공부해보자................
# 에엥 그래도 모르겟음.. ㅠ

discounts = [10, 20, 30, 40]#할인율
# 탐색은 최대 4^7번 필요함. (m 최대 7)
answer = [-1, -1]


def solution(users, emoticons):
    n, m = len(users), len(emoticons)
    discount_list = [0] * m

    def search(idx):
        global answer
        if idx == m:
            sale_num, cost_num = 0, 0
            for i in range(n): #전체 다 돌기
                tmp = 0
                for j in range(m):
                    if users[i][0] <= discount_list[j]:
                        tmp += emoticons[j] * (100 - discount_list[j]) // 100
                if tmp >= users[i][1]:
                    sale_num += 1
                else:
                    cost_num += tmp
            if sale_num > answer[0] or sale_num == answer[0] and cost_num > answer[1]:
                # 조건에 맞으면 답에 넣기
                answer = [sale_num, cost_num]
            return

        for i in range(4):
            discount_list[idx] = discounts[i]
            search(idx + 1)

    search(0)

    return answer

