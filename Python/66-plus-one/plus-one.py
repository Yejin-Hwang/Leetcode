class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plus = ''.join(str(a) for a in digits)
        plus_one = int(plus)+1
        result = [int(digit) for digit in str(plus_one)]
        return result
