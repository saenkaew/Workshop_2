# Join Set
# EX1
set1 = {"a", "b", "c"}
set2 = {"d", "e", "f"}
set3 = set1.union(set2)
print(set3) # {'d', 'e', 'c', 'a', 'f', 'b'}

# EX2
set1 = {"a", "b", "c"}
set2 = {"d", "e", "f"}
set1.update(set2)
print(set1) # {'d', 'e', 'c', 'a', 'f', 'b'}

# EX3
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1) # {'apple'}

# EX4
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1) # {'banana', 'cherry', 'microsoft', 'google'}

