"""
Переписать функцию integrate для того, чтобы ее выполнение можно было распараллелить. Использовать concurrent.futures: ThreadPoolExecutor и ProcessPoolExecutor.  Добавить логирование (когда какая задача запускается), сравнить время выполнения для integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs) при разном числе n_jobs (от 1 до cpu_num*2) при использовании ThreadPoolExecutor и ProcessPoolExecutor.

Артефакт - файл логов, файл сравнения времени исполнения в обоих случаях в зависимости от числа воркеров

import math
def integrate(f, a, b, *, n_jobs=1, n_iter=10000000):
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc


"""

import math
import concurrent.futures
# import process_pool_executor
# import thread_pool_executor
import time
import logging
import os
import sys


def integrate_thread_pool(f, a, b, *, n_jobs=1, n_iter=10000000):
    acc = 0
    step = (b - a) / n_iter
    with concurrent.futures.ThreadPoolExecutor(max_workers=n_jobs) as executor:
        futures = {executor.submit(f, a + i * step): i for i in range(n_iter)}
        for future in concurrent.futures.as_completed(futures):
            acc += future.result() * step
    return acc


def integrate_process_pool(f, a, b, *, n_jobs=1, n_iter=10000000):
    acc = 0
    step = (b - a) / n_iter
    with concurrent.futures.ProcessPoolExecutor(max_workers=n_jobs) as executor:
        futures = {executor.submit(f, a + i * step): i for i in range(n_iter)}
        for future in concurrent.futures.as_completed(futures):
            acc += future.result() * step
    return acc


def main():
    logging.basicConfig(filename='benchmarking.log', level=logging.INFO)
    cpu_num = os.cpu_count()
    for n_jobs in range(1, cpu_num * 2 + 1):
        start = time.time()
        integrate_thread_pool(math.cos, 0, math.pi / 2, n_jobs=n_jobs)
        logging.info(f"Thread pool executor: {n_jobs} jobs, {time.time() - start} seconds")
        start = time.time()
        integrate_process_pool(math.cos, 0, math.pi / 2, n_jobs=n_jobs)
        logging.info(f"Process pool executor: {n_jobs} jobs, {time.time() - start} seconds")


if __name__ == '__main__':
    main()
