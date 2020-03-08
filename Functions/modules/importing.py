"""
Copyright (c) 2020, Souvik Ghosh.

Distributed under the terms of the MIT License.

The full license is in the file LICENSE, distributed with this software.

Created on Feb 25, 2020

@author
"""

import mod_1 as md1 # we're importing 'mod_1' file named as 'md1'

updated_put = md1.func_list()  # the function itself returns the list
                               # of all input entries.
for i in updated_put:
    print(i, end=' ')

from mod_1 import *          # 'import *' means it imports all the functions
                              #  altogether in this module.
updated_put = func_list()
for i in updated_put:
    print(i, end=' ')
    
