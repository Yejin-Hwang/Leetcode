class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        #reverse 
        l, r = 0,  len(matrix)-1
        while l<r: 
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l+=1
            r-=1
        
        rows, cols = len(matrix), len(matrix[0])

        # #transpose
        # for r in range(rows): 
        #     for c in range(cols): 
        #         matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        # transpose 
        for i in range(len(matrix)):
	        for j in range(i):
		        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


        