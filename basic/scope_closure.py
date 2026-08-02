# this is scope in py
x = 100

def outer():
    # x =200
    def inner():
        print("Inner x:", x)
    inner()
    print("Outer x:", x)

# outer()

# this is closure

def outer():
    # x = 100
    def inner():
        print("Inner x:", x)
    return inner

inner = outer()
inner()
