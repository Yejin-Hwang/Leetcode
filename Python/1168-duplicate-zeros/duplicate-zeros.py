class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        arr_copy=arr[:]

        p1=0  #copy
        p2=0 #arr
        n=len(arr)

        while p2<n: 
            if  arr_copy[p1]!=0: 
                arr[p2]=arr_copy[p1]
                p2+=1
            else:
                arr[p2]=0
                p2+=1
                if p2<n: 
                    arr[p2]=0
                    p2+=1
            p1+=1
        