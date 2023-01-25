# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def caesar(word, n):
    answer = ""
    n = n % 26
    for s in word :
        new_s = ord(s) + n
        if s.islower() :
            if new_s > 122 :
                new_s -= 26
        else :
            if new_s > 90 : 
                new_s -= 26
        answer += chr(new_s)
    return answer
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(caesar('apple', 5))      # fuuqj
    print(caesar('ssafy', 1))      # ttbgz
    print(caesar('Python', 10))    # Zidryx
