class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        
        if(len(intervals) in [0,1]):
            return len(intervals)
        
        intervals.sort(key = lambda x:(x[0],-x[1]))
        
        c = 0
        
        last_end = -1
        
        print(intervals)
        
        for i in intervals:
            
            if(i[1] <= last_end):
                c += 1
            
            else:
                last_end = i[1]
            
        
        
        
        
        return len(intervals) - c
        

    