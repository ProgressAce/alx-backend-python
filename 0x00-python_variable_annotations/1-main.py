#!/usr/bin/env python3
concat = __import__("1-concat").concat

str1 = "egg"
str2 = "shell"

print(concat(str1, str2) == "{}{}".format(str1, str2))
print(concat.__annotations__)

# add
print(concat(1, 3))  # ValueError - cannot convert 4
print(type(concat(1, 3)))  # int
print(concat(1, 3) == "{}{}".format(1, 3))  # False
