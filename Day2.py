# file = open('karthi.txt','r') # only read mode
# file = open('karthi.txt','w') # write mode which replaces the existing text
# file = open('karthi.txt','a') # append mode which add with the existing text
# content = file.read()
# print("Content:",content)

# line = file.readline()
# print("Line:", line)

# lines = file.readlines()
# print("Lines:",lines)

# file.close()


import os 
import os.path

# dir = os.mkdir(karthi)
# a = os.listdir('.')
# print(a)

x = os.path.exists('karthi.txt')
print('Is file existed in this folder:', x)