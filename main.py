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

def main():

	# Parse command line args
	debug = False
	if len(sys.argv) == 2:
		if sys.argv[1] == "help":
			print("Help") # TODO fix
		if sys.argv[1] == "run_tests":
			test = t_al.AnalyzeLanguageTest()
			print(test.OverallALTest())
		if sys.argv[1] == "debug": # TODO debug needs to be implemented
			print("Running in debug:")
			debug = True

	# Arrays to store data gathered from corpus
	upvotes = []
	data = {"word count":[], "word length":[], "sentence count":[],\
		"sentence length":[], "paragraph count":[], "paragraph length (words)":[],\
		"paragraph length (sentences)":[], "contains link":[], "all caps words":[],\
		"num bold phrases":[], "avg len bold phrase":[],\
		"num italics phrases":[], "avg len italics phrase":[],\
		"subjective_objective":[], "sentiments":[], "nouns":{},\
		"verbs":{}, "adjectives":{}, "adverbs":{}, "pronouns":{} }

	# Analyze corpus based on language and upvotes
	with open("data/May2015.csv", 'r') as fp:
		reader = csv.reader(fp)
		for row in reader:
			upvotes.append(int(row[2]))
			curr_comment = row[3]
			analysis = al.analyze_language(curr_comment, data)

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

	print(common_nouns)
	print(common_pronouns)
	print(common_adverbs)
	print(common_adjectives)

	avg_upvotes = mean(upvotes)

	# Make graphs (Joanne)

	# Make predictions (Hannah)

if __name__ == '__main__':
	main()
