def hello(func):
    def wrapper(*args):
        print("Hello!", func(*args))
    return wrapper

@hello
def greet(*name):
    return "-".join(name)
    
greet("Python", "Discord")