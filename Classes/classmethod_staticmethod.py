"""
Copyright (c) 2020, Souvik Ghosh.

Distributed under the terms of the MIT License.

The full license is in the file LICENSE, distributed with this software.

Created on Feb 21, 2020

@author
"""

class User:
    a_pay = 15000   # class variables.
    b_pay = 21000

    def __init__(self, value):
        self.list = []
        self.dict = {}
        self.pay = 500
        self.value = value

    def modifying(self, *args, **kwargs):
        self.list = list(args)  # updating 'self.list'.
        self.list = list(args)

        for i, j in kwargs.items():
            print(i, j, end='\n')
            
        self.dict = kwargs  # updating 'self.dict'.
        return self.list, self.dict

    def __str__(self):  # so 'str(self)' can now be applied.
        return f'The list is: {self.list} and the dictionary is: {self.dict}.'
        # returns the updated 'self.list' and 'self.dict'.
        self.dict = kwargs
        return self.list, self.dict

    def __str__(self):
        return f'The list is: {self.list} and the dictionary is: {self.dict}.'

    @classmethod
    def modvar_class(cls, c_pay):  # it is responsible for operating
        # class variables.
        tol_var = (cls.a_pay + cls.b_pay + c_pay)
        return f"Total value of their pays: {tol_var}."

    @classmethod
    def calling_class(cls, another_value):  # its job is to pass its argument
        # to the class itself.
        return cls(another_value)

    @staticmethod
    def pass_func(*args):  # it does't have any relation to
        # object instance or class instance.
        return sum(args)


u1 = User(500)  # '500' sets as the value of 'self.value', where 'u1'='self'.
print(u1)  # it prints all dunders inside
print(u1.value)
print(u1.modifying(10, 40, my_name='Souvik', language='Python'))
print(u1)  # after modifying it prints dunder...
print(User.modvar_class(16000))
u2 = u1.calling_class(1000)  # '500' is overwritten by '1000' here.
print(u2.value)  # overwritten value of 'self.value'.
=======
print(u2.value)
u3 = User.calling_class(2000)  # it passes its argument and newly sets 'self.value'.
print(u3.value)  # then, it prints the updated 'self.value'.
print(User.pass_func(10, 20, 30))
## can also be written as....
print(u2.pass_func(40, 50, 60))
print(str(u1))  # it works as __str__() defined in the class
print(u1.__str__())  # same condition as above..
## otherwise, 'it raises AttributeError' if '__str__()' was not defined.
print(User.__str__(u1))  # also applicable.
print(u2.modifying(20, 30, name='Guido Van Rossum', role='Python Creator'))
print(u2)
print(str(u2))
print(u2.__str__())
print(User.__str__(u2))
print(u2.pass_func(40,50,60))
