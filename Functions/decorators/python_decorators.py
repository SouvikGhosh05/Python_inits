def dec_1(func):
    def wrapper_1(*args, **kwargs):  # this 'wrapper_1()' function allows the arguments and
        # keyword argument to be pass in 'func()' function.

        print("I'm before decorator.")

        rv_1 = func(*args, **kwargs)  # as 'func()' is inside a decorator function, this function represents
        # several functions which is to be passed inside this decorator.
        print("I'm after decorator.")
        return rv_1  # here 'return' is used to return something from the 'wrapper_1()' function. If we don't
        # mention 'return' of 'wrapper_1(), then the inner-decorated function won't return anything even if any
        # defined function returns anything using this decorator.

    return wrapper_1  # this returns the function object of 'wrapper()' function.


def dec_2(func):
    def wrapper_2(*args, **kwargs):
        print("I'm behind.")
        rv_2 = func(*args, **kwargs)
        print("I'm ahead.")
        return rv_2

    return wrapper_2


@dec_1
def func_1(string, stat=None):  # here 'string' is argument and 'stat' is keyword argument.
    # here 'func_1()' function is defined as 'func()' inside the decorator.
    print("I'm func_1 in dec_1.")
    return [string, stat]


@dec_1
def func_2():  # similar as that of 'func_1()' defined.
    print("I'm func_2.")


@dec_1  # 'this is totally equivalent to 'dec_1(sum_func)' , where 'sum_func' is being treated as a
# function-object of 'sum_func()' function '. 'If we write as 'dec_1(sum_func)', then we're manually passing
# this function to be used by the decorator.'
# But, if we write as '@dec_1' then this function will always be used by the decorator.
def sum_func(*args):
    print(sum(args))
    return [i for i in args]


u_1 = func_1("I'm Souvik.", stat='Python')  # here, this 'func_1()' is being called as 'wrapper_1()' function
                                             # defined in the decorator 'dec_1'.

@dec_2
def func_1(string, stat=None):
    print("I'm func_1 in dec_2.")
    return [string, stat]


def out_dec(*args):  # this function is totally independent on any of these decorators.
    print("I'm called from outside.")
    return f'Returning independently with {args}.'


u_2 = func_1("Hello, What's up!", stat='Bro!')  # here, this 'func_1()' is being called as 'wrapper_2()' function
# defined in the decorator 'dec_1'.
v = func_2()
w = sum_func(5, 10, 20)

print(v)  # it returns 'None' since 'return' isn't specified in 'func_2()' function.
print(w)  # it is similar as that of 'u' defined above.

print(u_1)  # 'u_1' is the returned value of the 'func_1()' function passed in 'dec_1' decorator.
print(u_2)  # 'u_2' is the returned value of the 'func_1()' function passed in 'dec_2' decorator.

o_d = out_dec()  # this  'out_dec()' function is called independently here.
print(o_d)  # here, 'o_d' is the returned value of the 'out_dec()' function independently.
x = dec_1(out_dec)  # here, 'out_dec' is being treated as 'func' inside 'dec_1' decorator.
y = dec_2(out_dec)  # here, 'out_dec' is being treated as 'func' inside 'dec_2' decorator.
print(x)  # here, 'x' is 'wrapper_1' function-object from 'dec_1' decorator.
print(y)  # here, 'y' is 'wrapper_2' function-object from 'dec_2' decorator.
x_ret = x(100, 200, 300)  # here, 'x()' function is 'wrapper_1()' function.
y_ret = y(200, 400, 600)  # here, 'y()' function is 'wrapper_2()' function.
print(x_ret)  # here, 'x_ret' is the returned value of the 'out_dec()' function passed in 'dec_1' decorator.
print(y_ret)  # here, 'y_ret' is the returned value of the 'out_dec()' function passed in 'dec_2' decorator.
