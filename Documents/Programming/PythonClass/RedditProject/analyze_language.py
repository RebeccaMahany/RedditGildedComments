import nltk.data
import nltk.sentiment
import string
import re
from statistics import mean
# NOTE: you may need to run nltk.download()

def analyze_language(comment_body, results):
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
	grammar_info = get_grammar_info()

	sentiment_info = get_sentiment_info(comment_body, sentences)
	analysis["positive/negative"] = sentiment_info[0]
	analysis["subjective/objective"] = sentiment_info[1]
	analysis["sentiments"] = sentiment_info[2]

	return analysis

def get_word_info(words):
	# Get wordcount
	num_words = len(words)

	# Get average word length
	sum_len_words = 0
	for word in words:
		sum_len_words += len(word.translate(string.maketrans("", ""), string.punctuation)

	avg_len_words = sum_len_words / num_words

	return num_words, avg_len_words

def get_sentence_info(sentences):
	# Get number of sentences
	num_sentences = len(sentences)

	# Get average sentence length
	sum_len_sent = 0
	for sent in sentences:
		sum_len_sent += len(sent.split())

	avg_len_sent = sum_len_sent / num_sentences

	return num_sentences, avg_len_sent

def get_paragraph_info(paragraphs)
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

	avg_len_para_w = sum_len_para_w / num_paragraphs
	avg_len_para_s = sum_len_para_s / num_paragraphs

	return num_paragraphs, avg_len_para_w, avg_len_para_s
		

def get_content_info(comment):
	# Get whether comment contains a link
	contains_link = False

	# Get info on amount of comment in ALL CAPS

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
		lens_i = []
			for i in range(0, len(italics_indices)):
				if i%2 == 1:
					lens_i.append(italics_indices[i] - italics_indices[i-1] - 1)
		avg_len_italics_phrase = mean(lens_i)
	else:
		num_italics_phrases = 0
		avg_len_italics_phrase = 0
	
def get_grammar_info():
	# Get info on grammatical correctness

	# Get info on grammatical structure of sentences

def get_sentiment_info(comment, sentences):
	emotions = {"Neutral": 0, "Negative": 0, "Positive": 0}
	for sent in sentences:
		emotion = nltk.sentiment.util.demo_liu_hu_lexicon(sent, plot=False)
		if emotion is "Neutral":
			emotions["Neutral"] += 1
		elif emotion is "Negative":
			emotions["Negative"] += 1
		elif emotion is "Positive":
			emotions["Positive"] += 1
	
	# TODO Pass in classifier or this will take actually forever
	subj_or_obj = nltk.sentiment.util.demo_sent_subjectivity(comment)
	sentiments = nltk.sentiment.util.demo_vader_instance(comment)

	return emotions, subj_or_obj, sentiments

