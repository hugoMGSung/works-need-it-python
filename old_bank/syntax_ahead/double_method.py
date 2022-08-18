def say_hello(name):
    greeting = 'Hello'
    
    def say_name(name):
        nonlocal greeting
        greeting = name
        
    say_name(name)
    print(f'{greeting}, {name}')
    
say_hello('Hugo')