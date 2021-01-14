# 1 postional argument
# 2 default argument
# 3 keyword


# def linear_search(l,key):
# 	for value in l:
# 		if key==value:
# 			return True
# 	else:
# 		return False




# l=[100,200,300,400,500,600]

# key=400

# result=linear_search(l,key)

# print(result)


# 8 char

# 1 upper

# 1 lower

# 1 special

# 5  digits

# print(ord('a'),ord('z'))
# print(ord('A'),ord('z'))
# print(chr(97))

# -----------------------------



# import random


# def gen_password(len=5):
# 	l=['@','#','$','&']
# 	upper=chr(random.randint(65,90))
# 	lowe=chr(random.randint(97,122))
# 	special=random.choice(l)
# 	digits=random.randint(10000,99999)
# 	password=upper+lowe+special+str(digits)
# 	l=random.sample(password,len)
# 	password=("").join(l)
# 	return password





# result=gen_password()

# print(result)
# ----------------------------------------

# def validate(username,password):
# 	if username=="ABC" and password=="Abc@12":
# 		print("validate pass")
# 	else:
# 		print("invalid")


# validate(password="ABCd",username="Abc@12")
# validate(password="Abc@12",username="ABC")


def add_value(*args):
	l=[]
	
	for value in args:
		l.append(value)
    
    return l





result=add_value(100,200,300,400,500)
print(result)