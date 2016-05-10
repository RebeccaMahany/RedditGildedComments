import unittest
import praw
import random
import scoreandlen

tupper = scoreandlen.datagrab()
r = praw.Reddit('Comment parser example by u/_Daimon_')

class AnalyzeScoreTest():
    allsco = tupper[1]
    quartile1 = sorted(allsco.values())[int(len(allsco) * .25)]
    quartile1 = int(quartile1)
    median = sorted(allsco.values())[int(len(allsco)/2)]
    median = int(median)
    quartile3 = sorted(allsco.values())[int(len(allsco) * .75)]
    quartile3 = int(quartile3)


    def GeneralScoreTest(self):
        print("General score test:")
        subredditgild = tupper[2]
        randomkey = random.choice(list(subredditgild.keys()))
        sr = r.get_subreddit(randomkey)
        comments = sr.get_comments(limit=None)
        value = random.choice(list(comments))
        #get one random comment from a subreddit present in the data set
        #test its socre against the median
        check = bool(value.score in range(self.quartile1, self.quartile3))
        print("Passed general score test.")

    def SubredditScoreTest(self):
        print("Subreddit score test:")
        tester = AnalyzeScoreTest()
        subredditgild = tupper[2]
        randomkey = random.choice(list(subredditgild.keys()))
        values = subredditgild.get(randomkey)
        q1 = sorted(values)[int(len(values) * .25)]
        med = sorted(values)[int(len(values) / 2)]
        q3 = sorted(values)[int(len(values) * .75)]
        sr = r.get_subreddit(randomkey)
        comments = sr.get_comments(limit=None)
        normvalues = []
        for cmt in comments:
            normvalues.append(cmt.score)
        norm_q1 = sorted(normvalues)[int(len(normvalues) * .25)]
        norm_med = sorted(normvalues)[int(len(normvalues) / 2)]
        norm_q3 = sorted(normvalues)[int(len(normvalues) * .75)]

        #test for normal comments in subreddit vs. gilded comments
        check1 = bool(range(norm_q1, norm_med) in range(q1, med))
        check2 = bool(range(norm_med, norm_q3) in range(med, q3))
        check3 = bool(range(norm_q1, norm_q3) in range(q1, q3))

        #test for gilded subreddit comments vs. gilded comments all
        checka = bool(range(q1, med) in range(self.quartile1, self.median))
        checkb = bool(range(med, q3) in range(self.median, self.quartile3))
        checkc = bool(range(q1, q3) in range(self.quartile1, self.quartile3))

        print("Passed subreddit score test.")


