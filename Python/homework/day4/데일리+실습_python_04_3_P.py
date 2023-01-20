#1689. 데일리실습 4-3. 조건문과 반복문을 이용한 중복 숫자 제거 lv3
# 입력 예시
# [1, 1, 3, 3, 0, 1, 1]

# 출력 예시
# [1, 3, 0, 1]

ls = [1, 1, 3, 3, 3, 0, 1, 1]
newls = []
for i in range(0,len(ls)-1):
    if ls[i]!=ls[i+1]:
        newls.append(ls[i])
if ls[-1]!=newls[-1]:
    newls.append(ls[-1])

print(newls)