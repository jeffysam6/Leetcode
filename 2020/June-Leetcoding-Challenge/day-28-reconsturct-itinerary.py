class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict


        airport = defaultdict(list)

        for i in tickets:
            airport[i[0]].append(i[1])
            
        
        for i in airport:
            airport[i].sort(reverse=True)
        

        stack = ["JFK"]
        ans = []

        while(stack):
            
            p = stack[-1]
            
            if(p in airport and len(airport[p]) > 0):
                stack.append(airport[p].pop())
            
            else:
                ans.append(stack.pop())
 

        return(ans[::-1])