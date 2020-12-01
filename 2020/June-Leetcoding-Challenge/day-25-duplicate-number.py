class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        t,h = nums[0],nums[nums[0]]
        
        while(t != h):
            t,h = nums[t],nums[nums[h]]
        
        t = 0
        
        while(t != h):
            t,h = nums[t],nums[h]
        
        # print(t,h)
        return t



