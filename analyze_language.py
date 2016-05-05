import sys
import nltk.data
import nltk.sentiment
from nltk.sentiment import SentimentAnalyzer
import string
import io
import re
from statistics import mean
from contextlib import redirect_stdout
# NOTE: you may need to run nltk.download()

def analyze_language(comment_body):
	analysis = {}

	# Split into paragraphs
	paragraphs = comment_body.split("\n\n")
	
	# Split into sentences
	tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
	sentences = tokenizer.tokenize(comment_body)

	# Split into words
	words = comment_body.split()

	word_info = get_word_info(words)
	analysis["word count"] = word_info[0]
	analysis["word length"] = word_info[1]

	sent_info = get_sentence_info(sentences)
	analysis["sentence count"] = sent_info[0]
	analysis["sentence length"] = sent_info[1]

	para_info = get_paragraph_info(paragraphs)
	analysis["paragraph count"] = para_info[0]
	analysis["paragraph length (words)"] = para_info[1]
	analysis["paragraph length (sentences)"] = para_info[2]

	content_info = get_content_info(comment_body)
	analysis["contains link"] = content_info[0]
	analysis["all caps words"] = content_info[1]
	analysis["num bold phrases"] = content_info[2]
	analysis["avg len bold phrases"] = content_info[3]
	analysis["num italics phrases"] = content_info[4]
	analysis["avg len italics phrases"] = content_info[5]

	grammar_info = get_grammar_info()

	#sentiment_info = get_sentiment_info(comment_body, sentences)
	#analysis["positive/negative"] = sentiment_info[0]
	#analysis["subjective/objective"] = sentiment_info[1]
	#analysis["sentiments"] = sentiment_info[2]
	analysis["positive/negative"] = "positive"
	analysis["subjective/objective"] = "subj"
	analysis["sentiments"] = "sentimental"

	# TODO: get most common words for different parts of speech

	return analysis

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

def get_paragraph_info(paragraphs):
	# Get number of paragraphs
	num_paragraphs = len(paragraphs)

	# Get average paragraph length in words and in sentences
	sum_len_para_w = 0
	sum_len_para_s = 0
	# TODO: change so that we aren't tokenizing paragraphs here and in analyze_language()
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
		

def get_content_info(comment):
	# Get whether comment contains a link
	contains_link = False # TODO

	# Get info on amount of words in ALL CAPS
	num_caps_words = 0 # TODO

	# Get info on amount of comment in bold (in chars)
	if re.match("\*\*", comment) is not None:
		iter1 = re.finditer("\*\*", comment)
		bold_indices = [n.start(0) for n in iter1]
		num_bold_phrases = len(bold_indices)/2
		lens_b = []
		for i in range(0, len(bold_indices)):
			if i%2 == 1:
				lens_b.append(bold_indices[i] - bold_indices[i-1] - 2)
		avg_len_bold_phrase = mean(lens_b)
	else:
		num_bold_phrases = 0
		avg_len_bold_phrase = 0

	# Get info on amount of comment in italics (in chars)
	if re.match("[^*]\*[^*]", comment) is not None:
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
	return contains_link, num_caps_words, num_bold_phrases, avg_len_bold_phrase,\
		 num_italics_phrases, avg_len_italics_phrase 
	
def get_grammar_info():
	# TODO: Apparently this is still an area of active research, so I need to 
	# do more reading to see whether this is feasible

	# Get info on grammatical correctness

	# Get info on grammatical structure of sentences
	return True

# Get information on emotions, subjectivity, and sentiments
# Requires redirecting the stdout because all functions used print to stdout
def get_sentiment_info(comment, sentences):
	f = io.StringIO()
	with redirect_stdout(f):
		for sent in sentences:
			nltk.sentiment.util.demo_liu_hu_lexicon(sent, plot=False)
	
	emotions = {"Neutral": 0, "Negative": 0, "Positive": 0}
	e_results = f.getvalue().splitlines()
	for emotion in e_results:
		if emotion == "Neutral":
			emotions["Neutral"] += 1
		elif emotion == "Negative":
			emotions["Negative"] += 1
		elif emotion == "Positive":
			emotions["Positive"] += 1
	
	g = io.StringIO()
	with redirect_stdout(g):
		nltk.sentiment.util.demo_sent_subjectivity(comment)
	
	subj_or_obj = g.getvalue().rstrip()
	
	h = io.StringIO()
	with redirect_stdout(h):
		nltk.sentiment.util.demo_vader_instance(comment)
	
	sentiments = h.getvalue().rstrip()

	return emotions, subj_or_obj, sentiments

