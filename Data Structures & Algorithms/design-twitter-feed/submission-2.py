from collections import defaultdict
class Twitter:

    def __init__(self):
        self.followMap = defaultdict(list)
        self.postMap = defaultdict(list)
        self.curTimeStamp = 1
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.postMap[userId].append((self.curTimeStamp, tweetId))
        self.curTimeStamp += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        for i in self.followMap[userId]:
            res.extend(self.postMap[i])
        res.extend(self.postMap[userId])
        res.sort(key = lambda x : x[0])
        res = [x[1] for x in res[-10 :]]
        res.reverse()
        return res
        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId or followeeId in self.followMap[followerId]:
            return 
        self.followMap[followerId].append(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId or followeeId not in self.followMap[followerId]:
            return 
        self.followMap[followerId].remove(followeeId)
        
