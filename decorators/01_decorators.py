from functools import wraps


def study_decorators(func):
    @wraps(func)
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")

    return wrapper


@study_decorators
def study():
    print("I am studying")


study()

print("The name of the function is",study.__name__)
