from time import sleep, ctime, time
import threading

# Function to simulate making coffee for one customer
def make_coffee(customer_name):
    print(f"{ctime()} Making coffee for customer {customer_name}...")
    sleep(1)  # Simulate coffee-making time (1 second represents 1 minute)
    print(f"{ctime()} Customer {customer_name}: Coffee is ready!")


def main():
    # Customer queue
    queue = ["A", "B", "C"]

    print(f"{ctime()} === Starting Multi-threading Coffee Simulation ===")

    start_time = time()

    # List to store all threads
    threads = []

    # Create a thread for each customer so they can be served simultaneously
    for customer in queue:
        # Create a new thread that runs make_coffee() and passes the customer as an argument
        t = threading.Thread(
            target=make_coffee,
            args=(customer,)
        )

        threads.append(t)

        # Start the thread immediately
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    # Calculate the total execution time
    duration = time() - start_time

    print(
        f"{ctime()} {len(queue)} customers have received their coffee! "
        f"Total execution time: {duration:.2f} seconds"
    )


# Run the program
if __name__ == "__main__":
    main()