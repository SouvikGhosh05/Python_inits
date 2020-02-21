"""
Copyright (c) 2020, Souvik Ghosh.

Distributed under the terms of the MIT License.

The full license is in the file LICENSE, distributed with this software.

Created on Feb 20, 2020

@author
"""

def define(*args,**kwargs):
    for arg in args:
        print (arg)

    for i in kwargs.values():
        print (i)
    for j in kwargs.keys():
        print (j)
    for e,f in kwargs.items():
        print (e,f,sep=' ')

    print (args)    # 'args' is formed as tuples.
    print (kwargs)       # 'kwargs' is formed as dictionary.

## passing args and kwargs to the function
define('hello','world',my_language='python',my_postion='developer')
define()  # so it is not compulsory to put arguments in function always
          # with 'args' and 'kwargs'.
