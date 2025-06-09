def log_function_call (func):
    def wrapper():
        print("function have been called")
        return func()
    return wrapper
 
@log_function_call 
def say_hello():
    print("hello to ather")

say_hello()