# l=[10,20,30,40,50,60,70]

# def sqr(num1):
# 	return num**2

# result=map(sqr,l)

# print(result)
# l=[10,20,30,40,50,60,70,80]


# def sqr(num1):
# 	return num1**2


# result=map(sqr,l)
# print(result)


# for value in result:

# 	print(value)

# def add(num1,num2):
# 	return num1+num2;

# l1=[100,200,300,400,500]
# l2=[10,20,30,40,50]

# result=list(map(add,l1,l2))

# print(result)

# def mino(num1,num2):

# 	return num1-num2


# l1=[100,200,300,400,500,600,800,900]
# l2=[10,20,30,40,50,60]

# result=list(map(mino,l1,l2))


# print(result)


# def check_num(num1):
# 	if num1%2==0:
# 		return True
# 	else:
# 		return False




# l=[100,110,115,120,125,130,140]


# result=list(filter(check_num,l))

# print(result)


# def check_even(num1):

# 	if num1%2==0:

# 		return True

# 	else :

# 		return False


# l=[1,2,3,4,5,6,7,8,9,10]





# result=list(filter(check_even,l))


# print(result)




# l=[10,20,30,40,50,60,70,80]

# result=list(map(lambda num1:num1**2,l))


# print(result)

# l=[12,13,14,15,16,17,18,19,20]

# result=list(map(lambda num1:num1**2,l))

# print(l)


# l=[11,12,13,14,15,16,17,18,19,20]


# result=list(filter(lambda num:num%2==0 ,l))


# print(result)

# d={1:50,3:40,2:30,9:20,5:10}

# l=sorted(d.items(),key=lambda x:x[1])
# print(l)

# def printV(l):
# 	 for value in l :
# 	 	print (value)


# l=[10,20,30,40,50,60,70]

# printV(l)



# def fibo():

# 	first_num=0

# 	second_num=1

# 	while(True):

# 		next_val=first_num+second_num

# 		yield next_val

# 		first_num,second_num=second_num,next_val














# g=fibo()


# for value in range(10):

# 	print(value)


# for value in range(20):

# 	print(value)
def printb(l):
	for value in l:

		yield  value 


# l=[10,20,30,40,50,60]

# g=printb(l)



# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


l1=[10,20,30,40,50,60]

l2=(value*value for value in l1)


print(l2)

print(next(l2))
print(next(l2))
print(next(l2))
print(next(l2))
print(next(l2))
