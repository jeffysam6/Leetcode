class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        l = len(arr)
        
        d = defaultdict(list)
        
        for i,n in enumerate(arr):
            d[n].append(i)
        
        # print(d)
        
        visited, visited_groups = set(), set()
        
        queue = deque([(0,0)])
        
        while(queue):
        
            steps,index = queue.popleft()

            if(index == l - 1):
                return steps

            for diff in [index-1,index+1]:

                if(0<=diff<l and diff not in visited):
                    visited.add(diff)
                    queue.append([steps+1,diff])

            if(arr[index] not in visited_groups):
                for val in d[arr[index]]:
                    if(val not in visited):
                        visited.add(val)
                        queue.append([steps+1,val])

                visited_groups.add(arr[index])
        
