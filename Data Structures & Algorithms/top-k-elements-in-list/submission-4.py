class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        res = []

        for key,val in count.items():
            heapq.heappush(heap, (val,key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        while len(heap) > 0:
            res.append(heapq.heappop(heap)[1])
        
        return res