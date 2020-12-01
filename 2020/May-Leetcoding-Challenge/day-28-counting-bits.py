class Solution:
    def countBits(self, num: int) -> List[int]:
        
        arr = [0]
        
        for i in range(1,num+1):
            
            if(i%2 == 0 ):
                arr.append(arr[i//2])
            
            else:
                arr.append(arr[i//2] + 1)
                
        
        
        return arr
                