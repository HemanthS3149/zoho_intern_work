import multiprocessing
import time
import random

# Shared resource
shared_counter = multiprocessing.Value('i', 0)
lock = multiprocessing.Lock()

def increment_counter():
    global shared_counter, lock
    while True:
        with lock:
            current_value = shared_counter.value
            shared_counter.value += 1
            print(f"Process {multiprocessing.current_process().name} incremented the counter from {current_value} to {shared_counter.value}")
        time.sleep(random.uniform(0.1, 0.5))  # Simulate some work

def process_task():
    for _ in range(10):  # Increase the number of increments per process
        increment_counter()

if __name__ == "__main__":
    processes = []
    for i in range(5):  # Create more processes (you can increase this number)
        process = multiprocessing.Process(target=process_task, name=f"Process-{i+1}")
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f"Final value of the shared counter: {shared_counter.value}")
