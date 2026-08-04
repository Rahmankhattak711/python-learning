from functools import wraps


def study(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before calling the function")
        func(*args, **kwargs)
        print("After calling the function")

    return wrapper


@study
def study():
    print("I am studying")


study()
