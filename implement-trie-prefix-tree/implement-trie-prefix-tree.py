class TrieNode:
    
    def __init__(self):
        self.links = [None for i in range(26)]
        self.isWord = False
        
    
    @staticmethod    
    def idx(key):
        return ord(key) - ord('a')
        
    
    def containsKey(self, key):
        return self.links[TrieNode.idx(key)] != None
    
    
    def getKey(self, key):
        return self.links[TrieNode.idx(key)]
    
    
    def addKey(self, key, node):
        self.links[TrieNode.idx(key)] = node
        

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        
        for key in word:
            if not node.containsKey(key):
                node.addKey(key, TrieNode())
            node = node.getKey(key)
        node.isWord = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        
        for key in word:
            if not node.containsKey(key):
                return False
            node = node.getKey(key)
        
        if node.isWord:
            return True
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        
        for key in prefix:
            if not node.containsKey(key):
                return False
            node = node.getKey(key)
            
        return True
        
        

    
    
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)