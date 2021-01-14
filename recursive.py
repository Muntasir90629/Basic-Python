

# def factorial(l):
# 	for value in l:
# 		if value>1 :
# 			  sum=sum*value;
  
#             value=value-1;

       
#         else:
#         	break;
#         	return sum;


# def factorial(num):
# 	if num==1:
# 		return 1
# 	else:
# 	    return num*factorial(num-1)





# num=5

# result=factorial(1)

# print(result)
 
def binary_search(l,key):
	mid=len(l)//2

	if l[mid]==key:
		return True

	elif key<l[mid]:
		return binary_search(l[:mid],key)	
    
    else:
    	return binary_search(l[mid+1: ],key)


l=[100,200,300,400,500,600,700,800,900]

key=700

result=binary_search(key,l)