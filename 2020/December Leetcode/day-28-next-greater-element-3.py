class Solution:
    def nextGreaterElement(self, n: int) -> int:
        
        arr = list(str(n))
        
        
        if(arr == sorted(arr,reverse=True)):
            return -1
        
        
        i = len(arr)-1
        while(i >= 0):
            if(arr[i] > arr[i-1]):
                break
                # return int(''.join(arr))
            
            i -= 1
        
        j = i
        
        while(j+1 < len(arr) and arr[j+1] > arr[i-1]):
            j += 1
        
#         print(i,arr[i-1])
#         print(j,arr[j])
        
        arr[i-1],arr[j] = arr[j],arr[i-1]
        arr[i:] = arr[i:][::-1]
        
        ans =  int(''.join(arr))
        
        return ans if ans < 1<<31 else -1
        # print(i,arr[i])
