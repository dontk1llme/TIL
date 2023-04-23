# # 1. 멈추는 조건이 필요
# # 2. 조건을 맞추기 위해서 args 바뀌어야 합니다.
# # n + n-1 ~ 9 + 8 + 7 + ... + 0, print
# def func(n):
#     if n:
#         return n
#     return func(n-1) + n
    
# func(10)

##################################################################################

# def func(number):
#     print(number)
#     if number == "":
#         return 0
#     return func(number[:-1]) + int(number[-1])

# print(func("1234"))

##################################################################################

# cnt = 0
# def func(number):
#     global cnt
#     cnt += 1
#     if number == 0:
#         return 0
#     quotient =  number // 10
#     remainder = number % 10
#     return func(quotient) + remainder
# print(func(1234))
# print(cnt)

##################################################################################

cnt = 0
def func(number):
    global cnt
    cnt += 1
    quotient =  number // 10
    remainder = number % 10
    if quotient == 0:
        return remainder
    return func(quotient) + remainder
print(func(1234))
print(cnt)