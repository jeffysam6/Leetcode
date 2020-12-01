class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        arr = [0]*(amount+1)

        arr[0] = 1
        # print(arr)

        for c in coins:

            for i in range(1,len(arr)):
                # print(arr)
                if(i >= c):

                    arr[i] += arr[i-c]


        return (arr[-1])