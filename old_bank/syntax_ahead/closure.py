def say_hello(name):
    greeting = f'Hello, {name}'
    
    def output():
        print(greeting)
        
    return output


# say_hello('Hugo')
func = say_hello('Hugo')
func()
