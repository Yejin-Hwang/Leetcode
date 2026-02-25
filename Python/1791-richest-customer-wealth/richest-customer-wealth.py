class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = 0 
        curr = 0 

        for i in range(len(accounts)): 
            for j in range(len(accounts[i])): 
                curr+=accounts[i][j]
            
            if curr>=res: 
                res = curr
                curr = 0 

            else: 
                curr = 0

        return res
        