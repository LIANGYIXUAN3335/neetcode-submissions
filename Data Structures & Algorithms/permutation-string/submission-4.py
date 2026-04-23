class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Dic = {}
        slidingWindowDic = {}
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            s1Dic[s1[i]] = s1Dic.get(s1[i],0) + 1
            slidingWindowDic[s2[i]] = slidingWindowDic.get(s2[i],0) + 1
        left = 0
        for right in range(len(s1) , len(s2)):
            print(slidingWindowDic)
            if slidingWindowDic == s1Dic:
                return True
            if slidingWindowDic[s2[left]] == 1:
                del slidingWindowDic[s2[left]]
            else:
                slidingWindowDic[s2[left]] -= 1
            slidingWindowDic[s2[right]] = slidingWindowDic.get(s2[right],0) + 1
            left += 1
        return slidingWindowDic == s1Dic

            

                