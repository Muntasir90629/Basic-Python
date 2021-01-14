

# l=[100,200,300,400,500]
# i=iter(l)
# print(i)

# for value in i
# print(next(value))


# import itertools


# l1=[10,20,30,40,50]

# l2=[100,200,300,400,500]

# l3=[1000,2000,3000,4000,5000]



# i=itertools.chain(l1,l2,l3)

# print(i)


# for value in i:

# 	print(value)
import itertools


l=[10,20,30,40,50]
count=0
for value in itertools.cycle(l):

	if count<20:

		print(value)
	else:
		break
count+=1


