class Solution:
    def findMaxLength(self, arr: List[int]) -> int:

        c = 0

        maxi = 0

        d = {0:0}

        for index,val in enumerate(arr,1):

            if(val == 1):
                c += 1

            else:
                c -= 1

            # print(c)
            if(c in d):
                maxi = max(maxi,index - d[c])
                # print(maxi)

            else:
                d[c] = index

        return (maxi)
