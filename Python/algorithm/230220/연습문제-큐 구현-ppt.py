#Queue 구현
class Queue:
    def __init__(self):
        self.queue=[]
    def isEmpty(self):
        if not self.queue:
            return True
        else:
            return False
    def enqueue(self, data):
        self.queue.append(data)
    def deque(self):
        if self.isEmpty():
            return "큐가 비었따 인간"
        else:
            dequeued = self.queue[0]
            #나머지 재정비
            self.queue = self.queue[1:]
            return dequeued
    def peek(self):
        if self.isEmpty():
            return "큐가 비었따 인간"
        else:
            peeked = self.queue[0]
            return peeked

#1,2,3 차례로 삽입
q =Queue()
for i in range(1,4):
    q.enqueue(i)

#차례로 데이터 꺼내기
for i in range(3):
    print(q.deque())
