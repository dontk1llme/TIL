# [BAEKJOON] 4673 셀프 넘버
# set 활용해서 푸는 인사이트가 없어서.. 타 코드 참고
# 전체 set 하나,, 그리고 notselfnum set 하나,,, 두개 빼면 답이 나옴
allnum = set(range(1,10001))
notselfnum = set()

#selfnum 생성기
# ex. 123 -> 123+1+2+3 => str로 바꿔서 하나씩
for i in range(1, 10001):
    for j in str(i):
        i+=int(j)
    notselfnum.add(i)

selfnum = sorted(allnum-notselfnum) #sort 해줘야 순서대로
for i in selfnum:
    print(i)

