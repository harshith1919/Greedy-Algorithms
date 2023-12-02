import heapq


def strategy1(n: int, numWorking: list[int], total: list[int], k: int):
    # create an array of tuples (working devices, index, total devices)
    heap = [
        (working, index, tot)
        for index, (working, tot) in enumerate(zip(numWorking, total))
    ]
    heapq.heapify(heap)
    output: list[int] = []  # heap stores (working devices, index, total devices)
    while k:
        working, index, tot = heapq.heappop(heap)
        output.append(index)
        working += 1
        tot += 1  # total devices in a bag
        heapq.heappush(heap, (working, index, tot))
        k -= 1

    return output, [(w, t) for w, _, t in heap]
