#pgms 2023카카오 - 개인정보 수집 유효기간
#ㅁㅊ 변수 ㅅ하나 잘못써서 백년 삽질
# https://school.programmers.co.kr/questions/44243

terms =  ["A 23"]
privacies =  ["2020.01.28 A"]
today ="2022.02.28"
#[1, 3]

def solution(today, terms, privacies):
    #terms 나누기
    termchar = []
    termmon = []
    for i in range(len(terms)):
        char, mon = map(str, terms[i].split())
        termchar.append(char)
        termmon.append(int(mon))

    ty, tm, td = map(int, today.split('.')) #숫자화
    answer = []

    for i in range(len(privacies)):
        date,pt = map(str, privacies[i].split())
        py, pm, pd= map(int, date.split('.'))
        # tems 확인
        for j in range(len(terms)):
            if pt == termchar[j]:
                pm += termmon[j] #달 수 더해주기
                break
        while True: #기간 계산day는 더하기에는 필요업슴
            if pm>12:
                py+=1
                pm-=12
                if pm==0:
                    pm=1
            else: break
        if py<ty:
            answer.append(i+1)
        elif (py==ty) and (pm<tm):
            answer.append(i+1)
        elif (py==ty) and (pm==tm) and (pd<=td):
            answer.append(i+1)
        print('유효기간, 오늘날짜')
        print(py,pm,pd)
        print(ty, tm, td)

    return answer

print(solution(today, terms, privacies))

