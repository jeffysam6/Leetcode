class Solution:
    def maxSubarraySumCircular(self, arr: List[int]) -> int:

        maxi = float('-inf')
        
        mini = float('inf')
        # print(mini)

        temp = 0

        total_sum = sum(arr)

        for i in range(len(arr)):
            temp += arr[i]

            maxi = max(maxi,temp)


            if(temp < 0 ):
                temp = 0

        temp = 0

        for i in range(len(arr)):
            temp += arr[i]


            mini = min(mini,temp)

            if(temp > 0 ):
                temp = 0


        # print(maxi,total_sum,mini)

        if(total_sum == mini):
            return(maxi)

        else:
            return(max(total_sum - mini, maxi))
        # print(maxi,mini)