
1+2 
"Aishant"*2
lambda a,b:a+b 

print("Hello Aishant and pranav")
show=print
show("something")

names=["Aishant","Pranav",1,1.5]
for name in names:
    print(name)
for name in enumerate(names):
    print(name)
for name in enumerate(names):
    print(name[0],name[1])

a=1
b=2
temp=a
a=b
b=temp
print(a)
print(b)
a=1
b=2
a=a+b
b=a-b
a=a-b
print(a)
print(b)
a=1
b=2
a=a^b
b=a^b
a=a^b
print(a)
print(b)
a=1
b=2
a,b=b,a
print(a)
print(b)

#unpacking
a=[1,2,3]
b,c,d=a
print(b,c,d)

a=1,2 
print(a)
print(type(a))

#line23
#now using unpacking
for i,name in enumerate(names):
    print(i,"-",name)


#zip
names=["jatin","prateek","mukesh","rajesh"]
scores=[50,80,65,43]
for i,name in enumerate(names):
    score=scores[i]
    print(name,"-",score)
for name,score in zip(names,scores):
    print(name,"-",score)

