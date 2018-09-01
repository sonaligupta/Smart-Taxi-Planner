import tweepy  # twitter api module - python version
import datetime  # python datetime module
import json  # python json module
import os  # python os module, used for creating folders
import csv

OAuth = tweepy.OAuthHandler('2aYYtTLCVN94JJia6Jh6a5L0n', 'WivzZ8wh1NUR5ODBivf9DbGblUkEX0dXCG3ttq5GHjb2x2trix')
OAuth.set_access_token('2199387723-b2fofX8tr2vf4Sali0Nj2IrmdcJrmSYnEZCiYpl',
                       '9UBm43JWTLSBm0RSVyZ0P5bHJuoPz68aO9S0WzS4iNk44')


def rest_api():
    api = tweepy.API(OAuth)
    geo = '41.8781 -87.6298 20mi'
    latitude= 41.8781
    longitude = -87.6298
    radius =20
    i =0
    #raw_tweets =
    f = open('M-prime.csv', 'a+')
    writer = csv.writer(f)
    writer.writerow(["No.", "User ID", "Text", "Truth Value-1", "Truth Value-2"])
    for tweet in api.search(q = "(slow OR problems OR jam OR congestion OR collision OR crash OR accident) (street OR highway OR freeway OR traffic)", tweet_mode = "extended", count = 100, geocode = "%f,%f,%dmi" % (latitude, longitude, radius)):
        i+=1
        tweet_dict = dict()
        tweet_dict = tweet._json
        print tweet.full_text
        f = open('M-prime.csv', 'a+')
        writer = csv.writer(f)
        a = [[i, tweet_dict["user"]["id"], tweet.full_text.encode('utf-8')]]

        writer.writerows(a)
        f.close()
    '''status = api.user_timeline(user_id='76718450', count=1)
    s = status[0]._json
    print(s["text"])
    '''
    print i
    i = 0
    f = open('M-prime.csv', 'r')
    ff = open('D-prime.csv', 'a+')
    writer = csv.writer(ff)
    writer.writerow(["No.", "User ID", "Text", "Truth Value-1", "Truth Value-2"])
    reader = csv.reader(f)
    for row in reader:

        for tweet in api.user_timeline(user_id = row[1], count = 5):
            dictionary = tweet._json
            i += 1
            a = [[i, dictionary["user"]["id"], tweet.text.encode('utf-8')]]
            writer.writerows(a)

    f.close()
    ff.close()

    '''raw_tweets = api.search(q = 'traffic', count = 10, tweet_mode = 'extended')
    print len(raw_tweets['statuses'])

    for raw_tweet in range(len(raw_tweets['statuses'])):
        #        print raw_tweet
        tweet = raw_tweets['statuses'][raw_tweet]['full_text']#json.loads(str(raw_tweet))
        #tweet1 = raw_tweets['statuses'][1]['full_text']
        print(tweet)
        #print (tweet1)
'''
if __name__ == '__main__':
    rest_api()