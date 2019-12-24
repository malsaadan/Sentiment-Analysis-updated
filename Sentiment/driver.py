import comment_extract as CE
import tweet_extract as TE
import subReddit_extract as SE
import sentimentApi as SA
import fancySentiment as FS

def main():

	search_term = input('Enter a search keyword: ')
	# Youtube API
	comments = CE.retrieveVideos(search_term)

	# Twitter API
	api = TE.TwitterClient()
	tweets = api.get_tweets(search_term)

	# Reddit API
	reviews = SE.subRedditExtract(search_term)

	total_reviews = tweets
	if comments is not None:
		total_reviews.extend(comments)
	total_reviews.extend(reviews)
	SA.sentiment(total_reviews, search_term)
	FS.fancySentiment(total_reviews, search_term)


if __name__ == '__main__':
	main()
