class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        mapping = { ")" : "(", "]" : "[", "}" : "{"}
        for par in s : 
            if par in "({[":
                stack.append(par)
            elif par in ")}]": 
                if not stack or stack[-1]!=mapping[par]: 
                    return False
                stack.pop()
        return len(stack) == 0