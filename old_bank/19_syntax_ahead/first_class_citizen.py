def say_hello(name):
    
    def output():
        print(f'Hello, {name}')
        
    return output

# say_hello('Hugo')
func = say_hello('Hugo')
func()

print(dir(func))
# print(dir(func.__closure__[0]))

print(func.__closure__[0].cell_contents)