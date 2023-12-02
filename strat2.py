import heapq


def strategy2(n: int, numWorking: list[int], total: list[int], k: int):
    heap = [
        (working / tot, index, working, tot)
        for index, (working, tot) in enumerate(zip(numWorking, total))
    ]
    heapq.heapify(heap)
    # heap stores (working/total, index, working devices, total devices)
    output: list[int] = []
    while k:
        _, index, working, tot = heapq.heappop(heap)
        output.append(index)
        working += 1
        tot += 1
        heapq.heappush(heap, (working / tot, index, working, tot))
        k -= 1

    return output, [(w, t) for _, _, w, t in heap]
