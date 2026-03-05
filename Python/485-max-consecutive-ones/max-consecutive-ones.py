class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        
        count=0 
        res={}
        
        for i in range(len(nums)): 
            if nums[i]==1 and i!=len(nums)-1: 
                count+=1 
            
            elif nums[i]==1 and i==len(nums)-1: 
                count+=1
                index= i- count +1  
                res[count]=index
                
            elif nums[i]==0: 
                index= i- count +1  
                res[count]=index
                count=0 
                
            
        
        return max(res)
            
        