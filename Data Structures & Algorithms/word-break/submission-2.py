class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordMem = {}
        wordSet = set(wordDict)
        def helper(index :int):
            if index == len(s):
                return True
            if index in wordMem:
                return wordMem[index]
            for i in range(index + 1, len(s)+1):
                if s[index : i] in wordSet and helper(i):
                    wordMem[index] = True
                    return True
            wordMem[index] = False
            return False
        return helper(0)
