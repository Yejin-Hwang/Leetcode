class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sor = sorted(nums) #0,1,3
        if sor[0]!=0 : 
            return 0
        for i in range(1,len(sor)): 
            if sor[i] - sor[i-1]!= 1: 
                return sor[i-1] +1
        return sor[-1] +1