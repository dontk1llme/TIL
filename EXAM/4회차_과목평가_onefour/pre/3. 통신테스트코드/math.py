import math

#두 점의 좌표
start = (1,1)
end = (2,2)

a = abs(end[0] - start[0]) #x좌표의 차이
b = abs(end[1] - start[1]) #y좌표의 차이

#피타고라스 -> 두 점 사이의 거리
r = math.sqrt(a**2 + b**2)

#아크탄젠트.
#결과가 degree가 아닌 radian임
radian = math.atan(b/a)
#실제 각도는 이렇게 변경해 줘야 함
d = math.degrees(radian)
