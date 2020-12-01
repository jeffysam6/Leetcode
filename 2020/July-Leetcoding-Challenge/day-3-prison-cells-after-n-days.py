class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:

        if(n == 0):
            return cells
        
        repeated = {}

        day = 1

        # temp = [0]*len(cells)
        prev = cells

        while(day <= 14):

            curr = [0]*len(cells)
            for i in range(1,len(cells)-1):
                # print(cells[i-1],cells[i+1])
                if(prev[i-1] == prev[i+1]):
                    curr[i] = 1

                else:
                    curr[i]= 0

                repeated[day - 1] = curr

            if(day == n):
                return curr
                
            prev = curr
            day += 1


        return (repeated[(n-1)%14])