class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        #sol 3 space o(1) time o(n)
        
        curr = 0
        
        for index,i in enumerate(A):
            if(i%2 == 0):
                A[curr],A[index] = A[index],A[curr]
                curr += 1
        return A
    
    
    #sol 2 space o(1) time o(n^2)
        
#         for index,i in enumerate(A):
            
#             if(i % 2 == 0 or i == 0):
                
#                 curr = 0
                
#                 while(curr < index):
#                     # print(A[curr])
#                     if(A[curr]%2 != 0):
                        
#                         A[curr],A[index] = A[index],A[curr]
#                         break
#                     curr += 1
#         return A
                
        
        
        
        
        
        
        
        
        #sol 1 space o(n) time o(n)
#         even = []
#         odd = []
        
#         for i in A:
#             if(i%2 == 0):
#                 even.append(i)
#             else:
#                 odd.append(i)
        
        
#         return even+odd