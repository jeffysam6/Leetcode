class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        
        self.characters = characters
        self.combi = []
        self.combinationLength = combinationLength
        self.permute('',0)
        print(self.combi)
        self.curr = -1
        
    
    def permute(self,s,start):
        
        if(len(s) == self.combinationLength):
            self.combi.append(s)
            return
        else:
            for i in range(start,len(self.characters)):
                self.permute(s+self.characters[i],i+1)
            

    def next(self) -> str:
        self.curr += 1
        if(self.curr < len(self.combi)):
            return self.combi[self.curr]
        else:
            return False

    def hasNext(self) -> bool:
        if(self.curr+1 < len(self.combi)):
            return True
        
        else:
            return False


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()