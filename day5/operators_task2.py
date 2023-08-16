# Comparison Operators:

x = 50
y = 100

# Equal to
equal = x == y 
print(equal)
# resltu: False

# Not equal to
not_equal = x != y 
print(not_equal) 
# resltu: True

# Greater than
greater_than = x > y 
print(greater_than) 
# resltu: False

# Less than
less_than = x < y  
print(less_than)
# resltu: True

# Greater than or equal to
greater_equal = x >= y 
print(greater_equal) 
# resltu: False

# Less than or equal to
less_equal = x <= y  
print(less_equal)
# resltu: True

# Logical Operators:
p = 6
q = 8

# Logical AND
result_and = p and q  
print(result_and)
# result :6

# Logical OR
result_or = p or q 
print(result_or) 
# result : 8

# Logical NOT
result_not = not p  
print(result_not)
# result : false


# Membership Operators:

dogs = ["german shepard", "japanese spitz", "labrador"]

# Check if "japanese spitz" is in the list
membership = "japanese spitz" in dogs  
print(membership)
# result: True

# Identity Operators:
a = [1, 3, 5]
b = a

# Check if a and b refer to the same object
identity = a is b 
print(identity) 
#result: True


# Bitwise operators:
# Bitwise AND (&):

x = 5  
y = 3  

result_and = x & y  
print(result_and) 
# result:1

# Bitwise OR (|):
result_or = x | y  
print(result_or)
# result:7

# Bitwise XOR (^):
result_xor = x ^ y 
print(result_xor)  
# result: 6

# Bitwise NOT (~):
result_not = ~x
print(result_not)
# result:-6
# new comment

# Bitwise Left Shift (<<):
result_left_shift = x << 2  
print(result_left_shift)
# result: 20

# Bitwise Right Shift (>>):
result_right_shift = x >> 2  
print(result_right_shift)
# result: 5
