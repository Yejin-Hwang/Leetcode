class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        key_list = list(pattern)
        val_list = s.split()
        char_to_word = {}
        word_to_char = {}

        if len(key_list)!=len(val_list): 
            return False

        for k,v in zip(key_list,val_list): 
            if k in char_to_word: 
                if char_to_word[k] !=v: 
                    return False
            else: 
                char_to_word[k] = v

            if v in word_to_char: 
                if  word_to_char[v] != k:
                    return False 
            else: 
                word_to_char[v]=k
        return True
