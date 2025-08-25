class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [False] * (len(s) + 1)
        memo[0] = True
        n = len(s)
        wordDict.sort(key = lambda x : len(x))
        for i in range(len(memo)):
            if memo[i]:
                for word in wordDict:
                    if len(word) + i > n:
                        break
                    if s[i : i + len(word)] == word:
                        memo[i + len(word)] = True
        return memo[-1]
                    
                
        