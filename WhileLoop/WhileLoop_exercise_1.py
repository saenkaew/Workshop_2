num = 2
multi = 1
while num <= 12:
    print("    [", num,"]")
    while multi <= 12:
        print(num, " * ", multi, " : ", num * multi)
        multi = multi + 1
    print("-------------------")
    multi = 1
    num = num + 1