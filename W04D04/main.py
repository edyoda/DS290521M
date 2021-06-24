# import mod1 # it imports everything which is present inside mod1 here


# print(mod1.pipi)

# output = mod1.spacex('land us on mars')
# print(output)

# output2 = mod1.google('Make an Amazing Search Engine')
# print(output2)

# Question/Activity: Make a module mod2.py, write functions microsoft,
# netflix inside that.import mod2 here and use it in main.py file

# import mod2

# output3 = mod2.microsoft('Use Servers Inside Deep Sea')

# print(output3)

# print(mod2.netflix('Friends Reunion'))


# from mod2 import *

# print(microsoft('Create an Amazing Windows 11'))


# We can import the modules if they are present in :
# 1) Python sys path

# import sys

# print('We can import modules from these paths => ')

# for i in sys.path:
# 	print(i)

# import math

# print(math.pi)

# print(dir(math))

from mod2 import netflix

netflix('Do something Amazing!!')