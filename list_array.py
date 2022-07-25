def findVowels(arr):
    vowels = 'aeiouAEIOU'
    vcount =0
    
    for char in arr:
        if char in vowels:
            print(f'vowels: {char} \n')
            vcount += 1
    return vcount

def reverse(arr):
    i,j = 0, len(arr)-1
    count = (len(arr)/2)
    arr = list(arr)
    while count > 0:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] =temp
        i+=1
        j-=1
        count -=1 
    return "".join(arr)
def checkPalid(arr):
    return arr[::-1] in arr
def checkDub(string):
    hash = {}
    for char in string:
        if hash.get(char,-1) >= 0:
            hash[char] += 1
        else:
            hash[char] = 1
    return {key:value for key,value in hash.items() if value >=2}

def checkAna(string1,string2):
    hash = {}
    for char in string1:
        hash[char] = 1
    for char in string2:
        if not hash.get(char):
            return False
    return True

def toString(lis): return "".join(lis)
def stringPem(lis,l,h):
    i = l 
    if l == h: print(toString(lis))
    else:
        while i <= h:
            lis[l],lis[i] = lis[i],lis[l]
            stringPem(lis,l+1,h)
            lis[l],lis[i] = lis[i],lis[l]
            i+=1
string = list('ABC')
l = 0
h = len(string) -1
print(stringPem(string,l,h))





