class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        negative_nums =[-x for x in nums] 
        heapq.heapify(negative_nums)
        res=0
        
        for i in range(k): 
            res=heapq.heappop(negative_nums)
            
        return -res
        
        
        
        