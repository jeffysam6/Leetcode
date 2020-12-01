class Solution:
    def eraseOverlapIntervals(self, arr: List[List[int]]) -> int:

        visited = []
        arr.sort(key=lambda x:x[1])
        
        c = 0
        end = float('-inf')
        
        for i in arr:

            if(i[0] >= end):
                end = i[1]
                
            else:
                c += 1

        return  c


v