import heapq


def strategy3(n: int, numWorking: list[int], total: list[int], k: int):
    heap = [
        (tot, index, working)
        for index, (working, tot) in enumerate(zip(numWorking, total))
    ]
    heapq.heapify(heap)  # heap stores (total devices, index, working devices)
    output = []
    while k:
        tot, index, working = heapq.heappop(heap)
        output.append(index)
        working += 1
        tot += 1
        heapq.heappush(heap, (tot, index, working))
        k -= 1

    return output, [(w, t) for t, _, w in heap]
