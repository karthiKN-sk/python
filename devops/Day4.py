# def is_even(num):
#     return num % 2 == 0

# def is_odd(num):
#     return num % 2 != 0

# def square(num):
#     return num ** 2

# num = int(input("Enter the Value: "))

# if is_even(num):
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")

# print(f"The square of {num} is {square(num)}")



###Modules
import sys
import os

# Add the parent folder (one level up) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from python_chapter.modules import math_utils


a = math_utils.add(5 ,8)

print(a)

