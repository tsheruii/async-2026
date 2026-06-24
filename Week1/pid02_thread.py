from time import sleep, ctime, time
import threading
import os

# Function to simulate making coffee for one customer
def make_coffee(customer_name):
    # Get the Process ID and Thread information
    pid = os.getpid()
    thread_id = threading.current_thread().native_id
    thread_name = threading.current_thread().name

    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] [Thread Name: {thread_name}] Making coffee for customer {customer_name}...")
    sleep(5)  # Simulate making coffee for 5 seconds
    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] [Thread Name: {thread_name}] Customer {customer_name} has received the coffee!")


def main():
    queue = ['A', 'B', 'C']

    main_pid = os.getpid()
    main_tid = threading.current_thread().native_id

    print(f"{ctime()} | [Main PID: {main_pid}] [Main TID: {main_tid}] === Starting Multi-Thread Coffee Simulation ===")

    start_time = time()

    threads = []

    # Create and start threads
    for customer in queue:
        t = threading.Thread(
            target=make_coffee,
            args=(customer,),
            name=f"Thread-{customer}"
        )
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    duration = time() - start_time
    print(f"{ctime()} | Total execution time: {duration:.2f} seconds")


if __name__ == "__main__":
    main()