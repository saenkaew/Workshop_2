import json

python_dict = {"name": "Nan", "age": 21, "city": "Chonburi"}

json_string = json.dumps(python_dict)

print(json_string)