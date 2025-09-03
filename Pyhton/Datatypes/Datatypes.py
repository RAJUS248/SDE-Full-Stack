import sys

# Integer data type
int_variable = 5
age = 10
print("Integer:", int_variable)
print("Memory size of integer:", sys.getsizeof(int_variable), "bytes")

# Float data type
float_variable = 5.0
print("\nFloat:", float_variable)
print("Memory size of float:", sys.getsizeof(float_variable), "bytes")


# String data type
string_variable = "Hello how are you this is our first class we are learning sizeof"
print("\nString:", string_variable)
print("Memory size of string:", sys.getsizeof(string_variable), "bytes")



# List data type
list_variable = [1, 2, 3, 4, 5]
print("\nList:", list_variable)
print("Memory size of list:", sys.getsizeof(list_variable), "bytes")

# Tuple data type
tuple_variable = (1, 2, 3, 4, 5)
print("\nTuple:", tuple_variable)
print("Memory size of tuple:", sys.getsizeof(tuple_variable), "bytes")

# Dictionary data type
dict_variable = {'a': 1, 'b': 2, 'a':3 }
print("\nDictionary:", dict_variable)
print("Memory size of dictionary:", sys.getsizeof(dict_variable), "bytes")

# Set data type

set_variable = {}
print("\nSet:", set_variable)
print("Memory size of set:", sys.getsizeof(set_variable), "bytes")

# Set data type char
set_variable_char = {}
print("\nSet:", set_variable_char)
print("Memory size of set:", sys.getsizeof(set_variable_char), "bytes")

# Boolean data type
bool_variable = True
print("\nBoolean:", bool_variable)
print("Memory size of boolean:", sys.getsizeof(bool_variable), "bytes")
