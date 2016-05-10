import unittest
import praw
import random
import scoreandlen

tupper = scoreandlen.datagrab()
r = praw.Reddit('Comment parser example by u/_Daimon_')

class AnalyzeScoreTest():
    def ___init___(self):
        allsco = tupper[1]
        quartile1 = sorted(allsco)[int(len(allsco) * .25)]
        median = sorted(allsco)[len(allsco)/2]
        quartile3 = sorted(allsco)[int(len(allsco) * .75)]


    def GeneralScoreTest(self):
        tester = AnalyzeScoreTest()
        subredditgild = tupper[2]
        randomkey = random.choice(list(subredditgild.keys()))
        sr = r.get_subreddit(randomkey)
        comments = sr.get_comments(limit=None)
        value = random.choice(list(comments))
        #get one random comment from a subreddit present in the data set
        #test its socre against the median
        self.assertEqual(value.score, range(tester.quartile1, tester.quartile3))

    def SubredditScoreTest(self):
        tester = AnalyzeScoreTest()
        subredditgild = tupper[2]
        randomkey = random.choice(subredditgild.key())
        values = subredditgild.get(randomkey)
        q1 = sorted(values)[int(len(values) * .25)]
        med = sorted(values)[len(values) / 2]
        q3 = sorted(values)[int(len(values) * .75)]
        sr = r.get_subreddit(randomkey)
        comments = sr.get_comments(limit=None)
        normvalues = []
        for cmt in comments:
            normvalues.append(cmt.score)
        norm_q1 = sorted(normvalues)[int(len(normvalues) * .25)]
        norm_med = sorted(normvalues)[len(normvalues) / 2]
        norm_q3 = sorted(normvalues)[int(len(normvalues) * .75)]

        #test for normal comments in subreddit vs. gilded comments
        self.assertEqual(range(norm_q1, norm_med), range(q1, med))
        self.assertEqual(range(norm_med, norm_q3), range(med, q3))
        self.assertEqual(range(norm_q1, norm_q3), range(q1, q3))

        #test for gilded subreddit comments vs. gilded comments all
        self.assertEqual(range(q1, med), range(tester.quartile1, tester.median))
        self.assertEqual(range(med, q3), range(tester.median, tester.quartile3))
        self.assertEqual(range(q1, q3), range(tester.quartile1, tester.quartile3))


