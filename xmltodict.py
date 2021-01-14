import xmltodict


open("xml_input.xml","r")


content=handle.read()

# print(content)

xmltodict.parse(content)

print(d)


print(d['result']['Message'])

print(d['result']['RequestCode'])

d['result']['RequestCode']=4

print(d)

x=xmltodict.unparse(d)

print(x)