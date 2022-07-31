class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the tree
    def PreOrder(self):

        if self.data:
            print(self.data)
            if self.left:
                self.left.PreOrder()
            if self.right:
                self.right.PreOrder()

    def Ipreorder(self):
        stack = []
        stack.append(self.data)
        p = self
        while stack:
            while p.left:
                stack.append(p.left)
                p = p.left
            
        

# Use the insert method to add nodes
root = Node(10)
for i in range(1,10):
    root.insert(i)
root.PreOrder()