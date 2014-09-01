#!/usr/bin/env python

from twython import Twython
import time

def tweet(list_of_tweets):
    API_KEY = 'SviKWezy1ohjALJG91exYJ1qn'
    API_SECRET = 'MazAwFFYV3XNLs0aWMPuW3q9jrWSK1IS0E5Nabl8RyLX8EHfGq'
    ACCESS_TOKEN = '2538298806-UrVB8auRC9452OLGf7pEHAqs08rJI9XbFk15EA7'
    ACCESS_TOKEN_SECRET = 'PHWwXSLdHEogzX4S7CXHwFPb0FudtZajOcDlR2KhaKqLz'
 
    twitter = Twython(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    for message in list_of_tweets:
        twitter.update_status(status=message)
        time.sleep(3)


def main():
    tweet_list = [u'one ', u'date', u' two ', u'level', u' three ', u'allergylevel', u' four ', u'location', u' five ',
                  u'rowNumber', u'  six']
    tweet(tweet_list)
    print "tweeted successfully"

if __name__ == "__main__":
    main()
