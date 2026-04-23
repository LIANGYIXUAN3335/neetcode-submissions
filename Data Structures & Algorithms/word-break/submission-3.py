class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # solution 1
        # wordMem = {}
        # wordSet = set(wordDict)
        # def helper(index :int):
        #     if index == len(s):
        #         return True
        #     if index in wordMem:
        #         return wordMem[index]
        #     for i in range(index + 1, len(s)+1):
        #         if s[index : i] in wordSet and helper(i):
        #             wordMem[index] = True
        #             return True
        #     wordMem[index] = False
        #     return False
        # return helper(0)
        # solution 2 
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for start in range(len(s)):
            for end in range(start + 1,len(s) + 1):
                if dp[start] and s[start : end] in wordDict:
                    dp[end] = True
        return dp[-1]  
