
#forms the automated reply for the grammar comments
def make_reply_grammar(comment):
    print("Match found! Comment ID: " + comment.id)
    comment.reply("Should *have*, could *have*, would *have*"
	".\n\n*^I ^am ^a ^bot. ^Please"
	" ^don't ^hesitate ^to ^PM ^me ^any ^questions.*")
    print("Reply successful!")
    #cache.append(comment.id+',')
    comment_text_file = open("commentid.txt", 'a')
    comment_text_file.write(comment.id+',')
    comment_text_file.close()

#creates the automated reply to the sadfaced comments
def make_reply_sadface(comment):
    print("Match found! Comment ID: " + comment.id)
    comment.reply("I saw that you typed a sad face emoticon in"
    " your comment, so I just wanted to let you "
    "know that I hope you have a wonderful day!"
	"\n\n *^I ^am ^a ^bot. ^Please ^don't ^hesitate ^to"
	" ^PM ^me ^any ^questions.*")
    print("Reply successful!")
    sadface_text_file = open("sadcommentid.txt", 'a')
    sadface_text_file.write(comment.id+',')
    sadface_text_file.close()
