class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        from collections import Counter
        c = 0
        d = Counter()
        
        for i in range(len(time)):
            time[i] = time[i]%60
            d[time[i]] += 1
        # print(time,d)
        
        for i in time:
            d[i] -= 1
            if(i is 0 and d[i] > 0):
                c += d[0]
                
            if((d[60-i] > 0)):
                # print(i,60-i)
                c += d[60-i]
            # print(d)
        
        
        return c
            
        