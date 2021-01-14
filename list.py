
# list 
 # 1 are mutable - update , delete and update
 # 2 indexing and slicing
 # 3 heteragenous datatype 

# l=[10,20,30,40,50,"python", "java",[100,200,300]]


# print(l,type(l))

 # 2 indexing and slicing

# print(l[-1][1])

# print(l[-1][2])

# print(l[1:3])


# reverse of list

# print(l[::-1])

# l=[100,200,300,400,500]

# for value in l[::4]:
# 	print(value)

# append
# num1=100
# print(id(num1))
# print(id(l))
# l.append(660)

# print(id(l))
# print(id(l[0]))

#extend 

# l.extend([600,700,800,900])

# print(l)

# l.extend("python")

# print(l)
# l.insert(1,1000)
# print(l)
# l=[10,20,30]
# l2=l.copy()

# l.append(40)
# print(id(l),id(l2))
# print(l,l2)

# l=[10,20,20 ,20 ,30,40,50,300]
# l[2]=300
# print(l)

# pop
# remove
# clear
# delete

# r=l.pop(1)
# print(l,r)

# r=l[2].pop()
# print(l)
# print(l)
# l.remove(300)
# print(l)
# l.remove(30)
# print(l)
# l.remove(20)
# print(l)

# l.remove(200)
# print(l)
# l.remove(20)
# print(l)

# l.clear()
# print(l)

# del l
# print(l)

# l=[50,40,30,30,30,10,20]
# l2=[500,400]
# print(l+l2)
# l.sort()
# print(l)

# print(l[::-1])
# l.reverse()

# print(l)

# l3=sorted(l)
# print(l3)

# print(l.index(30))
# print(l.count(30))
l=[0.1]
print(l*10)