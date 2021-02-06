# Remove Set Items
# EX1
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset) # {'cherry', 'apple'}

# EX2
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset) # {'apple', 'cherry'}

# EX3
thisset = {"apple", "banana", "cherry"}
thisset.pop()
print(thisset) # {'banana', 'cherry'}

# EX4
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset) # set()