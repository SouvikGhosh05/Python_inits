import timeit
class Static:
    counter = 0
    
    @staticmethod
    def myfunc():    
        Static.counter += 1
        return Static.counter
    
    def __delattr__(self, name):
        del self.name
        

if __name__ == '__main__':
    
    def main1():
        count = Static()                #with instance of class and slower
        count.myfunc()
        count.myfunc()
        #count.__delattr__('counter')
        #delattr(count, 'counter')
        
    t1=timeit.timeit(main1, number=100000)
    print(timeit.default_timer()-t1)
    
    
    def main2():

        count1 = Static.myfunc()            #with class name and faster
        count2 = Static.myfunc()
        
    #t2=timeit.timeit(main2, number=100000)
    #print(timeit.default_timer()-t2)
    #delattr(Static(), 'counter')
    #main1()
    
