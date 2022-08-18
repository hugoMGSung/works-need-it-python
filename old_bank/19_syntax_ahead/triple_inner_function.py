a = 6

def outer_func():
    a = 7
    
    def mid_func():
        a = 8
        
        def inner_func():
            global a
            a = a * 3   # "a" is not defined        
            print(a)
            
        inner_func()
    mid_func()
outer_func()