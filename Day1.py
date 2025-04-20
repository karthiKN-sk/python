print("Hello, World !!")
# Data Types

# Numeric Data Type
  # x = 123  (Interger)
  # y =1.234 (Float)

# String Data Type
#   a = "Karthi"
#   b = 'Keyan'

# Boolean Data Type

#   is_valid = True
#   has_permission = False

# List
#   a = [1,2,3,'Karthi',True] -> mutable

# Tuple
#   b = (1, 2, 3,'Karthi',True) -> immutable

# Dictonaries key-value pair
#    my_dict = {'name': 'Karthi', 'age':30, 'city':'Chennai'}
#    print(my_dict['age'])  -> 30

# Set (It remove duplicate items)
#   my_set = {1,2,2,3,3,3,4,4,5}
#   print(my_set) --->{1,2,3.4,5}



# Basic Program

x = 6
y = 9

addition = x + y
sub = y - x
multiply = x * y
division = y / x

print(addition, sub, multiply, division)

# List 
my_list = [1,2,3,4,5,'Karthi']

print(my_list[5])
my_list[5] = 'Devops'
print(my_list)


# Integer
integer_var = 42
print("Integer Variable:", integer_var)

# Float
float_var = 3.14
print("Float Variable: ", float_var)

# String
string_var = "Hello, World!"
print("String Variable:" , string_var)

# List
list_var = [1,2,3,4,5]
print("List Variable:" , list_var)

# Tuple
tuple_var = (10,20,30,40,50,60,)
print("Tuple varbile:" , tuple_var)

# Dictionary 
dict_var = {
'a':1,
'b':2,
'c':3,
'd':4
}
print("Dictionary Varibale:", dict_var)

# Set
set_var = {1,2,3,4,5}
print("Set Varible:", set_var)

# Basic Task

# Integer and Float Operation
result = integer_var + float_var
print("Integer + Float:", result)

# String Concatenation
new_string = string_var + "Have a nice day!"
print("Concatenated String:" , new_string)

# List Manipulation
list_var.append(6)
list_var.remove(2)
print("Modified List")

# Dictionary operations
dict_var["d"] = 4
del dict_var["a"]
print("Modified Dictionary:" ,dict_var)

# Set operations
set_var.add(6)
set_var.remove(3)
print("Modified Set:" ,set_var)
