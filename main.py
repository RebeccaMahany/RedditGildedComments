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
	word_count = []
	word_length = []
	sent_count = []
	sent_length = []
	parag_count = []
	parag_length_words = []
	parag_length_sents = []
	contains_link = []
	all_caps_words = []
	num_bold_phrases = []
	avg_len_bold_phrase = []
	num_italics_phrases = []
	avg_len_italics_phrase = []
	# TODO grammar info
	positive_negative = []
	subjective_objective = []
	sentiments = []
	nouns = {}
	verbs = {}
	adjectives = {}
	adverbs = {}
	pronouns = {}

	# Analyze corpus based on language and upvotes
	with open("data/May2015.csv", 'r') as fp:
		reader = csv.reader(fp)
		for row in reader:
			upvotes.append(int(row[2]))
			curr_comment = row[3]
			analysis = al.analyze_language(curr_comment)
			word_count.append(analysis["word count"])
			word_length.append(analysis["word length"])
			sent_count.append(analysis["sentence count"])
			sent_length.append(analysis["sentence length"])
			parag_count.append(analysis["paragraph count"])
			parag_length_words.append(analysis["paragraph length (words)"])
			parag_length_sents.append(analysis["paragraph length (sentences)"])
			contains_link.append(analysis["contains link"])
			all_caps_words.append(analysis["all caps words"])
			num_bold_phrases.append(analysis["num bold phrases"])
			avg_len_bold_phrase.append(analysis["avg len bold phrases"])
			num_italics_phrases.append(analysis["num italics phrases"])
			avg_len_italics_phrase.append(analysis["avg len italics phrases"])
			# TODO Grammar stuff here
			positive_negative.append(analysis["positive/negative"])
			subjective_objective.append(analysis["subjective/objective"])
			sentiments.append(analysis["sentiments"])
			# TODO Get most common words		

	avg_upvotes = mean(upvotes)

	# Make graphs (Joanne)

	# Make predictions (Hannah)

if __name__ == '__main__':
	main()
