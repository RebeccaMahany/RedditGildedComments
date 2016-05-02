import analyze_language as al

def main():
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
			wish rather than something you should do.\
			\
			I had aspirations way back when to be a professional athlete \
			in my sport. Currently going to my first competition made me \
			realized that spending 10-20 hours per week working towards that \
			goal would NOT make me happy in the long term. Yay, it would be \
			nice to wake up and be there but then what, the happiness would \
			fade quickly because that's not what I love DOING.\
			\
			Best of luck trying to find your dream 😊"
	# Source: https://www.reddit.com/r/books/comments/4h43vd/what_books_do_you_reckon_are_unfilmable/d2nbz13
	comment_3 = "While *The C Programming Language* by Brian Kernighan and Dennis \
			Ritchie is a time-tested classic in its genre, I think the story \
			it tells could never be adequately captured on screen. What actor \
			today could do justice to the Void Pointer, or deliver the nuance \
			of a dereference from const?\
			\
			I suppose Schwarzenegger could play the Null String Terminator.\
			\
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
	
	result_1 = al.analyze_language(comment_1)
	result_2 = al.analyze_language(comment_2)
	result_3 = al.analyze_language(comment_3)
	result_4 = al.analyze_language(comment_4)

if __name__ == "__main__":
	main()
