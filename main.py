"""Main method for RedditGildedComments.
Project by:
Hannah Ahn
Joanne Kim
Rebecca Mahany
"""

import sys
import csv

from statistics import mean

import analyze_language as al

from tests import test_analyze_language as t_al

import pdb

def run_program():
	upvotes, data = al.run_analysis()

	# Get most common words for each part of speech
	sorted_nouns = sorted(zip(data["nouns"].values(), data["nouns"].keys()))
	common_nouns = sorted_nouns[-30:]
	sorted_pronouns = sorted(zip(data["pronouns"].values(), data["pronouns"].keys()))
	common_pronouns = sorted_pronouns[-5:]
	sorted_adverbs = sorted(zip(data["adverbs"].values(), data["adverbs"].keys()))
	common_adverbs = sorted_adverbs[-15:]
	sorted_adjs = sorted(zip(data["adjectives"].values(), data["adjectives"].keys()))
	common_adjectives = sorted_adjs[-20:]
	sorted_verbs = sorted(zip(data["verbs"].values(), data["verbs"].keys()))
	common_verbs = sorted_verbs[-25:]

	# Make graphs (Joanne)
	# Make predictions (Hannah)


def main():

	# Parse command line args
	debug = False
	run = False
	if len(sys.argv) == 2:
		
		if sys.argv[1] == "help":
			print("To run, please enter \"python3 main.py\"! No args needed.") #TODO Please change this if we need command line args down the line!
			print("If you're having difficulties, you may need to enter \"nltk.download()\" first.")
		
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
