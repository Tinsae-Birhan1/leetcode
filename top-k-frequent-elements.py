
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for i in nums:
            if i not in frequency:
                frequency[i] = 1
            else:
                frequency[i] += 1
        
        heap = []
        for i in frequency:
            if len(heap) < k:
                heapq.heappush(heap, (frequency[i] , i))
            else:
                if heap[0][0] < frequency[i]:
                    heapq.heappush(heap, (frequency[i] , i))
                    heapq.heappop(heap)
        
        return [x[1] for x in heap]
