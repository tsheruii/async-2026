from time import sleep, ctime, time
import multiprocessing
import threading
import os

# Function to simulate making coffee for one customer
def make_coffee(customer_name):
    # Get the Process ID and Thread information
    pid = os.getpid()
    thread_id = threading.current_thread().native_id
    thread_name = threading.current_thread().name

    print(
        f"{ctime()} | [PID: {pid}] [TID: {thread_id}] [Thread Name: {thread_name}] "
        f"Making coffee for customer {customer_name}..."
    )

    sleep(5)  # Simulate making coffee for 5 seconds

    print(
        f"{ctime()} | [PID: {pid}] [TID: {thread_id}] [Thread Name: {thread_name}] "
        f"Customer {customer_name} has received the coffee!"
    )


def main():
    queue = ["A", "B", "C"]

    main_pid = os.getpid()
    main_tid = threading.current_thread().native_id

    print(
        f"{ctime()} | [Main PID: {main_pid}] [Main TID: {main_tid}] "
        f"=== Starting Multi-processing Coffee Simulation ==="
    )

    start_time = time()

    processes = []

    # Create a separate process for each customer
    for customer in queue:
        p = multiprocessing.Process(
            target=make_coffee,
            args=(customer,)
        )
        processes.append(p)
        p.start()

    # Wait for all processes to finish
    for p in processes:
        p.join()

    duration = time() - start_time
    print(f"{ctime()} | Total execution time: {duration:.2f} seconds")


if __name__ == "__main__":
    main()