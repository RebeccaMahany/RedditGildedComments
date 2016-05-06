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
			subjective_objective.append(analysis["subjective/objective"])
			sentiments.append(analysis["sentiments"])
			for noun in analysis["nouns"]:
				if noun not in nouns:
					nouns[noun] = 1
				else:
					nouns[noun] += 1
			for pronoun in analysis["pronouns"]:
				if pronoun not in pronouns:
					pronouns[pronoun] = 1
				else:
					pronouns[pronoun] += 1
			for adverb in analysis["adverbs"]:
				if adverb not in adverbs:
					adverbs[adverb] = 1
				else:
					adverbs[adverb] += 1
			for adj in analysis["adjectives"]:
				if adj not in adjectives:
					adjectives[adj] = 1
				else:
					adjectives[adj] += 1
			for verb in analysis["verbs"]:
				if verb not in verbs:
					verbs[verb] = 1
				else:
					verbs[verb] += 1

	# Get most common words for each part of speech
	sorted_nouns = sorted(zip(nouns.values(), nouns.keys()))
	common_nouns = sorted_nouns[-30:]
	sorted_pronouns = sorted(zip(pronouns.values(), pronouns.keys()))
	common_pronouns = sorted_pronouns[-5:]
	sorted_adverbs = sorted(zip(adverbs.values(), adverbs.keys()))
	common_adverbs = sorted_adverbs[-15:]
	sorted_adjs = sorted(zip(adjectives.values(), adjectives.keys()))
	common_adjectives = sorted_adjs[-20:]
	sorted_verbs = sorted(zip(verbs.values(), verbs.keys()))
	common_verbs = sorted_verbs[-25:]

	print(common_verbs)


	avg_upvotes = mean(upvotes)

	# Make graphs (Joanne)

	# Make predictions (Hannah)

if __name__ == '__main__':
	main()
