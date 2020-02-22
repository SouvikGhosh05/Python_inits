"""
Copyright (c) 2020, Souvik Ghosh.

Distributed under the terms of the MIT License.

The full license is in the file LICENSE, distributed with this software.

Created on Feb 20, 2020

@author
"""

def func_1(name1,message,name2):   # defined function
    print("printing the message with" ,name1,",",name2,",and",message)
func_1("John",message="hello",name2="David")   #calling function

# 'in the above function we are passing the arguments as their values
# mentioned inside the caller function.'
# 'in the above 'message' and 'name2' are the keys,those are passing their key
# values to the function.'
# in this, we are treating 'message' and 'name2' as the keys.

def func_2(name1,message=None,name2=None): # None specifies its keyword value.
    print("printing the message with" ,name1,",",name2,",and",message)
    print(message)
    print(name2)
func_2("John","hello","David") # here, message="hello" and name2="David".
func_2("V","AGT",name2="Unbeatable") # here, message="AGT" and name2="Unbeatable".
# 'in the above function 'name1' is a argument, and 'message','name2' are
# the keyword arguments, and their key values are mentioned in the caller function.'
# 'here, func_2() is allowed to treat 'message' and 'name2'
# as the keyword arguments.'
# 'keyword arguments are the keys of arguments, keyword arguments are used
# to pass their respective arguments.'

