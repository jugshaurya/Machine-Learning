import math
def countPrime(num):
    list1 = [x for x in range(num+1)]
    list2 = [True for x in range(num+1)]
    d = dict(zip(list1, list2))
    
    d[0] = False
    d[1] = False
    d[2] = True
    for x in range(4,num+1,2):
        d[x] = False
    
    for x in range(3,int(math.sqrt(num))+1,2):
        if d[x]:
            for y in range(x**2,num + 1,x):
                d[y] = False
        
    count = 0
    for x in d.values():
        if x:
            count += 1
            
    return count

print(countPrime(100))