def decorator_func(func):
    def new_func(*args, **kwargs):
        print(f"running function : {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return new_func