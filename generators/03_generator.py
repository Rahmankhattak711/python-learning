def customer_order():
    print("Welcome to the cafe!")
    customer_order = yield
    while True:
        print(f"Your order is: {customer_order}")
        customer_order = yield


order = customer_order()
next(order)
order.send("Latte")
order.send("Cappuccino")
