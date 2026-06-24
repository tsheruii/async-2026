from time import sleep, ctime, time

# Function to simulate making coffee for one customer
def make_coffee(customer_name):
    print(f"{ctime()} Making coffee for customer {customer_name}...")
    sleep(1)  # Simulate coffee-making time (1 second represents 1 minute)
    print(f"{ctime()} Customer {customer_name}: Coffee is ready!")


def main():
    # Customer queue
    queue = ["A", "B", "C"]

    print(f"{ctime()} === Starting Synchronous Coffee Simulation ===")

    start_time = time()

    # Serve customers one by one (synchronous execution)
    for customer in queue:
        # Process each customer's coffee order
        make_coffee(customer)

    duration = time() - start_time  # Calculate the total execution time

    print(
        f"{ctime()} {len(queue)} customers were served in {duration:.2f} seconds."
    )


# Run the program
if __name__ == "__main__":
    main()