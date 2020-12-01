class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import math


        dist = []

        for index,point in enumerate(points):

            dist.append([math.sqrt(point[0]**2 + point[1]**2) , index])


        dist.sort(key = lambda x:x[0])


        ans = []

        for i in range(k):
            ans.append(points[dist[i][1]])

        return(ans)