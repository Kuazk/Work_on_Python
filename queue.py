
import time

class Queue:

    def __init__(self,size):

        self.size = size
        self.front = -1
        self.rear = -1
        self.arr = ['_'] * size

    def isEmpty(self):
        return self.rear == self.front
    def isFull(self):
        return (self.rear+1) == self.front
    def enqueue(self,value):
        if self.isFull():
            return False
        elif self.isEmpty():
            self.rear +=1
            self.arr[self.rear] = value
        else: 
            self.rear = (self.rear + 1) % self.size
            self.arr[self.rear] = value
        return True

    def dequeue(self):
        if self.isEmpty():
            return -1
        self.front = (self.front +1) % self.size
        x = self.arr[self.front]
        self.arr[self.front] = '_'
        return x
    def Display(self):
        
        for i in self.arr:
            print(f'{i}', end = ' ')

queued = Queue(40)
queued.enqueue('L')
queued.enqueue('O')
queued.enqueue('O')
queued.enqueue('S')
queued.enqueue('E')
queued.enqueue('E')
queued.enqueue('R')

count = 1
queued.Display()
print('')
while count <999:
    count +=1 
    queued.enqueue(queued.dequeue())
    queued.Display()
    print('')
    time.sleep(0.1)
