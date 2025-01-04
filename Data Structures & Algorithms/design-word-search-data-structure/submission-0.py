class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word: str) -> None:
        cur = self.root
        for i in word:
            if not cur.children[ord(i) -  ord('a')]:
                cur.children[ord(i) -  ord('a')] = TrieNode()
            cur =  cur.children[ord(i) -  ord('a')] 
        cur.isWord = True
        
    def search(self, word: str) -> bool:
        cur = self.root
        return self.searchHelper(cur,word)

    def searchHelper(self, cur: TrieNode,word: str) -> bool:
        for i in range(len(word)):
            if word[i] == '.':
                for j in cur.children:
                    if j and self.searchHelper(j,word[i + 1:]):
                        return True
                return False
            if not cur.children[ord(word[i]) -  ord('a')]:
                return False
            cur = cur.children[ord(word[i]) -  ord('a')]
        if cur.isWord:
            return True
        else:
            return False



        
