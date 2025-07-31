class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        major = 0
        major_key = None
        for key, value in freq.items(): 
            if value > major : 
                major = value
                major_key = key
        return major_key
            
        