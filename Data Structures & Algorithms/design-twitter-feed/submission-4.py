class Twitter:

    def __init__(self):
        self.tweets = []
        self.time = 0
        self.userFollows = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.tweets, [self.time, tweetId, userId])
        self.time = self.time - 1


    def getNewsFeed(self, userId: int) -> List[int]:
        validIds = [userId]
        if userId in self.userFollows:
            validIds.extend(self.userFollows[userId])
        allTweets = []
        validTweets = []
        while self.tweets and len(validTweets) < 10:
            tweet = heapq.heappop(self.tweets)
            if tweet[-1] in validIds:
                validTweets.append(tweet[1])
            allTweets.append(tweet)
        for tweet in allTweets:
            heapq.heappush(self.tweets, tweet)
        print(self.userFollows, "getNewsFeed")
        return validTweets     

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.userFollows and followeeId not in self.userFollows[followerId]:
            if followeeId not in self.userFollows[followerId]:
                self.userFollows[followerId].append(followeeId)
        else:
            self.userFollows[followerId] = [followeeId]
        print(self.userFollows, "follow")

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.userFollows and followeeId in self.userFollows[followerId]:
            self.userFollows[followerId].remove(followeeId)
        print(self.userFollows, "unfollow")





