class PrefixTree:

    def __init__(self):
        self.rootNode = TrieNode()
        
    def insert(self, word: str) -> None:
        root = self.rootNode
        cur= root
        for i in word:
            if cur.children[ord(i) - ord('a')] ==None:
                cur.children[ord(i) - ord('a')] = TrieNode()
            cur = cur.children[ord(i) - ord('a')]
        cur.isWord = True


    def search(self, word: str) -> bool:
        root = self.rootNode
        cur= root
        for i in word:
            if cur.children[ord(i) - ord('a')] ==None:
                return False
            cur = cur.children[ord(i) - ord('a')]
        if cur.isWord:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        root = self.rootNode
        cur= root
        for i in prefix:
            if cur.children[ord(i) - ord('a')] ==None:
                return False
            cur = cur.children[ord(i) - ord('a')]
        return True

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False

        
        