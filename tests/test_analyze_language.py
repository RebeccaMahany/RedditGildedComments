import unittest
import analyze_language as al
import nltk

class AnalyzeLanguageTest(unittest.TestCase):

	# Source: https://www.reddit.com/r/IAmA/comments/4h9gae/iama_24_year_old_blogger_living_with_cystic/d2oiagf
	comment_1 = "I guess hope and laughter. This actually brings out something \
			very positive I have learned about CF. We are positive \
			people. I'm not sure why. We were given such a cruel disease, \
			but we make the most of it. Why let it bring you down when \
			there is nothing you can do about it, but make the best of it? \
			I just take life one day at a time. I make sure that every day \
			I am doing what I WANT to do and not what I think I have to do. \
			I travel a lot. One thing I really want to do is see the beauty \
			of the world, so I just make sure that happens. You get your \
			priorities in order very quickly. I think we live just as \
			fulfilling life as anyone else, just quicker."
	# Source: https://www.reddit.com/r/AskWomen/comments/4h902u/ladies_who_realized_that_some_of_their_deepest/d2ok7j9
	comment_2 = "A lot of people have dreams of being a writer rather than dreams \
			of writing. These are two very different dreams. One is \
			achievable and will make you happy, the other one is not. \
			Figure out what makes you happy WHEN you are putting the time \
			and effort to do it and realizing than the other is more of a \
			wish rather than something you should do.\n\n\
			I had aspirations way back when to be a professional athlete \
			in my sport. Currently going to my first competition made me \
			realized that spending 10-20 hours per week working towards that \
			goal would NOT make me happy in the long term. Yay, it would be \
			nice to wake up and be there but then what, the happiness would \
			fade quickly because that's not what I love DOING.\n\n\
			Best of luck trying to find your dream 😊"
	# Source: https://www.reddit.com/r/books/comments/4h43vd/what_books_do_you_reckon_are_unfilmable/d2nbz13
	comment_3 = "While *The C Programming Language* by Brian Kernighan and Dennis \
			Ritchie is a time-tested classic in its genre, I think the story \
			it tells could never be adequately captured on screen. What actor \
			today could do justice to the Void Pointer, or deliver the nuance \
			of a dereference from const?\n\n\
			I suppose Schwarzenegger could play the Null String Terminator.\n\n\
			    sprintf(newcomment, \"%s\n\nEDIT -- Thanks %u the gold, %s!!\\n\", \
			oldcomment, 4, \"kind stranger\");"
	# Source: https://www.reddit.com/r/interestingasfuck/comments/4hbqmr/haycurling_machine/d2p3n3i
	comment_4 = "Wet wrapping is a process in which hay is cut and wrapped shortly \
			after cutting, usually within 24 hours. This hay ferments and is \
			referred to as baleage. Typically this works better than traditional \
			baling methods in wetter environments where leaving hay to dry for \
			several days is not possible. It can also be used to get an extra \
			cutting earlier. The fast wrapping after cutting, along with controls \
			for temperature and moisture content prevent mold."



	def ALTest(self): # TODO complete -- MockTest candidate?
		print("Testing the functionality of analyze_language() as a whole.")

	def RATest(self): # TODO complete -- MockTest candidate?
		print("Testing functionality of run_analyze() as a whole.")

	def WordInfoTest(self):
		print("Testing functionality of get_word_info().")
		
		result_1 = al.get_word_info(self.comment_1.split())
		result_2 = al.get_word_info(self.comment_2.split())
		result_3 = al.get_word_info(self.comment_3.split())
		result_4 = al.get_word_info(self.comment_4.split())

		# Testing number of words (calculated manually)
		self.assertEqual(result_1[0], 138)
		self.assertEqual(result_2[0], 144)
		self.assertEqual(result_3[0], 72)
		self.assertEqual(result_4[0], 76)

		# Testing average length of words
		self.assertAlmostEqual(result_1[1], 3.6376811594)
		self.assertAlmostEqual(result_2[1], 4.1388888889)
		self.assertAlmostEqual(result_3[1], 4.8472222222)
		self.assertAlmostEqual(result_4[1], 4.8815789473)
		
		print("Passed all tests for get_word_info().")

	def SentInfoTest(self):
		print("Testing functionality of get_sentence_info().")
		
		tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
		result_1 = al.get_sentence_info(tokenizer.tokenize(self.comment_1))
		result_2 = al.get_sentence_info(tokenizer.tokenize(self.comment_2))
		result_3 = al.get_sentence_info(tokenizer.tokenize(self.comment_3))
		result_4 = al.get_sentence_info(tokenizer.tokenize(self.comment_4))

		# Testing number of sentences (calculated manually)
		self.assertEqual(result_1[0], 12)
		self.assertEqual(result_2[0], 8)
		self.assertEqual(result_3[0], 5)
		self.assertEqual(result_4[0], 5)

		# Testing average length of sentence (calculated manually)
		self.assertAlmostEqual(result_1[1], 11.5)
		self.assertAlmostEqual(result_2[1], 18)
		self.assertAlmostEqual(result_3[1], 14.6)
		self.assertAlmostEqual(result_4[1], 15.2)

		print("Passed all tests for get_sentence_info().")

	def ParagInfoTest(self):
		print("Testing functionality of get_paragraph_info().")

		result_1 = al.get_paragraph_info(self.comment_1.split("\n\n"))
		result_2 = al.get_paragraph_info(self.comment_2.split("\n\n"))
		result_3 = al.get_paragraph_info(self.comment_3.split("\n\n"))
		result_4 = al.get_paragraph_info(self.comment_4.split("\n\n"))		

		# Testing number of paragraphs
		self.assertEqual(result_1[0], 1)
		self.assertEqual(result_2[0], 3)
		self.assertEqual(result_3[0], 4)
		self.assertEqual(result_4[0], 1)

		# Testing avg number of words per paragraph
		self.assertEqual(result_1[1], 138)
		self.assertAlmostEqual(result_2[1], 48)
		self.assertAlmostEqual(result_3[1], 18.25)
		self.assertEqual(result_4[1], 76)

		# Testing avg number of sentences per paragraph
		self.assertAlmostEqual(result_1[2], 12)
		self.assertAlmostEqual(result_2[2], 2.6666666666667)
		self.assertAlmostEqual(result_3[2], 1.5)
		self.assertAlmostEqual(result_4[2], 5)

		print("Passed all tests for get_paragraph_info().")

	def ContentInfoTest(self):
		print("Testing functionality of get_content_info().")
		
		result_1 = al.get_content_info(self.comment_1)
		result_2 = al.get_content_info(self.comment_2)
		result_3 = al.get_content_info(self.comment_3)
		result_4 = al.get_content_info(self.comment_4)

		# Testing contains link
		self.assertFalse(result_1[0])
		self.assertFalse(result_2[0])
		self.assertFalse(result_3[0])
		self.assertFalse(result_4[0])

		# Testing number of bold phrases
		self.assertEqual(result_1[1], 0)
		self.assertEqual(result_2[1], 0)
		self.assertEqual(result_3[1], 0)
		self.assertEqual(result_4[1], 0)

		# Testing avg length of bold phrases
		self.assertEqual(result_1[2], 0)
		self.assertEqual(result_2[2], 0)
		self.assertEqual(result_3[2], 0)
		self.assertEqual(result_4[2], 0)

		# Testing number of italics phrases
		self.assertEqual(result_1[3], 0)
		self.assertEqual(result_2[3], 0)
		self.assertEqual(result_3[3], 1)
		self.assertEqual(result_4[3], 0)
		
		# Testing avg length of italics phrases
		self.assertEqual(result_1[4], 0)
		self.assertEqual(result_2[4], 0)
		self.assertEqual(result_3[4], 26)
		self.assertEqual(result_4[4], 0)

		print("Passed all tests for get_content_info().")

	def SentimentInfoTest(self):
		print("Testing functionality of get_sentiment_info().")

		result_1 = al.get_sentiment_info(self.comment_1)
		result_2 = al.get_sentiment_info(self.comment_2)
		result_3 = al.get_sentiment_info(self.comment_3)
		result_4 = al.get_sentiment_info(self.comment_4)
		
		# Test subjective/objective
		self.assertAlmostEqual(result_1, 0.56857864357)
		self.assertAlmostEqual(result_2, 0.52137254901)
		self.assertAlmostEqual(result_3, 0.4)
		self.assertAlmostEqual(result_4, 0.54666666667)
		
		print("Passed all tests for get_sentiment_info().")

	def POSTest(self):
		print("Testing functionality of get_pos().")
		
		result_1 = al.get_pos(self.comment_1)
		result_2 = al.get_pos(self.comment_2)
		result_3 = al.get_pos(self.comment_3)
		result_4 = al.get_pos(self.comment_4)
		
		# Test nouns
		self.assertIn("laughter", result_1[0])
		self.assertIn("writer", result_2[0])
		self.assertIn("story", result_3[0])
		self.assertIn("process", result_4[0])
	
		# Test pronouns
		self.assertIn("I", result_1[1])
		self.assertIn("I", result_2[1])
		self.assertIn("I", result_3[1])
		self.assertIn("It", result_4[1])
	
		# Test adverbs
		self.assertIn("very", result_1[2])
		self.assertIn("very", result_2[2])
		self.assertIn("adequately", result_3[2])
		self.assertIn("shortly", result_4[2])

		# Test adjectives
		self.assertIn("cruel", result_1[3])
		self.assertIn("professional", result_2[3])
		self.assertIn("traditional", result_4[3])

		# Test verbs
		self.assertIn("brings", result_1[4])
		self.assertIn("going", result_2[4])
		self.assertIn("deliver", result_3[4])
		self.assertIn("cutting", result_4[4])

		print("Passed all tests for get_pos().")
