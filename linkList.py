






class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
class linkList:
    def __init__(self):
        self.head = Node()

    def creat(self,arr):
        self.head.data = arr[0]
        last = self.head
        for num in arr[1:]:
            last.next = Node(num)
            last = last.next
        del last
    def sum(self):
        sum = 0
        last = self.head
        while last:
            sum += last.data
            last = last.next
        del last
        return sum
    def find_max(self):
        max = 0
        last = self.head
        while last:
            if max < last.data:
                max = last.data
            last = last.next
        return max
    
    def Search(self,key):
        q = None
        p = self.head
        while p:
            if key == p.data:
                q.next = p.next
                p.next = self.head
                self.head = p
                del q,p
                return True
            q = p
            p = p.next
        del p
        return False
    
    def Reverse(self):
        p = self.head
        q = None
        r = None
        while p:
            r = q
            q = p 
            p = p.next
            q.next =r 
        self.head =q
            
            

    def Display(self):
        last = self.head
        while(last):
            print(f'current value is: {last.data}')
            last = last.next
        del last

linkli = linkList()
arr = [1,2,3,4,5,6,7,8,9]
linkli.creat(arr)
linkli.Reverse()
linkli.Display()



