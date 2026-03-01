from functools import cache
class Solution:
    @cache
    def climbStairs(self, n: int) -> int:

        if n==1: 
            return 1
        
        elif n==2: #1+1, 2
            return 2
        
        elif n==3: #1+2, 2+1, 1+1+1
            return 3
        
        elif n>3: 
            return self.climbStairs(n-1)+ self.climbStairs(n-2)