import heapq


def comparator(tot: int, working: int):
    return (working / tot) - ((working + 1) / (tot + 1))


def strategy4(n: int, numWorking: list[int], total: list[int], k: int):
    heap = [
        (comparator(tot, working), index, working, tot)
        for index, (working, tot) in enumerate(zip(numWorking, total))
    ]  # use a comparator to compare the next value in the heap

    heapq.heapify(heap)
    # heap stores (working/total, index, working devices, total devices)
    output: list[int] = []
    while k:
        _, index, working, tot = heapq.heappop(heap)
        output.append(index)
        working += 1
        tot += 1
        heapq.heappush(heap, (comparator(tot, working), index, working, tot))
        k -= 1

    return output, [(w, t) for _, _, w, t in heap]
