# 1 code reuse :

# 2 MODULARITY 


# S="PYTHON,HTML"

# print(S.index("HTML"))

# def value_reverse(value):
# 	reverse=value[::-1]
# 	print(reverse)
# 	return(reverse)


# s="python"

# result=value_reverse(s)

# print("the result",result)

def value_auto(value):
	if type==list or type(value)==str:
		reverse=value[::-1]
	else:
		temp=str(value)
		reverse=temp[::-1]
	return reverse

l=[100,200,300,400,500]

result=value_auto(10)

print(result)
