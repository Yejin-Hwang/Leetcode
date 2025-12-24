class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] 
        nums.sort() 
        n = len(nums)

        for i in range(len(nums)-3): 
            if i>0 and nums[i] == nums[i-1]: 
                continue
            for r in range(len(nums)-1,i+2, -1):
                if r<n-1 and nums[r] == nums[r+1]: 
                    continue
                l,k = i+1, r-1
                while l<k: 
                    total = nums[i]+nums[l]+nums[k]+nums[r]
                    if total <target:
                        l+=1
                    elif total>target:
                        k-=1
                    else: 
                     #total == target 
                        res.append([nums[i],nums[l],nums[k],nums[r]])
                        l+=1
                        k-=1
                        while nums[l]==nums[l-1] and l<k:
                            l+=1
                        while nums[k]==nums[k+1] and l<k:
                            k-=1
        return res

        #[-2,-1,0,0,1,2]



            
