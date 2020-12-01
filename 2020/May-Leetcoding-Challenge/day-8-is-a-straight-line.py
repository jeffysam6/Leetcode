class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        if(len(coordinates) == 2):
            return True
        
        if((coordinates[1][0] - coordinates[0][0]) == 0):
            slope = 0
        
        else:
            slope = (coordinates[1][1] - coordinates[0][1])/(coordinates[1][0] - coordinates[0][0])
        
        
        # y = slope(x-coordinates[1][0]) + coordinates[1][1]
        
        for i in range(2,len(coordinates)):
            
            x,y = coordinates[i][0],coordinates[i][1]
            
            if(y != slope * (x-coordinates[1][0]) + coordinates[1][1]):
                return False
        
        
        return True