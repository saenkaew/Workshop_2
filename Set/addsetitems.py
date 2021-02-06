# Add Set Items
# EX1
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset) # {'apple', 'cherry', 'orange', 'banana'}

# EX2
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
# Output
# {'banana', 'cherry', 'apple', 'orange'}
# {'mango', 'pineapple', 'banana', 'papaya', 'cherry', 'apple'}