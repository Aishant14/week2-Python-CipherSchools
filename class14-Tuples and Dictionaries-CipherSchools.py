#Tuples
#these are not changable i.e they can't be altered or upadted
a=[1,2,3]
a[0]=100
a[2]=200
print(a)

a=(1,2,3,4)
print(type(a))
def func(*args):
    print(type(args))
func(1,2,3,4)

a=5
b=9
a,b=b,a
c=a,b
print(type(c))
def sum_diff(a,b):
    s=a+b
    d=a-b
    return s,d
c=sum_diff(10,5)
print(type(c))

s,d=sum_diff(10,5)
print(s,d) #unpack iterables

a=1,2,3,4
print(type(a))

print(list(a))
print(tuple(a))

print(list(range(0,5)))

a=dict()
a={
    "name":"Aishant Parashar",
    1:"a specific thing",
    (1,2):"tuple keys whatt??????"
    }
print(a["name"])


a={
    "name":"Aishant",
    "company":"IBM",
    "college":"lpu"
}
key="marks"
if key in a:
    print(a[key])
else:
    print("Key doesn't exists")
a={
    "name":"jatin",
    "company":"shuttl",
    "college":"LPU"
}
print(a.get(key))
print(a.get(key,"Key does not exists and couldnt be found"))

#keys()
print(a.keys())

#values()
print(a.values())

#items()
for i in a.items():
    print(i)       
"""
It return pairs in tuple
('name', 'Aishant')
('company', 'IBM')
('college', 'lpu')
"""
for key,value in a.items(): #Unpacking
    print(key,"--->",value) 
"""
name ---> Aishant
company ---> IBM
college ---> lpu
"""
for i in a:
    print(i)
print(list(a))

a.clear()
print(a)

#NOTE: Keys of dictionary can be any immutable object, since keys can't be changed 



#given task

# {
#     {
#         'roll-no':1211,
#         'name':Ravi,
#         'branch':eee,
#     },
#     {
#         'roll-no':202,
#         'name':rajesh,
#         'branch':chem,
#     },
#     {
#         'roll-no':1202,
#         'name':Sam,
#         'branch':mech,
#     }
# }

n=int(input("Enter n: ")) 
dic={} 
for i in range(n):
    d={}
    record_no=int(input("Enter record no: ")) 
    roll_no=int(input("Enter roll no: ")) 
    name=input("Enter name: ") 
    branch=input("Enter branch: ") 
    d["roll-no"]=roll_no
    d["name"]=name
    d["branch"]=branch
    dic[record_no]=d
