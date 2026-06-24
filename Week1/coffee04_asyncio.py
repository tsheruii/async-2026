from time import ctime, time
import asyncio

# Function to simulate making coffee for one customer asynchronously
async def make_coffee(customer_name):
    print(f"{ctime()} Making coffee for customer {customer_name}...")

    # Simulate coffee-making time (1 second represents 1 minute)
    await asyncio.sleep(1)

    print(f"{ctime()} Customer {customer_name}: Coffee is ready!")


async def main():
    # Customer queue
    queue = ["A", "B", "C"]

    print(f"{ctime()} === Starting Asyncio Coffee Simulation ===")

    start_time = time()

    # Store all async tasks
    tasks = []

    # Create an async task for each customer
    for customer in queue:
        task = asyncio.create_task(make_coffee(customer))
        tasks.append(task)

    # Wait until all tasks finish
    await asyncio.gather(*tasks)

    # Calculate the total execution time
    duration = time() - start_time

    print(
        f"{ctime()} {len(queue)} customers have received their coffee! "
        f"Total execution time: {duration:.2f} seconds"
    )


# Run the async program
if __name__ == "__main__":
    asyncio.run(main())