# 1677. 데일리실습 2-5. 딕셔너리와 리스트 특징 이해 및 메

todo = [("Python Homework", 3), ("Assay", 4), ("Vacation", 100)]

name = input()
days = int(input())
new = (name, days)

todo.append(new) 
# todo는 리스트고 new는 튜플이라 append를 해 줘야만 튜플 형태 그대로 들어감
# +로 더하려고 하면 그냥 각각 요소로 들어가버림
print(todo)

