




num1=400

num2=200

if num1>num2 :
	print("num1 is greater")
	print("another statement")
elif  num2>num1 :
    print("num2 is greater than num1")

else :
	print("both are equal")


if 1:
	print(" 1")
else :
   print(" no")	



loop in python

iterable datatype

str list tupple dict set

for [variable_name] in [iterable datatype]
   statements


l=[10,20,30,40,50]

sum=0
for value in l:
	sum=sum+value;



print(sum)

sum=0
for value in range(1,101,20):
	sum=sum+value;
	#print(sum)

print(" the value is ", sum)	

l=[10,20,30,40,50]

key=350

for index,value in enumerate(l):
	print(index,value)
	if value==key:
		print(" Element found",value)
		print("index",index)
		break 
	else :
		pass
		print("join our journey")
else :
	
	print("Element not found")


print("statements after for loop")


count=1
sum=0

while count<=20:
	sum=sum+count
	count=count+1

print(sum)
