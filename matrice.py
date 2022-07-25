def n_sum(n):
    if n == 0: return 0
    return int(n + n_sum(n-1))
class Matrix:
    def __init__(self,dimension):
        self.dimension = dimension
        self.array = [0 for _ in range(n_sum(dimension))]

    def set(self,i,j,x):
        if(i<=j):
            self.array[i*(i-1)/2 +j-1]=x

    def get(self,i,j):
        if(i<=j):
            return self.array[i*(i-1)/2 +j-1]
        else:
            return 0

    def Display(self):
        i=1
        while i <= self.dimension:
            j= 1
            while j <= self.dimension:
                if i <= j: print(self.array[int(j*(j-1)/2) +i-1], end = " ")
                else: print("0 ", end = "")
                j+=1
            print('')
            i+=1

n = 4
matrix = Matrix(n)
# print(matrix.array)
# print(matrix.Display())
import random

class s_element:
    def __init__(self,i,j,x):
        self.i = i
        self.j = j
        self.x = x

class Sparse:
    lis = []
    def __init__(self,m,n,num):
        self.m =m
        self.n = n
        self.num = num
    def create(self):
        for _ in range(self.num):
            i = random.choice(range(1,self.num))
            j = random.choice(range(1,self.num))
            x = random.choice(range(1,self.num))
            self.lis.append(s_element(i,j,x))

    def Display(self):
        for obj in self.lis:
            print(obj.i,end = " ")
        print('')
        for obj in self.lis:
            print(obj.j,end = " ")
        print('')
        for obj in self.lis:
            print(obj.x,end = " ")
        print('')

    # def add(self, sparse):
    #     if(self.m != sparse.m or self.n != sparse.n): return -1
    #     sum = Sparse(self.m,self.n,self.num + sparse.num)


# sparse = Sparse(4,5,5)
# sparse.create()
# sparse.Display()

class Term:
    def __init__(self,coef,Exp):
        self.coef =coef
        self.Exp = Exp
class Poly:
    def __init__(self,size):
        self.size = size
        self.term_list = []
    def create(self,coef,Exp):
        self.term_list.append(Term(coef,Exp))
    def create_random(self):
        for _ in range(self.size):
            coef = random.choice(range(5))
            Exp = random.choice(range(5))
            self.create(coef,Exp)
    def Display(self):
        


        





