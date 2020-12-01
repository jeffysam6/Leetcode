class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        diff = [a-b for a,b in costs]

        sorted_diff = sorted((value,i) for i,value in enumerate(diff))

        # print(sorted_diff)

        ans = 0


        for i in sorted_diff[:len(costs)//2]:
            ans += costs[i[-1]][0]



        for i in sorted_diff[len(costs)//2:]:
            ans += costs[i[-1]][1]

        return(ans)