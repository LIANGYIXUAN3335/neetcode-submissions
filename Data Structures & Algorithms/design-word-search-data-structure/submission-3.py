class WordDictionary:

    def __init__(self):
        self.TrieHead = TrieNode()

    def addWord(self, word: str) -> None:
        curNode = self.TrieHead
        for i in word:
            if curNode.children[ord(i) - ord('a')] == None:
                curNode.children[ord(i) - ord('a')] = TrieNode()
            curNode = curNode.children[ord(i) - ord('a')]
        curNode.isWord = True

    def search(self, word: str) -> bool:
        n = len(word)
        def searchHelper(curNode, curIndex) -> bool:
            for i in range(curIndex, n):
                if word[i] == '.':
                    for nxtNode in curNode.children:
                        if nxtNode:
                            if searchHelper(nxtNode, i + 1):
                                return True
                    return False
                elif curNode.children[ord(word[i]) - ord('a')] == None:
                    return False
                else:
                    curNode = curNode.children[ord(word[i]) - ord('a')]
            return curNode.isWord
        curNode = self.TrieHead
        return searchHelper(curNode, 0)
    

class TrieNode:
    def __init__(self):
        self.children =[None] * 26   
        self.isWord = False     
        