import tweepy

CONSUMER_KEY = "3v7DfArio0rwzLTchxEZO39gY"
CONSUMER_SECRET = "zKAEOJRMfIxBUAeNyeMnZIKUJsaZWlCxx2EdL83MgPDoBdzwn5"
ACCESS_KEY = "200177108-ACIaVIUYRnKKFTsNrzKFbslluZwpyXOUUr59DpS3"
ACCESS_SECRET = "CaeVF0kVRTYJa3c8N2Fsh2cdMTpPx0PoxqVkkRVbJYcZu"


def get_all_tweets(screen_name):

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    alltweets = []

    #if add include_rts=False or exclude_replies=True, retweets will not be collected

    while True:
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest, exclude_replies=True)
        if not new_tweets:
            break
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