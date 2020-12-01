class Solution:

    def __init__(self, w: List[int]):
        self.arr = [0]
        
        for i in w:
            self.arr.append(self.arr[-1]+i)
        
        

    def pickIndex(self) -> int:
        random_number = random.randint(1,self.arr[-1])
        
        return bisect.bisect_left(self.arr,random_number) - 1
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()