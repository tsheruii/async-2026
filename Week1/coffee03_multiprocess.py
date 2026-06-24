from time import sleep, ctime, time
import multiprocessing

# Function to simulate making coffee for one customer
def make_coffee(customer_name):
    print(
        f"{ctime()} [Process ID: {multiprocessing.current_process().pid}] "
        f"Making coffee for customer {customer_name}..."
    )

    sleep(1)  # Simulate coffee-making time (1 second represents 1 minute)

    print(
        f"{ctime()} [Process ID: {multiprocessing.current_process().pid}] "
        f"Customer {customer_name}: Coffee is ready!"
    )


def main():
    # Customer queue
    queue = ["A", "B", "C"]

    print(f"{ctime()} === Starting Multi-processing Coffee Simulation ===")

    start_time = time()

    # List to store all processes
    processes = []

    # 1. Create a separate process for each customer (one customer per CPU core/process)
    for customer in queue:
        p = multiprocessing.Process(
            target=make_coffee,
            args=(customer,)
        )
        processes.append(p)

        # Start the process immediately
        p.start()

    # 2. Wait until all processes have finished
    for p in processes:
        p.join()

    # 3. Display the final result
    duration = time() - start_time

    print(
        f"{ctime()} Success! All processes have completed. "
        f"Total execution time: {duration:.2f} seconds"
    )


# This guard is required when using multiprocessing in Python
if __name__ == "__main__":
    main()