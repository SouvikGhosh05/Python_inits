class Dunders:
    def __init__(self,*args):
        self.amount=1000
        self.list=list(args)

    def __repr__(self):
        print ("This will print the  class with arguments.")
        return f'Dunders({self.list})'

    def __str__(self):
        print("This will return a line format with format specifier.")
        self.line= f'Amount= {self.amount} and list= {self.list}.'
        return self.line

    def __call__(self,*args,new_amount):
        self.amount=new_amount
        self.list= list(args)
        print("Old values are updated.")

    def __setitem__(self, index, value):
        self.list[index]=value

    def __getitem__(self, index):
        return self.list[index]

    def __delitem__(self, index):
        del self.list[index]

    def __add__(self, other):
        return self.amount + other.amount

    def __sub__(self, other):
        return self.amount - other.amount

    def __mul__(self, other):
        return self.amount * other.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __ne__(self, other):
        return self.amount != other.amount

    def __lt__(self, other):
        return self.amount < other.amount

    def __gt__(self, other):
        return self.amount > other.amount

    def __len__(self):
        return len(self.list)

    def __reversed__(self):
       return self.list[::-1]

dun_obj1=Dunders(20,40,70)        ## it takes arguments as '*args'.
dun_obj2=Dunders(50,100,150)

print(dun_obj1.list)              ## prints a value of an attribute 'self.list'.
print(dun_obj2.list)

print(repr(dun_obj1))             ## calls __repr__() function.
print(repr(dun_obj2))

print(dun_obj1.__repr__())        ## same as above...
print(dun_obj2.__repr__())

print(str(dun_obj1))              ## calls __str__() function.
print(str(dun_obj2))

print(dun_obj1.__str__())         ## same as above...
print(dun_obj2.__str__())

dun_obj1(200,300,400,new_amount=1500)    ## updates these values by calling __call__() function.
dun_obj2(100,500,1000,new_amount=2000)

print(dun_obj1.list)              ## prints the updated list after calling __call__() function.
print(dun_obj2.list)

print(dun_obj1.amount)            ## prints the updated amount after calling __call__() function.
print(dun_obj2.amount)

dun_obj1[0]=50                    ## calls __setitem__() function and sets the given new value in the list.
dun_obj2[1]=100

print(dun_obj1.list)              ## prints the updated list after calling __setitem__() function.
print(dun_obj2.list)

print(dun_obj1[0])                ## prints a value for a specific index by __getitem__() function.
print(dun_obj2[2])


print(len(dun_obj1))              ## prints the length of 'self.list' by calling __len__() functon.
print(len(dun_obj2))              ## same as above...


del dun_obj1[1]                   ## deletes a value for a specific index by __delitem__() function.
del dun_obj2[2]

print(len(dun_obj1))              ## prints the length of 'self.list' after deleting value.
print(len(dun_obj2))

print(dun_obj1.list)              ## prints the updated list after calling __delitem__() function.
print(dun_obj2.list)

print(dun_obj1 + dun_obj2)        ## calls __add__() function.
print(dun_obj1 - dun_obj2)        ## calls __sub__() function.
print(dun_obj1 * dun_obj2)        ## calls __mul__() function.

print(dun_obj1 < dun_obj2)        ## calls __lt__() function.
print(dun_obj1 > dun_obj2)        ## calls __gt__() function.
print(dun_obj1 == dun_obj2)       ## calls __eq__() function.
print(dun_obj1 != dun_obj2)       ## calls __ne__() function.

print(reversed(dun_obj1))         ## prints the reversed 'self.list' by calling __reversed__() function.
print(reversed(dun_obj2))         ## same as above...
