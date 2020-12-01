class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        
        oldColor = image[sr][sc]
        
        def filling(sr,sc,newColor):
            
            if(image[sr][sc] == oldColor and oldColor != newColor):
                
                image[sr][sc] = newColor
            
                
                if(sr+1 < len(image)):
                    filling(sr + 1, sc,newColor)
                
                if(sc + 1 < len(image[0])):
                    filling(sr, sc+1,newColor)
                
                if(sc-1 >= 0 ):
                    filling(sr, sc - 1 ,newColor)
                    
                if(sr-1 >= 0 ):
                    filling(sr - 1, sc,newColor)

#                 filling(sr - 1, sc,newColor)
#                 filling(sr, sc + 1,newColor)
                
                
        filling(sr,sc,newColor)
            
    
        return image

