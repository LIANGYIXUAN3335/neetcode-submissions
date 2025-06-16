class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        wordDictionary = WordDictionary()
        for word in words:
            wordDictionary.addWord(word)
        res = []
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        used = [[False] * len(board[0]) for _ in range(len(board))]
        def helper(curNode: TrieNode, i : int, j : int):
            idx = ord(board[i][j]) - ord('a')
            if curNode.children[idx] == None:
                return
            used[i][j] = True
            curNode = curNode.children[idx]
            if curNode.curWord != '':
                res.append(curNode.curWord)
                curNode.curWord = ''
            for x, y in directions:
                curI, curJ = i + x, j + y
                if curI < 0 or curJ < 0 or curI >= len(board) or curJ >= len(board[0]) or used[curI][curJ]:
                    continue
                helper(curNode, curI, curJ)  
            used[i][j] = False          
        for i in range(len(board)):
            for j in range(len(board[0])):
                helper(wordDictionary.TrieHead, i, j)
        return res

        
class WordDictionary:

    def __init__(self):
        self.TrieHead = TrieNode()

    def addWord(self, word: str) -> None:
        curNode = self.TrieHead
        for i in word:
            if curNode.children[ord(i) - ord('a')] == None:
                curNode.children[ord(i) - ord('a')] = TrieNode()
            curNode = curNode.children[ord(i) - ord('a')]
        curNode.curWord = word
    
class TrieNode:
    def __init__(self):
        self.children =[None] * 26   
        self.curWord = ''     
        