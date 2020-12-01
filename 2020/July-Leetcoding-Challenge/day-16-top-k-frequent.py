class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq
        
        d = Counter()
        
        for i in nums:
            d[i] += 1
        
            
        arr = d.items()
        temp = []
        
        for el in arr:
            el = list(el)
            el[0],el[1] = (-1 * el[1]),el[0]
            temp.append(el)
            
        
        
        
        out = []
        # print(temp)
        heapq.heapify(temp)
        
        while(k):
            out.append(heapq.heappop(temp)[1])
            k -= 1
            
        
        return out
        
        # return k[v.index(max(v))]