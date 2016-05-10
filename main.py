"""Main method for RedditGildedComments.
Project by:
Joanne Kim
Rebecca Mahany
"""

import sys
import csv

from statistics import mean

import analyze_language as al
from tests import test_analyze_language as t_al

import scoreandlen
from tests import score_test

import pdb

def run_program():

	# Run analysis on Reddit comments from May 2015
	upvotes, data = al.run_analysis()

	# Get most common words for each part of speech
	sorted_nouns = sorted(zip(data["nouns"].values(), data["nouns"].keys()))
	common_nouns = sorted_nouns[-10:]
	sorted_pronouns = sorted(zip(data["pronouns"].values(), data["pronouns"].keys()))
	common_pronouns = sorted_pronouns[-5:]
	sorted_adverbs = sorted(zip(data["adverbs"].values(), data["adverbs"].keys()))
	common_adverbs = sorted_adverbs[-10:]
	sorted_adjs = sorted(zip(data["adjectives"].values(), data["adjectives"].keys()))
	common_adjectives = sorted_adjs[-10:]
	sorted_verbs = sorted(zip(data["verbs"].values(), data["verbs"].keys()))
	common_verbs = sorted_verbs[-10:]

	# Print interesting data about gilded comments
	print("Average number of upvotes:")
	print(mean(upvotes))

	print("Most common nouns:")
	for noun in common_nouns:
		print(noun[1])
	print("Most common adjectives:")
	for adj in common_adjectives:
		print(adj[1])
	print("(Adverbs, verbs, and pronouns also calculated.)")

	print("Average subjectivity score for gilded comments:")
	print("(Objective = 0; subjective = 1)")
	print(mean(data["subjective/objective"]))

	print("Average word count:")
	print(mean(data["word count"]))

	print("Average word length:")
	print(mean(data["word length"]))
	print("Average sentence count:")
	print(mean(data["sentence count"]))
	print("Average sentence length:")
	print(str(mean(data["sentence length"])) + " words")

	print("Average paragraph count:")
	print(mean(data["paragraph count"]))
	print("Average length of paragraph in words:")
	print(mean(data["paragraph length (words)"]))
	print("Average length of paragraph in sentences:")
	print(mean(data["paragraph length (sentences)"]))

	contains_link = mean(data["contains link"])
	if contains_link > 0.16666666666667:
		print("More than 50% of comments contained links.")
	else:
		print("More than 50% of comments did not contain links.")

	print("Average number of bold phrases:")
	print(mean(data["num bold phrases"]))
	print("Average length of bold phrase:")
	print(mean(data["avg len bold phrase"]))
	print("Average number of italics phrases:")
	print(mean(data["num italics phrases"]))
	print("Average length of italics phrase:")
	print(mean(data["avg len italics phrase"]))

	# Make graphs (Joanne)
	tup = scoreandlen.datagrab()
	scores = tup[0]
	subredditavg = tup[1]
	scoreandlen.allscores(scores)
	scoreandlen.subredditaverage(subredditavg)


def main():

	# Parse command line args
	debug = False
	run = False
	if len(sys.argv) == 2:
		
		if sys.argv[1] == "help":
			print("To run, please enter \"python3 main.py\"! No args needed.")
			print("And please make sure you have all the necessary packages installed.")
		
		if sys.argv[1] == "run_tests":
			# Run tests for analyze_language.py (Rebecca)
			test = t_al.AnalyzeLanguageTest()
			test.ALTest()
			test.RATest()
			test.WordInfoTest()
			test.SentInfoTest()
			test.ParagInfoTest()
			test.ContentInfoTest()
			test.SentimentInfoTest()
			test.POSTest()
			object = score_test.AnalyzeScoreTest()
			object.GeneralScoreTest()
			object.SubredditScoreTest()



		if sys.argv[1] == "debug":
			print("Running in debug:")
			debug = True
			run = True

	if len(sys.argv) == 1:
		run = True

	if run:
		
		if debug:
			pdb.run("run_program()")
		else:
			run_program()


if __name__ == '__main__':
	main()
