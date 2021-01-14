deic:
1 mutable 
2 unorder
3 key should be unique
4 key should be immutable int ,str, float , tupple 
d={"emp_id":101,"name":"ABC", "email":"abc@gmail.com","name":"CBC"}

d["contact_no"]=32444


d["contact_no"]=354354354
print(d)


get
set

print(d.get("emp_id"))
print(d.get("age","key doesnt exist"))

print(d.setdefault("age",50))

print(d)


for x in d :
	print(x, d[x])

d={}

for value in range(1,11):
    d[value]=value*value;

print(d)


print(d.keys())
print(d.values())

print(d.items())

for t in d.items() : 
    print(t)

l1=[1,2,3,4,5,6]
l2=[11,12,13,14,15,16]

d=dict(zip(l1,l2))

print(d)

l1=[1,2,3,4,5]
l2=[5,6,7,8,9]

d=dict(zip(l1,l2))
print(d)


l=[1,2,3,4,5]

d=dict.fromkeys(l,0)

print(d)


d1={1:2,2:4,3:43,4:434,5:45,6:5454}

d2={10:10,11:11,12:12,13:13,14:14,15:15}

d1.update(d2)


print(d1)

pop
popitem
clear
del

r=d1.pop(2)

print(d1,r)


r=d1.popitem()
print(d1,r)

d1.clear()

print(d1)

del d1


print(d1)



