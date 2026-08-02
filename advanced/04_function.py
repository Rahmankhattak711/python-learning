def func_arguments(*a, **b):
    print("Positional arguments:", a)
    print("Keyword arguments:", b)


func_arguments(1, 2, 3, a=4, b=5)


# recursive function
def factorial(n):
    print("Calculating factorial of", n)
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
