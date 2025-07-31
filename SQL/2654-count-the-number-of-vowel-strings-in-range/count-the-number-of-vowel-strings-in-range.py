class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowel = ["a","e","i","o","u"]
        count=0 
        for i in range(len(words)): 
            if words[i][0] in vowel and words[i][-1] in vowel:
                if left<=i<=right: 
                    count+=1
        return count