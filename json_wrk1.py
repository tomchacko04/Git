import json
data_dict = {"name":"chacko", "age": 55}
json_str= json.dumps(data_dict)
print(json_str)
print(type(json_str)) # it will be string
back_to_dict = json.loads(json_str)
print(type(back_to_dict))# it will be dict