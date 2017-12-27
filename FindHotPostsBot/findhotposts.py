import praw
import prawcore
import webbrowser

''' This python program will search through all of the SFW top of the 'hour' posts in r/all,
    and will prompt you to open the post(s) if the post has more than 60 upvotes
    and if you type in yes ('y'/'Y') in the input. If you have typed yes to one or more
    inputs, the link(s) will open in individual Google Chrome tabs at the end of the program.
'''

print("Logging in...")

#fill user details here (see PRAW documentation).
r = praw.Reddit(user_agent='**********',
                client_id='**********',
                client_secret='**********',
                username='**********',
                password='**********')

me = r.user.me()

#feel free to add to this
filtered_subreddits_list = ['The_Donald', 'politics', 'EnoughTrumpSpam', 'soccer']

#alter accordingly
chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

def grab_posts():
    new_tab = 2
    urls_to_open = []

    print("Grabbing submissions..")
    subreddit = r.subreddit('all')
    submissions = subreddit.top('hour')
    for submission in submissions:
        subreddit_name = submission.subreddit.display_name
        if (submission.score > 60 and submission.over_18 == False
        and subreddit_name not in filtered_subreddits_list):

            print("TITLE:\n\t" + submission.title)
            print("SUBREDDIT:\n\t" + submission.subreddit.display_name)
            print("UPVOTES:\n\t" + str(submission.score))
            print("NUMBER OF COMMENTS:\n\t" + str(submission.num_comments))
            print("LINK:\n\t" + submission.shortlink)

            raw_user_input = input("Would you like to open this post in a new tab (Y/N)? ")
            user_input = raw_user_input.strip(' \t\n\r')
            if (user_input == 'y' or user_input == 'Y'):
                url = submission.shortlink
                urls_to_open.append(url)

    if (len(urls_to_open) > 0):
        print("Now opening " + str(len(urls_to_open)) + " urls..")
        for url in urls_to_open:
            webbrowser.get(chrome_path).open(url, new = new_tab)

def main():
	try:
		grab_posts()
	except Exception as e:
		print(e)

	print("Done")

if __name__ == '__main__':
    main()
