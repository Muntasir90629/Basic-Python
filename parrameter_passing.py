
# 5 keyword argument

# def add_value(*args):
# 	l=[]
# 	for value in args:
# 		l.append(value)

# 	return l

# result=add_value(10,20,30)

# print(result)

# result=add_value(10,20,30,40,50,60)

# print(result)

def get_detail(**kwargs):
	print(kwargs)




get_detail(name="ABC",email="abc@gmail.com",contact=23222222,dob="12-05-1990")

get_detail(name="ABC",email="abc@gmail.com",contact=23222222,dob="12-05-1990")
