class Solution:
    def singleNonDuplicate(self, arr: List[int]) -> int:
        

        left = 0     

        right = len(arr) - 1


        while(left<right):


            mid = 2 * ((right + left)//4)

            # print('bef',  left,mid,right)


            if(arr[mid] == arr[mid + 1]):
                left = mid + 2

            else:
                right = mid

            # print('aft',left,mid,right)


        # print('ans',arr[left])
        
        return arr[left]

