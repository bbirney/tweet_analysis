import csv

with open('tweets.csv', 'r') as csvfile:
    raw_tweets = csv.reader(csvfile, delimiter=',', quotechar='\"')
    
