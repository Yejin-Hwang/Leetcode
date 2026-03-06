class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #Three pointers
        nums1_copy = nums1[:m]

        p1 = 0 #m
        p2 = 0 #n

        for p in range(n+m): 
            if p2>=n or (p1<m and nums1_copy[p1]<nums2[p2]): 
                nums1[p]=nums1_copy[p1]
                p1+=1
            else: 
                nums1[p]=nums2[p2]
                p2+=1


        #---------------------------
        # Merge and sort 

        # for i in range (n): 
        #     nums1[i+m]=nums2[i]

        # nums1.sort()
        