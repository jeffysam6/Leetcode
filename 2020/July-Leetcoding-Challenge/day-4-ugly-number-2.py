class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        
        arr = [1]

        index_2,index_3,index_5 = 0,0,0


        while(n > 1):

            multi_2,multi_3,multi_5 = 2* arr[index_2], 3 * arr[index_3], 5 * arr[index_5]

            mini_val = min(multi_2,multi_3,multi_5)

            arr.append(mini_val)

            if(multi_2 == mini_val):
                index_2 += 1

            if(multi_3 == mini_val):
                index_3 += 1 


            if(multi_5 == mini_val):
                index_5 += 1

            n -= 1


        return arr[-1]

