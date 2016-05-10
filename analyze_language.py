import sys
import ast
import nltk.data
import nltk.sentiment
from nltk.sentiment import SentimentAnalyzer
from textblob import TextBlob
import string
import io
import csv
import re
from statistics import mean
from contextlib import redirect_stdout


# Reads through csv file, analyzes each comment in the csv file, returns data
def run_analysis():
	#Arrays to store data gathered from corpus
	upvotes = []
	data = {"word count":[], "word length":[], "sentence count":[],\
		"sentence length":[], "paragraph count":[], "paragraph length (words)":[],\
		"paragraph length (sentences)":[], "contains link":[],\
		"num bold phrases":[], "avg len bold phrase":[],\
		"num italics phrases":[], "avg len italics phrase":[],\
		"subjective/objective":[], "nouns":{},\
		"verbs":{}, "adjectives":{}, "adverbs":{}, "pronouns":{} }

	# Analyze corpus based on language and upvotes
	with open("data/May2015.csv", 'r') as fp:
		reader = csv.reader(fp)
		for row in reader:
			upvotes.append(int(row[2]))
			curr_comment = row[3]
			analysis = analyze_language(curr_comment, data)

	return upvotes, data


# Runs analysis on each Reddit comment
def analyze_language(comment_body, analysis):

	# Split into paragraphs
	paragraphs = comment_body.split("\n\n")
	
	# Split into sentences
	tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
	sentences = tokenizer.tokenize(comment_body)

	# Split into words
	words = comment_body.split()

	word_info = get_word_info(words)
	analysis["word count"].append(word_info[0])
	analysis["word length"].append(word_info[1])

	sent_info = get_sentence_info(sentences)
	analysis["sentence count"].append(sent_info[0])
	analysis["sentence length"].append(sent_info[1])

	para_info = get_paragraph_info(paragraphs)
	analysis["paragraph count"].append(para_info[0])
	analysis["paragraph length (words)"].append(para_info[1])
	analysis["paragraph length (sentences)"].append(para_info[2])

	content_info = get_content_info(comment_body)
	analysis["contains link"].append(content_info[0])
	analysis["num bold phrases"].append(content_info[1])
	analysis["avg len bold phrase"].append(content_info[2])
	analysis["num italics phrases"].append(content_info[3])
	analysis["avg len italics phrase"].append(content_info[4])

	sentiment_info = get_sentiment_info(comment_body)
	analysis["subjective/objective"].append(sentiment_info)

	pos = get_pos(comment_body)
	for noun in pos[0]:
		# Having a problem with [, ], and * especially being recognized as nouns
		if noun not in string.punctuation:
			if noun not in analysis["nouns"]:
				analysis["nouns"][noun] = 1
			else:
				analysis["nouns"][noun] += 1
	for pronoun in pos[1]:
		if pronoun not in analysis["pronouns"]:
			analysis["pronouns"][pronoun] = 1
		else:
			analysis["pronouns"][pronoun] += 1
	for adverb in pos[2]:
		if adverb not in analysis["adverbs"]:
			analysis["adverbs"][adverb] = 1
		else:
			analysis["adverbs"][adverb] += 1
	for adjective in pos[3]:
		if adjective not in analysis["adjectives"]:
			analysis["adjectives"][adjective] = 1
		else:
			analysis["adjectives"][adjective] += 1
	for verb in pos[4]:
		if verb not in analysis["verbs"]:
			analysis["verbs"][verb] = 1
		else:
			analysis["verbs"][verb] += 1	


# Gets wordcount, average word length
def get_word_info(words):
	# Get wordcount
	num_words = len(words)

	# Get average word length
	sum_len_words = 0
	for word in words:
		sum_len_words += len(word.translate(str.maketrans({p: None for p in string.punctuation})))

	if num_words == 0:
		avg_len_words = 0
	else:
		avg_len_words = sum_len_words / num_words

	return num_words, avg_len_words


# Gets sentence count, average sentence length
def get_sentence_info(sentences):
	# Get number of sentences
	num_sentences = len(sentences)

	# Get average sentence length
	sum_len_sent = 0
	for sent in sentences:
		sum_len_sent += len(sent.split())

	if num_sentences == 0:
		avg_len_sent = 0
	else:
		avg_len_sent = sum_len_sent / num_sentences

	return num_sentences, avg_len_sent


# Gets paragraph count, avg length of paragraphs in words and in sentences
def get_paragraph_info(paragraphs):
	# Get number of paragraphs
	num_paragraphs = len(paragraphs)

	# Get average paragraph length in words and in sentences
	sum_len_para_w = 0
	sum_len_para_s = 0
	tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
	for para in paragraphs:
		sents = tokenizer.tokenize(para)
		sum_len_para_s += len(sents)
		for sent in sents:
			sum_len_para_w += len(sent.split())

	if num_paragraphs == 0:
		avg_len_para_w = 0
		avg_len_para_s = 0
	else:
		avg_len_para_w = sum_len_para_w / num_paragraphs
		avg_len_para_s = sum_len_para_s / num_paragraphs

	return num_paragraphs, avg_len_para_w, avg_len_para_s
		

# Get whether comment contains link, has bold/italic text
def get_content_info(comment):
	# List of domain names as regexes. Domains taken from https://en.wikipedia.org/wiki/List_of_Internet_top-level_domains
	domains = ["\.com", "\.org", "\.net", "\.int", "\.edu", "\.gov", "\.mil", "\.ca", "\.uk"]

	# Get whether comment contains a link
	contains_link = False
	if re.search("http", comment) is not None:
		contains_link = True
	else:
		for domain_name in domains:
			if re.search(domain_name, comment) is not None:
				contains_link = True
				break

	# Get info on amount of comment in bold (in chars)
	if re.search("\*\*", comment) is not None:
		iter1 = re.finditer("\*\*", comment)
		bold_indices = [n.start(0) for n in iter1]
		num_bold_phrases = len(bold_indices)/2
		if num_bold_phrases > 0.5:
			lens_b = []
			for i in range(0, len(bold_indices)):
				if i%2 == 1:
					lens_b.append(bold_indices[i] - bold_indices[i-1] - 2)
			avg_len_bold_phrase = mean(lens_b)
		else:
			num_bold_phrases = 0
			avg_len_bold_phrase = 0
	else:
		num_bold_phrases = 0
		avg_len_bold_phrase = 0

	# Get info on amount of comment in italics (in chars)
	if re.search("[^*]\*[^*]", comment) is not None:
		iter2 = re.finditer("\*", comment)
		italics_indices = [m.start(0) for m in iter2]
		num_italics_phrases = len(italics_indices)/2
		if num_italics_phrases > 0.5:
			lens_i = []
			for i in range(0, len(italics_indices)):
				if i%2 == 1:
					lens_i.append(italics_indices[i] - italics_indices[i-1] - 1)
			avg_len_italics_phrase = mean(lens_i)
		else:
			num_italics_phrases = 0
			avg_len_italics_phrase = 0
	else:
		num_italics_phrases = 0
		avg_len_italics_phrase = 0

	return contains_link, num_bold_phrases, avg_len_bold_phrase,\
		 num_italics_phrases, avg_len_italics_phrase 


# Get information on sentiments
def get_sentiment_info(comment):	

	blob = TextBlob(comment)
	subj_or_obj = blob.subjectivity

	return subj_or_obj


# Tag each word with its part of speech; return words organized by POS
def get_pos(comment):

	# Tag words in the comment with their POS
	text = nltk.word_tokenize(comment)
	tagged = nltk.pos_tag(text)
	
	nouns = []
	pronouns = []
	adverbs = []
	adjectives = []
	verbs = []
	
	# Add words to their respective lists
	# TODO: it would be smart to group words by stems (eg group "cat" w/ "cats")
	for tag in tagged:
		if tag[1] == "NNS" or tag[1] == "NNP" or tag[1] == "NNPS" or tag[1] == "NN":
			nouns.append(tag[0])
		elif tag[1] == "PRP" or tag[1] == "PRP$":
			pronouns.append(tag[0])
		elif tag[1] == "RBR" or tag[1] == "RBS" or tag[1] == "RB":
			adverbs.append(tag[0])
		elif tag[1] == "JJ" or tag[1] == "JJR" or tag[1] == "JJS":
			adjectives.append(tag[0])
		elif tag[1] == "VB" or tag[1] == "VBP" or tag[1] == "VBD" or \
				tag[1] == "VBG" or tag[1] == "VBN" or tag[1] == "VBZ":
			verbs.append(tag[0])

	return nouns, pronouns, adverbs, adjectives, verbs
