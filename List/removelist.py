# Remove List Items
# Example 1
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) # ['apple', 'cherry']

# Example 2
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) # ['apple', 'cherry']

# Example 3
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist) # ['apple', 'banana']

# Example 4
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) # ['banana', 'cherry']

# Example 5
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) # []