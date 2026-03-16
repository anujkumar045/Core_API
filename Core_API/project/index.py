import json
p_data=True
j_data=json.dumps(p_data)
print(j_data)
print(type(j_data))
p_data='python'
print(json.dumps(p_data))
j_data="python"
print(type(j_data))
j_data='[10,20,"python"]'
print(type(j_data))
j_data='{"x":true,"y"=false,"z":null}'
print(type(j_data))
p_data=json.loads(j_data)
print(p_data)
print(type(p_data))

