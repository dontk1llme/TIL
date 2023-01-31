# 1467. 데일리과제 8-4. 객체지향의 특성과 심화 사용 예제 2 Lv4

class Stack:
    def __init__(self):
        self.stack = [] #이름 공간에 넣으라는 말 잘 알아듣기...
    
    def empty(self):
        if len(self.stack) == 0: return True
        else: return False
    
    def top(self):
        if len(self.stack) == 0: return None
        else: return self.stack[-1]
    
    def pop(self):
        if len(self.stack) == 0: return None
        else: 
            last = self.stack.pop() #자체 함수 써도 되나봐
            return last
    
    def push(self, data):
        self.stack.append(data)
    
    def __repr__(self):
        print(self.stack)

