a=[1,2,3,4]
print(a)
b=["Aishant",1,2,print]
print(b)

a=[1,2,3]
a[0]=100 #list can be altered but tuple can't
print(a)

print(len("Aishant")) 

print("Parashar"+"Sharma")
print([1,2,3]+[4,5,6])

print([1]*4)

a=[1,2,3,4,5]
for i in a:
    print(i)

print("a" in "jatin")
print(1 in [1,2,3,4])

#Indexing and list Slicing
a=[1,2,3,4,5]
print(a[-5])
print(a[-4])
print(a[-3])
print(a[-2])
print(a[-1])

a=[1,2,3]
a.insert(1,100) #used to insert
print(a)

#append
a=[1,2,3,4]
a.append(5) #used to upadte
print(a)

a=[1,2,3,4]
a.pop()
print(a)
a.pop(1)
print(a)

#remove
a=[1,2,1,4]
a.remove(1) #It remove  the given no. form the list
print(a)
a.remove(1)
print(a)

#it delets the given number
a=[1,2,1,4]



#Sorting and reversing
a=[1,5,3,7,9,5]
a.sort()
print(a)

b=[1,5,3,7,9,5]
print(sorted(b)) #It returns the sorted array but keep your actual array intact
print(b)

c=[3,6,2,8,6,1,9,0]
c.reverse()

d=[3,6,2,8,6,1,9,0]
print(reversed(d)) 
print(d) 
for i in reversed(d): 
    print(i)
#map
b=[1,2,3,4,5]
for i in map(lambda x: x**2,b):
    print(i)

def sqr(x):
    return x**2
for i in map(sqr,b):
    print(i)

a=input().split()
print(a)
a=map(int,input().split())
print(a) #<map object at 0x0000013B1E0EFFD0>

#join
print(",".join(["Aishant","raj","chandler"]))