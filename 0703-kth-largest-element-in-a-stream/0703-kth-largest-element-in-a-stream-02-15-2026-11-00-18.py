import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = sorted(nums, reverse=True)[:k]
        heapify(self.heap) 
        self.k = k

    def add(self, val: int) -> int:
        if len(self.heap) == self.k:
            if val > self.heap[0]:
                heapreplace(self.heap, val)
        else:
            heappush(self.heap, val)
        return self.heap[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)