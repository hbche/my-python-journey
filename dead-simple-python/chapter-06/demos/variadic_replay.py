def say_hi(name):
    """模拟问候"""
    print(f"Hello, {name.title()}!")
    
def call_something_else(func, *args, **kwargs):
    return func(*args, **kwargs)

call_something_else(say_hi, name='Bob')