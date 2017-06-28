import praw
import prawcore
import time
import reply

'''
TODO - Optimisation
	- .
'''

print("Logging in...")
r = praw.Reddit(user_agent='**********',
                client_id='**********',
                client_secret='**********',
                username='**********',
                password='**********')

me = r.user.me()

misspelled_words = ['should of', 'could of', 'would of']
misspelled_combination = ['of', 'of,', 'of.', 'of!', 'of/', 'of?']

'''
for some reason, this creates a list inside a list. So I had to
iterate through cache[0]
'''
cache = [line.split(',') for line in open("commentid.txt")]
sad_faces = [':(', ':(.', ':-(',':-(.', ';(', ';(.', '=(', '=(.', "='(", "='(."]
sad_face_cache = [line.split(',') for line in open("sadcommentid.txt")]

'''
Calculates whether the word (as a string) being parsed in is one of these words,
'''
def is_incorrect(word):
    if word == 'should' or word == 'would' or word == 'could':
        return True

    return False;
	
def bot_listener():
	print("Grabbing subreddit...")
    #get_subreddit("test+test+test") for multiple subreddits
	subreddit = r.subreddit("all")
	print("Grabbing comments...")
	comments = subreddit.stream.comments()
	'''
	iterates through comments in the subreddit, finds if the comment has words
	that match the criteria, then replies to the comment.
	'''
	for comment in comments:
		comment_text = comment.body
		comments = comment_text.split()
		'''
		iterates through the comment through every individual character
		to try and find if it fits the criterium
		'''
		is_match = any(string in comment_text for string in misspelled_words)
		'''
		iterates through the comment as each word and sees if it fits the
		criterium
		'''
		sad_face_match = any(string in comments for string in sad_faces)
		
		if (comment.id not in cache[0] and is_match and '>' not in comment_text
		and comment.author != me):
			count = 0
			'''
			finds the incorrect grammar combination of the words, makes a reply,
			and adds the comment ID to the list so that we don't reply to the
			same person more than once
			'''
			for word in comments:
				if is_incorrect(comments[count-1]):
					if word in misspelled_combination:
						reply.make_reply_grammar(comment)
						cache.append(comment.id)
						#can contain multiple words
						continue
				count+=1
			count = 0

		#Makes a reply to the comment as it contains a sad face emoticon
		if (comment.id not in sad_face_cache[0] and sad_face_match
		and '>' not in comment_text and comment.author != me):
			reply.make_reply_sadface(comment)
			sad_face_cache.append(comment.id)
			continue

def main():
	try:
		bot_listener()
		
	except praw.exceptions.APIException as error:
		if 'RATELIMIT' in str(error):
			print("\t'You are doing that too much' restriction encountered."
			" Skipping the comment reply.")
			'''
			+ ". Sleeping for 600 seconds")
			time.sleep(600)
			'''
			time.sleep(10)
			main()
		
	except prawcore.exceptions.Forbidden as error:
		if str(error) == 'received 403 HTTP response':
			print("\tPotentially banned from this subreddit, skipping..")
			time.sleep(10)
			main()
	
	#unknown exception occurred
	print("Done")

if __name__ == '__main__':
    main()
