class PrefixTree:

    def __init__(self):
        self.TrieHead = TrieNode()

    def insert(self, word: str) -> None:
        curNode = self.TrieHead
        for i in word:
            if curNode.children[ord(i) - ord('a')] == None:
                curNode.children[ord(i) - ord('a')] = TrieNode()
            curNode = curNode.children[ord(i) - ord('a')]
        curNode.isWord = True
            
    def search(self, word: str) -> bool:
        curNode = self.TrieHead
        for i in word:
            if curNode.children[ord(i) - ord('a')] == None:
                return False
            curNode = curNode.children[ord(i) - ord('a')]
        return curNode.isWord
        
    def startsWith(self, prefix: str) -> bool:
        curNode = self.TrieHead
        for i in prefix:
            if curNode.children[ord(i) - ord('a')] == None:
                return False
            curNode = curNode.children[ord(i) - ord('a')]
        return True

class TrieNode:
    def __init__(self):
        self.children =[None] * 26   
        self.isWord = False     
        