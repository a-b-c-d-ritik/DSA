from array import *;

a1=array('i',[1,2,3,4,5])

def printarr():
    for x in a1:
        print(x)

a1.append(5)
print(type(a1))
print(a1.__sizeof__())
print(a1.count(5))
printarr()
a1.pop()
#a1.append([6,7,8])
printarr()

#a1=a1.extend([6,7,8])
printarr()
print(a1.index(5))
a1.insert(4,6)
printarr()