import json

data = '{"var1":"harry", "var2":56}'
print(data)

data2 = json.loads(data)
print(data2['var1'])

