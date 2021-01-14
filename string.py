s1="python simple string"
print(type(s1))
print(id(s1))
s1="java"
print(id(s1))

s="python sample string"

print(s[0])
print(s[-1])

print(s[100])
print(s[7:])
print(s[:6])

print(dir(str))

print(s[::-2])



for value in s[::2]:
	print(value)


num1=100
num2=200

print("value of num1 is {} value of num2 {}".format(num1,num2))
print("value of num1 is ",num1,"value of num2 ",num2)


a=200
b=300

print("Value of a {1} ,Value of b {0}".format(a,b))

c=200
d=400

print("value of c {val2} ,Value of D {val1}".format(val1=num1,val2=num2))


s="python sample string"
print(id(s))
s=s.capitalize()
print(s)
print(id(s))

print(s.upper())
print(s.lower())
print(s.title())

b ="my name is  muntasir"

print(b)

print(b.upper())
print(b.lower())
print(b.title())

b=b.capitalize()

b=b.upper()
print(b.isupper())


b=b.lower()
print(b.islower())

s="HTML,CSS,python,java,django"
# l=s.split(",")
# print(l)
# print(l)

s1=(" ").join(s)
print(s1)

s1="abcd"
s2="1234"
s3="python is sample string abcd"


table=str.maketrans(s1,s2)

result=s3.translate(table)

print(result)

maketrans
translate



a="good"
b="nbad"

s3="python is good boy"

c=str.maketrans(a,b)


d=s3.translate(c)

print(d)

a="4567"
b="vgoo"

c="python is vgoo"

table=str.maketrans(b,a)

d=c.translate(table)

print(d)

index
find
rfind function
s="HTML,CSS,Python,Python"

print("python" in s)

 print(s.index("python"))

print(s.find("python"))

print(s.rfind("Python"))


s="    this is simple string    "
s1=s.strip(" ")
print(s1)



s="****Revmovestar*****"
s1=s.strip("*")
print(s1)

s="python"

s1=s.center(20,"*")
print(s1)
   



s1=s.ljust(20,"*")
print(s1)

s1=s.rjust(20,"*")
print(s1)

s="html,css,python,html"

s1=s.replace("html","HTML5")

print(s1)




























