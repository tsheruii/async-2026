from time import ctime, time
import asyncio
import os
import threading

# Function to simulate making coffee asynchronously
async def make_coffee(customer_name):
    # Get the Process ID and Thread ID (they remain the same)
    pid = os.getpid()
    thread_id = threading.current_thread().native_id

    # Get information about the current asyncio task
    current_task = asyncio.current_task()
    task_name = current_task.get_name()

    # Get a unique ID for the task
    task_id = id(current_task)

    print(
        f"{ctime()} | [PID: {pid}] [TID: {thread_id}] "
        f"[Async Task ID: {task_id}] [Task Name: {task_name}] "
        f"Making coffee for customer {customer_name}..."
    )

    # Non-blocking wait
    await asyncio.sleep(5)

    print(
        f"{ctime()} | [PID: {pid}] [TID: {thread_id}] "
        f"[Async Task ID: {task_id}] [Task Name: {task_name}] "
        f"Customer {customer_name} has received the coffee!"
    )


async def main():
    queue = ["A", "B", "C"]

    main_pid = os.getpid()
    main_tid = threading.current_thread().native_id

    print(
        f"{ctime()} | [Main PID: {main_pid}] [Main TID: {main_tid}] "
        f"=== Starting Asyncio Coffee Simulation ==="
    )

    start_time = time()

    tasks = []

    for customer in queue:
        # Create a coroutine
        coro = make_coffee(customer)

        # Convert the coroutine into an asyncio Task
        task = asyncio.create_task(
            coro,
            name=f"Task-{customer}"
        )

        tasks.append(task)

    # Wait for all tasks to complete
    await asyncio.gather(*tasks)

    duration = time() - start_time
    print(f"{ctime()} | Total execution time: {duration:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())