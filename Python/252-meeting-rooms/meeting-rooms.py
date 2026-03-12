class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """



        for i in range(len(intervals)): 
            for j in range(len(intervals)): 
                if i<j: #prevent overlapping
                    start_1=intervals[i][0]
                    start_2=intervals[j][0]
                    end_1=intervals[i][1]
                    end_2=intervals[j][1]

                    if (start_2<start_1<end_2)  or (start_1<start_2<end_1): 
                        return False 

                    if (start_1==start_2) and (end_1==end_2): 
                        return False

        return True
