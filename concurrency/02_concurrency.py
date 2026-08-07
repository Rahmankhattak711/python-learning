from multiprocessing import Process
import time


def taking_order():
    for i in range(1, 10):
        print(f"Order {i} is being prepared")
        time.sleep(1)


def serve_order():
    for i in range(1, 10):
        print(f"Order {i} is being served")
        time.sleep(1)


def collect_payment():
    for i in range(1, 10):
        print(f"Payment for order {i} is being collected")
        time.sleep(1)


if __name__ == "__main__":
    start = time.time()

    taking_order_process = Process(target=taking_order)
    serve_order_process = Process(target=serve_order)
    collect_payment_process = Process(target=collect_payment)

    taking_order_process.start()
    serve_order_process.start()
    collect_payment_process.start()

    taking_order_process.join()
    serve_order_process.join()
    collect_payment_process.join()

    end = time.time()

    print(f"Time taken: {end - start:.2f} seconds")
