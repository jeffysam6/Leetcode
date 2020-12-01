class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        hourhand = hour*30  + minutes/60 * 30
        
        minutehand = minutes * 6
        
        
        angle = abs(hourhand - minutehand)
        
        if(angle > 180):
            return 360-angle
        
        return angle