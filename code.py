class Solution:
    def eraseOverlapIntervals(self, intervals):
        end = float('-inf')
        erased = 0
        for i in sorted(intervals, key=lambda i: i[-1]):
            if i[0] >= end:
                end = i[-1]
            else:
                erased += 1
        return erased
    
   
