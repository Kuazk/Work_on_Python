



class stack():
    def __init__(self,size):
        self.top = -1
        self.size = size 
        self.arr = [0]*size  
    
    def isFull(self): return self.top +1 == self.size 
    def isEmpty(self): return self.top == -1

    def append(self,val):
        if self.isFull(): return False

        self.top +=1  
        self.arr[self.top] = val
        return True
    def POP(self):
        if self.top == -1: return None 
        val = self.arr[self.top]
        self.top -= 1 
        return val  

st = stack(10)
for i in range(10):
    st.append(i)
st2 = stack(10)
while not st.isEmpty():
    st2.append(st.POP())
print(st2.arr)
    