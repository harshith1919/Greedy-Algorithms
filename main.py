from strat1 import strategy1
from strat2 import strategy2
from strat3 import strategy3
from strat4 import strategy4

import sys
import time

# set to True to enable performance measurement and printing it to stdout
measure_enabled = False


def measure_performance(heap):
    percentage = 0

    for working, tot in heap:
        percentage += working / tot

    return (percentage / len(heap)) * 100


if __name__ == "__main__":
    n, k = map(int, input().split())
    workingDevices = []
    totalDevices = []

    for _ in range(n):
        working, total = map(int, input().split())
        workingDevices.append(working)
        totalDevices.append(total)

    start_time = time.time()

    if sys.argv[1] == "1":
        output, heap = strategy1(n, workingDevices, totalDevices, k)
    elif sys.argv[1] == "2":
        output, heap = strategy2(n, workingDevices, totalDevices, k)
    elif sys.argv[1] == "3":
        output, heap = strategy3(n, workingDevices, totalDevices, k)
    elif sys.argv[1] == "4":
        output, heap = strategy4(n, workingDevices, totalDevices, k)
    else:
        raise ValueError("Invalid strategy number")

    end_time = time.time()

    print(" ".join(map(str, output)))

    if measure_enabled:
        print(f"Time taken: {(end_time - start_time) * 1000:.2f} ms")
        print(f"Percentage: {measure_performance(heap):.2f}")
