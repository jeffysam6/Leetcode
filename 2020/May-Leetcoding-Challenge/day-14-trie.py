class Node:
    def __init__(self):
        self.child = [None]*26
        self.end = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        head = self.root
        for c in word:
            index = ord(c) - ord('a')
            if(not head.child[index]):
                head.child[index] = Node()
            
            head = head.child[index]
        
        head.end = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        head = self.root
        for c in word:
            index = ord(c) - ord('a')
            if(not head.child[index]):
                return False
            
            head = head.child[index]
        
        return head != None and head.end
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        head = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if(not head.child[index]):
                return False
            head = head.child[index]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)