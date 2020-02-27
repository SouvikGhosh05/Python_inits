"""
Copyright (c) 2020, Souvik Ghosh.

Distributed under the terms of the MIT License.

The full license is in the file LICENSE, distributed with this software.

Created on Feb 28, 2020

@author
"""

# '''The following code basically shows how different functions
#    can call themselves inside a class.'''

class Func:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def opt1_func(self):
        self.add=self.num1 + self.num2  # a new attribute 'add' is added
                                        # for the instance.
        return self.add

    def opt2_func(self,num3):
        self.num3=num3
        print("Subtracting with entered number...")
        return num3 - self.opt1_func()

    def opt3_func(self,x1):
        x2=int(input("Enter the power: "))
        self.num4=self.opt2_func(x1**x2)  # here also a new attribute 'num4' is added.
        return self.num4

    def opt4_func(self,num5):
        return self.opt3_func(self.num3+num5)


func_twist=Func(20,5)

print(func_twist.opt1_func())    # 20+5

print(func_twist.opt2_func(7))   # 7-(20+5)

print(func_twist.num3)           # 7

# here, 'x2' is the manual input value taken by 'opt3_func()'.
print(func_twist.opt3_func(8))   # {8**(x2)}-(20+5)

print(func_twist.num3)           # overwritten and updated which is (8**x2).

print(func_twist.opt4_func(6))  # {((8**x2)+6)**(x2)}-(20+5)

print(func_twist.num3)          # again overwritten and updated which is {((8**x2)+6)**(x2)}.



