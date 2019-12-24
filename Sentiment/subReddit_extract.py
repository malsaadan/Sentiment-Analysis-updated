import praw

reddit = praw.Reddit(client_id='zoq10cuAou8EGQ', client_secret='XovsEgldtAcH2eDJhzkIDOfcTVw', user_agent='Fetch')

def subRedditExtract(keyword):
    subreddit = reddit.subreddit('all').search(keyword,sort='relevance', limit=5)
    reviews = []

    for submission in subreddit:
        #sub = submission.selftext
        #reviews.extend(sub)
        submission.comments.replace_more(limit=0)
        for top_level_comments in submission.comments:
            comment = top_level_comments.body
            reviews.append(comment)

    return reviews