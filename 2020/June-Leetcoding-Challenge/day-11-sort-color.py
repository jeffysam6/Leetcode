class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r,index,b = 0,0,len(nums)-1
        
        while(index <= b):
            
            if(nums[index] == 0):
                nums[index],nums[r] = nums[r],nums[index]
                index += 1
                r += 1
                
            
            elif(nums[index] == 2):
                nums[index],nums[b] = nums[b],nums[index]
                b -= 1
                
            
            else:
                index += 1
        
        return nums