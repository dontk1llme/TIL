# pgm 92341 주차 요금 계산
# 카카오 블라인드 채용
#시간단위를 분단위로 바꾸고 기본요금 이하면 그냥, 기본요금 이상이면 기본요금+10분단위 올림
#출차내역 없으면 23:59에 나간걸로
#차량번호 작은 자동차부터 주차요금 담아서 return
# 나갈 때마다 계산이 아니라 하루 총량 계산이엇네.. 그니까 답이 안나오지

import math #올림 하려고
#
# fees = [180, 5000, 10, 600]
# records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
# result = [14600, 34400, 5000]

def solution(fees, records):
    instack, outstack = [], []

    #in, out 나눠서 만들어주기
    for i in records:
        time, carnum, inout = map(str, i.split())
        if inout=='IN':
            instack.append([time, carnum])
        else: outstack.append([time, carnum])

    answer = {}
    while instack:
        it, ic = instack[0]
        ot,oc = '23:59',''
        for i in range(len(outstack)): #outstack에 잇으면 시간으로 계산
            if outstack[i][1]==ic:
                ot, oc = outstack[i]
                instack.pop(0)
                outstack.pop(i)
                break
        if ot =='23:59':
            instack.pop(0)

        #시간 계산
        hour = int(ot[:2])-int(it[:2])
        minute = int(ot[3:])-int(it[3:])
        if minute<0:
            hour-=1
            minute = 60 + minute
        totalmin = hour * 60 + minute
        if ic in answer:
            answer[ic] += totalmin
        else: answer[ic] = totalmin

    answer = sorted(answer.items())
    real_answer = []

    for i in answer:
        # 요금 계산
        if i[1]>fees[0]:
            totalfee = fees[1] + math.ceil((i[1]-fees[0])/fees[2]) * fees[3]
        else: totalfee = fees[1]
        real_answer.append(totalfee)

    return real_answer
