# r=reload()

# r+
# w=write

# w+

# a=append
# a+


# fp=open("input.txt","r")

# content=fp.read()


# print(content)




# fp=open("input.txt","r")

# content=fp.read(25)

# print(content)


# fp=open("input.txt","r")


# content=fp.readlines()

# print(content)

# content=fp.readlines()

# print(content)


# fp=open("input2.txt","w")

# fp.write("sample line ")


# fp=open("input3.txt","w+")

# print(fp.tell())

# fp.write(" sample line 2")

# print(fp.tell())

# fp.seek(0,0)



# content=fp.read()

# print(fp.tell())
# print(content)

# tell=> current  fp possiton

# seek=> change the position 

#ofset => it means number of character 


# fp=open("input3.txt","r+")

# content=fp.read()
# print(content)


# fp.write("\n\n sample line added  using python script")

# content=fp.read()
# print(content)


fp=open("input.txt","a")
print(fp.tell())


fp.write("\n\n\nabc")