# json object   dict{"key":"value"}

# number 10 10.5   int float

# array[10,"string"]  list
#                     tuple

# ""                 '' '"" 




import json

open("json_input.json","r")
content =handle.read()
handle.close()


d=json.loads(content)

# print(d['database']['port'])

# d['database']['port']=3330


# print(d)

print(d['files']['log'])
d['files']['log']=("","")

json.dumps(d,indent=4,sort_key=True)

print(j)

handle=open("json_output.json","w")

handle.write(j)
handle.close()