class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        from collections import Counter
        
        
        d = Counter(nums)
        print(d)
        c = 0

        for i in d:
            if(k > 0 and i+k in d):
                c += 1
            
            elif(k == 0 and d[i] > 1):
                c += 1
        
        
        return c
#         nums.sort()
#         c = 0
        
#         s = set()
        
#         print(nums)
        
#         for i in range(len(nums)-1):
            
#             for j in range(i+1,len(nums)):
                
#                 if(nums[i] not in s and nums[j] - nums[i] ==k):
#                     c +=1
#                     s.add(nums[i])
                
                
                    
#         return(c)


#java
import java.util.HashMap;

class Solution {
    public int findPairs(int[] nums, int k) {
        
        
        HashMap<Integer,Integer> d = new HashMap();
        
        int c = 0;
        
        for(int x:nums){
            d.put(x,d.getOrDefault(x,0) + 1);
        }

        for(int y:d.keySet()){
            
            if(k > 0 && d.containsKey(k+y)){
                c += 1;
            }
            
            else if(k == 0 && d.get(y)>1){
                c += 1;
            }
        }
        
        return c;
    }
}