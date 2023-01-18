#1434. 데일리실습 1-2. 게시판의 페이지 수 구하기 예제

total = int(input("게시글의 총 갯수를 입력하세요: "))
one = int(input("한 페이지에 필요한 게시글 수를 입력하세요: "))

if total%one == 0:
    print(total//one)
else: print(total//one + 1)
