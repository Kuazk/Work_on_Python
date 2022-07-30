



class Node():
    def __init__(self,val = None,next = None):
        self.val = val
        self.next = next

class Dequeue:
    def __init__(self):
        self.rear = Node()
        self.front = self.rear
    
    def isEmpty(self):  return not self.front.val

    def enqueue(self,val):

        self.rear.val = val
        self.rear.next = Node()
        self.rear = self.rear.next
        return True
    
    def dequeue(self):
        if self.isEmpty(): return None
        p = self.front
        x = self.front.val
        self.front = self.front.next
        del p 
        return x



queue =Dequeue()
print(queue.enqueue(1))
print(queue.enqueue(2))
print(queue.enqueue(3))
print(queue.front.val)
queue.dequeue()
print(queue.front.val)
queue.dequeue()
print(queue.front.val)
queue.dequeue()
