class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count={}
        for i in s: 
            if i in char_count : 
                char_count[i] +=1
            else : 
                char_count[i]=1
        for index, i in enumerate(s):
            if char_count[i]==1:
                return index
        return -1