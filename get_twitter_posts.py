import tweepy

consumer_key = "3v7DfArio0rwzLTchxEZO39gY"
consumer_secret = "zKAEOJRMfIxBUAeNyeMnZIKUJsaZWlCxx2EdL83MgPDoBdzwn5"
access_key = "200177108-ACIaVIUYRnKKFTsNrzKFbslluZwpyXOUUr59DpS3"
access_secret = "CaeVF0kVRTYJa3c8N2Fsh2cdMTpPx0PoxqVkkRVbJYcZu"


def get_all_tweets(screen_name):

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    alltweets = []

    #if add include_rts=False or exclude_replies=True, retweets will not be collected
    new_tweets = api.user_timeline(screen_name=screen_name, exclude_replies=True)
    alltweets.extend(new_tweets)

    oldest = alltweets[-1].id - 1

    while len(new_tweets) > 0:
        print("getting tweets before %s" % (oldest))

        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest, exclude_replies=True)
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1

        print("...%s tweets downloaded so far" % (len(alltweets)))

    return [[
            tweet.id_str,
            '-'.join([str(tweet.created_at.year), str(tweet.created_at.month), str(tweet.created_at.day)]),
            ':'.join([str(tweet.created_at.hour), str(tweet.created_at.minute), str(tweet.created_at.second)]),
             tweet.text]
            for tweet in alltweets]


if __name__ == '__main__':
    print(get_all_tweets("Twitter"))