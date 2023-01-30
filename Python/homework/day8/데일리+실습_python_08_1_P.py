class kkakdugi:
    def __init__(self, list):
        self.list = list
    
    def find(self):
        self.list.sort()
        i = 0
        while (i<len(self.list)):
            try:
                if self.list[i]==self.list[i+1]: 
                    i+=2
            except: 
                print(self.list[i])
                break



participants =  [3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21]

k = kkakdugi(participants)
k.find()