def decorator_func(func):
    '''decorator for printing executed function name'''
    def new_func(*args, **kwargs):
        print(f"running function : {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return new_func