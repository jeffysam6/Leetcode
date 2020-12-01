def maxProfit(arr):
    


    dp = [[None,None] for _ in range(len(arr))]

    if(len(arr) <=1 ):
        return(0)

    if(len(arr) == 2 and arr[1] > arr[0]):
        return(arr[1] - arr[0])

    elif(len(arr) == 2 and arr[1] < arr[0]):
        return(0)



    dp[0][0] = 0

    dp[0][1] = -arr[0]

    dp[1][0] = max(dp[0][0],dp[0][1] + arr[1])

    dp[1][1] = max(dp[0][1],dp[0][0] - arr[1])

    for i in range(2,len(arr)):

        # [1,2,3,0,2]

        dp[i][0] = max(dp[i-1][0],dp[i-1][1] + arr[i])

        dp[i][1] = max(dp[i-1][1],dp[i-2][0] - arr[i])


        print(dp)



    return dp[-1][0]


print(maxProfit([1,2,3,0,2]))