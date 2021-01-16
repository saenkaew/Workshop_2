# ModifyString
strings = " Hello, World! "
print(strings.upper()) # " HELLO, WORLD! "
print(strings.lower()) # " hello, world! "
print(strings.strip()) # "Hello, World!"
print(strings.replace(" ", "")) #  "Hello,World!"
print(strings.replace("H", "J")) #  Jello, World!
print(strings.split(",")) # [' Hello', ' World! ']
print(len(strings)) # 15