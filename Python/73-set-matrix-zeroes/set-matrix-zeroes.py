class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        row0, col0 = False, False

        #base case 
        if not matrix : 
            return []


        # Step1. Marking
        # first row, first col
        for r in range(rows): 
            for c in range(cols): 
                if matrix[r][0] == 0 : 
                    col0 = True 
                if matrix[0][c] == 0: 
                    row0 = True
                    
        #besids first row, first col -> Marking at first row and first col
        for r in range(1,rows): 
            for c in range(1,cols):
                if matrix[r][c] == 0: 
                    matrix[r][0], matrix[0][c] = 0, 0 

        # Step2. Set to Zero

        for r in range(1,rows): 
            for c in range(1,cols): 
                if matrix[r][0] ==0 or matrix[0][c] ==0: 
                    matrix[r][c] = 0 

        for r in range(rows): 
            for c in range(cols): 
                if col0 == True : 
                    matrix[r][0] = 0 
                if row0 == True : 
                    matrix[0][c] = 0 
            
        

