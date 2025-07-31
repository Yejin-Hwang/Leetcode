class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        stack = [] 
        output = [] 
        for num in nums : 
            if num not in stack : 
                stack.append(num)
            else : 
                output.append(num)
        return output