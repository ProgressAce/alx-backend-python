#!/usr/bin/env python3
add = __import__("0-add").add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)
# additional
print(add(0, 0) == 0.0 + 0.0)
print(add("ab", "1"))  # ValueError can't convert str to float 'ab1'
print(type(add("ab", "1")))  # str
