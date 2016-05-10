import csv
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import pylab
import math

def datagrab():
    f0215 = open("./data/Feb2015.csv")
    f0315 = open("./data/Mar2015.csv")
    f0415 = open("./data/Apr2015.csv")
    f0515 = open("./data/May2015.csv")
    filelist = [f0215, f0315, f0415, f0515]

    scoregroup = []
    scores = {} #(subreddit: score)
    for files in filelist:
        reader = csv.reader(files, delimiter=',')
        for row in reader:
            number = int(row[2])
            if row[1] not in scores:
                scores[row[1]] = []
                scores[row[1]].append(number)
            else:
                scores[row[1]].append(number)
            scoregroup.append(number)

    subredditscore = {}
    for entry in scores:
        listy = scores.get(entry)
        if len(listy) > 200:
            subredditscore[entry] = sum(listy)/len(listy)

    f0215.close()
    f0315.close()
    f0415.close()
    f0515.close()

    return scoregroup, subredditscore, scores

#all scores
def allscores(scoregroup):
    bins = np.linspace(math.ceil(min(scoregroup)),
                   math.floor(max(scoregroup)),
                   500)  # fixed number of bins
    plt.xlim([min(scoregroup)-100, max(scoregroup)+1000])
    plt.ylim(0, 50000)
    plt.hist(scoregroup, bins=bins, alpha=0.5)
    plt.title('Histogram of All Gilded Comment Scores')
    plt.xlabel('variable X (bin size = 100)')
    plt.ylabel('count')
    plt.savefig("scores.png")

#subreddit score average
def subredditaverage(subredditscore):
    xaxis = np.arange(len(subredditscore))
    plt.figure(figsize=(140, 3))
    plt.bar(xaxis, subredditscore.values(), align='center', width=3)
    plt.xticks(xaxis, subredditscore.keys())
    ymax = max(subredditscore.values()) +200
    plt.ylim(0, ymax)
    plt.title("Subreddit Score Average")
    plt.xlabel("subreddit")
    plt.ylabel("value")
    plt.savefig("subredditscores.png")

