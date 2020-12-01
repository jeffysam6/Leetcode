class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        import heapq
        import collections
        
        
        graph = collections.defaultdict(dict)
        
        for f in flights:
            i,j,k = f
            graph[i][j] = k
            
        
        heap = [(0,src,K+1)]
        
        while(heap):
            node = heapq.heappop(heap)
            
            if(node[1] == dst):
                return node[0]
            
            if(node[-1] >0 ):  
                for j in graph[node[1]]:
                    heapq.heappush(heap,(node[0]+graph[node[1]][j],j,node[-1]-1))
        
        return -1