import csv
import operator

def getTweets(fname):
    with open(fname, newline='') as csvfile:
        raw_tweets = csv.reader(csvfile, delimiter=',')
        tweets = []
        for row in raw_tweets:
            tweets.append(row[7])
    return tweets

def main():
    fname = input("Tweet file: ")
    tweets = getTweets(fname)
    freqDict = {}
    common = ['a', 'an', 'the']
    for e in tweets:
        for word in e.split(" "):
            if word.lower() not in common:
                if word.lower() in freqDict.keys():
                    freqDict[word.lower()] += 1
                else:
                    freqDict[word.lower()] = 1

    sortedFreq = sorted(freqDict.items(), reverse=True, key=lambda x:x[1])

    for i in range(10):
        print (sortedFreq[i])




if __name__ == "__main__":
    main()
    
