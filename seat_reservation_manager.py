from heapq import heapify, heappush, heappop 
class SeatManager:

    def __init__(self, n: int):
        self.minHeap = [i for i in range(1, n+1)]
        heapify(self.minHeap)

    def reserve(self) -> int:
        return heappop(self.minHeap)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.minHeap, seatNumber)