def add_number(number):
    return number + 1

number = 1
result = add_number(number)
print("result ", result)


def edit_dict(dict):
    dict["nickname"] = "jimmie"

profile = {"name": "pipusana", "age": 26}

edit_dict(profile)

print("profile ", profile)
