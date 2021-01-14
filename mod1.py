
print(1+1)


def binary_search(l,key):
	mid=len(l) // 2

	if l[mid]==key:
		return true

    elif key < l[mid]:
    	return binary_search(l[:mid],key)
    	
    else:

    	return binary_search(l[mid+1:],key)







l=[100,200,300,400,500,600,700,800,900]

key=700

result=binary_search(l,key)