"""
Copyright (c) 2020, Souvik Ghosh.

Distributed under the terms of the MIT License.

The full license is in the file LICENSE, distributed with this software.

Created on Mar 15, 2020

@author
"""
def Solve():
    m = []
    for j in range(1, i):
        if i % j == 0:
            m.append(j)
    yield sum(m)


e = int(input("Enter a range of numbers to check: "))
for _ in range(e):
    i = int(input("Enter a number: "))
    for u in Solve():
        if i == u:
            print("Yes")
        else:
            print("No")
