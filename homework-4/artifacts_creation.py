from benchmarking.fibonacci import run_fibonacci, run_threads, run_processes
import time


def task4_1():
    n = 35
    results = []
    artifacts_path = "artifacts/4_1.txt"

    for _ in range(10):
        start = time.time()
        run_fibonacci(n)
        results.append(time.time() - start)

    with open(artifacts_path, "w") as file:
        file.write(f"Sync: {sum(results) / len(results)}\n")

    results = []
    for _ in range(10):
        start = time.time()
        run_threads(n)
        results.append(time.time() - start)

    with open(artifacts_path, "a") as file:
        file.write(f"Threads: {sum(results) / len(results)}\n")

    results = []
    for _ in range(10):
        start = time.time()
        run_processes(n)
        results.append(time.time() - start)

    with open(artifacts_path, "a") as file:
        file.write(f"Processes: {sum(results) / len(results)}\n")


if __name__ == "__main__":
    task4_1()
