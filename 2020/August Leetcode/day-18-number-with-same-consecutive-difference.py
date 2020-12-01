class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:

        ans = []
        visited = set()
        
        if(n == 1):
            return [i for i in range(10)]

        def find_rest(i,tot):
            

            if(len(tot) == n):
                if(int(tot) not in visited):
                    if(tot == '0' or len(str(int(tot))) == n ):
                        ans.append(int(tot))
                        visited.add(int(tot))			
                # print(ans)
                return

            for j in range(10):
                if(abs(j - i) == k):
                    find_rest(j,tot+str(i))


        for i in range(0,10):
            find_rest(i,'')
        

        return(ans)