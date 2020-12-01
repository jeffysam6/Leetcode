class Solution:
    def searchInsert(self, nums: List[int], val: int) -> int:
        import bisect
        
        arr = []


        for i in range(len(arr)):
            arr[i] = [nums[i],i]


        # print(arr)

        l,r = 0,len(arr)-1

        while(l < r):

            mid = ((r-l)//2) + l
            # print(l,mid,r)
            if(arr[mid][0] == val):
                return(arr[mid][1])
                exit()

            elif(arr[mid][0] > val):
                r = mid

            else:
                l = mid + 1



        return(bisect.bisect_left(nums,val))