class Solution:
    def findOrder(self, n: int, arr: List[List[int]]) -> List[int]:
        from collections import defaultdict
        
        def dfs(node):
            
            if(visited[node] == -1):
                return False
            
            if(visited[node] == 1):
                return True
            
            visited[node] = -1
            
            for k in d[node]:
                if(not dfs(k)):
                    return False
            
            ans.append(node)
            visited[node] = 1
            
            return True
                
        d = defaultdict(list)

        ans = []

        for i in arr:
            d[i[0]].append(i[1])
            
        visited = [0 for _ in range(n)]
        
        for x in range(n):
            if( not dfs(x)):
                return []
            
        return ans

        # print(d)

                

