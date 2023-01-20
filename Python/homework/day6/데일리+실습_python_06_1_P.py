# 1447. 데일리실습 6-1. 크롤링을 통한 서비스 개발 예제1

# A. 입력예시
# de_identify('970103-1234567')
# de_identify('8611232345678')

# B. 출력예시
# 970103*******
# 861123******* 

def de_identify(str):
    newstr=str[:6]+'*******'
    print(newstr)


de_identify('970103-1234567')
de_identify('8611232345678')

        