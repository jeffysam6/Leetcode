class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        from collections import defaultdict


        c = defaultdict(set)

        for i in dislikes:

            c[i[0]].add(i[1])
            c[i[1]].add(i[0])

        # print(c)
        visited = {}

        def dfs(node,group):

            if(node in visited):
                return visited[node] == group

            visited[node] = group

            return all(dfs(n,1-group) for n in c[node])


        return(all(dfs(node,0) for node in range(1,N+1) if node not in visited))


