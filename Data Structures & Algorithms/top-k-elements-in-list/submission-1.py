from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_dict = Counter(nums)
        heap = []
        for key, value in counter_dict.items():
            heapq.heappush(heap, (value, key))
            if(len(heap) > k):
                heapq.heappop(heap)
        res = []
        for value, key in heap:
            res.append(key)
        return res
