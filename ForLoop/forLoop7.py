#Example 1
string_upper_list = []
string_list = ["jim", "por", "tide", "bb", "lohma"]

for string in string_list:
    string_upper_list.append(string.upper())

print("Example 1 => string_upper_list ", string_upper_list)

#Example 2
string_list = ["jim", "por", "tide", "bb", "lohma"]
string_upper_list = [string.upper() for string in string_list]
print("Example 2 => string_upper_list ", string_upper_list)

#Example 3
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [number for number in number_list if number > 5]
print("result ", result)

#Example 4
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mod_number = []
for number in number_list:
    if number % 2 == 0:
        mod_number.append(0)
    else:
        mod_number.append(1)
print("mod_number ", mod_number)

#Example 5
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mod_number = [0 if number % 2 == 0 else 1 for number in number_list]