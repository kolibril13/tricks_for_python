def repeat(num_times=1):
    def decorator_repeat(func):
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat
@repeat(num_times=2)
def greet(name):
    print(f"Hello {name}")

greet("emma")