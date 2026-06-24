from time import sleep, ctime, time
import threading


def update_cup_number(customer_name):
    print(f"{ctime()} | LCD: Processing for customer {customer_name}...", flush=True)
    sleep(1)
    print(f"{ctime()} | LCD: Done for customer {customer_name}.", flush=True)


def make_coffee(customer_name):
    print(f"{ctime()} | Making coffee for {customer_name}...", flush=True)
    sleep(1)
    print(f"{ctime()} | Coffee ready for {customer_name}!", flush=True)
    update_cup_number(customer_name)


def main():
    customers = ["A", "B", "C"]

    print(f"{ctime()} | === Multi-threading Coffee Machine ===", flush=True)
    start_time = time()

    threads = []

    for customer in customers:
        t = threading.Thread(target=make_coffee, args=(customer,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    duration = time() - start_time
    print(f"{ctime()} | Total time: {duration:.2f} seconds", flush=True)


if __name__ == "__main__":
    main()