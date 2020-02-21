"""
Copyright (c) 2020, Souvik Ghosh.

Distributed under the terms of the MIT License.

The full license is in the file LICENSE, distributed with this software.

Created on Feb 20, 2020

@author
"""

string = "11-13,12-14,13-15"

Dict = dict((x, y) for x, y in (element.split('-') for element in string.split(',')))
# elements are '11-13','12-14','13-15'

print(Dict)
for element in string.split(','):
    for x,y in element.split('-'):
        print(x,y,end=' ')
        print(x,y,end=' ')
        