
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
            self.rear +=1
            if self.rear == self.size:
                self.rear = 0
            self.arr[self.rear] = value
        return True

    def dequeue(self):
        if self.isEmpty():
            return -1
        self.front += 1 #
        if self.front == self.size:
            self.front =0
        x = self.arr[self.front]
        self.arr[self.front] = '_'
        return x
    def Display(self):
        
        for i in self.arr:
            print(f'{i}', end = ' ')


