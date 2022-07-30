

def isBalance(arr): 
    dict = {
        '}' : '{',
        ')' : '(',
        ']' : '[',   
        }
    stack = []
    for i in arr:
        if i in '{[(': 
            stack.append(i)
        elif i in '})]':
            if not stack:
                return False
            val = stack.pop()
            if val != dict[i]:
                return False
    
    return True if not stack else False

        




str = list('{((+b)*(c+d))}]')

print(isBalance(str))