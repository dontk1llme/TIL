# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def average(scores):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    '''
    점수의 총 합을 리스트 원소 수 만큼 나누어 평균을 구해주자
    '''
    
    ave = sum(scores)/len(scores)
    return ave


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    scores = [80, 90, 85, 75]
    print(average(scores))    # 82.5