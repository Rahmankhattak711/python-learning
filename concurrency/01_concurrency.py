import threading
import time


def taking_order():
    for i in range(1, 10):
        print(f"Order {i} is being prepared")
        time.sleep(5)


def serve_order():
    for i in range(1, 10):
        print(f"Order {i} is being served")
        time.sleep(5)


def collect_payment():
    for i in range(1, 10):
        print(f"Payment for order {i} is being collected")
        time.sleep(5)


taking_order_thread = threading.Thread(target=taking_order)
serve_order_thread = threading.Thread(target=serve_order)
collect_payment_thread = threading.Thread(target=collect_payment)

taking_order_thread.start()
serve_order_thread.start()
collect_payment_thread.start()

taking_order_thread.join()
serve_order_thread.join()
collect_payment_thread.join()

# print("All orders have been completed")
