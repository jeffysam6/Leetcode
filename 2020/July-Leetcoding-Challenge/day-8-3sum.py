class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        nums.sort()
        
        for i in range(len(nums)-2):
            
            if(i == 0 or (i>0 and nums[i] != nums[i-1])):
                
                sums = 0 - nums[i]
                left = i + 1
                right = len(nums) - 1
                
                while(left < right):
                    
                    # print(nums[left] + nums[right] == sums)
                    if(nums[left] + nums[right] == sums):
                        ans.append([nums[i],nums[left],nums[right]])
                        
                        while(left < right and nums[left] == nums[left+1]):
                            left += 1
                        
                        while(left < right and nums[right] == nums[right- 1]):
                            right -= 1


                        left += 1
                        right -= 1
                    
                    elif(nums[left] + nums[right] > sums):
                        right -= 1
                    
                    else:
                        left += 1
                    

        return ans