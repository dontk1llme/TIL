# 코딩테스트 연습 - PCCE 기출문제 - [PCCE 기출문제] 10번 / 데이터 분석

def solution(data, ext, val_ext, sort_by):
    answer = []
    #     정렬 아이디어 부족
    #     출처: https://1ets-just-do-it.tistory.com/140 [파이썬은 신이야:티스토리]
    sort_type = {"code" : 0, "date" : 1, "maximum" : 2, "remain" : 3}
    for i in data:
        if i[sort_type[ext]] <= val_ext: #무조건 date가 아닌 걸 간과했음
            answer.append(i)
    print(answer)


    sorted_filtered_data = sorted(answer, key=lambda x: x[sort_type[sort_by]])
    return sorted_filtered_data