import threading
import time
import multiprocessing


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def run_fibonacci(n):
    fibonacci(n)


def run_threads(n):
    threads = []
    for _ in range(10):
        thread = threading.Thread(target=run_fibonacci, args=(n,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def run_processes(n):
    processes = []
    for _ in range(10):
        process = multiprocessing.Process(target=run_fibonacci, args=(n,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
