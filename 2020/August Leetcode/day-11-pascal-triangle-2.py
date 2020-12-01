class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        pascal = [[1],[1,1]]
        
        if(rowIndex == 1):
            return pascal[1]
        elif(rowIndex == 0):
            return pascal[0]
        
        prev = pascal[-1]

        for i in range(rowIndex-1):


            temp = [1]

            for i in range(len(prev)-1):
                temp.append(prev[i]+prev[i+1])

            temp.append(1)

            prev = temp
            

        
        return(temp)

