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
        text_insert_counter = 0
        column_counter = 0
        for num in range(text_segment_length):
            if num % 2 == 0:
                text += text_inserts[text_insert_counter]
                text_insert_counter += 1
            else:
                text += row[columns[column_counter]]
                column_counter += 1

        twitter.update_status(status=text)
        time.sleep(5)

def main():
    dataObject = [{'date': 'May 5', 'place': 'San Francisco', 'magnitude': '4.5'}, {'date': 'Jan 1', 'place': 'Taipei', 'magnitude': '6'}]
    columns = ['date', 'magnitude', 'place']
    textInserts = ['An earthquake occurred on the date of ', ', at a magnitude of ', ', and in the location of ']

    tweet(dataObject, columns, textInserts)
    print "tweeted successfully"

if __name__ == "__main__":
    main()
