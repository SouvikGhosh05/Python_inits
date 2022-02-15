class Static(): 
    counter = 0

    def __init__(self):
        self.cls_counter = Static.counter
    
    def __repr__(self):
        return f"Static class {self.__class__.__name__} with counter {Static.counter}"
    
    @staticmethod      
    def myfunc():
        Static.counter += 1
        return Static.counter


if __name__ == "__main__":

    def main1():
        static_instance = Static()  # with instance of class and slower
        print(f"First call from first : {static_instance.myfunc()}")
        print(f"Second call from first : {static_instance.myfunc()}")
        print(f"Third call from first : {static_instance.myfunc()}")
        return static_instance

    def main2():
        static_instance = Static()  
        print(f"First call from second : {Static.myfunc()}")
        print(f"Second call from second : {Static.myfunc()}")
        print(f"Third call from second : {Static.myfunc()}")
        return static_instance

    instance1 = main1()       
    print(instance1.__dict__)       # all attributes of 'self' are the part of self.__dict__
    instance2 = main2()             # this will initialize with previously incremented value of 'cls_counter'
    print(instance1)
    print(instance2)
    
    instance1.extra_purple = "purple"
    print(instance1.__dict__)      # You will see 'cls_counter' is still 0, to set that into dict, we need to use @property
    print(instance2.__dict__)
    del instance1.cls_counter
    print(instance1.__dict__)
