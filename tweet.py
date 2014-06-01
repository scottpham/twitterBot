#!/usr/bin/env python

import sys
import os
from os.path import exists
from twython import Twython
import time

def tweet(data, columns, text_inserts):
    API_KEY = 'SviKWezy1ohjALJG91exYJ1qn'
    API_SECRET = 'MazAwFFYV3XNLs0aWMPuW3q9jrWSK1IS0E5Nabl8RyLX8EHfGq'
    ACCESS_TOKEN = '2538298806-UrVB8auRC9452OLGf7pEHAqs08rJI9XbFk15EA7'
    ACCESS_TOKEN_SECRET = 'PHWwXSLdHEogzX4S7CXHwFPb0FudtZajOcDlR2KhaKqLz'
 
    twitter = Twython(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    text_segment_length = len(columns) + len(text_inserts)
    
    for row in data:
        text = ""
        for num in range(text_segment_length):
            if columns.get(str(num)):
                text += row[columns[str(num)]]
            else:
                text += text_inserts[str(num)]

        twitter.update_status(status=text)
        time.sleep(5)

def main():
    dataObject = [{'date': 'May 5', 'place': 'San Francisco', 'magnitude': '4.5'}, {'date': 'Jan 1', 'place': 'Taipei', 'magnitude': '6'}]
    columns = {'1':'date', '3':'magnitude', '5':'place'};
    textInserts = {'0':'An earthquake occurred on the date of ', '2':', at a magnitude of ', '4':', and in the location of '};

    tweet(dataObject, columns, textInserts)
    print "tweeted successfully"

if __name__ == "__main__":
    main()
