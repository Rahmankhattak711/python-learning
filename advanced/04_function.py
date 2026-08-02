def func_arguments(*a, **b):
    print("Positional arguments:", a)
    print("Keyword arguments:", b)


func_arguments(1, 2, 3, a=4, b=5)


